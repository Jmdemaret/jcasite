# Skill — `build-club-site`

Skill pour Claude qui guide la création d'un nouveau site web pour un club, association, ASBL, restaurant, ou petite entreprise — basé sur l'architecture du site Judo Club Anderlecht.

## Stack ciblée
- GitHub Pages (hosting statique gratuit)
- Netlify Functions (formulaires + persistance Blobs)
- Admin local en HTML pur, communique avec GitHub via PAT
- SEO complet (Schema.org, Open Graph, sitemap)
- Analytics Umami (gratuit, GDPR-friendly)
- Optionnel : sync Google Reviews via SerpAPI, RSS feed pour Zapier→Facebook

## Installation

### Option A — Skill globale (recommandé)
Pour que la skill soit utilisable dans **n'importe quel projet** :

```bash
# Linux/Mac
mkdir -p ~/.claude/skills
cp -r build-club-site ~/.claude/skills/
```

```powershell
# Windows
New-Item -ItemType Directory -Force "$env:USERPROFILE\.claude\skills"
Copy-Item -Recurse build-club-site "$env:USERPROFILE\.claude\skills\"
```

### Option B — Skill projet-spécifique
Garder dans `.claude/skills/build-club-site/` du repo concerné.

## Utilisation

Quand on commence un nouveau site, dire à Claude :
> *"Je veux construire un site pour [type d'organisation], peux-tu me guider ?"*

ou directement :
> *"Utilise la skill build-club-site pour démarrer un site pour mon club d'aïkido"*

Claude va :
1. Confirmer le scope en 3 questions
2. Dérouler le questionnaire de découverte (`references/01-questionnaire.md`)
3. Proposer une architecture (`references/02-architecture.md`)
4. Scaffold le projet à partir du template
5. Aider à remplir le contenu
6. Guider le déploiement

## Fichiers

```
build-club-site/
├── SKILL.md                    # Entry point Claude
├── README.md                   # Ce fichier
└── references/
    ├── 01-questionnaire.md     # Discovery client (le plus important)
    ├── 02-architecture.md      # Décisions techniques
    ├── 03-content-template.md  # Starter content.json
    ├── 04-customization.md     # Couleurs, fonts, mood
    ├── 05-deployment-checklist.md  # Étapes de mise en ligne
    └── 06-pitfalls.md          # Pièges et solutions
```

## Mise à jour

Cette skill évolue au fur et à mesure des projets réels. Pour chaque nouveau site construit avec :
- Ajouter dans `06-pitfalls.md` les nouveaux problèmes rencontrés
- Mettre à jour `04-customization.md` avec les nouveaux looks créés
- Ajouter dans `03-content-template.md` les nouveaux profils métiers (resto, kiné, etc.)

C'est un document vivant.

## Limitation

Ce template est optimisé pour :
- Sites simples 1 page (single-page) ou peu de pages
- Maintenance par 1-2 personnes
- Petites organisations (<500 membres / <100 produits)

**Ne pas utiliser pour** :
- E-commerce avec catalogue (>20 produits) → Shopify
- Site avec espace membre / login → Wordpress + plugin
- Plus de 3 langues → CMS dédié (Strapi, Sanity)
- Site avec >50 pages → CMS dédié

## Licence

Inspiré du site Judo Club Anderlecht (https://judoclubanderlecht.be).
Réutilisable librement pour tout projet, sans attribution requise.
