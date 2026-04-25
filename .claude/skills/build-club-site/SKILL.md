---
name: build-club-site
description: Build a complete club/association/small-business website using the Judo Club Anderlecht reference template (GitHub Pages + Netlify Functions + admin via GitHub API). Use when the user wants to start a new website project for a sports club, ASBL, association, school, restaurant, freelance, or small business — especially if they say "build me a site like X", "I want to migrate from Wix/Squarespace", or "I need a no-cost CMS". Skip if the user already has a different stack (Wordpress, Shopify, custom backend) and just wants edits.
---

# Build a Club Website — JCA Template Workflow

> Reference template: https://github.com/Jmdemaret/jcasite (live at https://judoclubanderlecht.be)

## What this skill does

Guides Claude through building a static + serverless website for a small organization, reusing the architecture and components from the Judo Club Anderlecht site:

- **Stack**: GitHub Pages (static, free) + Netlify Functions (forms, free tier) + GitHub API admin (free)
- **Built-in features**: Hero with cinematic photo/video, sections (about, courses/services, pricing, team, gallery with albums, news, events, testimonials, FAQ, sponsors, contact form, pre-registration form), date-driven announcements, calendar editor, custom favicon, SEO meta + Schema.org JSON-LD, Open Graph, sitemap.xml, robots.txt, RSS feed, Umami analytics integration, Google Reviews sync via SerpAPI workflow, version history with restore.
- **Maintenance model**: One single-page admin (HTML) running locally via `file://`, communicating with GitHub via PAT to publish content. No server to maintain.

## Triggers

Use this skill when the user:
- Asks to "build a website for [club/association/ASBL/business]"
- Wants to migrate from Wix, Squarespace, Wordpress, Wordpress.com, Joomla, etc.
- Mentions GitHub Pages, Netlify, or "no recurring cost" hosting
- Says "I want a site like the judo club one"
- Wants a CMS without paying monthly

DO NOT use this skill when:
- The user wants e-commerce with hundreds of products → Shopify/Woo recommended
- The user needs a member portal with logins/profiles → needs proper backend
- The user needs real-time data (booking with availability sync, chat, etc.)
- The user has 20+ pages with deep navigation → needs proper CMS like Wordpress/Strapi
- The user already has a working Wordpress they're happy with

## Required workflow (DO NOT SKIP STEPS)

### Phase 0 — Confirm scope (5 min)
Before anything, ask the user 3 questions:
1. **Type**: Sports club, ASBL/charity, school, restaurant, freelance, or other?
2. **Scale**: Roughly how many "things" to manage (members, products, events…)?
3. **Languages**: French only, French + Dutch, multilingual?

If type is e-commerce-heavy, members-portal, or 5+ languages → STOP, tell user this template isn't ideal and recommend alternatives.

### Phase 1 — Discovery questionnaire
Open `references/01-questionnaire.md` and walk through it WITH the user, section by section. Don't dump it all at once.

This is the most important phase. Aim for 30-45 minutes of guided interview. Don't write code until done.

For each unanswered question, either:
- Ask the user
- Suggest a sensible default and confirm

Output: a filled questionnaire document, ideally saved as `PROJECT.md` in the new repo.

### Phase 2 — Architecture decisions
Read `references/02-architecture.md` and walk through the decision tree based on questionnaire answers.

Key decisions to lock down:
- Custom domain or default GitHub Pages URL?
- Forms: contact only, pre-registration, both, none?
- Email backend: existing SMTP or set up new account?
- Analytics: Umami (free), Plausible (paid), GoatCounter (free), or none?
- Multilingual: i18n strategy or separate domain per language?
- Optional features to enable: announcements, gallery albums, schedule editor, Google Reviews sync, RSS, restore feature

### Phase 3 — Project scaffolding
1. Fork or copy `Jmdemaret/jcasite` repo, OR create fresh with template files copied
2. Adapt `index.html`:
   - Brand colors in Tailwind config (see `references/04-customization.md`)
   - Fonts (Fraunces + Shippori Mincho is the JCA default; can swap)
   - Hero text + CTA buttons
   - Disable sections not needed (use `sections.X = false` in content.json)
   - Adjust nav links
   - Replace logo (`logo2.png`), `dojo.jpeg`, optional `hero.mp4`
   - Update Schema.org JSON-LD with new business info
   - Update meta tags (title, description, OG, Twitter)
   - Update favicon (regenerate via `_gen_favicons.py` or replace SVG)
   - Update map coordinates and transit stops
   - Update sponsors/partners section
3. Adapt `content.json` to match the schema (keep ID stability for albums)
4. Update `CNAME` if custom domain
5. Set up Netlify site if forms needed:
   - Connect repo to Netlify
   - Add env vars (SMTP_*, ALLOWED_ORIGIN, LIST_SECRET, NETLIFY_BLOBS_TOKEN if dashboard)
   - Update `forms.scriptUrl` in content.json
6. Configure DNS at registrar if custom domain (4 A records to GH Pages IPs + CNAME for www)
7. Configure GitHub Pages in repo settings (deploy from main, root)
8. If Google Reviews sync wanted: add SERPAPI_KEY + GOOGLE_PLACE_ID as Actions secrets

### Phase 4 — Content fill
Use `references/03-content-template.md` as starting point. Fill in:
- Texts (hero, club intro, FAQ items, etc.)
- Schedule (courses, opening hours)
- Pricing table
- Team / sensei bios
- Initial gallery (1-2 photos minimum so the section isn't empty)
- Initial news + events (1-2 placeholder items)

### Phase 5 — Deployment & verification
Walk through `references/05-deployment-checklist.md`. Don't skip the final QA — most issues come from forgetting one of these:
- All test forms submit successfully
- Schema.org validator passes
- Mobile layout OK on real device
- All admin functions work (publish, restore, image upload)
- Search Console verified, sitemap submitted

### Phase 6 — Handoff
Generate a `CLAUDE.md` for the new repo (reuse the JCA template, swap names/URLs/secrets), generate the admin Guide tab content, write a "first-day onboarding" doc for the client.

## Critical rules

1. **Never write code in Phase 1** — premature implementation creates rework when discovery reveals constraints
2. **Always preserve admin gitignore** — `admin.html` MUST stay local, never deploy
3. **Never expose tokens** — PATs, SMTP passwords, secrets stay in env vars / localStorage
4. **Schema-driven** — all dynamic content goes through `content.json`, no hardcoded copy in `index.html` for client-editable text
5. **Versioning preserved** — keep the `_meta.version + history` pattern from JCA, don't simplify it
6. **Mobile-first verification** — every section must work on a 375px wide screen

## Estimated timing

| Phase | Duration |
|---|---|
| 0 — Scope | 5 min |
| 1 — Discovery | 30-60 min interactive |
| 2 — Architecture | 15 min |
| 3 — Scaffolding | 1-2h |
| 4 — Content | 2-4h (depends on client material) |
| 5 — Deployment | 30 min + 1-2h DNS propagation |
| 6 — Handoff | 30 min |

**Total realistic dev time: 1 full day for MVP, 2-3 days with content polish.**

Realistic project total (including client back-and-forth, photo collection, brand decisions): **2-3 weeks**.

## References

- `references/01-questionnaire.md` — discovery form to fill with client
- `references/02-architecture.md` — decision tree for stack choices
- `references/03-content-template.md` — starter content.json with examples
- `references/04-customization.md` — colors, fonts, tone, brand adaptation
- `references/05-deployment-checklist.md` — step-by-step go-live
- `references/06-pitfalls.md` — common mistakes to avoid

## When in doubt

If a feature request doesn't fit naturally in this template, DON'T force it. Tell the user honestly that a different stack would be better. The JCA template is excellent for ~80% of small org sites; the remaining 20% should use Wordpress, Astro+Sanity, Webflow, etc.
