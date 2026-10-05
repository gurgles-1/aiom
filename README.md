# AIOMetadata Collections

Importable [AIOMetadata](https://github.com/cedya77/aiometadata) fusion-widget collections — five collections, 37 tiles, 68 catalogs, all backed by **dynamic TMDB Discover catalogs** (no static lists to maintain).

## Collections

| Collection | Tiles | Backing |
|---|---|---|
| Decades | 1930s–2020s (10) | TMDB Discover, movies + series per decade |
| Genres | 14 genres | TMDB Discover, movies + series per genre |
| Streaming Services | 9 services | TMDB Discover with US watch providers (last 5 years) |
| Merna | Merna's Movies, Gentle Shows | TMDB Discover, animation/family, PG and under |
| Adrienne | Crime Series, Mystery & Thriller Movies | TMDB Discover, crime/mystery, highly rated |

## Two artwork options

- **`evan-art.json`** — Evan's cinematic genre artwork, betterer streaming covers, generated decade/personal tiles.
- **`betterer-style.json`** — fully generated betterer-style tiles (gradient + label + poster collage) for every tile.

## Import

In AIOMetadata → Collections → Import, paste the raw URL of whichever file you prefer:

- `https://raw.githubusercontent.com/gurgles-1/aiom-collections/main/evan-art.json`
- `https://raw.githubusercontent.com/gurgles-1/aiom-collections/main/betterer-style.json`

Choose **Merge** to fold them into your existing setup.

## Artwork

- `covers/evan/` — Evan's genre artwork (via postimg)
- `covers/my/` — generated betterer-style tiles (1485×835)
- `covers/streaming/` — betterer covers landing-page art for streaming services

To regenerate the JSON after changing artwork or catalogs, run `build/build_json.py` (needs the poster index + tiles) — or just edit the JSON directly; each tile's `imageURL` and `dataSources` are self-contained.
