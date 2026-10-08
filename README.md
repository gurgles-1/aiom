# AIOM image assets

Collection artwork for [AIOMetadata](https://github.com/cedya77/aiometadata) catalogs and Vio collections.

## Layout

| Folder | What's in it |
|---|---|
| `betterer/` | Betterer covers for AIOM catalogs (portrait + landscape) |
| `cinematic/` | Cinematic-style covers |
| `minimal/` | Minimal-style covers |
| `franchises/` | Franchise collections (Star Wars, Marvel, etc.) |
| `movie_collections/genres/` | Genre collections (horror, sci-fi, comedy...) |
| `movie_collections/decades/` | Decade collections (1970s–2020s) |
| `movie_collections/top/` | Top 250, top musicals |
| `studios/` | Movie studio backdrops |
| `networks/broadcast/` | Broadcast networks (ABC, CBS, NBC...) |
| `networks/cable/` | Cable networks (AMC, HGTV, History...) |
| `networks/streaming/` | Streaming services (Netflix, Hulu, Disney+...) |
| `streaming/` | Streaming service artwork |
| `my/` | Personal list artwork |

## Using with AIOMetadata

1. Find the image you want in the folders above
2. Copy its raw URL: `https://raw.githubusercontent.com/gurgles-1/aiom/main/<folder>/<file>`
3. In AIOMetadata, open your collection/catalog settings
4. Paste the URL into the **poster** or **backdrop** field
5. Save — AIOMetadata will cache and serve the image

### Poster vs backdrop

- **Portrait images** (tall) → use as posters
- **Landscape images** (wide) → use as backdrops
- The `betterer/` folder has both orientations for each catalog

## Using with Vio

Same raw URLs work in Vio collection settings. Paste into the artwork field when editing a collection.

## Autobuild

The `src/` folder contains a daily GitHub Actions workflow that syncs TMDB lists to `output/` as JSON catalogs. See `.github/workflows/sync.yml`.
