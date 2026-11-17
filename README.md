# Has it been Breached?

Search a company's publicly documented data breach history before you share your data with it.

A static website: no server, no accounts, no tracking. Search runs in the visitor's browser over `data/breaches.json`, so it can be hosted for free on GitHub Pages.

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
  "source_url": "https://..."
}
```

- `date` can be `YYYY` or `YYYY-MM`.
- `status` is `confirmed` (the company or a regulator says it happened) or `unverified_report`.
- Use a regulator or the company itself as the source whenever possible. Never link to leaked data.
- Update `"updated"` at the top of the file.

## Changing an inner page

Edit the file in `tools/pages/`, then run:

```bash
python3 tools/build_pages.py
```

## Previewing locally

```bash
python3 -m http.server 8000
```

Then open http://localhost:8000.

## Before launch

Search the site for `class="ph"`: those yellow placeholders (who runs the site, contact email, country) must be filled in.
