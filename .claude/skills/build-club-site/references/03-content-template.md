# Template `content.json` de démarrage

À copier dans le nouveau repo et remplir avec les infos du questionnaire.

```jsonc
{
  "_meta": {
    "version": "1.0001",
    "publishedAt": "2026-01-01T00:00:00.000Z",
    "history": [
      { "version": "1.0001", "date": "2026-01-01T00:00:00.000Z", "summary": "Initial content" }
    ]
  },

  "sections": {
    "club": true,
    "cours": true,         // ou "services" / "menu" selon le métier
    "tarifs": true,
    "actu": true,
    "evenements": true,
    "galerie": true,
    "equipe": true,
    "temoignages": true,
    "faq": true,
    "preInscription": true,
    "sponsors": false,     // souvent off au démarrage
    "contact": true
  },

  "banner": {
    "active": false,
    "type": "info",
    "text": ""
  },

  "announcements": [],

  "texts": {
    "hero": {
      "title": "<em>Titre principal</em><br>en 2 lignes",
      "intro": "Une phrase d'accroche qui résume la mission.",
      "ctaPrimary": "Pré-inscription",
      "ctaSecondary": "Voir les services",
      "stat1Number": "10",
      "stat1Label": "années",
      "stat2Number": "200+",
      "stat2Label": "clients",
      "stat3Number": "5",
      "stat3Label": "services / semaine"
    },
    "club": {
      "label": "About",
      "title": "Notre <em>histoire</em>",
      "intro": "Description de l'organisation, valeurs, mission. ~150-200 mots."
    },
    "galerie": {
      "label": "Gallery",
      "title": "Nos <em>moments</em>",
      "intro": "Description courte de la galerie."
    }
  },

  "groups": [
    { "id": "group1", "label": "Groupe 1",  "color": "#6E4C92", "ageRange": "4-7 ans" },
    { "id": "group2", "label": "Groupe 2",  "color": "#C8102E", "ageRange": "8-12 ans" },
    { "id": "group3", "label": "Adultes",   "color": "#1D1916", "ageRange": "15+" }
  ],

  "courses": [
    { "day": "Mercredi", "groupId": "group1", "start": "14:00", "end": "15:00" },
    { "day": "Mercredi", "groupId": "group2", "start": "15:00", "end": "16:00" },
    { "day": "Samedi",   "groupId": "group3", "start": "10:00", "end": "11:30" }
  ],

  "pricing": [
    { "label": "Cotisation annuelle", "price": "200€", "period": "an", "description": "Accès illimité à tous les cours" },
    { "label": "Licence fédérale",   "price": "30€",  "period": "an", "description": "Inclut l'assurance" },
    { "label": "Cours d'essai",      "price": "Gratuit", "period": "1 séance", "description": "Pour découvrir" }
  ],

  "team": [
    {
      "name": "Prénom Nom",
      "role": "Responsable / Sensei / Manager",
      "photo": "team/prenom-nom.jpg",
      "bio": "3-5 lignes de bio.",
      "social": { "linkedin": "" }
    }
  ],

  "albums": [],
  "gallery": [],

  "news": [
    {
      "date": "2026-01-15",
      "title": "Bienvenue sur notre nouveau site",
      "tag": "Annonce",
      "body": "<p>Quelques mots d'introduction.</p>"
    }
  ],

  "events": [
    {
      "date": "2026-09-01",
      "title": "Rentrée saison",
      "type": "Cours",
      "loc": "Local"
    }
  ],

  "testimonials": [
    {
      "author": "Prénom",
      "role": "Membre / parent / client",
      "rating": 5,
      "text": "Quelques lignes de témoignage."
    }
  ],

  "faq": [
    { "q": "Question 1 ?", "a": "Réponse claire." },
    { "q": "Quels horaires ?", "a": "Voir la section Cours." }
  ],

  "sponsors": [
    {
      "name": "Sponsor / Partenaire",
      "logo": "sponsors/sponsor1.png",
      "url": "https://sponsor.com",
      "description": "Une ligne sur le partenariat"
    }
  ],

  "googleReviewsHidden": [],
  "googleReviewsPeriodMonths": 24,

  "socials": {
    "facebook":   { "url": "", "active": false },
    "instagram":  { "url": "", "active": false },
    "whatsapp":   { "url": "", "active": false },
    "youtube":    { "url": "", "active": false },
    "tiktok":     { "url": "", "active": false },
    "twitter":    { "url": "", "active": false },
    "linkedin":   { "url": "", "active": false },
    "googleMaps": { "url": "", "active": false }
  },

  "forms": {
    "scriptUrl": "https://your-netlify-site.netlify.app/.netlify/functions/send",
    "recipientEmail": ""
  },

  "legal": {
    "address": "Rue X 1, 1000 Ville",
    "registrationNumber": "ASBL / TVA / SIREN ...",
    "representative": "Nom du représentant légal",
    "privacyUrl": "/privacy.html"
  }
}
```

## Notes d'adaptation rapide par métier (synthétique)

### Cabinet professionnel (médecin, kiné, avocat)
- `cours` → `services` ou `consultations`
- `pricing` → tarifs des consultations
- `team` → praticiens
- `events` → désactiver ou utiliser pour formations
- `temoignages` → utiliser

### Freelance / consulting
- `cours` → `services`
- `team` → désactiver (one-person)
- `events` → portfolio / case studies
- `pricing` → tarifs ou "sur devis"
- `galerie` → projets réalisés

### ASBL / charity
- `cours` → `actions` / `missions`
- `pricing` → don suggéré + cotisation membre
- `team` → bureau / volontaires
- `events` → activités à venir
- Ajouter section "Nous soutenir" avec lien de don

---

## 📚 Variantes détaillées par métier

Chaque variante ci-dessous donne : structure spécifique, palette, fonts, tone of voice, Schema.org, fonctionnalités, pièges.

---

### 🍴 Variante 1 — Café / Restaurant

#### Sections adaptées
| JCA | Devient |
|---|---|
| club | Notre histoire (chef, philosophie, sourcing) |
| **cours → menu** | **Carte / Menu** (catégorisé entrées/plats/desserts/vins) |
| tarifs | À supprimer (prix dans le menu) |
| galerie albums | Plats par saison, soirées spéciales, coulisses cuisine |
| events | Soirées œnologiques, brunch dominical, événements privés |
| equipe | Brigade en cuisine + salle |
| temoignages | Avis Google + TripAdvisor + TheFork |
| FAQ | Réservation / allergènes / parking / vegan / privatisation |
| sponsors | Producteurs locaux mis en valeur |

#### Schema spécifique : structure menu
```json
"menu": {
  "categories": [
    { "id": "entrees", "label": "Entrées", "icon": "🥗" },
    { "id": "plats",   "label": "Plats",   "icon": "🍝" },
    { "id": "desserts","label": "Desserts","icon": "🍰" },
    { "id": "vins",    "label": "Vins",    "icon": "🍷" }
  ],
  "items": [
    {
      "id": "carbo-truffe",
      "category": "plats",
      "name": "Carbonara à la truffe noire",
      "description": "Pâtes fraîches, pancetta, jaune d'œuf, copeaux de truffe d'hiver",
      "price": "24",
      "allergens": ["gluten", "œuf", "lactose"],
      "tags": ["signature"]
    }
  ]
}
```

#### Schema.org
```json
{
  "@type": "Restaurant",
  "servesCuisine": "Italienne",
  "priceRange": "€€",
  "acceptsReservations": "https://calendly.com/restaurant/table",
  "menu": "https://trattoria.be/#menu",
  "openingHoursSpecification": [
    { "@type": "OpeningHoursSpecification", "dayOfWeek": ["Tuesday","Wednesday","Thursday"], "opens": "12:00", "closes": "14:00" },
    { "@type": "OpeningHoursSpecification", "dayOfWeek": ["Friday","Saturday"], "opens": "12:00", "closes": "23:00" }
  ]
}
```

#### Palette par genre
| Style | Palette |
|---|---|
| Italien chaleureux | Bordeaux `#7A1F1F` + crème `#F5E6D3` + vert sapin `#1F4029` |
| Bistrot français | Noir charbon `#1A1A1A` + crème + or `#C9A961` |
| Sushi/Japonais | Noir + rouge hinomaru `#C8102E` + papier washi `#F5E8D0` |
| Café cosy | Brun caramel `#8B5A3C` + crème + vert mousse `#5A7060` |
| Gastronomique étoilé | Anthracite `#2A2A2A` + or `#B8860B` + blanc cassé `#FAFAF7` |
| Brasserie / pub | Bois sienna `#A0522D` + ambré `#C97B5C` + vert sapin |

#### Fonts recommandées
- Display : Cormorant Garamond, Playfair Display, DM Serif Display
- Body : Source Sans Pro, Inter, Lato

#### Tone of voice
- "Vous" toujours
- Chaleureux, gourmand, pas guindé
- Quelques mots de la langue d'origine (italien, espagnol, japonais…) dispersés

#### Fonctionnalités essentielles
- ⭐ **Réservation** : Calendly, TheFork, Resengo, OpenTable
- **Newsletter** : Brevo gratuit (fideliser habitués)
- **Allergènes** : pictogrammes obligatoires en EU
- **Annonces calendrier** : congés annuels, soirées spéciales

#### Pièges
1. **Photos amateurs au flash = échec**. Investir 300-500€ photographe pro.
2. **Téléphone TRÈS visible** — beaucoup de clients préfèrent appeler.
3. **Multi-langue à Bruxelles** : FR + NL + EN souvent attendu.
4. **Photo Google Maps** : vérifier qu'elle est belle (juge avant le site).
5. **Menu qui change souvent** : admin doit être ULTRA simple.

---

### 🧘 Variante 2 — Centre de méditation

#### Sections adaptées
| JCA | Devient |
|---|---|
| club | Notre approche / La pratique |
| **cours → programmes** | Méditation guidée, MBSR, pleine conscience, yoga doux |
| tarifs | Adhésion + sessions à l'unité + retraites |
| galerie | Lieu, ambiance, retraites passées |
| events | Retraites annuelles, ateliers, conférences |
| equipe | Instructeurs + leur parcours |
| temoignages | ⭐ ESSENTIEL — transformations personnelles |
| FAQ | Pour débutants / posture / habits / agenda |
| **+ Section "Première fois ?"** | Crucial pour rassurer |
| **+ Citations / inspirations** | Cartes décoratives façon JCA mais kanji 静/心/道/禅 |

#### Palette
- Background : blanc cassé `#FAF8F5` ou sable `#F2EBE0`
- Texte : anthracite tendre `#2A2A2A` (jamais noir pur)
- Accent primaire : vert sauge `#7B9E7E` ou terracotta doux `#C97B5C`
- Accent secondaire : bleu pétrole `#3D5A6C` ou prune fanée `#9B7A8E`
- Détail : gold subtil `#B19770` (mat, pas brillant)

**Aucun rouge vif, aucun violet électrique.** La couleur est murmurée, pas criée.

#### Fonts
- Display : Cormorant Garamond, Lora (élégant, contemplatif)
- Body : Inter, Manrope (lisible mais doux)
- ❌ Pas de mono technique (trop "tech" pour ce contexte)

#### Tone of voice
| Judo (énergique) | Méditation (apaisé) |
|---|---|
| "Rejoignez le tatami" | "Prenez place, en douceur" |
| Stats agressives "47 années" | Citation contemplative |
| CTA fort "Pré-inscription !" | Invitation "Découvrir une séance" |

Exemple hero : *"Un espace pour <em>respirer.</em>"*

#### Schema.org
```json
{
  "@type": "LocalBusiness",
  "description": "Centre de pratique de la méditation laïque..."
}
```

⚠️ **Ne PAS utiliser** `HealthAndBeautyBusiness` ou `MedicalBusiness` — implique des certifications réglementées en EU.

#### Fonctionnalités essentielles
- ⭐ **Booking** : Cal.com / Calendly + Stripe Payment Links pour retraites
- **Newsletter** très valorisée (Brevo gratuit)
- **Audio guidances** : embed Spotify / SoundCloud si le centre en produit
- **Première séance gratuite** mise en avant

#### Pièges
1. **Sur-promesse spirituelle** — éviter "Transformez votre vie", "Guérissez votre anxiété". Implications légales + sentiment "secte".
2. **Vocabulaire ésotérique** — "vibrations", "chakras alignés"… repousse 80% du public. Préférer scientifique-bienveillant : *attention*, *présence*, *régulation émotionnelle*.
3. **Photos de méditants sans accord** — RGPD strict. Privilégier lieu sans personnes, mains, objets.
4. **Mention "thérapie"** — illégal sans titre médical en EU.
5. **Animations agressives** — réduire au max. `prefers-reduced-motion` à fond.

---

### 🔧 Variante 3 — Électricien / Réparation électroménager / Domotique

#### Sections adaptées
| JCA | Devient |
|---|---|
| club | Qui suis-je / Notre entreprise |
| **cours → services** | Liste des prestations (installations, dépannage, mise aux normes, domotique, bornes VE…) |
| tarifs | Devis gratuit + grille tarifaire indicative |
| galerie albums | **Avant/après installations** (super impact visuel) |
| events | À masquer ou : "Nouvelles normes 2026", actualités du métier |
| equipe | Techniciens (si entreprise) ou désactivé (si solo) |
| temoignages | ⭐ **CRITIQUE** — Avis Google = trust signal #1 dans ce métier |
| FAQ | Durée intervention, garantie, certificats, paiement, urgence |
| sponsors | **Marques partenaires** (Schneider, Niko, Legrand, Somfy, KNX) |
| **+ Zones desservies** | SEO local critique — carte avec polygon des communes |
| **+ Service urgence** | Si dépannage 24/7, mise en avant énorme |

#### Schema.org
```json
{
  "@type": "Electrician",
  "serviceType": ["Installation électrique", "Dépannage", "Domotique", "Bornes VE"],
  "areaServed": [
    { "@type": "City", "name": "Anderlecht" },
    { "@type": "City", "name": "Bruxelles" },
    { "@type": "City", "name": "Forest" },
    { "@type": "City", "name": "Uccle" }
  ],
  "priceRange": "€€",
  "hasOfferCatalog": {
    "@type": "OfferCatalog",
    "itemListElement": [
      { "@type": "Offer", "name": "Diagnostic électrique", "price": "0", "description": "Gratuit avec devis" }
    ]
  }
}
```

#### Palette
| Style | Palette |
|---|---|
| Pro classique confiance | Bleu marine `#1E3A8A` + blanc + accent jaune `#FCD34D` (signal/alerte) |
| Moderne tech | Anthracite `#2A2A2A` + cyan vif `#06B6D4` + blanc |
| Écolo / économies d'énergie | Vert forêt `#16A34A` + crème + or `#C9A961` |
| Domotique premium | Noir + or `#B8860B` + blanc cassé |

#### Fonts
- Display : Inter Display, Poppins, Manrope (moderne, ferme)
- Body : Inter (confiance > style)
- ❌ Pas de serif fantaisiste (trop "luxe", brouille le message confiance)

#### Tone of voice
- "Vous", direct, professionnel
- **Chiffres concrets** valorisés : "RGIE depuis 2008", "1500 interventions", "98% de satisfaction"
- Pas de marketing flou : annoncer délais réels, garanties écrites
- Exemple hero : *"<em>Électricien certifié RGIE</em><br>à Bruxelles."* / *"Devis gratuit, intervention sous 48h."*

#### Fonctionnalités essentielles
- ⭐ **Bouton flottant WhatsApp / Téléphone** toujours visible (urgence = appel rapide)
- **Formulaire devis structuré** : type d'intervention, surface, urgence, photos
- **Carte zone d'intervention** (Leaflet polygon des communes)
- **Affichage du numéro RGIE / agréments** dans le footer

#### Schéma de tarifs typique
```json
"pricing": [
  { "label": "Diagnostic + devis", "price": "Gratuit", "period": "Sur RDV", "description": "Sans engagement" },
  { "label": "Tarif horaire main d'œuvre", "price": "60-75€", "period": "/heure HTVA", "description": "Hors fournitures" },
  { "label": "Dépannage urgence (24/7)", "price": "+50%", "period": "Majoration", "description": "Soirées, week-ends, jours fériés" },
  { "label": "Installation borne VE", "price": "À partir de 800€", "period": "TTC", "description": "Selon configuration" }
]
```

#### Pièges
1. **Photos de chantier pixelisées** = perte de crédibilité. Soit photos pro, soit pas de photo.
2. **Ne pas afficher le numéro RGIE / agréments** = client ne peut pas vérifier la légitimité.
3. **Promesse "24/7" non tenue** = avis Google négatifs catastrophiques.
4. **Disponibilité affichée fausse** ("interventions sous 24h" mais en réalité 1 semaine) — détruit la confiance instantanément.
5. **RGPD photos clients** — photos avant/après dans la galerie nécessitent **autorisation écrite** (modèle à signer chez le client).
6. **Pas de mentions légales** = obligatoire (entreprise individuelle vs SRL, TVA, siège social).
7. **Concurrent direct** : pages Yellow / PagesBlanches. Différenciateur : **avis Google volume + récence + qualité réponses**.

---

### ✈️ Variante 4 — Tourisme / Conseiller voyage / Expert croisières

#### Sections adaptées
| JCA | Devient |
|---|---|
| club | Mon parcours / Mes voyages (storytelling) |
| **cours → spécialités** | Voyage sur mesure, croisières, voyages de noces, groupes, séminaires |
| tarifs | RDV découverte gratuit + transparence commission |
| galerie albums | ⭐ **Carnets de voyage** par destination (super match avec albums) |
| events | Salons voyage, soirées thématiques, départs en groupe |
| equipe | Soi-même ou collaborateurs |
| temoignages | ⭐ **CRITIQUE** — voyageurs adorent partager |
| FAQ | Assurance, paiement, urgence sur place, modifications |
| sponsors | Tour-opérateurs, compagnies aériennes, croisiéristes |
| **+ Section "Process"** | 4 étapes : RDV découverte → proposition → réservation → suivi pendant voyage |
| **+ Newsletter** | Destination du mois, promos exclusives |

#### Schema.org
```json
{
  "@type": "TravelAgency",
  "description": "Conseillère voyage sur mesure depuis 15 ans...",
  "knowsAbout": ["Croisières", "Voyages de noces", "Voyages sur mesure"],
  "areaServed": "Belgique",
  "priceRange": "€€-€€€€"
}
```

#### Palette par spécialité
| Spécialité | Palette |
|---|---|
| Croisières | Bleu marine `#1E3A5F` + or sable `#DBC894` + crème `#F5E6D3` |
| Aventure / nature | Vert forêt `#2D4A3E` + terracotta `#C97B5C` + sable |
| Luxe / sur mesure | Noir charbon `#1A1A1A` + or rose `#D4A574` + blanc cassé |
| Famille / soleil | Turquoise `#06B6D4` + corail `#F87171` + blanc |
| Culturel | Bordeaux `#7A1F1F` + crème + or |

#### Fonts
- Display : Cormorant Garamond, Playfair Display (élégant, voyage)
- Body : Inter, Source Sans Pro
- Mono pour code/référence : optionnel

#### Tone of voice
- "Vous", inspirant, expert mais accessible
- **Storytelling** subtil : "Mon voyage en Patagonie m'a appris…" — humanise le service
- Vocabulaire qui fait rêver mais reste **concret** (pas de "partez à l'aventure" générique)
- Exemple hero : *"<em>Votre voyage,</em><br>imaginé sur mesure."* / *"15 ans d'expertise, 60+ pays parcourus, 800+ voyages organisés."*

#### Fonctionnalités essentielles
- ⭐ **Galerie albums par destination** (le template JCA est parfait — 1 album = 1 destination ou 1 voyage)
- **WhatsApp direct** : réactivité = service premium
- **Embed Instagram** (les voyages = visuel ++)
- **Newsletter destination du mois** (Brevo gratuit)
- **Annonces calendrier** : promotions, départs limités, soirées présentation
- **Témoignages avec destination** ("Marie & Tom — voyage de noces aux Maldives")

#### Schéma de spécialités typique
```json
"services": [
  {
    "id": "voyage-mesure",
    "title": "Voyage sur mesure",
    "icon": "🗺",
    "description": "De la conception à votre retour, je m'occupe de tout. Vols, hôtels, excursions, transports — vous voyagez l'esprit léger.",
    "from": "À partir de 1500€/pers"
  },
  {
    "id": "croisieres",
    "title": "Croisières",
    "icon": "🛥",
    "description": "Toutes compagnies, toutes destinations. Mon expertise vous évite les pièges et trouve la cabine qui correspond vraiment à votre attente.",
    "from": "À partir de 800€/pers"
  },
  {
    "id": "lune-de-miel",
    "title": "Voyage de noces",
    "icon": "💕",
    "description": "Le voyage qui marque le début de votre vie ensemble mérite une attention particulière. Surprises, attentions, moments uniques.",
    "from": "Sur devis"
  }
]
```

#### Pièges
1. **Photos avec watermark fournisseurs** = très moche. Toujours utiliser ses propres photos OU acheter sur Unsplash/Pexels libre de droit.
2. **Texte trop générique** ("Partez à l'aventure...") — faire du concret, du vécu.
3. **Pas de prix indicatifs** = perte de leads (peur de demander). Toujours afficher fourchettes ("À partir de 1500€").
4. **Promesses non tenues** sur le luxe → avis catastrophiques.
5. **Réactivité affichée mais lente en réalité** : si tu dis "réponse sous 24h", il faut tenir.
6. **Mention licence d'agent de voyage** : obligatoire en Belgique (numéro de licence A ou B).
7. **Conditions générales de vente** : OBLIGATOIRES + assurance professionnelle visible.
8. **Concurrence agressive des plateformes** (Booking, Expedia) : différenciation = expertise + service personnalisé. Le site doit le **prouver**, pas juste l'affirmer.

#### Idée bonus — Carnet de voyages personnel
Une section "Mes carnets" avec albums chronologiques de ses propres voyages = **trust signal puissant**. Montre que tu connais réellement les destinations que tu vends.

---

### 📊 Tableau de synthèse — temps de dev avec la skill

| Variante | Complexité | Temps de dev avec skill |
|---|---|---|
| Restaurant simple | Moyenne | 1-2 jours |
| Restaurant multi-langue + booking | Haute | 2-3 jours |
| Centre méditation | Basse-moyenne | 1 jour |
| Électricien (pages services + zones) | Moyenne | 1-2 jours |
| Tourisme avec carnets | Haute (galerie complexe) | 2-3 jours |

À cela s'ajoute toujours **2-3 semaines** de collecte contenu côté client (incompressible).
