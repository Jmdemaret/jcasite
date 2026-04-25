# Mode d'emploi complet — Skill `build-club-site`

Guide pratique pour utiliser la skill quand tu démarres un nouveau site.

---

## 🚀 Table des matières

1. [Installation (une fois)](#1-installation-une-fois)
2. [Avant de démarrer un nouveau projet](#2-avant-de-démarrer-un-nouveau-projet)
3. [Démarrer un projet — workflow complet](#3-démarrer-un-projet--workflow-complet)
4. [Exemple concret — un restaurant](#4-exemple-concret--un-restaurant-de-a-à-z)
5. [Bonnes pratiques](#5-bonnes-pratiques)
6. [Dépannage](#6-dépannage)
7. [Faire évoluer la skill](#7-faire-évoluer-la-skill)
8. [FAQ](#8-faq)

---

## 1. Installation (une fois)

### Option A — Globale (recommandée pour toi)

Pour que la skill soit disponible **dans n'importe quel dossier**, copie-la dans ton dossier Claude global.

**Windows (PowerShell)** :
```powershell
$src = "C:\Users\jean-\OneDrive\Documents\Judosite\.claude\skills\build-club-site"
$dst = "$env:USERPROFILE\.claude\skills\build-club-site"
New-Item -ItemType Directory -Force "$env:USERPROFILE\.claude\skills" | Out-Null
Copy-Item -Recurse -Force $src $dst
Write-Host "✓ Skill installée dans $dst"
```

**Mac/Linux** :
```bash
mkdir -p ~/.claude/skills
cp -r "/path/to/Judosite/.claude/skills/build-club-site" ~/.claude/skills/
echo "✓ Skill installée dans ~/.claude/skills/build-club-site"
```

### Option B — Par projet

Garder dans `.claude/skills/build-club-site/` du dépôt en cours. Avantage : versionnable avec le projet, partageable via GitHub. Inconvénient : faut la recopier dans chaque nouveau projet.

### Option C — Depuis GitHub

À chaque nouveau projet, récupérer la skill depuis le repo JCA :

```bash
mkdir -p .claude/skills
git clone --filter=blob:none --sparse https://github.com/Jmdemaret/jcasite /tmp/jca-skill
cd /tmp/jca-skill && git sparse-checkout set .claude/skills/build-club-site && cd -
cp -r /tmp/jca-skill/.claude/skills/build-club-site .claude/skills/
rm -rf /tmp/jca-skill
```

---

## 2. Avant de démarrer un nouveau projet

### Prérequis côté toi

- [ ] Compte GitHub avec PAT créé (fine-grained, lifetime ≥ 1 an)
- [ ] Compte Netlify (free tier) — uniquement si formulaires
- [ ] Compte Umami Cloud (free tier) — uniquement si analytics
- [ ] Compte SerpAPI (free tier 100 calls/mois) — uniquement si Google Reviews sync

### Prérequis côté client

Avant le premier rendez-vous, demande au client de préparer :
- [ ] Logo en SVG ou PNG haute résolution
- [ ] 5-10 photos haute qualité (1500px+ de large)
- [ ] Texte de présentation (mission, histoire) en 200-300 mots
- [ ] Liste exhaustive des services / cours / produits
- [ ] Tarifs détaillés
- [ ] Bios équipe + 1 portrait par personne
- [ ] Liste des sponsors / partenaires + leurs logos
- [ ] FAQ (5-10 questions courantes)
- [ ] Adresse exacte + coordonnées GPS du local
- [ ] Identifiants des réseaux sociaux

> 💡 **Conseil** : envoie cette checklist au client par email **avant le rdv découverte**. 80% des projets bloquent sur la collecte de contenu, pas sur le code.

---

## 3. Démarrer un projet — workflow complet

### Étape 1 — Lance Claude depuis un dossier vide

Crée un dossier pour le nouveau projet, ouvre-le dans Claude Code (ou ton interface préférée) :

```bash
mkdir mon-nouveau-site
cd mon-nouveau-site
# Lance Claude
```

### Étape 2 — Invoque la skill

Tape simplement (en langage naturel) :

> *"Je veux créer un site pour [type d'organisation]. Utilise la skill build-club-site pour me guider."*

ou plus directement :

> *"/skill build-club-site"* (selon ton interface Claude)

### Étape 3 — Phase 0 : 3 questions de cadrage (5 min)

Claude va te poser :
1. Type d'organisation
2. Volume estimé de contenu à gérer
3. Langues souhaitées

**Si Claude te dit "ce template ne convient pas"** : fais confiance. Il te proposera une alternative (Wordpress, Shopify, etc.). N'insiste pas — forcer un mauvais outil coûte 3× plus cher au final.

### Étape 4 — Phase 1 : Questionnaire de découverte (30-60 min)

Claude va te poser **toutes les questions du questionnaire**, section par section :
1. Identité de l'organisation
2. Marque & identité visuelle
3. Contenu & sections
4. Fonctionnalités
5. Intégrations externes
6. Hébergement & domaine
7. Maintenance & accès
8. Légal & RGPD
9. SEO & marketing
10. Timeline

**Conseils** :
- Réponds avec le client en direct (visioconf, appel, sur place)
- Si tu ne sais pas une réponse, dis "je ne sais pas" → Claude te proposera un défaut sensé
- Pour les questions ouvertes, parle en bullet points — ça suffit largement
- Sauvegarde la conversation : à la fin, Claude écrira `PROJECT.md` qui résume tout

### Étape 5 — Phase 2 : Architecture (15 min)

Claude propose des choix techniques basés sur tes réponses :
- Hébergement (GitHub Pages seul ou + Netlify)
- Domaine (existant ou à acheter)
- Email (SMTP existant ou à créer)
- Analytics (Umami / Plausible / aucun)
- Fonctionnalités optionnelles à activer ou skipper

**Tu valides chaque choix.** Si tu n'es pas sûr, demande à Claude d'expliquer les tradeoffs.

### Étape 6 — Phase 3 : Scaffolding (1-2h)

Claude :
1. Crée le repo GitHub
2. Copie les fichiers du template JCA
3. Adapte les couleurs / fonts / textes selon la marque
4. Met à jour les meta tags, Schema.org
5. Configure le DNS si custom domain
6. Setup Netlify si formulaires
7. Configure GitHub Actions si Reviews sync

À cette étape **tu n'as quasiment rien à faire** sauf valider et fournir les credentials/tokens quand demandé.

### Étape 7 — Phase 4 : Remplissage du contenu (2-4h)

Claude crée un `content.json` initial avec des placeholders, puis te demande de remplir :
- Texte de la home (hero, intro)
- Sections (cours, tarifs, équipe, FAQ)
- Photos initiales

Tu peux faire ça à plusieurs sessions sur 1-2 semaines pendant que le client envoie le matériel.

### Étape 8 — Phase 5 : Déploiement (30 min + propagation DNS)

Claude déroule la checklist de mise en ligne :
- Configuration GitHub Pages
- DNS (4 A records + CNAME www)
- Netlify env vars
- Google Search Console
- Analytics
- Test de tous les formulaires
- QA mobile/desktop

### Étape 9 — Phase 6 : Handoff client (30 min)

Claude génère :
- `CLAUDE.md` — référence technique du projet
- `admin.html` adapté à la marque
- Guide pour le secrétaire (onglet intégré dans l'admin)
- Modèle d'email avec credentials sécurisés

Tu transmets `admin.html` + le secret au client par canal sécurisé (Signal/WhatsApp chiffré).

---

## 4. Exemple concret — un restaurant de A à Z

Voici comment ça se passe en pratique.

### Contexte
Tu démarres un site pour **"La Trattoria Gianni"**, restaurant italien à Bruxelles, géré par Gianni et sa femme Maria. Pas de site actuel, ils ont un compte Facebook avec 1500 abonnés.

### Session 1 — Découverte (1h, en visio avec Gianni & Maria)

Tu lances Claude :
> *"Je veux créer un site pour un restaurant italien à Bruxelles. Utilise la skill build-club-site."*

Claude pose les 3 questions de Phase 0 :
- **Type ?** → Restaurant
- **Volume ?** → Menu de 25 plats, événements occasionnels (cours de cuisine 1×/mois)
- **Langues ?** → FR + IT (langue d'origine de Gianni, marketing important)

Claude valide : *"OK, le template fonctionne pour un resto + bilingue FR/IT (option C : toggle JS lisant content.json). Plus complexe qu'un site monolingue mais faisable."*

Puis déroule le questionnaire. Quelques exemples de questions importantes :
- **1.1 Nom officiel** : "La Trattoria Gianni"
- **1.4 Année création** : 2018
- **1.5 Adresse + coords GPS** : Rue Haute 45, 1000 Bruxelles · 50.8378, 4.3464
- **2.1 Logo** : Gianni a un logo PNG basse résolution → tu décides de le redessiner en SVG simple (initiale "G" stylisée)
- **2.2 Couleurs** : rouge bordeaux (#7A1F1F), crème (#F5E6D3), vert sapin (#1F4029)
- **2.3 Typo** : *Cormorant Garamond* (display) + *Source Sans Pro* (body)
- **2.5 Tone of voice** : "Vous", chaleureux, italien (quelques mots en italien éparpillés)
- **3.1 Sections** : Hero, À propos, Menu, Événements, Galerie, Contact, Pas de team/sensei (juste "Notre équipe" en footer)
- **4.4 Réservation** → décision : Calendly free embedded, pas de système custom
- **5.1 Email** : Gianni a `info@trattoria-gianni.be` chez Combell, SMTP fonctionne
- **5.4 Analytics** : Umami (gratuit, GDPR-friendly)
- **6.1 Domaine** : `trattoria-gianni.be` à acheter chez Combell (~12€/an)

Sortie : Claude génère `PROJECT.md` avec tout résumé.

### Session 2 — Architecture (15 min, seul)

Claude propose :
- GitHub Pages + Netlify Functions ✓
- Domaine custom + 4 A records vers GH Pages + CNAME www ✓
- SMTP Combell port 587 ✓
- Umami Cloud ✓
- **Multilingue option C** : `texts.hero.title.fr` et `texts.hero.title.it` dans content.json, toggle FR/IT en JS ✓
- Pas de booking custom → Calendly embed dans la section Réservation ✓

Tu valides tout.

### Session 3 — Scaffolding (1h30)

Claude :
1. Crée le repo `gianni/trattoria-website`
2. Copie le template JCA
3. Adapte couleurs Tailwind : `bordeaux: #7A1F1F`, `cream: #F5E6D3`, `forest: #1F4029`
4. Change les fonts : Cormorant Garamond + Source Sans Pro
5. Renomme `cours` → `menu`, `equipe` → désactive
6. Met à jour Schema.org : `@type: Restaurant`, `servesCuisine: ["Italian"]`, `acceptsReservations: true`
7. Met à jour meta tags + OG
8. Configure le DNS (Gianni va valider chez Combell)
9. Setup Netlify avec env vars SMTP
10. Crée le système de toggle FR/IT en JS

Tu valides chaque étape.

### Session 4 — Contenu (3h sur 2 semaines)

Tu remplis `content.json` au fur et à mesure :
- Hero : "*Une cuisine italienne, vraiment italienne*" / "*Cucina italiana, davvero italiana*"
- Menu : 25 plats avec prix, allergènes, descriptions FR + IT
- Événements : 2 cours de cuisine programmés
- Galerie : 12 photos (plats + ambiance + Gianni en cuisine)
- FAQ : 6 questions (réservation, allergènes, événements privés, parking, vegan options)

Pendant ce temps, Claude relit le content.json et te signale les incohérences ("le menu mentionne un risotto au safran mais il n'apparaît pas dans la galerie — vouloir une photo ?").

### Session 5 — Déploiement (1h)

Claude déroule la checklist :
- GitHub Pages activé sur `main` / root
- DNS Combell propagé (vérifie `dnschecker.org` montre les 4 IPs GH)
- Netlify deploy ✓
- Test formulaire contact → email arrive ✓
- Umami snippet ajouté → 1ère visite trace ✓
- Google Search Console ajouté + sitemap soumis
- PageSpeed mobile : 92, desktop : 98
- Open Graph preview validée sur opengraph.dev

### Session 6 — Handoff (30 min)

Claude génère :
- `CLAUDE.md` adapté au projet
- `admin.html` avec brand bordeaux/crème
- Guide secrétaire dans l'onglet "Guide" de l'admin
- Modèle email pour Maria avec :
  - Lien admin.html
  - Token GitHub à créer + instructions
  - Endpoint Netlify pour le dashboard messages
  - Lien Umami pour les stats

Tu envoies tout à Maria via Signal.

### Bilan
Total : **3 jours de travail** réparti sur **3 semaines** (avec aller-retour client). Sans skill, ça aurait été ~2 semaines de dev pur, plus 4-6 semaines avec collecte de contenu.

---

## 5. Bonnes pratiques

### Avant chaque projet

- ✅ Réserve 1h pour une **session découverte avec le client en direct** — pas par email
- ✅ Demande la liste de matériel **avant** la session (cf. checklist Phase 11 du questionnaire)
- ✅ Si le client n'a pas son matériel : fixe une **deadline ferme** (ex: "envoie-moi tout d'ici 1 semaine sinon on décale")

### Pendant le projet

- ✅ **Fais des commits atomiques** : 1 fonctionnalité = 1 commit
- ✅ **Teste sur mobile RÉEL** dès Phase 5, pas seulement Chrome devtools
- ✅ Garde une **liste des questions ouvertes** pour le client (ne harcèle pas, regroupe)
- ✅ Demande des **feedbacks intermédiaires** (montre le hero+1 section, confirme la direction avant de tout faire)

### Après le projet

- ✅ **Documenter les pièges rencontrés** dans `06-pitfalls.md` (pour les futurs projets)
- ✅ **Mise à jour `04-customization.md`** si nouveau preset visuel créé
- ✅ **Note du client** : qu'est-ce qu'ils ont aimé, ce qui les a frustrés ?

### Pour la communication client

- ✅ **Toujours sauvegarder une version Word/PDF du PROJECT.md** au cas où ils veulent y revenir
- ✅ **Onboarding video** de 5 min (Loom gratuit) montrant l'admin → permet au client de se lancer seul
- ✅ **Première année** : prévoir 1 session de 30 min/mois pour ajustements (incluse dans le forfait)

---

## 6. Dépannage

### "La skill ne se déclenche pas"

Causes possibles :
- Skill mal placée → vérifier `~/.claude/skills/build-club-site/SKILL.md` existe
- Description trop générique → la skill ne matche pas le contexte
- Trigger keyword absent → utiliser "site web", "club", "association", "sites comme JCA"

**Solution** : invoque-la explicitement avec son nom :
> *"/skill build-club-site"* ou *"Utilise la skill build-club-site"*

### "Claude saute des étapes du workflow"

La SKILL.md dit "DO NOT SKIP STEPS" mais Claude peut être tenté.

**Solution** : à la fin de chaque phase, demande explicitement :
> *"Vérifions qu'on a bien fini la Phase X avant de passer à Y"*

### "Le client n'a pas son contenu prêt"

Solution la plus efficace :
> *"On va commencer avec du Lorem Ipsum / placeholder. Ça donne souvent envie de fournir le vrai contenu une fois qu'on voit le site prendre forme."*

Effet psychologique réel : voir le site presque-fini est un puissant motivateur.

### "Le client veut un truc hors scope (e-commerce, login, etc.)"

Phase 1 doit avoir détecté ça. Si découvert plus tard :
1. Documenter dans `PROJECT.md` que c'est hors scope initial
2. Proposer un **scope élargi** avec re-évaluation budget/délai
3. Ou proposer une **alternative tierce** (Stripe Payment Link pour 1-2 produits, Calendly pour booking, etc.)
4. Si insistance : refuser ou suggérer une stack différente (Wordpress / Astro+Sanity)

### "Ça plante au déploiement"

Référence : `06-pitfalls.md` couvre les 30 erreurs les plus courantes. Si ce n'est pas dedans, ajouter une nouvelle entrée.

### "Le site est en ligne mais Google ne le voit pas"

Normal : indexation prend 1-4 semaines pour un nouveau site.

Accélérer :
- Forcer l'indexation via Search Console (URL Inspection → Request Indexing)
- Obtenir 1-2 backlinks locaux (site commune, fédération, annuaire métier)
- Publier un article sur Facebook avec lien (signal externe)

---

## 7. Faire évoluer la skill

La skill est un **document vivant**. Après chaque projet :

### Mettre à jour `06-pitfalls.md`
Si tu rencontres une nouvelle erreur ou un piège évitable, ajoute une entrée formatée :
```markdown
### N. Titre court du piège
**Symptôme** : ce que tu vois.
**Cause** : pourquoi ça arrive.
**Fix** : comment le résoudre.
```

### Mettre à jour `04-customization.md`
Pour chaque nouveau client/métier, ajoute :
- Sa palette de couleurs si réussie
- Ses fonts si combinaison gagnante
- Une variante de tone-of-voice intéressante

### Mettre à jour `03-content-template.md`
Si tu fais un nouveau métier (ex: avocat, kiné), ajoute une section "Adaptation par métier".

### Mettre à jour `02-architecture.md`
Si tu découvres un nouveau service utile (ex: nouvelle alternative à Umami), ajoute-le aux options.

### Versionner la skill
Si la skill devient grosse, considère la mettre dans son propre repo GitHub :
```
mkdir ~/dev/claude-skill-build-club-site
cp -r ~/.claude/skills/build-club-site/* ~/dev/claude-skill-build-club-site/
cd ~/dev/claude-skill-build-club-site
git init && git add . && git commit -m "Initial"
gh repo create build-club-site-skill --public --push
```

Ensuite chaque PC où tu veux l'utiliser :
```bash
git clone https://github.com/YOU/build-club-site-skill ~/.claude/skills/build-club-site
```

Et la mise à jour devient un simple `git pull`.

---

## 8. FAQ

### Combien de temps prend un projet avec la skill ?

| Type de projet | Sans skill | Avec skill |
|---|---|---|
| Site simple monolingue (5 sections) | 3-5 jours dev | **1 jour dev** |
| Site moyen (10 sections + galerie) | 1 semaine dev | **2 jours dev** |
| Site complexe (multilingue, calendrier, RSS) | 2-3 semaines dev | **3-4 jours dev** |

À cela s'ajoute toujours **2-3 semaines** de collecte contenu côté client (incompressible).

### Combien je peux facturer ?

Cette template + skill produit un site **équivalent à un Wix Business (29€/mois) ou un Wordpress configuré (1500-3000€)**. Le tien : 0€/mois après domaine.

Tarification raisonnable :
- **MVP simple** : 800-1500€
- **Site standard** : 1500-3000€
- **Site complexe** : 3000-5000€

Inclure dans le forfait :
- 1 année de support léger (mois 1 : 30 min/sem ; mois 2-12 : 30 min/mois)
- 1 onboarding video pour le client
- Documentation (PROJECT.md + admin Guide)

### Puis-je vendre la skill elle-même ?

La skill est inspirée du site JCA, libre d'usage. Tu peux la repackager, la vendre, la mettre sur un marketplace de skills, etc. Aucune attribution requise.

### Qu'est-ce qui n'est PAS dans la skill et que je dois améliorer ?

- **Pas de tests automatisés** — pour l'instant le QA est manuel
- **Pas de templates par métier détaillés** — `03-content-template.md` a quelques variantes mais pas exhaustif
- **Pas de générateur de mentions légales / privacy policy** — utiliser cookiebot.com / iubenda
- **Pas de gestion budgétaire / facturation** — utiliser un outil dédié

### Le client peut-il faire des modifications structurelles (ajouter une section) ?

Non. La structure du site (sections, layout) est figée dans `index.html`. Le client édite uniquement le **contenu** via l'admin.

Si modification structurelle souhaitée :
- Le client doit te contacter
- Tu modifies `index.html` localement
- Tu push → GH Pages déploie

C'est volontaire : ça évite que le client casse le site en pensant pouvoir tout modifier.

### Quelle est la maintenance annuelle attendue ?

Sur le site lui-même : **quasi nulle**. GitHub Pages tient, Netlify tient.

Sur les comptes externes :
- PAT GitHub à renouveler chaque année
- Token Netlify Blobs à renouveler si expiration
- Domain à renouveler chaque année (~12€)
- Email pro à renouveler (~36-60€/an)

**Total maintenance annuelle pour le client : ~50-80€/an** + tes éventuelles heures de support.

### Puis-je utiliser cette skill pour mon propre site personnel ?

Oui ! Le site freelance / portfolio rentre dans le scope. Adapte juste les sections (probablement : hero, services, projets, à propos, contact).

### Comment gérer plusieurs sites avec ce template ?

Chaque site est un **repo GitHub séparé**. Le client a accès à son repo uniquement.

Toi, tu as ton compte GitHub avec accès à tous les repos clients (collaborateur). C'est propre.

Si tu en gères 5+, considère :
- Un dashboard custom qui liste tes sites + leur health (uptime, dernier publish, version)
- Un workflow GitHub Actions partagé pour vérifier les sites mensuellement
