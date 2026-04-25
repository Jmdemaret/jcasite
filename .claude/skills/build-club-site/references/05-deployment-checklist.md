# Checklist de déploiement

À cocher dans l'ordre. Ne sauter aucune étape.

## Phase A — GitHub repo

- [ ] Créer le repo `username/club-name` (public ou privé selon le contexte)
- [ ] Copier les fichiers du template JCA :
  - `index.html`, `content.json`, `CNAME`, `robots.txt`, `sitemap.xml`
  - `manifest.webmanifest`, `favicon.svg` + PNG fallbacks
  - `dojo.jpeg` ou photo équivalent + `logo2.png`
  - `.gitignore`, `README.md`
  - `.github/workflows/google-reviews.yml` + script (si Reviews sync)
  - `netlify/functions/send.js` + `list.js` + `package.json` + `netlify.toml`
- [ ] **Ne pas copier** `admin.html` du JCA (le client va recevoir le sien)
- [ ] Commit initial + push

## Phase B — GitHub Pages

- [ ] Repo Settings → Pages → Source: Deploy from a branch
- [ ] Branch: `main` · Folder: `/ (root)` → Save
- [ ] Vérifier que le site est en ligne sur `username.github.io/repo-name`
- [ ] Si custom domain : Settings → Pages → Custom domain → entrer le domaine
- [ ] Vérifier "Enforce HTTPS" coché

## Phase C — Custom domain (si applicable)

Chez le registrar (Combell, Gandi, OVH...) :
- [ ] Configurer 4 enregistrements A pour `@` :
  ```
  185.199.108.153
  185.199.109.153
  185.199.110.153
  185.199.111.153
  ```
- [ ] Configurer CNAME pour `www` → `username.github.io.`
- [ ] Attendre propagation (généralement 15min-2h, jusqu'à 24h)
- [ ] Vérifier avec `dig domain.tld` ou https://dnschecker.org/

## Phase D — Branding & contenu

- [ ] `index.html` : remplacer les couleurs brand dans Tailwind config
- [ ] `index.html` : changer fonts si demandé
- [ ] `index.html` : remplacer le titre, meta description, OG, Twitter Card
- [ ] `index.html` : adapter Schema.org JSON-LD avec :
  - Type approprié (`SportsClub`, `LocalBusiness`, `Restaurant`, etc.)
  - Adresse, téléphone, email
  - Coordonnées GPS
  - Horaires
  - URL du logo
- [ ] `index.html` : adapter le menu (nav links + sections IDs)
- [ ] `index.html` : adapter la map Leaflet (coords + popup)
- [ ] Remplacer `logo2.png` par le nouveau logo
- [ ] Remplacer `dojo.jpeg` par la photo hero
- [ ] Régénérer `favicon.svg` + PNG via `_gen_favicons.py` (modifier d'abord le SVG)
- [ ] `content.json` : remplir avec le contenu initial
- [ ] `sitemap.xml` : remplacer toutes les URLs par le nouveau domaine
- [ ] `robots.txt` : remplacer l'URL du sitemap
- [ ] `CNAME` : mettre le bon domaine

## Phase E — Netlify (si formulaires)

- [ ] Créer un compte Netlify (gratuit) si pas déjà fait
- [ ] Add new site → Import from GitHub → choisir le repo
- [ ] Build settings : déjà OK avec `netlify.toml`, juste valider
- [ ] Site name : choisir un nom (ou laisser le random)
- [ ] **Site settings → Environment variables** ajouter :
  ```
  SMTP_HOST           ex: smtp-auth.mailprotect.be
  SMTP_PORT           587
  SMTP_USER           contact@domain.tld
  SMTP_PASS           [mot de passe email]
  RECIPIENT_EMAIL     destinataire (peut être différent de SMTP_USER)
  ALLOWED_ORIGIN      https://domain.tld (en prod)
  LIST_SECRET         [secret généré aléatoirement, 24+ chars]
  NETLIFY_BLOBS_TOKEN [PAT Netlify pour Blobs]
  ```
- [ ] Trigger deploy (Clear cache and deploy)
- [ ] Tester le formulaire en envoyant un message test
- [ ] Récupérer l'URL de la fonction (`https://site-xxxxx.netlify.app/.netlify/functions/send`)
- [ ] Mettre cette URL dans `content.json.forms.scriptUrl`
- [ ] Republier (commit + push)

## Phase F — Analytics

### Si Umami :
- [ ] Créer compte sur cloud.umami.is
- [ ] Add website → coller le domaine
- [ ] Récupérer le snippet `<script defer src="https://cloud.umami.is/script.js" data-website-id="...">`
- [ ] Ajouter dans le `<head>` d'`index.html`
- [ ] Vérifier dans le dashboard Umami qu'une visite est tracée

### Si rien :
- [ ] Skipper

## Phase G — Google Search Console

- [ ] Aller sur https://search.google.com/search-console
- [ ] Add property → URL prefix → `https://domain.tld/`
- [ ] Méthode HTML tag :
  - Récupérer le `content="..."` de la balise meta
  - Soit : ajouter dans le `<head>` `<meta name="google-site-verification" content="...">`
  - Soit : créer un fichier `google[hash].html` à la racine avec le contenu attendu
- [ ] Cliquer Verify → ✓
- [ ] Sitemaps → Add new sitemap → `sitemap.xml`
- [ ] URL Inspection → coller la home → Request Indexing
- [ ] Tester rich results : https://search.google.com/test/rich-results?url=...

## Phase H — Google Business Profile (SEO local)

- [ ] Si pas créé : https://business.google.com → Create profile
- [ ] Compléter : adresse, horaires, téléphone, site web, photos
- [ ] Demander 2-3 avis aux premiers clients/membres
- [ ] (Pour Reviews sync auto : récupérer le Place ID via https://developers.google.com/maps/documentation/places/web-service/place-id)

## Phase I — Google Reviews sync (si activé)

- [ ] Créer compte sur https://serpapi.com (free tier 100 calls/mois)
- [ ] Récupérer la `SERPAPI_KEY` dans le dashboard
- [ ] Repo Settings → Secrets and variables → Actions → New repository secret :
  - `SERPAPI_KEY` = clé SerpAPI
  - `GOOGLE_PLACE_ID` = ChIJ... (Place ID du business)
- [ ] Actions → Sync Google Reviews → Run workflow → vérifier que `google-reviews.json` est créé

## Phase J — Admin local pour le client

- [ ] Adapter l'admin du JCA (admin.html) avec :
  - Owner / Repo / Branch par défaut pré-remplis
  - URL du Netlify endpoint (list) déjà saisie
  - Brand colors qui matchent le site
- [ ] Le client crée un PAT GitHub fine-grained avec write sur le repo
- [ ] Lui transmettre `admin.html` + le secret LIST_SECRET (canal sécurisé : Signal/WhatsApp chiffré)
- [ ] Test : connexion admin + publication d'un test
- [ ] Démontrer toutes les fonctions : ajouter actu, événement, photo, annonce, restore version

## Phase K — Pages légales

- [ ] Créer `/privacy.html` (Politique de confidentialité)
- [ ] Créer `/mentions-legales.html` (selon obligations locales)
- [ ] Créer `/cgu.html` ou `/cgv.html` si commerce
- [ ] Lier ces pages depuis le footer

## Phase L — QA final

- [ ] **Mobile** : tester sur smartphone réel (375-390px), pas juste devtools
- [ ] **Desktop** : Chrome / Firefox / Safari
- [ ] **Accessibilité** : tab navigation, contrast ratios, alt sur images
- [ ] **Vitesse** : PageSpeed Insights > 80 mobile, > 90 desktop
- [ ] **Liens** : tous les liens internes/externes fonctionnent
- [ ] **Forms** : 1 envoi test sur chaque formulaire, l'email arrive
- [ ] **Schema.org** : validateur Google passe sans erreur
- [ ] **Open Graph** : preview sur https://opengraph.dev/ ou en partageant sur Facebook
- [ ] **Sitemap** : visiter `/sitemap.xml` → XML valide
- [ ] **robots.txt** : visiter `/robots.txt` → contenu correct
- [ ] **Favicon** : visible dans l'onglet du navigateur, sur mobile (Add to home screen)

## Phase M — Lancement

- [ ] Communication : post Facebook, email à la liste membres, story Instagram
- [ ] Mettre à jour Google Business Profile avec la nouvelle URL
- [ ] Mettre à jour signatures email du client
- [ ] Mettre à jour cartes de visite si commande
- [ ] Mettre à jour profils réseaux sociaux (URL site dans bio)

## Phase N — Suivi (1 mois après lancement)

- [ ] Vérifier dans Search Console que le site est indexé
- [ ] Vérifier dans Umami le trafic
- [ ] Vérifier que les formulaires arrivent bien
- [ ] Mettre à jour le contenu si retours négatifs/positifs
- [ ] Demander 5 avis Google supplémentaires aux clients
