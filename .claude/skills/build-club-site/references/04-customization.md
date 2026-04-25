# Customisation visuelle

Comment adapter le template JCA à une nouvelle identité de marque.

## 1. Couleurs (Tailwind config)

Dans `index.html`, modifier le bloc :

```js
tailwind.config = {
  theme: {
    extend: {
      colors: {
        paper:  { 50:'#FEFCF6', 100:'#FBF6E9', 200:'#F6EEDB', 300:'#ECE1C8' },
        sumi:   { 700:'#2A2623', 800:'#1D1916', 900:'#0F0D0B' },
        hinomaru: { 400:'#E63A4C', 500:'#D41B33', 600:'#C8102E', 700:'#A10D25' },
        royal:  { 500:'#6E4C92', 600:'#553879', 700:'#432C5F' },
        gold:   '#B99A5A'
      }
    }
  }
}
```

ET dans le `<style>` :

```css
:root{
  --paper:#FBF6E9; --paper-warm:#F4EAD2;
  --sumi:#1D1916; --hinomaru:#C8102E; --royal:#6E4C92; --gold:#B99A5A;
}
```

### Recettes par mood

**Moderne / minimaliste** :
- Paper : `#FFFFFF` ou `#FAFAFA`
- Texte : `#000000` ou `#1A1A1A`
- Accent : 1 seule couleur vive (saturée)

**Premium / luxueux** :
- Paper : `#0F0F0F` ou `#1A1A1A` (dark mode)
- Texte : `#FFFFFF`, accents `#FBF6E9`
- Accent : doré `#B99A5A` ou cuivré

**Chaleureux / familial** :
- Paper : crème `#FBF6E9`
- Accent primaire : terracotta, ocre
- Accent secondaire : vert sauge ou bleu pétrole

**Tech / startup** :
- Paper : blanc cassé `#FAFAFA`
- Accent primaire : violet/indigo electric
- Accent secondaire : néon (jaune/vert) en parcimonie

**Restaurant / cuisine** :
- Paper : crème ou vert mousse
- Accent : rouge bordeaux ou orange brûlé
- Texte : noir charbon

### Outils
- [coolors.co](https://coolors.co) — palettes
- [colorhunt.co](https://colorhunt.co) — palettes curated
- [realtimecolors.com](https://realtimecolors.com) — preview live sur exemple
- [contrast checker](https://webaim.org/resources/contrastchecker/) — accessibilité (toujours vérifier ratio AA mini = 4.5:1)

## 2. Typographie

Dans `<head>` modifier le lien Google Fonts et le tailwind config :

```html
<link href="https://fonts.googleapis.com/css2?family=NEW_DISPLAY:wght@300..800&family=NEW_BODY:wght@400;600&display=swap" rel="stylesheet" />
```

```js
fontFamily: {
  display: ['NEW_DISPLAY','serif'],
  sans:    ['NEW_BODY','system-ui','sans-serif'],
  mono:    ['"JetBrains Mono"','monospace']
}
```

### Combinaisons recommandées

| Mood | Display | Body |
|---|---|---|
| Éditorial / luxe | Fraunces | Inter |
| Moderne minimal | DM Serif Display | Inter |
| Premium | Cormorant Garamond | Source Sans Pro |
| Tech / startup | Space Grotesk | Inter |
| Chaleureux | Lora | Open Sans |
| Italique / mood | Italiana | Manrope |
| Japonisant | Shippori Mincho | Noto Sans JP |
| Manuscrit / artisan | Caveat | Nunito |

### Règles d'or
- 2 fonts max (3 si vraiment besoin pour mono technique)
- Display : pour titres uniquement (h1, h2, gros chiffres)
- Body : pour tout le texte de lecture (15-17px sur desktop)
- Variable fonts > static (poids dynamiques)

## 3. Hero

### Variations possibles

**Photo cinématique** (JCA default) :
- Photo plein écran à droite, texte à gauche
- Effet Ken Burns subtil (zoom lent)

**Vidéo loop** :
- Remplace `<div class="hero-photo">` par `<video class="hero-photo" autoplay muted loop playsinline poster="poster.jpg"><source src="hero.mp4"></video>`
- Format MP4 max 5MB, ~1280px de large
- Désactiver l'animation Ken Burns sur la vidéo : `video.hero-photo{animation:none;}`

**Diaporama** :
- Plusieurs photos qui se succèdent (CSS transition opacity)
- Utiliser un setInterval qui swap les images

**Pleine largeur sans split** :
- Texte centré sur photo de fond floutée + overlay sombre
- Pour les sites plus "marketing"

### Kanji / signature culturelle
JCA utilise un kanji énorme en filigrane (`hero-kanji`) — propre à un club japonais. Pour autres métiers :
- Restaurant italien : signature tilde `~` ou un mot italique en fond
- Cabinet pro : initiales géantes en filigrane
- Tech : lignes/grid technique
- Tranche de vie : photo monochrome très contrastée en fond

## 4. Sections à adapter par métier

### Bandeau values / kanji band
JCA a un bandeau avec 4 kanji (技 心 礼 智) = technique, esprit, respect, sagesse. Adapter à la mission :
- Restaurant : "Frais — Local — Fait maison — Ensemble"
- Cabinet : "Écoute — Expertise — Bienveillance — Suivi"
- Sport : "Effort — Discipline — Communauté — Progrès"

### Map (Leaflet)
- Garder la map (utile localement)
- Mettre à jour les coords + transit stops
- Pour un commerce : montrer parking, accès handicapé
- Pour un freelance avec adresse virtuelle : skipper la map, mettre une zone d'intervention

### Schedule / cours
- Garder l'éditeur visuel calendrier si métier avec horaires récurrents
- Sinon remplacer par une section "Disponibilités" simple + lien vers Calendly

## 5. Tone of voice — exemples

| Métier | Hero text | Style |
|---|---|---|
| Club de judo (JCA) | "Club de Judo *Traditionnel et Familial*" | Italique, élégant, traditionnel |
| Restaurant gastronomique | "Une cuisine de saison, *en mouvement*" | Poétique |
| Cabinet kiné | "Votre santé, *en confiance*" | Rassurant, simple |
| Tech startup | "*Build the future*, today." | Direct, énergique |
| ASBL aide aux sans-abri | "*Ensemble*, on agit" | Engagé, inclusif |
| Café/coffeehouse | "Du bon café, *vraiment bon*" | Honnête, humble |

## 6. Photos

### Critères de qualité
- Résolution : minimum 1500px de large
- Format : JPEG (web) ou WebP (plus moderne, ~30% plus léger)
- Compression : qualité 80-85 (sweet spot taille/qualité)
- Hauteur : photos paysage 16:9 ou 4:3 préférables

### Outils
- [Squoosh](https://squoosh.app/) — compresser sans perte visible
- [TinyPNG](https://tinypng.com) — optimisation rapide
- [Pexels](https://pexels.com) / [Unsplash](https://unsplash.com) — photos libres si pas de matériel

### Pour le hero
- Une photo "cinématique" qui raconte (pas juste un produit/un local vide)
- Doit fonctionner avec du texte par-dessus (zones moins denses pour le texte)
- Privilégier des cadrages humains (visages, mains en action)

### Pour la galerie
- Variété : large + détail + portrait
- Cohérence visuelle : éclairage, palette
- Si albums : grouper par événement/saison/thème pour donner du contexte

## 7. Logo

### Format optimal
- **SVG** pour le logo principal (scalable, léger, parfait à toutes tailles)
- **PNG** transparent en backup (fond non-blanc)
- Si logo complexe : préparer une version simplifiée pour favicon (16-32px)

### Si logo fourni en JPG basse résolution
- Demander la version vectorielle au client (graphiste original)
- Si impossible : redessiner ou faire un nouveau (à budget client)

### Favicon
- Le logo complet est rarement lisible en 16x16
- Stratégie : initiale stylisée en cercle de couleur de marque
- Voir `_gen_favicons.py` du JCA template (Python + Pillow génère 5 tailles depuis SVG)
