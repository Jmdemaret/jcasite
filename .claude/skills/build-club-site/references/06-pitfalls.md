# Pièges courants & comment les éviter

## 🚨 Pièges techniques

### 1. CORS sur les Netlify Functions
**Symptôme** : "Failed to fetch" depuis l'admin local (`file://`).
**Cause** : `ALLOWED_ORIGIN` restreint à un domaine, mais admin tourne en `file://` (origine `null`).
**Fix** : Pour les endpoints d'admin protégés par secret (comme `list.js`), mettre `Access-Control-Allow-Origin: *`. Pour les endpoints publics (comme `send.js`), garder strict.

### 2. Conflit de sha GitHub
**Symptôme** : "content.json does not match <sha>" lors d'un publish.
**Cause** : un autre admin a publié entre temps, ou un workflow GitHub a modifié content.json (Google Reviews sync).
**Fix** : Implémenter un retry auto dans `publish()` : re-fetch le sha avant le PUT, et retry une fois en cas de 409.

### 3. Photos uploadées via admin invisibles dans l'admin
**Symptôme** : photos OK sur le site live, mais cassées dans l'admin local.
**Cause** : admin tourne en `file://`, les photos sont sur GitHub mais le PC local ne les a pas.
**Fix** : Dans l'admin, rewriter les chemins relatifs vers `https://raw.githubusercontent.com/...` pour le rendering. Voir `_adminImgSrc()` dans le JCA.

### 4. Google Search Console "Page en double"
**Symptôme** : message "Google n'a pas choisi la même URL canonique que l'utilisateur".
**Cause fréquente** : sitemap qui liste des URLs avec fragments (`/#cours`, `/#tarifs`) — Google les voit comme la même page dupliquée.
**Fix** : Dans `sitemap.xml`, ne mettre QUE la home URL. Pas de fragments.

### 5. Bandeau cache la moitié du site
**Symptôme** : avec plusieurs annonces empilées, le hero est masqué.
**Cause** : `body` n'a pas de `padding-top`, le contenu reste sous le bandeau fixed.
**Fix** : `body { padding-top: var(--bh, 0px); }` + s'assurer que `--bh` reflète bien la hauteur réelle des annonces.

### 6. SMTP Combell port 25 bloqué sur Netlify
**Symptôme** : "ETIMEDOUT" sur 25.
**Cause** : Netlify bloque les sorties sur port 25 (anti-spam).
**Fix** : Utiliser `smtp-auth.mailprotect.be:587` (STARTTLS).

### 7. Netlify Blobs "MissingBlobsEnvironmentError"
**Symptôme** : la fonction crash à l'usage de `getStore()`.
**Cause** : legacy `exports.handler` ne fait pas l'auto-config Blobs.
**Fix** : Passer `siteID` + `token` explicitement. Le siteID est fourni via env vars Netlify (`SITE_ID`), le token doit être un Personal Access Token Netlify créé manuellement et stocké comme env var (`NETLIFY_BLOBS_TOKEN`).

### 8. Push rejeté après workflow GitHub Actions
**Symptôme** : `git push` échoue avec "fetch first" alors qu'on vient de cloner.
**Cause** : un workflow (Google Reviews) a fait un commit pendant qu'on travaillait localement.
**Fix** : `git pull --rebase && git push` systématique avant chaque push.

### 9. Photos en base64 dans content.json (heavy)
**Symptôme** : content.json fait 5+ MB, lent à charger.
**Cause** : photos uploadées via admin en base64 sans migration vers `/images/`.
**Fix** : implémenter `migrateGalleryBase64()` qui upload chaque base64 en fichier physique avant le commit content.json.

### 10. Rate limit GitHub
**Symptôme** : "API rate limit exceeded" en pleine session admin.
**Cause** : trop de requêtes API en peu de temps (uploads de 20 photos d'un coup).
**Fix** : Token authentifié = 5000 req/h (vs 60 sans). Toujours utiliser PAT. Si quand même atteint : ajouter du throttling dans le code.

---

## 💼 Pièges projet (humains, organisationnels)

### 11. Contenu jamais fourni
**Symptôme** : 6 mois après le début, le client n'a toujours pas envoyé sa bio.
**Solution** : Donner une **deadline ferme** pour la livraison du contenu. Si dépassée, mettre un "Lorem ipsum" pour les bios manquantes — souvent ça motive le client à fournir.

### 12. Photos amateures au flash sur smartphone
**Symptôme** : galerie pleine de photos floues, surexposées, mal cadrées.
**Solution** : Avant le projet, demander si shooting photo pro nécessaire (~300-500€ pour 1 demi-journée). Sinon, fournir des conseils :
- Pas de flash, lumière naturelle (matin/fin d'après-midi)
- Photos paysage, pas portrait
- Privilégier l'action plutôt que les poses
- Cadrer avec espace pour le texte

### 13. "Faut que tout le monde puisse modifier"
**Symptôme** : le client veut donner accès admin à 10 personnes.
**Risque** : conflits de version, chaos, sécurité.
**Solution** : 1-2 admins maximum. Si plus de personnes doivent contribuer, créer un workflow où ils envoient leurs propositions à l'admin officiel.

### 14. "Je veux que ça ressemble à ce site SUPER complexe"
**Symptôme** : référence = Apple.com / Stripe / etc.
**Réalité** : ces sites ont des équipes de 50 designers / devs et des budgets de 6 chiffres.
**Solution** : Identifier UN aspect concret (couleurs, typo, layout d'une section) à reprendre. Ne pas essayer de cloner.

### 15. Demande de fonctionnalités hors scope en cours de projet
**Symptôme** : à mi-projet, le client veut un système de réservation de cours en ligne.
**Solution** : Refuser ou facturer en plus. Documenter le scope initial dans un PROJECT.md signé.

### 16. Lance et oublie
**Symptôme** : 2 ans après, le site n'a plus été modifié, les actus datent, les avis Google sont vieux.
**Solution** : Établir avec le client un **rythme minimum** (1 actu/mois, 1 nouvelle photo de séance/saison). Le contenu frais est crucial pour SEO et engagement.

### 17. Multilingue "juste au cas où"
**Symptôme** : client en Belgique demande FR + NL + EN dès le début.
**Réalité** : il a 5 visites/mois de néerlandophones et 0 d'anglophones.
**Solution** : Démarrer en monolingue, ajouter NL/EN seulement quand le besoin est démontré par les analytics.

---

## ⚖️ Pièges légaux

### 18. Photos d'enfants sans autorisation
**Risque** : amende RGPD, plainte parents.
**Solution** : 
- Modèle d'autorisation parentale écrit signé par les 2 parents AVANT publication
- Photos de groupe préférables aux portraits individuels
- Possibilité de retirer une photo à la demande (contact form)

### 19. Mentions légales manquantes
**Risque** : mise en demeure, amende.
**Obligations** (Belgique/France/EU) :
- Nom de l'entité légale + numéro d'enregistrement
- Adresse siège social
- Représentant légal (nom + email)
- Hébergeur (nom + adresse)

### 20. Cookie banner manquant alors qu'analytics avec cookies
**Risque** : amende RGPD (jusqu'à 4% CA mondial).
**Solution** : choisir analytics SANS cookie (Umami, Plausible, GoatCounter, Cloudflare Web Analytics) pour éviter le bandeau. Si GA4 obligatoire : implémenter un consent banner.

### 21. Privacy policy générique copiée d'un autre site
**Risque** : non-conforme, mensongère.
**Solution** : utiliser un générateur fiable (cookiebot.com, iubenda) ou faire valider par juriste. Adapter aux DONNÉES RÉELLES collectées.

---

## 📈 Pièges SEO

### 22. Indexation lente / pas d'indexation
**Symptôme** : 3 mois après lancement, site invisible dans Google.
**Causes** :
- Pas de Search Console configuré
- robots.txt qui bloque tout
- Sitemap pas soumis
- Site très récent (peu de backlinks)
**Solution** : Search Console + sitemap + 1 backlink local (ex: site de la commune, fédération, annuaire).

### 23. Site rapide mais SEO mauvais
**Symptôme** : PageSpeed 95 mais 0 visite organique.
**Cause** : SEO ≠ vitesse. Il faut aussi du contenu pertinent, des mots-clés bien placés, des backlinks.
**Solution** : Article mensuel (2 paragraphes suffisent) avec mots-clés métier, +backlinks locaux.

### 24. Mots-clés trop généraux
**Symptôme** : viser "judo" — impossible à classer (millions de pages).
**Solution** : viser long-tail local : "judo Anderlecht", "cours judo enfants Bruxelles 4 ans".

---

## 🛠 Pièges de design

### 25. Trop de polices différentes
**Symptôme** : 5 fonts différentes, illisible.
**Solution** : 2 fonts max (display + body), 3 si vraiment besoin (mono technique).

### 26. Animation/effet sur tout
**Symptôme** : tout bouge, tout pulse, le site donne le tournis.
**Solution** : 1-2 effets max, et toujours respecter `prefers-reduced-motion`.

### 27. Trop de couleurs
**Symptôme** : le site ressemble à un sapin de Noël.
**Solution** : palette restreinte. 1 couleur primaire + 1 secondaire + neutres (paper/sumi/gris). Accents très ponctuels.

### 28. Photos disparates
**Symptôme** : galerie de photos sans cohérence (filtres différents, qualités variables).
**Solution** : passage par un même preset Lightroom/VSCO. Ou simple correction : tout en JPEG quality 80, balance des blancs cohérente.

### 29. Texte par-dessus photo illisible
**Symptôme** : titre blanc sur photo qui a du blanc en arrière.
**Solution** : overlay sombre + text-shadow sur titre. Toujours tester sur la photo réelle.

### 30. Layout ne tient pas sur mobile
**Symptôme** : tout est cassé en dessous de 600px.
**Solution** : Mobile-first dès le début. Tester sur smartphone réel à chaque section terminée.
