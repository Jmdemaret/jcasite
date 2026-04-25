# Architecture — Décisions à prendre

Une fois le questionnaire rempli, dérouler ces choix dans l'ordre.

---

## 1. Domaine

| Situation | Choix |
|---|---|
| Pas de domaine, pas de budget | URL GitHub Pages : `username.github.io/repo-name` |
| Pas de domaine, budget OK | Acheter chez Combell (BE) / Gandi / OVH ~10-15€/an |
| Domaine existant chez Wix/Squarespace | Récupérer chez l'ancien fournisseur, transférer chez registrar standard |
| Domaine existant chez registrar standard | Configurer DNS (4 A records vers GitHub Pages + CNAME www) |

**Pour Combell** : interface DNS → "Manage records" → Effacer existing A records (s'ils pointent vers Wix), ajouter :
```
@   A     185.199.108.153
@   A     185.199.109.153
@   A     185.199.110.153
@   A     185.199.111.153
www CNAME username.github.io.
```
Délai propagation : 1-24h.

---

## 2. Hébergement

**Toujours** : GitHub Pages pour le site statique. Gratuit, fiable, déploiement à chaque push.

**Optionnel** : Netlify pour les fonctions serverless (formulaires).
- À ajouter si formulaires nécessaires
- À skipper si pas de formulaire (juste boutons mailto:)

---

## 3. Email transactionnel (formulaires)

```
Question: existe-t-il déjà un email pro ?
├─ Oui → utiliser le SMTP existant (configurer SMTP_HOST/PORT/USER/PASS)
└─ Non → créer une boîte chez Combell/OVH (~3€/mois pour 1 boîte)
```

**Si SMTP du registrar pas autorisé sur Netlify (port 25 bloqué)** :
- Combell : utiliser `smtp-auth.mailprotect.be:587` (STARTTLS)
- OVH : utiliser `ssl0.ovh.net:587` 
- Gandi : `mail.gandi.net:587`

**Alternative gratuite** :
- Resend.com (3000 emails/mois free)
- Mailtrap free tier
- Brevo (Sendinblue) SMTP free tier 300/jour

---

## 4. Analytics

```
Cookies acceptables ? 
├─ Non (préférer pas de bandeau) :
│  ├─ Umami Cloud (free 100k events/mois) ⭐ recommandé
│  ├─ GoatCounter (gratuit illimité, ultra simple)
│  └─ Plausible (9€/mois, dashboard plus joli)
└─ Oui (ok pour bandeau) :
   ├─ Cloudflare Web Analytics (gratuit, demande DNS via CF)
   └─ Google Analytics 4 (gratuit mais GDPR pénible)
```

**Setup Umami** : 5 min de l'utilisateur pour créer le compte, je récupère le snippet et l'intègre.

---

## 5. Multilingue

```
Combien de langues ?
├─ 1 → simple
├─ 2 (FR/NL) → 2 options :
│  ├─ A) Sous-domaines : nl.club.be / fr.club.be (2 sites, plus de maintenance)
│  ├─ B) Suffixes URL : /fr/, /nl/ (1 site, complexité dans le rendering)
│  └─ C) Toggle FR/NL en JS lisant content.json (le plus simple, content.json a {fr: "...", nl: "..."})
└─ 3+ → recommander un CMS dédié (Strapi, Sanity, Storyblok)
```

Pour le template JCA : option C est le naturel. Le content.json a déjà la structure pour évoluer vers `{fr: "..."}` mais il faut adapter le rendering.

⚠️ Multilingue ajoute 30-50% de temps de dev et 2× de temps de maintenance.

---

## 6. Système d'admin

**Toujours** : `admin.html` local + GitHub PAT. Aucune alternative dans ce template.

Si client veut un admin "vraiment" web (multi-utilisateurs, accessible depuis tablette etc.) → Wordpress, Strapi, Decap CMS sont des alternatives mais SORTENT du scope de ce template.

---

## 7. Sections du site à activer

Du questionnaire, déterminer quelles sections garder dans `index.html`.

**Sections du template JCA** (à toggle dans `content.json.sections`) :
- club, cours, tarifs, actu, evenements, galerie, equipe, temoignages, faq, preInscription, sponsors, contact

Pour un restaurant on remplacerait :
- cours → menu
- tarifs → carte
- equipe → personnel
- galerie → plats / décor
- evenements → événements/réservations
- preInscription → contact pour réservation

Garder la structure de toggle + sections, juste renommer/adapter les sections selon le métier.

---

## 8. Optionnels à activer ou skipper

| Feature | Quand l'activer | Quand skipper |
|---|---|---|
| **Annonces calendrier** | Si fermetures/vacances récurrentes | Site sans périodes de fermeture |
| **Galerie albums** | Si plusieurs événements à documenter | Galerie simple < 20 photos |
| **Calendrier visuel cours** | Sport/cours récurrents | Pas d'horaires fixes |
| **Google Reviews sync** | Si fiche Google Business active avec >5 avis | Si pas encore de Business Profile |
| **RSS feed** | Si le client va publier régulièrement (actu/blog/events) | Site stable peu de mises à jour |
| **Restore versions** | Toujours (très peu de coût) | Jamais skip |
| **Schema.org** | Toujours (gros gain SEO) | Jamais skip |
| **Sitemap + Search Console** | Toujours | Jamais skip |

---

## 9. Contenu critique pour le SEO local

Toujours configurer dès le début :
1. **Schema.org** avec :
   - Type `LocalBusiness` (ou subtype : `SportsClub`, `Restaurant`, `Dentist`, etc.)
   - Adresse complète (`PostalAddress`)
   - Coordonnées GPS (`GeoCoordinates`)
   - Horaires (`openingHoursSpecification`)
   - Téléphone, email
   - `aggregateRating` si Google Reviews
2. **Open Graph + Twitter Card** : titre, description, image
3. **Meta description** unique, riche, locale (mention de la ville)
4. **`<link rel="canonical">`** vers la version www-less HTTPS
5. **`robots.txt`** avec `/admin.html` bloqué
6. **`sitemap.xml`** avec UNE seule URL (la page d'accueil) — pas de fragments
7. **Verification Google Search Console** avec balise meta ou fichier HTML

---

## 10. Pré-requis avant de commencer le code

À s'assurer AVANT le scaffolding :
- [ ] Compte GitHub du client (sinon, partager le repo via collaboration)
- [ ] Compte Netlify (gratuit) si formulaires
- [ ] Domaine acheté + accès aux DNS (ou décision de prendre le default github.io)
- [ ] Email pro (ou décision sur celui à créer)
- [ ] Logo + 3 photos minimum reçues
- [ ] Texte de mission (au moins 1 phrase) reçu
- [ ] Mentions légales rédigées (peuvent être ajoutées plus tard mais à prévoir)
