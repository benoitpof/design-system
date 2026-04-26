# ICONS.md — POF Curated Icon Set (Tabler Icons)

**Library:** Tabler Icons — MIT License — https://tabler.io/icons
**CDN base:** `https://unpkg.com/@tabler/icons/icons/outline/[name].svg`
**In pptxgenjs:** rasterize via `sharp` + `react-icons` or fetch SVG from CDN, convert to base64 PNG at 256px
**Default color on light bg:** `#1C1F3B` navy · **On dark bg:** `#FFFFFF` white
**Never use:** coral `#E8546C` for icons — emphasis color only

### Size guide (LAYOUT_WIDE slides)
- Feature card icon: 0.6"×0.6" (rasterize at 256px)
- Inline header icon: 0.4"×0.4"
- Full-width hero: 1.0"×1.0"
- Process step: 0.5"×0.5"

---

## ♻️ ENVIRONNEMENT & DURABILITÉ — Icônes prioritaires recyclage/écologie

> Fichiers SVG disponibles localement dans `assets/icons/ecology/`
> Usage direct sans CDN : `../assets/icons/ecology/[name].svg`

| Fichier | Local | Usage principal | Contexte interdit |
|---|:---:|---|---|
| `recycle.svg` | ✅ | Boucle plastique, circularité, slide 1.1 | — |
| `leaf.svg` | ✅ | Durabilité, impact environnemental | Pas pour section finance |
| `solar-panel.svg` | ✅ | Énergie solaire, solar-ready factories | — |
| `droplet.svg` | ✅ | Closed-loop water, eau recyclée | — |
| `planet.svg` | ✅ | Planète, pollution globale, planetary boundary | Pas pour métriques financières |
| `fish.svg` | ✅ | Océan, plastic leakage, contexte marin | — |
| `bolt.svg` | ✅ | Énergie, efficacité opérationnelle | — |
| `flame.svg` | ✅ | Incinération, burning déchets, contexte Acte 1 | **Jamais** dans section Solution ou Impact |

---

# POF — Shortlist Tabler Icons

| Fichier                  | Usage principal                                                | Contexte interdit                          |
|--------------------------|----------------------------------------------------------------|--------------------------------------------|
| **INFRASTRUCTURE & PRODUCTION**                                                                                               |||
| `building-factory-2.svg` | CDF/PTF, site de production, couverture deck                   | Pas sur fond teal                          |
| `container.svg`          | Unité conteneurisée, déploiement, logistique                   | -                                          |
| `package.svg`            | Produit fini, palette, livraison                               | -                                          |
| `hammer.svg`             | Fabrication, assemblage, atelier                               | Pas pour symboliser l'impact social        |
| `tools.svg`              | Maintenance locale, SAV, réseau technique                      | -                                          |
| `filter.svg`             | Tri, sorting du plastique, étape CDF                           | -                                          |
| `arrows-exchange.svg`    | Transformation, flux matière, boucle circulaire                | -                                          |
| `truck.svg`              | Reverse logistics, consolidation réseau, AGL                   | -                                          |
| `trash.svg`              | Déchets collectés, problème, contexte Acte 1                   | Pas dans section Impact (connotation négative) |
| `scan.svg`               | QR code, collecte terrain, traçabilité physique                | -                                          |
| **RÉSEAU & FRANCHISE**                                                                                                        |||
| `network.svg`            | Réseau franchise, maillage de factories                        | -                                          |
| `world.svg`              | Déploiement international, 3 clusters                          | -                                          |
| `map-2.svg`              | Carte réseau, section géographie site                          | -                                          |
| `map-pin.svg`            | Localisation d'une factory, hub                                | -                                          |
| `building-store.svg`     | Hub local, entrepreneur franchisé                              | -                                          |
| `route.svg`              | Chaîne de valeur, supply chain locale                          | -                                          |
| **IMPACT & KPIs**                                                                                                             |||
| `chart-bar.svg`          | KPIs agrégés, tableau de bord impact                           | -                                          |
| `chart-line.svg`         | Croissance, trajectoire 2030, scalabilité                      | -                                          |
| `chart-dots.svg`         | ImpactLab, données terrain, scatter                            | -                                          |
| `award.svg`              | Certification, impact prouvé, B Corp                           | Pas pour finance                           |
| `target.svg`             | Objectif 200 factories, vision 2030                            | -                                          |
| `circle-check.svg`       | Validation, proof point, factory opérationnelle                | -                                          |
| `trending-up.svg`        | Scalabilité, croissance réseau                                 | -                                          |
| `clipboard-list.svg`     | Reporting ESG, audit, due diligence                            | -                                          |
| `users.svg`              | Emplois créés, équipe, 10 000 jobs                             | -                                          |
| **ENVIRONNEMENT & DURABILITÉ** *(voir section dédiée en tête de doc)*                                                        |||
| `recycle.svg`            | Boucle plastique, circularité, slide 1.1                       | -                                          |
| `leaf.svg`               | Durabilité, impact environnemental                             | Pas pour section finance                   |
| `solar-panel.svg`        | Énergie solaire, solar-ready factories                         | -                                          |
| `droplet.svg`            | Closed-loop water, eau recyclée                                | -                                          |
| `planet.svg`             | Planète, pollution globale, planetary boundary                 | Pas pour métriques financières             |
| `fish.svg`               | Océan, plastic leakage, contexte marin                         | -                                          |
| `bolt.svg`               | Énergie, efficacité opérationnelle                             | -                                          |
| `flame.svg`              | Incinération, burning déchets, contexte Acte 1                 | Jamais dans section Solution ou Impact     |
| **FINANCE & INVESTISSEMENT**                                                                                                  |||
| `coins.svg`              | CAPEX, financement, unit economics                             | -                                          |
| `currency-euro.svg`      | Revenus, modèle économique, hub Dakar                          | -                                          |
| `currency-dollar.svg`    | Green bonds, DFI, plateforme $50M                              | -                                          |
| `scale.svg`              | Équilibre impact/rentabilité                                   | -                                          |
| `shield-check.svg`       | Conformité ESG, CSRD, EPR                                      | -                                          |
| `certificate.svg`        | Plastic Certificates, blockchain cert                          | Pas pour team/people                       |
| `building-bank.svg`      | DFIs, AFD, investisseurs institutionnels                       | -                                          |
| **TRAÇABILITÉ & TECH**                                                                                                        |||
| `qrcode.svg`             | QR code, blockchain, suivi lot                                 | -                                          |
| `link.svg`               | Blockchain, chaîne de données, Inclusiv                        | -                                          |
| `database.svg`           | MRV, données impact, ImpactLab                                 | -                                          |
| `lock.svg`               | Sécurité, audit, gouvernance                                   | -                                          |
| `telescope.svg`          | Vision R&D, prospective 2030–2035                              | -                                          |
| **PERSONNES & FORMATION**                                                                                                     |||
| `user-check.svg`         | Entrepreneur validé, opérateur certifié                        | -                                          |
| `handshake.svg`          | Partenariat corporate, Forvia / AGL                            | -                                          |
| `school.svg`             | Plastic Odyssey Academy, formation opérateurs                  | -                                          |
| **DOCUMENTS & COMMUNICATION**                                                                                                 |||
| `file-text.svg`          | Étude de faisabilité, rapport, annexes deck                    | -                                          |
| `presentation.svg`       | Pitch, deck investisseur, slide header                         | -                                          |
| `tag.svg`                | Label Impact Plastic, marque produit                           | -                                          |

---

## 🆕 ICÔNES GÉNÉRALES — Extension emoji coverage

> Fichiers SVG dans `assets/icons/` — stroke="#1A2B4A" (POF dark-blue)
> Source: Tabler Icons v3.41.1 (MIT) — https://tabler.io/icons

### Outils & Actions
| Fichier | Emoji | Usage |
|---|:---:|---|
| `tool.svg` | 🔧 | Maintenance, réparation, technique |
| `settings.svg` | ⚙️ | Configuration, paramètres |
| `writing.svg` | ✍🏻 | Rédaction, signature, contenu |
| `pencil.svg` | ✏️ | Édition, annotation |
| `notes.svg` | 📝 | Notes, mémos, suivi |
| `paperclip.svg` | 📎 | Pièce jointe, document lié |
| `refresh.svg` | 🔄 | Mise à jour, synchronisation |
| `arrows-shuffle.svg` | 🔀 | Réorganisation, shuffle |
| `player-play.svg` | ▶️ | Lancer, démarrer, vidéo |
| `circle-x.svg` | ❌ | Annulation, refus, erreur |
| `copyright.svg` | ©️ | Droits, propriété intellectuelle |

### Communication & Médias
| Fichier | Emoji | Usage |
|---|:---:|---|
| `mail.svg` | ✉️ | Email, correspondance |
| `microphone.svg` | 🎙️ | Podcast, prise de parole, interview |
| `camera.svg` | 📷 | Photo, documentation visuelle |
| `video.svg` | 🎥 | Vidéo, formation, contenu |
| `device-mobile.svg` | 📲 | App mobile, communication terrain |
| `antenna.svg` | 📡 | Connectivité, signal, IoT |

### Documents & Savoir
| Fichier | Emoji | Usage |
|---|:---:|---|
| `book.svg` | 📗 | Formation, guide |
| `books.svg` | 📚 | Bibliothèque, ressources |
| `inbox.svg` | 📥 | Réception, collecte |
| `key.svg` | 🔑 | Accès, sécurité, licence |
| `pin.svg` | 📌 | Point clé, épinglé |
| `bulb.svg` | 💡 | Idée, innovation, insight |
| `sparkles.svg` | ✨ | Nouveauté, excellence, IA |

### Finances & Business
| Fichier | Emoji | Usage |
|---|:---:|---|
| `cash.svg` | 💰 | Revenus, investissement, cash |
| `trophy.svg` | 🏆 | Performance, succès, KPI |
| `star.svg` | ⭐️ | Priorité, qualité |
| `flag.svg` | 🏳️ | Pays, territoire, jalons |
| `barrel.svg` | 🛢️ | Matière, stock plastique |
| `microscope.svg` | 🔬 | R&D, analyse, lab |
| `hourglass.svg` | ⏳ | Délai, durée, deadline |

### Personnes & Relations
| Fichier | Emoji | Usage |
|---|:---:|---|
| `hand-stop.svg` | 🙌🏻 | Collaboration, validation |
| `heart.svg` | ❤️ | Impact social, bien-être |

### Nature & Environnement
| Fichier | Emoji | Usage |
|---|:---:|---|
| `leaf-2.svg` | 🌿 | Naturalité, bio, organique |
| `seedling.svg` | 🌱 | Croissance, démarrage, germination |
| `plant-2.svg` | 🪴 | Culture, soin |
| `tree.svg` | 🌳 | Forêt, reforestation, CO₂ |

### Transport & Logistique
| Fichier | Emoji | Usage |
|---|:---:|---|
| `plane.svg` | ✈️ | Voyage, export, international |
| `plane-departure.svg` | 🛫 | Départ, début de mission |
| `plane-arrival.svg` | 🛬 | Arrivée, réception |
| `ship.svg` | ⛴️ | Transport maritime, conteneur |
| `lifebuoy.svg` | 🛟 | Support, sécurité, secours |
| `rocket.svg` | 🚀 | Lancement, scale-up, ambition |

### Infrastructure
| Fichier | Emoji | Usage |
|---|:---:|---|
| `building.svg` | 🏢 | Bureau, siège, partenaire |
| `plug.svg` | 🔌 | Connexion électrique, intégration |
| `tool.svg` | 🔧 | Maintenance, mécanique |

### Alimentation
| Fichier | Emoji | Usage |
|---|:---:|---|
| `tools-kitchen.svg` | 🍽️ | Restauration, alimentation locale |

---

*Icônes manquantes dans Tabler v3.41.1 : `palm-tree` (→ utiliser `tree`), `handshake` (→ utiliser `users-group`), `wrench` (→ utiliser `tool`), `file-cabinet` (→ utiliser `database`)*
