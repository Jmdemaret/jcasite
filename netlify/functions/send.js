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
  const subject = data._subject || '[Site] Nouveau message';
  const source  = data._source  || 'site';
  const replyTo = (data.email || data.Email || '').trim();

  const lines = Object.keys(data)
    .filter(k => !k.startsWith('_'))
    .map(k => `  ${k} : ${data[k]}`);

  const textBody =
    `Nouveau message depuis ${source}\n` +
    `Date : ${new Date().toLocaleString('fr-BE')}\n\n` +
    `--- Contenu ---\n${lines.join('\n')}\n--- Fin ---\n`;

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

  try {
    await transporter.sendMail({
      from: `"Site Judo Club Anderlecht" <${process.env.SMTP_USER}>`,
      to: process.env.RECIPIENT_EMAIL || process.env.SMTP_USER,
      replyTo: replyTo || undefined,
      subject: subject,
      text: textBody
    });
    return { statusCode: 200, headers, body: JSON.stringify({ ok: true }) };
  } catch (err) {
    console.error('SMTP error:', err);
    return {
      statusCode: 500,
      headers,
      body: JSON.stringify({ ok: false, error: 'Envoi échoué : ' + (err.message || 'SMTP error') })
    };
  }
};
