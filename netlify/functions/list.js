/**
 * Judo Club Anderlecht — Liste des soumissions de formulaires (admin)
 *
 * Retourne les N dernières soumissions stockées via Netlify Blobs.
 * Authentification via un secret partagé (env var LIST_SECRET) passé en header
 * Authorization: Bearer <secret> OU query ?key=<secret>.
 *
 * Variables d'environnement requises :
 *   LIST_SECRET   Un mot de passe arbitraire, partagé entre cette fonction et l'admin.
 *                 Exemple : openssl rand -base64 24  →  mettre dans Netlify env + localStorage admin.
 *   ALLOWED_ORIGIN  (facultatif)  ex: https://judoclubanderlecht.be
 */

const { getStore } = require('@netlify/blobs');

exports.handler = async (event) => {
  const allowedOrigin = process.env.ALLOWED_ORIGIN || '*';
  const headers = {
    'Access-Control-Allow-Origin': allowedOrigin,
    'Access-Control-Allow-Headers': 'Content-Type, Authorization',
    'Access-Control-Allow-Methods': 'GET, DELETE, OPTIONS',
    'Content-Type': 'application/json'
  };

  if (event.httpMethod === 'OPTIONS') {
    return { statusCode: 204, headers, body: '' };
  }

  // Auth : Bearer token ou ?key=
  const expected = process.env.LIST_SECRET;
  if (!expected) {
    return { statusCode: 500, headers, body: JSON.stringify({ ok: false, error: 'LIST_SECRET non configuré côté serveur' }) };
  }
  const authHeader = event.headers.authorization || event.headers.Authorization || '';
  const bearer = authHeader.startsWith('Bearer ') ? authHeader.slice(7) : '';
  const qkey = (event.queryStringParameters || {}).key || '';
  const provided = bearer || qkey;
  if (provided !== expected) {
    return { statusCode: 401, headers, body: JSON.stringify({ ok: false, error: 'Non autorisé' }) };
  }

  const store = getStore('form-submissions');

  // DELETE : supprimer une soumission précise (?id=...) ou toutes (?all=1)
  if (event.httpMethod === 'DELETE') {
    const p = event.queryStringParameters || {};
    if (p.all === '1') {
      const { blobs } = await store.list();
      for (const b of blobs) await store.delete(b.key);
      return { statusCode: 200, headers, body: JSON.stringify({ ok: true, deleted: blobs.length }) };
    }
    if (p.id) {
      await store.delete(p.id);
      return { statusCode: 200, headers, body: JSON.stringify({ ok: true }) };
    }
    return { statusCode: 400, headers, body: JSON.stringify({ ok: false, error: 'Missing id or all=1' }) };
  }

  // GET : liste des soumissions
  try {
    const { blobs } = await store.list();
    const items = [];
    for (const b of blobs) {
      try {
        const v = await store.get(b.key, { type: 'json' });
        if (v) items.push(v);
      } catch (_) { /* skip corrupted */ }
    }
    // Tri descendant par timestamp (plus récent en premier)
    items.sort((a, b) => (b.timestamp || 0) - (a.timestamp || 0));
    const limit = Math.min(parseInt((event.queryStringParameters || {}).limit || '50', 10), 200);
    return {
      statusCode: 200,
      headers,
      body: JSON.stringify({ ok: true, total: items.length, items: items.slice(0, limit) })
    };
  } catch (err) {
    console.error('List error:', err);
    return { statusCode: 500, headers, body: JSON.stringify({ ok: false, error: err.message }) };
  }
};
