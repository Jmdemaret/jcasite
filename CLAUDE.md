# CLAUDE.md

> Guide à destination de Claude (et de tout futur dev) pour travailler sur le site
> du **Judo Club Anderlecht**. Ce fichier est lu en priorité au début de chaque
> session. Mets-le à jour après chaque évolution architecturale notable.

---

## 1. Vue d'ensemble

**Site live** : https://judoclubanderlecht.be (custom domain)
**Repo GitHub** : https://github.com/Jmdemaret/jcasite (branche `main`)
**Site Netlify** : https://lovely-clafoutis-91f16b.netlify.app (uniquement les fonctions)
**Hébergement public** : GitHub Pages (statique)
**Owner** : Jean-Marc Demaret, trésorier du club

Le site est un **single-page** statique élégant (style éditorial japonisant) avec :
- Mosaïque éditoriale d'albums photo (lightbox masonry + photo)
- Bandeau d'information catégorisé (Information / Horaires vacances / Important)
- Carte interactive Leaflet avec arrêts transports + parking
- Schema.org riche (SportsClub, Organization, WebSite)
- Analytics privacy-first (Umami)
- Avis Google synchronisés automatiquement (workflow GitHub hebdo)
- Formulaires email via SMTP Combell + persistance Netlify Blobs

---

## 2. Architecture

```
┌─────────────────────────────────────────────────────────────┐
│  Site public — judoclubanderlecht.be                        │
│  (GitHub Pages, statique, CNAME)                            │
│   index.html ◄─── lit ──── content.json                     │
│                            rss.xml                          │
│                            google-reviews.json              │
│                            sitemap.xml                      │
│                            /images/                         │
└─────────────────────────────────────────────────────────────┘
        │  POST /.netlify/functions/send   (formulaires)
        │  GET  /.netlify/functions/list   (admin uniquement)
        ▼
┌─────────────────────────────────────────────────────────────┐
│  Netlify Functions                                          │
│  send.js : SMTP Combell + persistance Netlify Blobs         │
│  list.js : lecture des soumissions (auth Bearer LIST_SECRET)│
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│  Admin — admin.html (LOCAL, gitignored, file://)            │
│  Édite content.json + RSS + uploads images                  │
│  via GitHub Contents API (PAT du trésorier)                 │
└─────────────────────────────────────────────────────────────┘
        │  PUT /repos/.../content.json
        │  PUT /repos/.../images/xxx.jpg
        │  PUT /repos/.../rss.xml
        ▼
┌─────────────────────────────────────────────────────────────┐
│  GitHub Pages (déploiement auto sur push main, ~1 min)      │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│  GitHub Actions — workflow hebdo (lundi 06:00 UTC)          │
│  fetch_google_reviews.py : SerpAPI → google-reviews.json    │
└─────────────────────────────────────────────────────────────┘
```

---

## 3. Inventaire des fichiers

### À la racine (servis par GitHub Pages)
| Fichier | Rôle |
|---|---|
| `index.html` | Site public, single-page, ~3000 lignes |
| `content.json` | Données dynamiques du site (édité par admin) |
| `rss.xml` | Flux RSS (régénéré à chaque publish admin) |
| `sitemap.xml` | Sitemap pour Google (URL canonique unique) |
| `robots.txt` | Bloque `/admin.html` et `/.github/` aux crawlers |
| `google-reviews.json` | Avis Google fraîchis via SerpAPI hebdo |
| `manifest.webmanifest` | PWA manifest |
| `CNAME` | Custom domain GitHub Pages : `judoclubanderlecht.be` |
| `google84f0d08f9ecfa31a.html` | Verification Google Search Console |
| `favicon.svg` + `favicon-{16,32}.png` + `apple-touch-icon.png` + `icon-{192,512}.png` | Icônes du site |
| `dojo.jpeg`, `logo.png`, `logo2.png` | Images principales |
| `hero.mp4` | Vidéo hero (cinematic mode) |
| `/images/` | Photos uploadées via admin (auto-organisées) |
| `/sponsors/` | Logos partenaires (`anderlecht.svg`, `cocof.png`) |
| `/judoclubanderlecht/` | Photos additionnelles (kids, training) |

### Local-only (gitignored)
| Fichier | Rôle |
|---|---|
| `admin.html` | Interface admin auto-portée, lit/écrit via GitHub API |

### Outils & config
| Fichier | Rôle |
|---|---|
| `_gen_favicons.py` | Génère les PNG favicon depuis le SVG (Pillow) |
| `package.json` | Dépendances Netlify Functions |
| `netlify.toml` | Build config Netlify |
| `.gitignore` | Exclut `admin.html`, logos sources, `.claude/` |

### Backend serverless
| Fichier | Rôle |
|---|---|
| `netlify/functions/send.js` | Envoi SMTP + persistance Blobs |
| `netlify/functions/list.js` | API listing soumissions (admin) |

### CI/CD
| Fichier | Rôle |
|---|---|
| `.github/workflows/google-reviews.yml` | Cron hebdomadaire (lundi 06:00 UTC) |
| `.github/scripts/fetch_google_reviews.py` | Récupère avis via SerpAPI, paginé jusqu'à 5 pages (~40 avis) |

---

## 4. Modèle de données — `content.json`

Schéma simplifié (les défauts dans index.html prennent le relais si une clé manque) :

```jsonc
{
  "_meta": {
    "version": "1.0023",            // sémantique : 1.000X, incrémenté à chaque publish
    "publishedAt": "2026-04-25T...",
    "history": [                    // 50 dernières publications max
      { "version": "1.0023", "date": "...", "summary": "+1 album, 2 photos" }
    ]
  },
  "sections": {                     // toggle d'affichage par section
    "club": true, "cours": true, "tarifs": true, "actu": true,
    "evenements": true, "galerie": true, "equipe": true,
    "temoignages": true, "faq": true, "preInscription": true, "sponsors": true
  },
  "banner": {                       // LEGACY — utilisé en fallback si announcements vide
    "active": false,
    "type": "info",                 // info | horaires | important
    "text": "Texte du bandeau"
  },
  "announcements": [                // Calendrier de bandeaux automatiques (priorité sur banner)
    {
      "id": "ann-20261223-x9k",
      "type": "vacances",           // fermeture | vacances | important | information | evenement
      "title": "Congés de Noël",
      "message": "Reprise normale des cours pour tous les groupes.",
      "startDate": "2026-12-23",    // ISO YYYY-MM-DD
      "endDate": "2027-01-06",      // optionnel — si absent, date unique
      "showDaysBefore": 14,         // X jours avant startDate, l'annonce devient visible
      "showDaysAfter": 1,           // X jours après endDate, l'annonce reste visible
      "active": true                // toggle manuel
    }
  ],
  "texts": {                        // surcharge des textes par défaut (par section)
    "hero": { "title": "...", "stat1Label": "..." },
    "club": { "intro": "..." }
  },
  "groups": [],                     // groupes d'âge personnalisés (sinon défauts: 4-5, 5-7, 7-10, 11-15, 15+)
  "courses": [                      // planning hebdo (éditeur calendrier visuel)
    { "day": "Mercredi", "groupId": "4-5", "start": "14:15", "end": "15:00" }
  ],
  "pricing": [],                    // tarifs (vide = défauts)
  "team": [],                       // sensei (vide = défauts)
  "albums": [                       // galerie organisée en albums
    {
      "id": "album-20260424-x9k2",
      "title": "Championnat de Belgique 2026",
      "date": "2026-03-15",         // ISO
      "kanji": "試合",              // 行事|試合|稽古|昇級|道場|演武
      "description": "6 médailles dont 2 en or",
      "cover": "images/podium.jpg", // ou null = première photo
      "photos": [
        { "img": "images/xxx.jpg", "title": "...", "caption": "..." }
      ]
    }
  ],
  "gallery": [],                    // legacy (avant migration albums) — fallback
  "news": [],                       // actualités { date, title, body, image? }
  "events": [],                     // événements { date, title, type, loc }
  "testimonials": [],               // témoignages écrits (en + des avis Google)
  "googleReviewsHidden": [],        // IDs d'avis Google à masquer
  "googleReviewsPeriodMonths": 60,  // 0=tous, sinon nb de mois rétention
  "socials": {                      // réseaux sociaux pied de page
    "facebook":  { "url": "...", "active": true },
    "instagram": { "url": "...", "active": false },
    "whatsapp":  { "url": "...", "active": false },
    "youtube":   { "url": "",    "active": false }
  },
  "forms": {
    "scriptUrl": "https://lovely-clafoutis-91f16b.netlify.app/.netlify/functions/send",
    "recipientEmail": "..."
  }
}
```

### Versioning
- Format `1.000X` (4 décimales pour permettre des milliers de versions sans changer la longueur)
- Bump auto à chaque publish via `bumpVersion()`
- Si conflit de sha (publication parallèle), bump réaligné sur version en ligne + 1

---

## 5. Workflows critiques

### 5.1 Publication via admin
1. Trésorier ouvre `admin.html` (file://) → connect avec PAT GitHub
2. `ghGetContent()` → fetch `content.json` + sha
3. Édite l'état local en mémoire
4. Clic **Publier** :
   - Re-fetch sha (anti-conflit)
   - Bump version + ajoute entry historique avec résumé auto
   - **Migration base64 → /images/** : pour chaque photo encore en `data:`, upload via `ghPutBinary` puis remplace par chemin relatif
   - PUT `content.json` (avec retry auto sur conflit 409)
   - Régénère `rss.xml` (1 entrée par actu/event/album)
   - GitHub Pages déploie en ~1 min

### 5.2 Soumission formulaire
1. User soumet sur le site → POST JSON vers `/.netlify/functions/send`
2. `send.js` : honeypot check, construit email, envoie via Combell SMTP
3. **Toujours** stocke dans Netlify Blobs (`form-submissions` store) — même si email échoue
4. Trésorier voit dans admin → onglet Sécurité → "Formulaires reçus"

### 5.3 Avis Google (workflow hebdo)
- Cron lundi 06:00 UTC
- `fetch_google_reviews.py` lit `googleReviewsPeriodMonths` depuis content.json
- Pagine SerpAPI jusqu'à 5 pages (~40 avis max)
- Filtre par période, écrit `google-reviews.json`
- Commit auto si changements

### 5.4 Restauration de version
- L'admin liste l'historique stocké dans `_meta.history`
- Bouton **↶ Restaurer** par ligne (sauf version active)
- `ghGetCommits('content.json', 100)` → liste les 100 derniers commits qui ont touché content.json
- Match par regex `\bvX.XXXX\b` dans le message de commit
- `ghGetContentAtRef(sha)` → récupère content.json à ce commit
- Le state local est remplacé MAIS `_meta` actuel conservé (pas de régression de version)
- L'utilisateur prévisualise puis publie normalement → nouveau commit créé

### 5.5 Upload image (depuis admin)
- User glisse fichier → compressed (1600px max, quality 85) → base64 dans state
- À la publication : migration auto vers `/images/YYYYMMDD-HHMMSS-slug.ext`
- Filename via `makeImageFilename()` : timestamp + slug du titre
- Plus de base64 dans content.json après publication ✓

---

## 6. Secrets & services externes

### 6.1 GitHub
- **Repo** : `Jmdemaret/jcasite`
- **PAT (admin)** : Fine-grained, scope = repo, permissions Contents read/write, expiration 1 an
- **Stocké** : `localStorage` du navigateur du trésorier (jamais commité)

### 6.2 Netlify (env vars du site `lovely-clafoutis-91f16b`)
| Variable | Usage |
|---|---|
| `SMTP_HOST` | `smtp-auth.mailprotect.be` (port 587 STARTTLS) |
| `SMTP_PORT` | `587` |
| `SMTP_USER` | `send@judoclubanderlecht.be` |
| `SMTP_PASS` | mot de passe boîte Combell |
| `RECIPIENT_EMAIL` | destinataire des messages (= jmdemaret@gmail.com par défaut) |
| `ALLOWED_ORIGIN` | `https://judoclubanderlecht.be` (CORS strict pour `send`) |
| `LIST_SECRET` | Bearer token pour authentifier le dashboard admin → `list.js` |
| `NETLIFY_BLOBS_TOKEN` | Personal Access Token Netlify (legacy Functions API ne fait pas l'auto-config Blobs) |
| `SITE_ID` | (auto, fourni par runtime) |

> ⚠️ Le legacy `exports.handler` ne configure pas Blobs automatiquement. On passe siteID + token en explicite via `getStore({ name, siteID, token })`.

### 6.3 GitHub Actions secrets
| Secret | Usage |
|---|---|
| `SERPAPI_KEY` | Récupération des avis Google Maps (workflow hebdo) |
| `GOOGLE_PLACE_ID` | `ChIJ22u18afGw0cRHu7iNfdBoQ4` (Judo Club Anderlecht) |

### 6.4 Services tiers
| Service | URL/ID | Usage |
|---|---|---|
| **Umami Cloud** | `e6823a84-d558-440b-af10-99ede2da94ff` | Analytics sans cookie |
| **Combell SMTP** | `smtp-auth.mailprotect.be:587` | Email transactionnel |
| **SerpAPI** | account du trésorier | Scraping avis Google Maps |
| **Cloud Umami dashboard** | https://cloud.umami.is/websites/e6823a84-d558-440b-af10-99ede2da94ff | Vue des stats |
| **Google Search Console** | propriété URL prefix | SEO monitoring |

### 6.5 DNS (Combell)
- `A judoclubanderlecht.be → 185.199.108.153` (et 109/110/111)
- `CNAME www → jmdemaret.github.io`

---

## 7. Conventions de code

### 7.1 Versioning sémantique custom
- `1.000X` où X est l'incrément
- Stocké dans `content.json._meta.version`
- Affiché dans l'admin (badge top)

### 7.2 Commit messages
Format type-scope-description :
```
feat(gallery): Phase 2 — editorial magazine mosaic with lightbox
fix(seo): remove fragment URLs from sitemap
chore(gallery): remove hardcoded 柔 quote card
```
Types : `feat`, `fix`, `chore`, `docs`, `refactor`, `style`, `perf`

Footer obligatoire :
```
Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
```

### 7.3 Charte graphique (Tailwind extended)
| Couleur | Hex | Variable |
|---|---|---|
| Paper (fond) | `#FBF6E9` | `--paper` |
| Sumi (texte) | `#1D1916` | `--sumi` |
| Hinomaru (rouge accent) | `#C8102E` | `--hinomaru` |
| Royal (violet logo) | `#6E4C92` | `--royal` |
| Gold | `#B99A5A` | `--gold` |

### 7.4 Fonts
- Display : **Fraunces** (variable, opsz 144)
- Japan : **Shippori Mincho** (kanji)
- Sans : **Inter**
- Mono : **JetBrains Mono**

### 7.5 Patterns admin
- `_adminImgSrc(path)` : convertit chemin relatif → URL `raw.githubusercontent.com` (preview en file://)
- `data-requires-section="X"` : élément qui suit l'état d'une section (utilisé pour CTA hero)
- `markDirty()` / `markClean()` : tracking modifications
- `confirmDialog(title, body, btn, class)` : modale promise-based
- `toast(msg, type)` : notification éphémère (`ok` | `err` | `info`)

---

## 8. Décisions architecturales (les "pourquoi")

| Décision | Raison |
|---|---|
| **Hybride GitHub Pages + Netlify Functions** | Pages = gratuit, fast, SEO. Netlify = serverless free tier pour SMTP. Pas de serveur à maintenir. |
| **Admin en `file://`** | Aucun serveur d'admin = aucune surface d'attaque. PAT GitHub donne write scope précis sur le seul repo. |
| **`raw.githubusercontent.com` pour preview admin** | Le PC du trésorier n'a pas les images uploadées en local (ne pull pas). Raw URL = instantané post-commit, pas de wait Pages. |
| **Umami plutôt que GA** | Pas de cookie = pas de bandeau GDPR. Plus léger. Privacy-first match l'éthique club. |
| **RSS + Zapier plutôt que Graph API Facebook** | Évite la maintenance des Page Tokens (renouvellement 60j) et la complexité Facebook Developer. |
| **SerpAPI plutôt que Google Places API** | Évite Google Cloud Console (le trésorier avait galéré dessus). 100 calls free/mois suffit pour un cron hebdo. |
| **Schema.org JSON-LD au lieu de microdata** | Plus propre, séparé du HTML, plus facile à maintenir. |
| **Albums (Phase 2) avec migration auto depuis gallery plat** | Permet de faire évoluer le modèle sans casser le contenu existant. |
| **Bandeau catégorisé (Information / Horaires / Important)** | Un seul bandeau = simplicité. Catégorie pilote la couleur + l'animation. |
| **Versioning local 1.000X** | Format compact lisible. Permet d'identifier un commit du site sans regarder git. |

---

## 9. Troubleshooting / FAQ technique

### "Failed to fetch" sur le dashboard messages
→ CORS. Le `list.js` doit avoir `Access-Control-Allow-Origin: *` (admin tourne en `file://` donc origine `null`).

### "content.json does not match <sha>"
→ Conflit de sha (publication parallèle). L'admin retry auto une fois en re-fetchant le sha. Si ça persiste, cliquer **⟲ Recharger depuis GitHub**.

### Photos invisibles dans l'admin
→ L'admin tente de charger via le chemin relatif. Vérifier que `_adminImgSrc()` est utilisé partout. Si le navigateur a coupé le réseau, c'est normal.

### "Page en double" Google Search Console
→ Le sitemap listait des URLs avec fragments (`/#cours`). Maintenant unique URL canonique uniquement.

### Bandeau pas visible alors qu'activé
→ Vérifier `state.banner.message` non vide ET `state.banner.active === true`.

### Admin ouvre mais ne charge pas le contenu
→ Vérifier le PAT GitHub : expiré, supprimé, ou scope insuffisant. Recréer un PAT fine-grained avec `Contents: Read and write` sur le repo `jcasite`.

### Erreur "MissingBlobsEnvironmentError"
→ La fonction Netlify n'a pas `NETLIFY_BLOBS_TOKEN` configuré, ou il est expiré. Régénérer un PAT Netlify, mettre à jour env vars, **Clear cache and deploy**.

### Avis Google pas mis à jour
→ Vérifier le workflow GitHub Actions : Actions tab → "Sync Google Reviews" → dernière exécution. Si ✓ mais 0 avis, vérifier `googleReviewsPeriodMonths` (peut-être trop restrictif) et secrets `SERPAPI_KEY` / `GOOGLE_PLACE_ID`.

---

## 10. État actuel & TODO

### ✅ En place
- [x] Site responsive complet (hero, cours, tarifs, équipe, galerie albums, FAQ, sponsors, contact)
- [x] Système d'annonces date-driven (fermeture / vacances / important / information / événement) avec auto-display selon proximité, progress bar pour fermetures actives, kanji watermark, animations
- [x] Galerie éditoriale Phase 2 (mosaïque + lightbox masonry + photo lightbox)
- [x] SEO complet : meta, Open Graph, Twitter Card, Schema.org JSON-LD, robots.txt, sitemap.xml
- [x] Favicon SVG + PNG + manifest PWA
- [x] Analytics Umami
- [x] Avis Google synchronisés
- [x] Formulaires SMTP Combell + persistance Netlify Blobs
- [x] Dashboard messages dans admin
- [x] Anti-conflit sha auto-retry
- [x] **Restauration de version** depuis l'historique (un clic, fetch via API GitHub à un commit passé, l'état revient en local pour preview avant publish)
- [x] Migration auto base64 → /images/
- [x] Google Search Console vérifié + sitemap soumis
- [x] Onglet Guide intégré dans admin (pour secrétaire)

### 🚧 À faire (prioritaire)
- [x] **Calendrier des fermetures** (avec bandeau auto basé sur dates) — module Annonces
- [ ] **Éditeur tarifs visuel** (similaire à l'éditeur de cours, par lignes de produits)
- [ ] Schema.org Events (stages/tournois → onglet Events Google)
- [ ] Pages dédiées par groupe d'âge (`/judo-enfants-4-5-ans`) pour SEO long-tail

### 💡 Idées (back-burner)
- Newsletter (Brevo/MailerLite)
- Bouton flottant WhatsApp direct
- Calculateur tarifs interactif
- "Judoka du mois"
- Espace membres avec password
- Blog (2 articles/mois)
- Témoignages vidéo courtes
- Mode sombre toggle
- Countdown rentrée

### 🧹 Nettoyage à faire
- Photos en doublon à la racine : `Provincial.jpg`, `provincial.jpg`, `Regional.jpg`, `regional.jpg`, `provicial.jpg` (typo), `2.png`, `641184603_*.jpg`. À déplacer dans `/images/` ou supprimer.
- README.md mentionne encore "localStorage" pour le stockage admin → mettre à jour pour refléter "GitHub API"
- `hello-test.txt` est un fichier de test admin → on peut le laisser

---

## 11. Marketing & croissance (stratégie validée)

### Phase 1 — SEO gratuit (en cours, 2-3 mois)
- Google Business Profile (à créer si pas fait)
- Demander 2-3 avis Google par mois aux parents satisfaits
- Backlinks locaux : Anderlecht.be, LFJ, annuaires judo

### Phase 2 — Pub ciblée (budget 100-200€/mois, période rentrée)
- Google Ads Performance Max : code postal 1070 + 1030-1190
- Meta Ads : parents 28-45 ans rayon 5km
- Périodes clés : août → mi-octobre + janvier

### Phase 3 — Content & communauté
- Reels/Shorts 15-30sec
- Partenariats écoles (flyer + QR code)
- Visite pédiatres / kinés du quartier
- Journée portes ouvertes en septembre

### Phase 4 — Fidélisation
- Parrainage (-10% pour duo)
- Email annuel rétrospective avec photos
- Anniversaires enfants

---

## 12. Comment travailler sur ce repo

### Ouvrir une session de modification
1. `git pull` pour avoir la dernière version
2. Lire ce CLAUDE.md
3. Identifier la zone à toucher (data model ? rendering ? admin ? functions ?)

### Modifier le contenu via admin
- Ouvrir `admin.html` localement → modifs → Publier
- Ne **jamais** éditer `content.json` à la main si l'admin peut le faire (préserve le versioning + history)

### Modifier le code (HTML/CSS/JS)
1. Édition `index.html` ou `admin.html`
2. Validation syntaxe : `node -e "const fs=require('fs');const re=/<script(?![^>]*\bsrc=)[^>]*>([\s\S]*?)<\/script>/g;const html=fs.readFileSync('index.html','utf8');let m;while((m=re.exec(html))){try{new Function(m[1])}catch(e){console.error(e.message)}}"`
3. Test en preview local (juste ouvrir index.html dans le browser)
4. Commit avec message conforme + footer Co-Authored-By
5. `git pull --rebase && git push` (pull avant push, conflits fréquents avec workflow auto)

### Modifier les Netlify Functions
1. Édition `netlify/functions/*.js`
2. Push → Netlify redéploie auto (~1-2 min)
3. Tester le endpoint en GET/POST
4. Si nouvelle env var requise : la documenter section 6.2

### Mettre à jour le CLAUDE.md
À chaque évolution architecturale notable. Particulièrement :
- Nouveau secret externe
- Nouveau workflow
- Nouvelle dépendance
- Changement de modèle de données

---

## 13. Contacts & responsables

- **Trésorier (administrateur du site)** : Jean-Marc Demaret — jmdemaret@gmail.com
- **Email club** : `send@judoclubanderlecht.be` (boîte Combell, sender SMTP)
- **GitHub** : @Jmdemaret
- **Adresse club** : Rue du Serment 54, 1070 Anderlecht (lat 50.838389, lon 4.306456)

---

*Dernière mise à jour : 2026-04-25*
