# Web-Crawler

A small same-domain web crawler that walks a site breadth-first for a fixed time budget, keeps only English text, and writes the harvested content to a PDF. Used as a data-collection step for a retrieval-augmented question-answering project (see the companion `AI-Assistant` repo, which consumes a `Web-Crawler/output_uscis_3.pdf` produced by this script).

## What it does

`crawler.py` (around 80 lines) implements:

1. BFS over links whose `urlparse().netloc` matches the start URL's domain (no cross-domain wandering).
2. Page fetch via `requests`, parse via `BeautifulSoup`, text extraction with whitespace normalized.
3. Language gate using `langdetect`; non-English pages are skipped.
4. Light sanitization that keeps alphanumerics, spaces, and basic punctuation.
5. PDF output via `fpdf`, one block per visited URL.
6. A wall-clock budget (default 30 seconds) so the queue stops draining once time is up.

The start URL is hardcoded at the bottom of `main()`. Change it there, or edit the file to accept a CLI argument.

## Dependencies

```
requests
beautifulsoup4
langdetect
fpdf
```

Install with `pip install requests beautifulsoup4 langdetect fpdf`.

## Run

```bash
python crawler.py
```

Output is written to `output.pdf` in the working directory.

## Limitations (honest list)

- No `robots.txt` handling, no rate limiting, no retries, no proxy or user-agent rotation.
- No concurrency: pages are fetched serially.
- No deduplication beyond the visited set; query-string variants count as distinct URLs.
- PDF output is plain text dumped through `fpdf`; non-ASCII characters that survive sanitization can fail the default font.
- The 30-second budget is wall-clock, not per-request; a slow page can eat most of it.

Treat this as a focused utility for grabbing the text of a single domain into one file, not a production crawler.

## License

MIT.
