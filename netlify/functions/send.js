/**
 * Judo Club Anderlecht — Envoi des formulaires via SMTP Combell
 *
 * Variables d'environnement requises (Netlify → Site settings → Environment variables) :
 *   SMTP_HOST         ex: smtp.mailprotect.be
 *   SMTP_PORT         ex: 587 (STARTTLS) ou 465 (SSL)
 *   SMTP_USER         ex: secretariat@judoclubanderlecht.be
 *   SMTP_PASS         mot de passe de la boîte email
 *   RECIPIENT_EMAIL   ex: secretariat@judoclubanderlecht.be (où recevoir les messages)
 *   ALLOWED_ORIGIN    ex: https://judoclubanderlecht.be (facultatif, pour CORS strict)
 */

const nodemailer = require('nodemailer');
const { getStore } = require('@netlify/blobs');

exports.handler = async (event) => {
  const allowedOrigin = process.env.ALLOWED_ORIGIN || '*';
  const headers = {
    'Access-Control-Allow-Origin': allowedOrigin,
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Allow-Methods': 'POST, OPTIONS',
    'Content-Type': 'application/json'
  };

  // CORS preflight
  if (event.httpMethod === 'OPTIONS') {
    return { statusCode: 204, headers, body: '' };
  }

  if (event.httpMethod !== 'POST') {
    return { statusCode: 405, headers, body: JSON.stringify({ ok: false, error: 'Method not allowed' }) };
  }

  // Parse body (JSON only — le client poste en JSON)
  let data;
  try {
    data = JSON.parse(event.body || '{}');
  } catch {
    return { statusCode: 400, headers, body: JSON.stringify({ ok: false, error: 'Invalid JSON' }) };
  }

  // Anti-spam basique : honeypot field '_gotcha' + longueur message
  if (data._gotcha) {
    return { statusCode: 200, headers, body: JSON.stringify({ ok: true, bot: true }) };
  }
  if ((data.message || '').length > 5000) {
    return { statusCode: 413, headers, body: JSON.stringify({ ok: false, error: 'Message too long' }) };
  }

  // Construction du mail
  const baseSubject = data._subject || '[Site] Nouveau message';
  const source  = data._source  || 'site';
  const replyTo = (data.email || data.Email || '').trim();

  // Identifier le visiteur (prenom + nom OU nom seul OU email)
  const visitorName = [
    (data.prenom || data.Prenom || data.firstName || '').trim(),
    (data.nom    || data.Nom    || data.lastName  || data.name || '').trim()
  ].filter(Boolean).join(' ').trim();

  const visitorLabel = visitorName || replyTo || 'Visiteur anonyme';

  // Subject enrichi : « [Site] Marie Dupont — Cours d'essai »
  const subject = visitorName
    ? baseSubject.replace(/^(\[[^\]]+\]\s*)?/, m => (m||'') + visitorName + ' — ').replace(/\[Site\]\s+/, '[Site] ')
    : baseSubject;

  const lines = Object.keys(data)
    .filter(k => !k.startsWith('_') && !k.startsWith('$'))
    .map(k => `  ${k} : ${data[k]}`);

  const textBody =
    `Nouveau message depuis ${source}\n` +
    `De      : ${visitorLabel}${replyTo ? ' <' + replyTo + '>' : ''}\n` +
    `Date    : ${new Date().toLocaleString('fr-BE')}\n` +
    (replyTo ? `\n💡 Cliquez « Répondre » pour répondre directement à ${replyTo}\n` : '') +
    `\n--- Contenu ---\n${lines.join('\n')}\n--- Fin ---\n`;

  // Configuration SMTP
  const port = parseInt(process.env.SMTP_PORT || '587', 10);
  const transporter = nodemailer.createTransport({
    host: process.env.SMTP_HOST,
    port: port,
    secure: port === 465,          // true pour 465, false pour 587
    auth: {
      user: process.env.SMTP_USER,
      pass: process.env.SMTP_PASS
    }
  });

  // Sender display name : « Marie Dupont via Site JCA »
  const senderName = visitorName
    ? `${visitorName} via Site JCA`
    : 'Site Judo Club Anderlecht';

  let emailOk = false;
  let emailError = null;
  try {
    await transporter.sendMail({
      from: `"${senderName}" <${process.env.SMTP_USER}>`,
      to: process.env.RECIPIENT_EMAIL || process.env.SMTP_USER,
      replyTo: replyTo || undefined,
      subject: subject,
      text: textBody
    });
    emailOk = true;
  } catch (err) {
    console.error('SMTP error:', err);
    emailError = err.message || 'SMTP error';
  }

  // Persistance dans Netlify Blobs (même si l'email a échoué — on garde la trace)
  try {
    const siteID = process.env.SITE_ID || process.env.NETLIFY_SITE_ID;
    const token  = process.env.NETLIFY_BLOBS_TOKEN || process.env.NETLIFY_API_TOKEN;
    if (!siteID || !token) throw new Error('NETLIFY_BLOBS_TOKEN / SITE_ID manquant');
    const store = getStore({ name: 'form-submissions', siteID, token });
    const now = Date.now();
    const key = String(now) + '-' + Math.random().toString(36).slice(2, 8);
    const submission = {
      id: key,
      timestamp: now,
      iso: new Date(now).toISOString(),
      source: source,
      subject: baseSubject,
      visitorName: visitorLabel,
      email: replyTo,
      data: Object.fromEntries(Object.entries(data).filter(([k]) => !k.startsWith('_') && !k.startsWith('$'))),
      emailOk: emailOk,
      emailError: emailError
    };
    await store.setJSON(key, submission);
  } catch (blobErr) {
    console.error('Blobs error (non-fatal):', blobErr);
    // Non bloquant — l'important c'est l'email
  }

  if (emailOk) {
    return { statusCode: 200, headers, body: JSON.stringify({ ok: true }) };
  }
  return {
    statusCode: 500,
    headers,
    body: JSON.stringify({ ok: false, error: 'Envoi échoué : ' + emailError })
  };
};
