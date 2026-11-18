# Has it been Breached?

Search a company's publicly documented data breach history before you share your data with it.

A static website: no server, no accounts, no tracking. Search runs in the visitor's browser over `data/breaches.json`, so it can be hosted for free. It is served at https://hasitbeenbreached.com by a Cloudflare Worker that builds from `main` (see `wrangler.jsonc`; `.assetsignore` keeps repo-only files off the site).

## Files

| Path | What it is |
| --- | --- |
| `index.html` | Home page with search, browse list and FAQ (edit directly) |
| `data/breaches.json` | **The database.** One entry per company, each with a list of breaches |
| `tools/pages/*.html` | Text of the inner pages (about, sources, contact, privacy, terms, 404) |
| `tools/build_pages.py` | Wraps those pages in the shared header and footer |
| `assets/` | Styles, search script and icon |

## Adding or changing a record

Edit `data/breaches.json`. Every breach needs:

```json
{
  "title": "Short name of the incident",
  "date": "2021-03",
  "status": "confirmed",
  "affected": "About 2 million customers",
  "categories": ["Names", "Email addresses"],
  "description": "Two or three plain sentences. State allegations as allegations.",
  "source_name": "Who published the source",
  "source_url": "https://...",
  "statement": { "title": "Title of the company's own statement", "url": "https://..." },
  "disclosed": "2021-05",
  "outcomes": [ { "kind": "fine", "text": "Fined €1 million by the Dutch Data Protection Authority", "year": 2022 } ]
}
```

- `date` can be `YYYY` or `YYYY-MM`.
- `status` is `confirmed` (the company or a regulator says it happened) or `unverified_report`.
- Use a regulator or the company itself as the source whenever possible. Never link to leaked data.
- `statement` is the company's own public statement about the breach, or `null` if there isn't one.
- Risk colours for exposed data are set automatically from the category name (see `HIGH` and `MED` in `assets/search.js`).
- `disclosed` is when the company first made the breach known. Add `"timing_unclear": true` if nobody knows when the breach really happened, so no delay is shown.
- `outcomes` lists what regulators or courts did: `kind` is `fine`, `settlement`, `court`, `investigation` or `order`. Use `[]` if nothing is known.
- Update `"updated"` at the top of the file.

## Changing an inner page

Edit the file in `tools/pages/`, then run:

```bash
python3 tools/build_pages.py
```

## Hosting

Cloudflare rebuilds the site whenever `main` changes. The 404 page sets its base address itself, so it works at the domain root and at the old GitHub Pages address.

## Previewing locally

```bash
python3 -m http.server 8000
```

Then open http://localhost:8000.

## Before launch

Before publishing new pages, search for `class="ph"`: that marks yellow placeholder text that still needs filling in.
