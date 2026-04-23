# Judo Club Anderlecht — Site web

Site officiel du **Judo Club Anderlecht**, école traditionnelle de judo fondée en 1977
par Jean-Marc Demaret — Rue du Serment 54, 1070 Anderlecht.

## 🌐 Voir le site

Une fois publié via GitHub Pages : **https://jmdemaret.github.io/jcasite/**

## 📁 Structure

```
/
├── index.html                 # Site public (hero, cours, tarifs, galerie, contact…)
├── admin.html                 # Admin : bannière, galerie, actu, événements, témoignages
├── logo2.png                  # Logo principal du club
├── dojo.jpeg                  # Photo du dojo (hero cinématique + galerie)
├── judoclubanderlecht/        # Photos additionnelles (kids, training, dojo-hall)
└── README.md
```

## ✏️ Administration

L'interface `/admin.html` permet d'éditer :

- **Bannière d'information** en haut du site (message, on/off)
- **Galerie photo** (ajouter, supprimer, réordonner, modifier les titres)
- **Actualités** (news du club)
- **Événements & calendrier** (stages, passages de grade, compétitions)
- **Témoignages** parents & judokas

Les données sont stockées dans le `localStorage` du navigateur. Un bouton
**Exporter / Importer** permet de sauvegarder un JSON pour backup ou transfert.

## 🚀 Déploiement — GitHub Pages

1. Settings → Pages → Build and deployment
2. Source : **Deploy from a branch**
3. Branch : **main** · Folder : **/ (root)** → Save

Site publié à : `https://jmdemaret.github.io/jcasite/`

## 🛠 Dev local

C'est du HTML / CSS / JavaScript pur — aucune dépendance à installer.
Pour le servir localement :

```bash
python -m http.server 8000
# ouvrir http://localhost:8000/
```

## 📞 Contact

- **Adresse** : Rue du Serment 54, 1070 Anderlecht
- **Téléphone** : +32 476 79 10 29
- **Email** : secretariat.judoclubanderlecht@gmail.com
