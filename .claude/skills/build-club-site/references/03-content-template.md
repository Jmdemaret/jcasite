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

## Notes d'adaptation par métier

### Restaurant
- Renommer `cours` → `menu`, `pricing` → `carte`, `team` → `equipe`
- Ajouter un champ `gallery` ou `albums` pour les plats
- Activer `events` pour réservations privées

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
