# Questionnaire de découverte — Nouveau site

Document à remplir AVEC le client lors d'un appel de 30-60 min. Ne pas envoyer en mode "à remplir tout seul" — la moitié des cases resteront vides ou floues.

Format de chaque question :
- **Question** (court)
- *Pourquoi on demande* (au cas où le client ne comprend pas)
- Réponse(s) typique(s) ou défaut

À la fin, sauvegarder cette feuille comme `PROJECT.md` dans la racine du nouveau repo.

---

## 1. Identité de l'organisation

### 1.1 Nom officiel
*Apparaît dans les meta tags, sitemap, JSON-LD, Schema.org.*
> Réponse : __________

### 1.2 Type d'organisation
- [ ] Sports club / association
- [ ] ASBL / charity
- [ ] École privée
- [ ] Restaurant / café
- [ ] Cabinet professionnel (médecin, avocat, kiné…)
- [ ] Freelance / consulting
- [ ] Petite entreprise
- [ ] Autre : __________

### 1.3 Mission en 1 phrase
*Pour le hero du site et la meta description.*
> Réponse : __________

### 1.4 Année de création
*Si > 5 ans, c'est un argument crédibilité. Si neuf, on insiste sur autre chose.*
> Réponse : __________

### 1.5 Adresse physique
*Apparaît dans le footer, Schema.org, Google Maps, sitemap.*
- Rue + numéro : __________
- Code postal + ville : __________
- Pays : __________
- Coordonnées GPS (lat, lon) : __________ *(à récupérer sur OpenStreetMap si pas connues)*

### 1.6 Contact
- Email principal (visible publiquement) : __________
- Email réception formulaires (peut être différent) : __________
- Téléphone : __________
- WhatsApp ? (numéro si différent) : __________

### 1.7 Site web actuel
*Pour migration et benchmark.*
- URL : __________
- CMS / hébergeur actuel : __________
- Ce qui marche et qu'on garde : __________
- Ce qui ne marche pas : __________

---

## 2. Marque & identité visuelle

### 2.1 Logo
- [ ] Logo existant fourni en : SVG / PNG haute résolution / PDF / autre
- [ ] À redessiner par un designer
- [ ] Pas de budget logo → faire avec un texte stylisé en attendant

### 2.2 Couleurs de marque
*Dans la JCA on a paper #FBF6E9, sumi #1D1916, hinomaru #C8102E, royal #6E4C92, gold #B99A5A. Pour le nouveau site on adapte.*
- Couleur primaire (accent fort) : __________
- Couleur secondaire (accent doux) : __________
- Fond (clair / sombre / nuancé) : __________
- Texte principal : __________

Si pas connues : demander 3 sites web que le client trouve beaux et déduire de là.

### 2.3 Typographie
- Préférence existante ? (font name) : __________
- Style souhaité : moderne / traditionnel / luxueux / playful / japonisant / minimaliste
- Combinaison habituelle : 1 serif display + 1 sans-serif lecture

### 2.4 Mood / ambiance
*Choisir 3 mots qui décrivent le site rêvé.*
- 1 : __________
- 2 : __________
- 3 : __________

### 2.5 Tone of voice
- "Tu" ou "Vous" ? __________
- Formel / décontracté / familial / professionnel ? __________
- Émojis OK ou jamais ? __________
- Termes techniques (jargon métier) : à éviter / à embrasser ? __________

### 2.6 Sites de référence
*Demander 3-5 sites concrets que le client aime. Encore mieux : ce qui leur plaît dans chacun.*
- 1 : __________
- 2 : __________
- 3 : __________
- 4 : __________
- 5 : __________

---

## 3. Contenu & sections

### 3.1 Sections obligatoires (cocher)
- [ ] Hero (page d'accueil avec CTA)
- [ ] À propos / histoire
- [ ] Services / cours / produits / activités
- [ ] Tarifs / cotisation
- [ ] Équipe / staff
- [ ] Galerie photo
- [ ] Actualités / blog
- [ ] Calendrier / événements
- [ ] Témoignages (écrits et/ou Google Reviews)
- [ ] FAQ
- [ ] Sponsors / partenaires
- [ ] Mentions légales / RGPD
- [ ] Contact (formulaire + carte)
- [ ] Pré-inscription / réservation cours d'essai
- [ ] Section sur mesure : __________

### 3.2 Galerie
- [ ] Pas de galerie (juste des photos en illustration des sections)
- [ ] Galerie unique (toutes les photos en vrac)
- [ ] **Galerie par albums** (recommandé pour clubs avec compétitions/événements distincts)

### 3.3 Calendrier / horaires
- [ ] Horaires fixes (ex: cours hebdo récurrents) → éditeur calendrier visuel
- [ ] Événements ponctuels (ex: stages, tournois) → liste d'événements
- [ ] Les deux (cas judo)
- [ ] Système de réservation en ligne avec disponibilité ⚠️ **NON SUPPORTÉ par le template** — il faut un service tiers (Calendly, Eventbrite, SimplyBook)

### 3.4 Tarifs
- [ ] Affichage simple (1 prix par formule)
- [ ] Tableau avec plusieurs colonnes (jeunes/adultes/famille…)
- [ ] Tarif "sur devis" (formulaire de contact)
- [ ] **Paiement en ligne** ⚠️ **NON SUPPORTÉ** — recommander Stripe Payment Links / PayPal.me / virement bancaire

---

## 4. Fonctionnalités

### 4.1 Formulaires
- [ ] Contact (nom, email, message)
- [ ] Pré-inscription (nom, prénom, âge enfant, téléphone, message…)
- [ ] Newsletter (email seul → service tiers comme Brevo/MailerLite)
- [ ] Custom : __________

Pour chaque, lister les champs requis.

### 4.2 Bandeaux d'annonces
- [ ] Système date-driven (vacances, fermetures auto-affichées)
- [ ] Pas besoin (un site sans annonces périodiques)

### 4.3 Multilingue
- [ ] Une seule langue : __________
- [ ] Bilingue FR/NL (Belgique standard)
- [ ] Trilingue FR/NL/EN
- [ ] Plus de 3 langues ⚠️ **template pas idéal**

⚠️ Multilingue = forte augmentation de complexité (i18n, contenu dupliqué à maintenir, SEO par langue). Si bilingue obligatoire, prévoir 2× plus de temps.

### 4.4 Espace privé / membres
- [ ] Pas besoin
- [ ] Espace réservé par mot de passe (statique, simple)
- [ ] Comptes individuels par membre ⚠️ **template pas adapté** — Wordpress + plugin membership

### 4.5 E-commerce
- [ ] Pas besoin
- [ ] Quelques produits (1-10) → Stripe Payment Links suffisent
- [ ] Catalogue 10+ produits ⚠️ **utiliser Shopify ou Wordpress + WooCommerce**

### 4.6 Recherche interne
- [ ] Pas besoin (site < 10 pages)
- [ ] Voulu mais accepter une recherche basique côté client

### 4.7 Newsletter
- [ ] Pas besoin
- [ ] Brevo (Sendinblue) free tier
- [ ] MailerLite free tier
- [ ] Mailchimp (payant rapidement)

---

## 5. Intégrations externes

### 5.1 Email transactionnel (formulaires)
- Email existant + SMTP : oui / non
- Si oui : hébergeur + paramètres SMTP (host, port, user) : __________
- Si non : créer un email pro chez Combell / OVH / Gandi → coût ~3-5€/mois

### 5.2 Réseaux sociaux
- Facebook : URL de la page : __________ (existe-t-elle ? est-elle utilisée ?)
- Instagram : __________
- WhatsApp : __________
- YouTube : __________
- TikTok : __________
- LinkedIn : __________
- Strava (sport) : __________

### 5.3 Services Google
- Google Business Profile (essentiel pour SEO local) : existe ? URL : __________
- Google Maps Place ID (pour Schema.org) : __________
- Google Search Console (pour SEO monitoring) : à créer
- Google Reviews à afficher sur le site ? oui / non
  - Si oui : compte SerpAPI (free tier 100 calls/mois)

### 5.4 Analytics
- [ ] Aucune (vie privée totale)
- [ ] **Umami Cloud** (free 100k events/mois, GDPR-OK, pas de cookie banner) — recommandé
- [ ] GoatCounter (gratuit, ultra simple)
- [ ] Plausible (9€/mois, dashboard joli)
- [ ] Cloudflare Web Analytics (gratuit si DNS via Cloudflare)
- [ ] Google Analytics ⚠️ nécessite un cookie banner GDPR

### 5.5 Booking / réservation
*Si client veut réserver un essai/cours via le site.*
- [ ] Calendly free
- [ ] SimplyBook
- [ ] Cal.com
- [ ] Eventbrite (événements ponctuels)
- [ ] Aucun → formulaire de contact suffit

### 5.6 Paiement
*Pour cotisation, dons, achat.*
- [ ] Aucun (paiement hors ligne)
- [ ] Stripe Payment Links (gratuits, ~1.5% par transaction)
- [ ] PayPal.me
- [ ] Virement bancaire (RIB affiché)
- [ ] Tirelime / GoFundMe / HelloAsso (asso française)

---

## 6. Hébergement & domaine

### 6.1 Domaine
- [ ] Domaine existant : __________
  - Registrar (où acheté) : __________
  - DNS géré par : __________
- [ ] À acheter (suggérer Combell, Gandi, OVH)
- [ ] Pas de domaine personnalisé (utiliser le default `username.github.io/repo`)

### 6.2 Coût annuel acceptable
- [ ] 0€ (tout doit être gratuit)
- [ ] 0-30€/an (domaine seul)
- [ ] 30-100€/an (domaine + email pro)
- [ ] 100€+/an (services premium, analytics payant…)

---

## 7. Maintenance & accès

### 7.1 Qui va éditer le contenu
- Personne référente : __________
- Niveau technique : débutant / intermédiaire / avancé
- À l'aise avec une interface admin web : oui / non
- Plusieurs personnes vont éditer ? __________

### 7.2 Fréquence de mise à jour
- [ ] Très occasionnelle (1× / mois ou moins)
- [ ] Régulière (2-4× / mois)
- [ ] Fréquente (1× / semaine)
- [ ] Quotidienne ⚠️ — peut-être prévoir un workflow plus léger

### 7.3 Backup & sécurité
- Backup auto via GitHub history : OK
- Restauration version précédente : intégrée
- Permissions différentes par utilisateur : oui / non (le template = un seul niveau admin)

---

## 8. Légal & RGPD

### 8.1 Mentions légales
*Obligatoires en Belgique/France pour tout site web.*
- Nom officiel de l'organisation : __________
- Numéro d'entreprise / TVA / ASBL : __________
- Adresse siège social : __________
- Représentant légal : __________

### 8.2 Privacy policy
*Obligatoire si tu collectes des données (formulaires, analytics, cookies).*
- Existe déjà : oui / non
- Données collectées : email contact, IP via analytics, photos, autres
- Durée de conservation des données : __________

### 8.3 Cookies & RGPD
- Cookies utilisés : oui (GA, Umami avec ID, etc.) / non (Umami sans cookie, Plausible)
- Si oui : besoin de bandeau de consentement RGPD ⚠️
- Recommandation : choisir analytics sans cookie pour éviter le bandeau

### 8.4 Photos de personnes (RGPD)
- Photos de personnes identifiables (membres) : oui / non
- **Photos d'enfants** : oui / non
- Si oui : autorisation parentale **obligatoire** au format écrit avant publication
- Modèle d'autorisation à fournir : __________

---

## 9. SEO & marketing

### 9.1 Mots-clés cibles
*Pour quoi le client veut être trouvé sur Google.*
- Top 3 (ex: "judo Anderlecht", "cours judo enfants Bruxelles") :
  - 1 : __________
  - 2 : __________
  - 3 : __________
- Zone géographique : __________

### 9.2 Concurrence
- 3 concurrents directs (URL) : __________

### 9.3 Stratégie de contenu
- [ ] Aucune (juste être trouvable)
- [ ] Blog régulier (1-2 articles/mois)
- [ ] Vidéos (Reels, YouTube Shorts)
- [ ] Newsletter

### 9.4 Pub payante envisagée
- [ ] Aucune
- [ ] Google Ads
- [ ] Meta Ads (Facebook/Instagram)
- [ ] Budget mensuel : __________

---

## 10. Timeline

### 10.1 Deadline
- Souhaitée : __________
- Hard (anniversaire, rentrée, événement) : __________

### 10.2 Stratégie de lancement
- [ ] Soft launch (mise en ligne discrète, on ajuste)
- [ ] Lancement promotionnel (post Facebook, email aux membres, événement)

### 10.3 Priorité MVP vs full
- [ ] MVP rapide (3-5 sections, pas de gallerie complexe, pas d'analytics) — 1-2 jours dev
- [ ] Full featured (toutes sections, calendrier, analytics, RSS, restore) — 2-3 jours dev + 2 semaines collecte contenu

---

## 11. Assets à fournir par le client

Checklist à donner au client après l'interview :

- [ ] Logo en SVG ou PNG haute résolution (>1000px)
- [ ] 5-10 photos haute qualité (>1500px de large) : dojo/local, équipe, ambiance, action
- [ ] Texte de présentation (mission, histoire) — 200-300 mots
- [ ] Bios de l'équipe (3-5 lignes par personne + 1 photo portrait)
- [ ] Liste complète des services/cours/horaires
- [ ] Tarifs détaillés
- [ ] Liste des sponsors/partenaires + leurs logos en SVG/PNG
- [ ] Témoignages (3-5 minimum)
- [ ] FAQ (5-10 questions courantes)
- [ ] Mentions légales rédigées
- [ ] Privacy policy rédigée (ou validée par juriste)
- [ ] Autorisations parentales si photos d'enfants

⚠️ **80% des projets bloquent ici, pas sur le code.** Le client n'a souvent pas tout ce matériel et il faut l'aider à le rassembler / le rédiger.

---

## 12. Risques & inquiétudes du client

*Question ouverte importante : qu'est-ce qui leur fait peur dans ce projet ?*

> Réponse client : __________

Reformuler comment chaque inquiétude est adressée par la solution proposée.

---

## Sortie

Ce document rempli devient le **brief technique du projet**. À sauvegarder :
- Dans le repo du nouveau projet (`PROJECT.md`)
- Dans le drive partagé client/dev
- Mis à jour à chaque évolution majeure
