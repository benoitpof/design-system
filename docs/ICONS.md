# POF Design System — Icon Library

> **93 pictos** · 3 variantes couleur chacun · 279 fichiers SVG totaux
> Tous les fichiers sont auto-suffisants — **aucune dépendance CDN**.

---

## Utilisation

Chaque picto existe en 3 variantes couleur dans le repo :

```
{nom}_{couleur}.svg
```

| Variante | Couleur | Usage |
|---|---|---|
| `_navy.svg` | `#1A2B4A` | Fond blanc ou clair — usage par défaut |
| `_white.svg` | `#FFFFFF` | Fond marine, teal, sombre |
| `_teal.svg` | `#80C8C3` | Accent, mise en valeur sur fond marine |

### Intégration dans pptxgenjs

```js
const fs = require("fs");
const svgData = path =>
  "image/svg+xml;base64," + Buffer.from(fs.readFileSync(path, "utf8")).toString("base64");

// Icône "tool" en navy sur fond blanc
slide.addImage({ data: svgData("assets/icons/tool_navy.svg"), x:1, y:1, w:0.6, h:0.6 });

// Picto env "poubelle-de-tri" blanc sur fond marine
slide.addImage({ data: svgData("assets/icons/environment/poubelle-de-tri_white.svg"), x:1, y:1, w:1, h:1 });
```

### Tailles recommandées (LAYOUT_WIDE 13.3"×7.5")

| Contexte | Taille |
|---|---|
| Icône feature card | 0.6"×0.6" |
| Icône inline header | 0.4"×0.4" |
| Hero full-width | 1.0"×1.0" |
| Picto environnement | 0.9"×0.9" |

---

## Structure du repo

```
assets/icons/
├── environment/          # 38 pictos environnement custom (filaire POF) × 3 couleurs
│   ├── poubelle-de-tri_navy.svg
│   ├── poubelle-de-tri_white.svg
│   ├── poubelle-de-tri_teal.svg
│   └── ...
├── ecology/              # 8 icônes écologie (Tabler outline) × 3 couleurs
│   ├── recycle_navy.svg
│   └── ...
├── tool_navy.svg         # 47 icônes générales (Tabler v3.41.1) × 3 couleurs
└── ...
```

---

## Section 1 — Pictos Environnement (custom POF)

> Source : vectorisation filaire OpenCV depuis PPTX POF · ViewBox 984×984 · sw=45
> Dossier : `assets/icons/environment/`

| Fichier slug | Nom FR | Description |
|---|---|---|
| `poubelle-de-tri` | Poubelle de tri | Collecte et tri des ressources plastiques |
| `recyclage` | Recyclage | Symbole recyclage, boucle matière générale |
| `eau-recyclee` | Eau recyclée | Circuit eau fermé, ressource hydrique |
| `circularite` | Circularité | Économie circulaire, boucle produit |
| `collecte-mobile` | Collecte mobile | Camion collecte et transport matière |
| `emballage-recycle` | Emballage recyclé | Sac / emballage recyclable en fin de vie |
| `cle-outil` | Clé / outil | Équipement, maintenance, accès technique |
| `don-vegetal` | Don végétal | Apport de matière, collecte verte |
| `contenant-eco` | Contenant éco | Bouteille / emballage environnemental |
| `co2` | CO2 | Émissions carbone, bilan GES |
| `affichage-eco` | Affichage éco | Information environnementale, reporting |
| `document-recycle` | Document recyclé | Fiche de tri, documentation recyclage |
| `innovation-verte` | Innovation verte | Idée éco, R&D, solution durable |
| `etiquette-recyclable` | Étiquette recyclable | Label écologique, certification produit |
| `contenant-reutilisable` | Contenant réutilisable | Bocal / emballage réutilisable |
| `produit-eco-concu` | Produit éco-conçu | Spray, produit chimique écologique |
| `plastique-marin` | Plastique marin | Pollution océan, recyclage mer |
| `verre-recyclable` | Verre recyclable | Verre, matière fragile, recyclage verre |
| `agriculture` | Agriculture | Culture locale, main verte, agriculture |
| `borne-de-collecte` | Borne de collecte | Point de collecte digital / kiosque |
| `vegetal` | Végétal | Nature, espace vert, reforestation |
| `textile-recycle` | Textile recyclé | Mode éco, fast fashion circulaire |
| `industrie-verte` | Industrie verte | Usine écologique, ville durable |
| `usine-recyclage` | Usine recyclage | Site de traitement des ressources plastiques |
| `eau-propre` | Eau propre | Eau potable, robinet, économie eau |
| `energie-verte` | Énergie verte | Centrale éco, production d'énergie propre |
| `energie-solaire` | Énergie solaire | Panneaux solaires, solaire off-grid |
| `point-de-collecte` | Point de collecte | Corbeille, bac de collecte |
| `produit-marin` | Produit marin | Pêche, produit de la mer, plastique océan |
| `sac-recyclable` | Sac recyclable | Emballage collecte, sac réutilisable |
| `arbre` | Arbre | Reforestation, nature, séquestration CO2 |
| `borne-depot` | Borne dépôt | Borne de dépôt matière, point fixe |
| `eolien` | Éolien | Énergie éolienne, vent, renouvelable |
| `mobilite-electrique` | Mobilité électrique | Véhicule électrique, recharge, logistique verte |
| `economie-circulaire` | Économie circulaire | Cycle complet, réutilisation, boucle fermée |
| `liquide-huile` | Liquide / huile | Produit liquide, huile, matière fluide |
| `danger-nucleaire` | Danger / nucléaire | Symbole danger, matière radioactive |
| `velo` | Vélo | Mobilité douce, transport durable, vélo |

---

## Section 2 — Écologie (Tabler outline)

> Source : Tabler Icons v3.41.1 (MIT) — stockés localement, pas de CDN
> ViewBox 24×24 · sw=2 · Dossier : `assets/icons/ecology/`

| Fichier slug | Usage |
|---|---|
| `recycle` | Boucle plastique, circularité |
| `leaf` | Durabilité, impact environnemental |
| `solar-panel` | Énergie solaire, solar-ready |
| `droplet` | Circuit eau fermé, eau recyclée |
| `planet` | Planète, pollution globale |
| `fish` | Océan, plastic leakage, contexte marin |
| `bolt` | Énergie, efficacité opérationnelle |
| `flame` | Thermique, valorisation énergétique |

---

## Section 3 — Icônes générales (Tabler v3.41.1)

> Source : Tabler Icons v3.41.1 (MIT) — stockés localement, pas de CDN
> ViewBox 24×24 · sw=2 · Dossier : `assets/icons/`

| Fichier slug | Usage |
|---|---|
| `tool` | Maintenance, réparation, technique |
| `settings` | Configuration, paramètres système |
| `writing` | Rédaction, signature, contenu |
| `pencil` | Édition, annotation |
| `notes` | Notes, mémos, suivi terrain |
| `paperclip` | Pièce jointe, document lié |
| `refresh` | Synchronisation, mise à jour |
| `arrows-shuffle` | Réorganisation, allocation matière |
| `player-play` | Lancer, démarrer, activer |
| `circle-x` | Annulation, refus, erreur |
| `copyright` | Droits, propriété intellectuelle |
| `mail` | Email, correspondance officielle |
| `microphone` | Podcast, prise de parole |
| `camera` | Photo, documentation terrain |
| `video` | Vidéo, formation, contenu |
| `star` | Favori, excellence |
| `heart` | Impact social, valeurs |
| `home` | Siège, accueil, local |
| `building-factory-2` | Site de production, usine |
| `map-pin` | Localisation, site, terrain |
| `users` | Équipe, communauté, partenaires |
| `user-check` | Validation, certification |
| `chart-bar` | Métriques, KPIs, reporting |
| `trending-up` | Croissance, progression |
| `coin` | Budget, coût, investissement |
| `currency-dollar` | Revenus, pricing |
| `shopping-cart` | Achat, marketplace |
| `package` | Produit, livraison, kit |
| `truck` | Logistique, transport |
| `building-warehouse` | Entrepôt, stockage, hub |
| `certificate` | Certification, label |
| `shield-check` | Sécurité, conformité |
| `file-text` | Document, rapport |
| `clipboard-list` | Checklist, protocole |
| `world` | International, global |
| `plane` | Déplacement, mission, export |
| `tree` | Nature, reforestation |
| `hand-stop` | Stop, refus |
| `users-group` | Partenariat, réseau |
| `server` | Infrastructure, data |
| `cloud` | Cloud, sauvegarde |
| `link` | Connexion, intégration |
| `qrcode` | QR code, traçabilité |
| `barcode` | Code barre, identification |
| `lock` | Sécurité, accès restreint |
| `key` | Accès, authentification |

---

## Charte couleur

| Couleur | Hex | Usage |
|---|---|---|
| Marine POF | `#1A2B4A` | Fond clair — standard |
| Blanc | `#FFFFFF` | Fond sombre / marine |
| Teal | `#80C8C3` | Accent sur fond marine |

> Jamais coral `#E8546C` pour les icônes.

---

## Licence

- Pictos environnement : © Plastic Odyssey Factories — tous droits réservés
- Tabler Icons : MIT License — https://tabler.io/icons
