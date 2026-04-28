# ICONS.md — POF Icon System

**Version:** 3.0 | **Updated:** 2026-04-27 | **Design system:** v3.3.6

POF icon system uses **Tabler Icons CDN** as the primary source. Custom curated POF SVG icons (ecology, environment) have been archived because their custom stroke-width (28) was incompatible with the visual lightness of Tabler outline style.

---

## 1. Tabler Icons via CDN — primary source

```
https://unpkg.com/@tabler/icons/icons/outline/[name].svg
```

Examples : `building-factory-2`, `container`, `package`, `truck`, `arrows-exchange`, `chart-bar`, `users`, `settings`, `mail`, `recycle`, `leaf`, `droplet`, `flame`, `bolt`, `fish`, `planet`, `solar-panel`.

### Selection workflow

1. Browse https://tabler.io/icons or https://tabler-icons.io to find the icon
2. Use the outline variant: `unpkg.com/@tabler/icons/icons/outline/<name>.svg`
3. The SVG already has `stroke="currentColor"` and `stroke-width="2"` (light, modern)
4. Recolor via CSS : `<svg style="color: var(--pof-navy)">` or `color: var(--pof-teal)` etc.

### Embed strategies

| Context | Approach |
|---|---|
| HTML / Web | `<img src="https://unpkg.com/@tabler/icons/icons/outline/[name].svg">` + CSS `color` (currentColor cascade) |
| Inline HTML | Fetch SVG, paste inline, add `style="color: ..."` |
| PPTX | Fetch SVG, rasterize to PNG at target color (e.g. via `sharp` Node.js or any vector tool), embed PNG |
| DOCX / PDF | Fetch SVG, convert to PNG, embed image |

### Default colors per medium

- **Light bg** : `#1C1F3B` (navy)
- **Dark bg** : `#FFFFFF` (white)
- **Accent / highlight** : `#80C7C2` (teal)
- **Forbidden** : coral `#E8546C` for icons (emphasis only, not iconography)

### Recommended icon shortlist for POF

Industrial / production : `building-factory-2`, `container`, `package`, `tools`, `hammer`, `filter`, `truck`, `arrows-exchange`
Ecology / environment : `recycle`, `leaf`, `droplet`, `flame`, `bolt`, `fish`, `planet`, `solar-panel`, `tree`, `seedling`
Process / data : `chart-bar`, `chart-line`, `arrows-shuffle`, `refresh`, `settings`
Impact / people : `users`, `heart`, `trophy`, `award`, `school`
Logistics : `ship`, `plane`, `route`

---

## 2. POF brand pictos — `/assets/pictos/`

Two files only :

| File | Color | Use |
|---|---|---|
| `pof-picto-color.svg` | Teal `#80C7C2` | Mark on light backgrounds |
| `pof-picto-white.svg` | White | Mark on dark backgrounds |

POF brand symbol (waves stacked). Use cases : favicon, loading state, decorative corner mark, internal asset.

**NOT a UI icon.** Do not place inline in body text.

---

## 3. Archived (out of scope)

- `assets/icons/_archived/ecology/` — 32 SVG with stroke-width 28 (too thick vs Tabler style). Kept for reference, not used.
- `assets/icons/_archived/environment/` — 138 SVG, archived in v3.3.5.

These can be un-archived if a future need justifies it.

---

## Size guide

| Use case | Render size |
|---|---|
| Feature card icon | 0.6 × 0.6" (rasterize at 256px for PPTX) |
| Inline header icon | 0.4 × 0.4" |
| Full-width hero icon | 1.0 × 1.0" |
| Process step icon | 0.5 × 0.5" |
| Web (HTML/CSS) | 24 × 24 px to 64 × 64 px |

---

## Forbidden

- Drawing custom SVG icons inline (use Tabler CDN)
- Coral `#E8546C` for icons (emphasis only)
- Adding shadow / drop-shadow / blur / filter on icons
- Using brand picto as a UI icon
- Stretching, rotating, distorting icons
- Mixing different icon families in the same row / context (visual inconsistency)

---

# Annexe — Détails Tabler (ex ICONS-TABLER.md, fusionné v3.4.0)

name: icons-tabler
description: Curated Tabler icon library for POF — 106 icons × 3 colors + recolorable
---

# POF Design System — Icônes Tabler

> **106 icônes** · Tabler Icons v3.41.1 (MIT) · 4 variants par icône · 424 fichiers SVG
> Disponibles en ligne : https://tabler.io/icons — fichiers locaux pour usage offline et pptxgenjs

---

## Variantes couleur

| Fichier | Couleur | Usage |
|---|---|---|
| `{slug}.svg` | `stroke=currentColor` | CSS / HTML dynamique |
| `{slug}_navy.svg` | `#1A2B4A` | Fond blanc ou clair — défaut |
| `{slug}_teal.svg` | `#80C8C3` | Accent sur fond marine |
| `{slug}_white.svg` | `#FFFFFF` | Fond sombre / marine |

## Intégration pptxgenjs

```js
const fs = require("fs");
const svgData = p => "image/svg+xml;base64," + Buffer.from(fs.readFileSync(p, "utf8")).toString("base64");
slide.addImage({ data: svgData("assets/icons/tool_navy.svg"), x:1, y:1, w:0.5, h:0.5 });
```

---

## Alertes & statuts

| Slug | Nom | Usage POF |
|---|---|---|
| `alert-triangle` | Alerte | Avertissement, risque, situation critique |
| `circle-x` | Erreur | Annulation, refus, erreur de validation |
| `check` | Valider | Confirmation, tâche complétée, OK |
| `x` | Fermer | Suppression, annulation, fermeture |
| `hand-stop` | Stop | Arrêt, refus, limite opérationnelle |
| `shield-check` | Sécurité | Conformité, sécurité, validation qualité |
| `lock` | Verrouillé | Sécurité, accès restreint, confidentiel |
| `bell` | Notification | Alerte, rappel, notification terrain |

## Personnes & équipe

| Slug | Nom | Usage POF |
|---|---|---|
| `user` | Utilisateur | Profil individuel, membre de l'équipe |
| `users` | Équipe | Équipe, communauté, partenaires locaux |
| `user-check` | Accrédité | Validation, certification, opérateur formé |
| `user-plus` | Ajouter membre | Recrutement, onboarding, ajout accès |
| `id-badge` | Badge ID | Identification, accréditation, carte terrain |
| `address-book` | Contacts | Répertoire, contacts partenaires |
| `heart` | Impact | Impact social, valeurs, communauté |
| `award` | Récompense | Succès, meilleure pratique, top franchisé |
| `trophy` | Trophée | Excellence, performance, objectif atteint |
| `certificate` | Certification | Label qualité, norme, accréditation POF |

## Finance & business

| Slug | Nom | Usage POF |
|---|---|---|
| `coin` | Budget | Coût unitaire, investissement, capex |
| `coins` | Revenus | Flux financiers, cumul revenus |
| `currency-dollar` | Devise | Pricing, tarification, devise locale |
| `wallet` | Portefeuille | Trésorerie, fonds de roulement |
| `receipt` | Facture | Justificatif, facture, pièce comptable |
| `cash` | Cash | Paiement comptant, liquidités |
| `shopping-cart` | Achat | Commande, marketplace, approvisionnement |
| `briefcase` | Business | Activité commerciale, partenariat B2B |

## Données & analytics

| Slug | Nom | Usage POF |
|---|---|---|
| `chart-bar` | Graphique barres | KPIs, métriques, comparaison franchisés |
| `chart-pie` | Camembert | Répartition, parts, segmentation |
| `chart-line` | Courbe | Tendance, évolution, progression |
| `trending-up` | Croissance | Croissance, scale, montée en puissance |
| `target` | Objectif | Cible, KPI, objectif opérationnel |
| `gauge` | Performance | Indicateur, mesure de performance |
| `presentation` | Présentation | Pitch, slide deck, formation |
| `report` | Rapport | Rapport terrain, bilan périodique |

## Documents & fichiers

| Slug | Nom | Usage POF |
|---|---|---|
| `file-text` | Document | Rapport, contrat, fiche technique |
| `file` | Fichier | Fichier générique, export |
| `folder` | Dossier | Classement, projet, dossier franchisé |
| `clipboard-list` | Checklist | Protocole, SOP, liste de contrôle terrain |
| `notes` | Notes | Mémos, annotations, suivi terrain |
| `paperclip` | Pièce jointe | Document lié, attachement mail |
| `writing` | Rédaction | Contrat signé, accord, rédaction |
| `pencil` | Édition | Modification, annotation, mise à jour |
| `copyright` | Copyright | Propriété intellectuelle, droits POF |

## Communication

| Slug | Nom | Usage POF |
|---|---|---|
| `mail` | Email | Correspondance, communication officielle |
| `phone` | Téléphone | Contact direct, appel terrain |
| `message` | Message | Chat, discussion, feedback franchisé |
| `send` | Envoyer | Envoi, transmission, notification push |
| `microphone` | Micro | Podcast, prise de parole, audio |
| `video` | Vidéo | Formation vidéo, tutoriel, contenu |

## Navigation & localisation

| Slug | Nom | Usage POF |
|---|---|---|
| `map-pin` | Localisation | Site franchisé, localisation GPS, implantation |
| `pin` | Épingle | Marqueur, point d'intérêt |
| `map` | Carte | Carte territoire, couverture géographique |
| `compass` | Direction | Orientation, boussole, navigation |
| `world` | Monde | International, global, déploiement pays |
| `flag` | Pays | Pays cible, drapeau, implantation |

## Logistique & opérations

| Slug | Nom | Usage POF |
|---|---|---|
| `truck` | Transport | Logistique, livraison, collecte terrain |
| `ship` | Navire | Export maritime, fret, supply chain |
| `plane` | Avion | Déplacement, mission internationale |
| `plane-arrival` | Arrivée | Import, réception matériel |
| `plane-departure` | Départ | Export, départ mission |
| `package` | Colis | Kit machine, livraison, emballage |
| `building-warehouse` | Entrepôt | Stockage matière, hub logistique |
| `barrel` | Baril | Stockage vrac, pétrochimie, matière |
| `arrows-shuffle` | Réallocation | Redistribution matière, flux |
| `refresh` | Actualiser | Synchronisation, mise à jour process |

## Infrastructure & technique

| Slug | Nom | Usage POF |
|---|---|---|
| `tool` | Outil | Maintenance, réparation, technique terrain |
| `tools-kitchen` | Atelier | Outillage, poste de travail, fabrication |
| `settings` | Paramètres | Configuration système, réglage |
| `plug` | Branchement | Connexion électrique, alimentation |
| `database` | Base de données | Données opérationnelles, ERP, Notion |
| `server` | Serveur | Infrastructure, cloud, IT |
| `cloud` | Cloud | Sauvegarde, synchronisation, SaaS |
| `wifi` | Wi-Fi | Connectivité terrain, IoT machine |
| `link` | Lien | Intégration, connexion inter-systèmes |
| `qrcode` | QR Code | Traçabilité, identification lot, scan |
| `barcode` | Code barre | Identification produit, inventaire |
| `antenna` | Antenne | Signal, télémesure, connectivité |

## Gestion & planning

| Slug | Nom | Usage POF |
|---|---|---|
| `calendar` | Calendrier | Planning, maintenance préventive, agenda |
| `clock` | Horloge | Délai, temps de cycle, durée process |
| `hourglass` | Sablier | Attente, délai, temps restant |
| `inbox` | Inbox | Réception tâches, boîte mail, triage |
| `key` | Accès | Authentification, accréditation, accès site |
| `filter` | Filtrer | Filtrage données, tri, sélection |
| `search` | Recherche | Recherche franchisé, requête données |
| `plus` | Ajouter | Création, ajout, nouveau franchisé |
| `external-link` | Lien externe | Lien vers doc, ressource externe |

## Médias & création

| Slug | Nom | Usage POF |
|---|---|---|
| `camera` | Photo | Documentation terrain, photo machine |
| `photo` | Photo | Visuel, photo produit, asset |
| `star` | Favori | Mise en avant, top performance |
| `sparkles` | Innovation | Nouveau, IA, solution disruptive |
| `bulb` | Idée | Innovation, R&D, amélioration process |
| `rocket` | Lancement | Démarrage franchise, scale, go-live |
| `download` | Télécharger | Récupérer doc, export données |
| `upload` | Uploader | Envoi doc, rapport terrain |
| `share` | Partager | Diffusion, partage ressource |

## Nature & durabilité

| Slug | Nom | Usage POF |
|---|---|---|
| `tree` | Arbre | Reforestation, nature, CO2 |
| `leaf-2` | Feuille | Durabilité, éco-conception |
| `seedling` | Semis | Démarrage, croissance locale |
| `plant-2` | Plante | Végétal, agriculture locale |

## Divers

| Slug | Nom | Usage POF |
|---|---|---|
| `book` | Guide | Documentation, guide opérateur, SOP |
| `books` | Bibliothèque | Catalogue ressources, formation |
| `microscope` | Analyse | R&D, analyse qualité, laboratoire |
| `lifebuoy` | Support | Assistance, hotline, support franchisé |
| `player-play` | Démarrer | Lancer process, activer machine |
| `building` | Bâtiment | Entité, bureau, infrastructure |
| `device-mobile` | Mobile | Application terrain, notification |

---

*106 icônes · Tabler Icons MIT License · https://tabler.io/icons*
