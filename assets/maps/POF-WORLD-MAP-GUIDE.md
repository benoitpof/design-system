# POF World Map — Guide complet v1.1.0

> Dernière mise à jour : 2026-04-26  
> Auteur : Benoît Blancher / Plastic Odyssey Factories  
> Repo : `benoitpof/design-system` → `assets/maps/`

---

## Contenu du package

| Fichier | Description |
|---------|-------------|
| `pof-world-map-blank.svg` | Carte vierge — shapes pays + codes ISO, sans noms |
| `pof-world-map-annotated.svg` | Carte annotée — noms pays, codes ISO, dots îles |
| `POF-WORLD-MAP-GUIDE.md` | Ce document |

---

## Spécifications techniques

| Paramètre | Valeur |
|-----------|--------|
| Projection | Robinson (`+proj=robin +lon_0=0 +datum=WGS84 +units=m`) |
| Source | Natural Earth 110m admin_0_countries (domaine public) |
| Dimensions | 2418 × 1248 px (slide L09 full-bleed @ 2×) |
| Pays | 177 shapes individuels |
| Format | SVG 1.1, UTF-8 |
| Version design system | POF v3.2.3 |

---

## Structure du SVG

Chaque pays est un `<path>` dans `<g id="countries">`.

### Attributs sur chaque `<path>`

| Attribut | Exemple | Description |
|----------|---------|-------------|
| `id` | `c-SN` | `c-` + ISO 3166-1 alpha-2 |
| `data-iso2` | `SN` | Code pays ISO alpha-2 |
| `data-iso3` | `SEN` | Code pays ISO alpha-3 |
| `data-name` | `Senegal` | Nom anglais (Natural Earth) |
| `data-continent` | `Africa` | Continent |
| `data-subregion` | `Western Africa` | Sous-région |
| `data-groups` | `UEMOA CEDEAO UA` | Groupes séparés par espaces |

### Sélection par code

```js
// Un pays
document.getElementById('c-SN')           // Sénégal
document.getElementById('c-NG')           // Nigeria
document.getElementById('c-PH')           // Philippines
document.getElementById('c-ID')           // Indonésie

// Un groupe
document.querySelectorAll('[data-groups~="UEMOA"]')
document.querySelectorAll('[data-groups~="WEST_AFRICA_REGION"]')
document.querySelectorAll('[data-groups~="AFRICA"]')

// Un continent
document.querySelectorAll('[data-continent="Africa"]')
document.querySelectorAll('[data-continent="Asia"]')
```

---

## Pays prioritaires POF

Labels en **Poppins 11px 600** dans la carte annotée.  
Pays de déploiement actif ou d'intérêt stratégique.

| ISO | Pays | Région POF |
|-----|------|-----------|
| SN | Sénégal | Afrique de l'Ouest |
| GN | Guinée | Afrique de l'Ouest |
| CI | Côte d'Ivoire | Afrique de l'Ouest |
| CM | Cameroun | Afrique de l'Ouest |
| NG | Nigeria | Afrique de l'Ouest |
| KE | Kenya | Afrique de l'Est & Océan Indien |
| MA | Maroc | Afrique du Nord |
| MG | Madagascar | Océan Indien |
| MU | Île Maurice | Océan Indien |
| RW | Rwanda | Afrique de l'Est & Océan Indien |
| ID | Indonésie | Asie du Sud-Est |
| PH | Philippines | Asie du Sud-Est |

---

## Petites îles — dots teal

Ces pays sont trop petits pour être visibles à l'échelle 110m.  
Représentés par un **point teal (#80C7C2) ø7px** avec leader et label.

| ISO | Pays | Lon | Lat | Position SVG |
|-----|------|-----|-----|--------------|
| KM | Comores | 43.87°E | 11.67°S | (1498, 703) |
| SC | Seychelles | 55.49°E | 4.68°S | (1578, 649) |
| MU | Île Maurice | 57.55°E | 20.35°S | (1585, 770) |
| RE | La Réunion | 55.57°E | 21.12°S | (1571, 776) |

> **Note :** La Réunion est un département français (ISO FR-RE), représenté sous `RE` dans ce fichier pour la lisibilité.

---

## Groupes / Ensembles

Embarqués dans `<metadata id="pof-map-groupings">` en JSON, et appliqués via `data-groups` sur chaque path.

### Unions économiques et politiques

#### UEMOA
- **Nom complet :** Union Économique et Monétaire Ouest-Africaine
- **Type :** union_economique
- **Membres (8) :** BF · BJ · CI · GW · ML · NE · SN · TG

#### CEDEAO / ECOWAS
- **Nom complet :** Communauté Économique des États de l'Afrique de l'Ouest
- **Type :** union_economique
- **Membres (15) :** BF · BJ · CI · CV · GM · GH · GN · GW · LR · ML · MR · NE · NG · SL · SN · TG

#### Union Africaine (UA)
- **Nom complet :** Union Africaine / African Union
- **Type :** union_continentale
- **Membres (55) :** Tous les États souverains africains reconnus
- **Clé :** `UA`

#### Union Européenne (EU)
- **Nom complet :** Union Européenne / European Union
- **Type :** union_politique
- **Membres (27) :** AT · BE · BG · HR · CY · CZ · DK · EE · FI · FR · DE · GR · HU · IE · IT · LV · LT · LU · MT · NL · PL · PT · RO · SK · SI · ES · SE

#### ASEAN
- **Nom complet :** Association des Nations de l'Asie du Sud-Est
- **Type :** union_economique
- **Membres (10) :** BN · KH · ID · LA · MY · MM · PH · SG · TH · VN

#### ACP
- **Nom complet :** Organisation des États d'Afrique, des Caraïbes et du Pacifique
- **Type :** intergouvernemental
- **Membres (~79) :** Majorité des pays d'Afrique subsaharienne + Caraïbes + Pacifique

---

### Régions géographiques

#### Afrique (`AFRICA`)
- **Type :** continent
- **Description :** 54 États souverains + Sahara occidental
- **Membres :** Tous les pays du continent africain incluant les îles (Madagascar, Maurice, Comores, Seychelles, Cap-Vert, São Tomé)
- **Clé :** `AFRICA`

#### Asie du Sud-Est — continent (`SEA_CONTINENT`)
- **Type :** sous-région géographique
- **Description :** 11 pays de la sous-région Asie du Sud-Est
- **Membres :** BN · KH · ID · LA · MY · MM · PH · SG · TH · VN · TL
- **Clé :** `SEA_CONTINENT`

---

### Régions prioritaires POF

#### Afrique de l'Ouest (`WEST_AFRICA_REGION`)
- **Membres (17) :** SN · GN · CI · CM · NG · GH · ML · BF · NE · TG · BJ · SL · LR · GW · GM · MR · CV
- **Statut :** Région de déploiement actif POF

#### Afrique de l'Est & Océan Indien (`EAST_AFRICA_IO_REGION`)
- **Membres (10) :** KE · TZ · RW · UG · BI · ET · MG · MU · KM · SC
- **Statut :** Région de déploiement actif POF

#### Asie du Sud-Est (`SEA_REGION`)
- **Membres (11) :** ID · PH · KH · MY · TH · VN · MM · SG · BN · LA · TL
- **Statut :** Région de déploiement actif POF

---

## Couleurs POF — états de la carte

À appliquer via CSS inline ou `<style>` dans le SVG, ou depuis Claude Design.

| État | Fill | Usage |
|------|------|-------|
| Inactif (défaut) | `#EAEBED` | Pays non concernés |
| Pipeline | `#435D74` (steel) | Pays en cours d'étude / pipeline |
| Actif / déployé | `#1C1F3B` (navy) | Usines déployées |
| Highlight | `#80C7C2` (teal) | Survol / sélection |
| Accent | `#E8546C` (coral) | Donné clé — max 1-2 pays |

### Exemple CSS

```css
/* Nigeria déployé */
#c-NG { fill: #1C1F3B; }

/* Sénégal en pipeline */
#c-SN { fill: #435D74; }

/* Tous les membres UEMOA en pipeline */
[data-groups~="UEMOA"] { fill: #435D74; }

/* Tous les pays d'Afrique de l'Ouest POF */
[data-groups~="WEST_AFRICA_REGION"] { fill: #435D74; }

/* Indonésie active, Philippines pipeline */
#c-ID { fill: #1C1F3B; }
#c-PH { fill: #435D74; }
```

---

## Ajouter des dots d'usines

Les dots représentent les usines déployées. Couleur : teal `#80C7C2`, rayon : 8-12px.

### Conversion lon/lat → SVG (Python)

```python
from pyproj import Transformer

t = Transformer.from_crs("EPSG:4326",
    "+proj=robin +lon_0=0 +x_0=0 +y_0=0 +datum=WGS84 +units=m +no_defs",
    always_xy=True)

# Paramètres du SVG (ne pas modifier)
SCALE    = 5.9462e-05   # px/m
OFFSET_X = 997.8        # px
OFFSET_Y = 541.6        # px (origine haut-gauche, Y inversé)

def lon_lat_to_svg(lon, lat):
    xp, yp = t.transform(lon, lat)
    return (xp * SCALE + OFFSET_X, -yp * SCALE + OFFSET_Y)

# Exemples
dakar   = lon_lat_to_svg(-17.45, 14.69)   # → ~(895, 490)
nairobi = lon_lat_to_svg(36.82, -1.29)    # → ~(1455, 625)
```

### SVG snippet — dot usine

```xml
<!-- Dot usine Dakar, Sénégal -->
<circle cx="895" cy="490" r="8"
  fill="#80C7C2" stroke="#FFFFFF" stroke-width="1.5"
  aria-label="Dakar — Sénégal"/>
```

---

## Intégration Claude Design

Inclure le SVG en tant qu'asset dans un slide PPTX ou un rapport DOCX :

1. Ouvrir `pof-world-map-blank.svg` (pour personnalisation complète)  
   ou `pof-world-map-annotated.svg` (prêt à l'emploi)
2. Ajouter un `<style>` block ou des attributs `fill` inline pour colorer les pays
3. Ajouter les dots d'usines via `<circle>` avec les coordonnées calculées ci-dessus
4. Exporter en PNG 2× (2418×1248px) pour insertion dans PPTX

---

## Historique

| Version | Date | Changements |
|---------|------|-------------|
| 1.0.0 | 2026-04-26 | Première version — 177 pays, Robinson, 9 groupes, labels prioritaires |
| 1.1.0 | 2026-04-26 | + codes ISO sur tous les pays, dots Comores/Seychelles/Maurice/Réunion, groupes AFRICA + SEA_CONTINENT, map vierge séparée |

