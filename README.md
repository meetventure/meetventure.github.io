# meetventure.ca - v8 (multi-page, SEO-structured)

Complete rewrite implementing Phase 2 (on-page SEO) and Phase 3 (multi-page structure)
from the SEO plan, with a fully fluid mobile-first stylesheet.

## What's in here

```
index.html                                  → /
mortgage-renewal-ontario/index.html         → /mortgage-renewal-ontario/
first-time-home-buyer-ontario/index.html    → /first-time-home-buyer-ontario/
self-employed-mortgage/index.html           → /self-employed-mortgage/
newcomer-mortgage-canada/index.html         → /newcomer-mortgage-canada/
pre-construction-mortgage/index.html        → /pre-construction-mortgage/
mortgage-affordability-calculator/index.html→ /mortgage-affordability-calculator/
rent-vs-buy-calculator/index.html           → /rent-vs-buy-calculator/
commercial-lending/index.html               → /commercial-lending/
business-financing/index.html               → /business-financing/
404.html                                    → served automatically by GitHub Pages
style.css        script.js        favicon.svg
sitemap.xml      robots.txt       images/image.jpg
_source/         → the page generator (see "Editing" below)
```

Upload **everything except `_source/`** to the root of your repo. `_source/` is
optional - keep it in the repo so you can regenerate pages later.

## Deployment

Same as before: push to your repo root, then Settings → Pages → deploy from
branch, `/ (root)`. The folder-per-page structure gives clean URLs like
`meetventure.ca/mortgage-renewal-ontario/` with no `.html` extension.

**After deploying:** resubmit `sitemap.xml` in Google Search Console, then use
URL Inspection → Request Indexing on the homepage *and* on the renewal page,
since that's your highest-value target for the 2026-27 renewal wave.

## Phase 2 - SEO implemented on every page

- **Unique `<title>`** (31-52 chars, all under Google's ~60 char display limit),
  location and service first, name last
- **Unique meta description** (128-158 chars) written to earn a click
- **Canonical URL** on every page
- **Open Graph + Twitter Card** tags, so shared links render properly on
  Facebook, LinkedIn, WhatsApp and iMessage instead of a blank grey box
- **JSON-LD structured data** on every page, as a single `@graph` containing:
  `FinancialService` (with `areaServed` for 12 cities), `Person`, `WebPage`,
  `BreadcrumbList`, and `FAQPage`
- **FAQ schema on all 10 pages** (4-6 questions each) - this is what can earn
  expanded results in Google. Answers are real answers, not keyword filler.
- **One `<h1>` per page**, semantic heading order, `<main>` landmark, skip link
- Visible breadcrumbs matching the breadcrumb schema
- Internal linking between related pages via the "Keep reading" block
- No fabricated review or rating markup - inventing those violates Google's
  guidelines and can earn a manual penalty

## Phase 3 - Page structure

Each page targets one search intent instead of ten competing on one URL:

| Page | Target search |
|---|---|
| `/` | mortgage agent brampton |
| `/mortgage-renewal-ontario/` | mortgage renewal ontario |
| `/first-time-home-buyer-ontario/` | first time home buyer mortgage ontario |
| `/self-employed-mortgage/` | self employed mortgage ontario |
| `/newcomer-mortgage-canada/` | newcomer mortgage no credit history |
| `/pre-construction-mortgage/` | pre construction mortgage ontario |
| `/mortgage-affordability-calculator/` | mortgage affordability calculator ontario |
| `/rent-vs-buy-calculator/` | rent vs buy calculator canada |
| `/commercial-lending/` | commercial mortgage ontario |
| `/business-financing/` | business financing ontario |

The two calculator pages exist as standalone URLs on purpose - tools attract
backlinks, and backlinks are the strongest ranking signal you can earn.

## Mobile: what makes this work on any phone

The stylesheet is **fluid, not breakpoint-based**. Nearly every size uses
`clamp(min, preferred, max)`, so type and spacing scale continuously with the
screen instead of jumping at fixed widths. Measured across real widths:

| Viewport | H1 size | Overflow | Nav | Min tap target |
|---|---|---|---|---|
| 320px | 28.0px | none | hamburger | 48px |
| 360px | 29.2px | none | hamburger | 48px |
| 390px | 30.1px | none | hamburger | 48px |
| 412px | 30.8px | none | hamburger | 48px |
| 768px | 41.4px | none | hamburger | 48px |
| 1024px | 49.1px | none | desktop | 48px |
| 1440px | 56.0px | none | desktop | 48px |

Specific iOS/Android protections built in:

- `-webkit-text-size-adjust:100%` - stops iOS silently inflating text in landscape
- **All font sizes on inputs stay at/above 16px equivalent** - iOS force-zooms
  the page when you focus an input smaller than that
- `env(safe-area-inset-*)` on the contact bar, footer and modal - keeps content
  clear of the iPhone notch and home-bar
- `touch-action:manipulation` on buttons - removes the 300ms tap delay
- `touch-action:pan-y` on sliders - lets you still scroll the page vertically
  when your thumb starts on a slider
- `-webkit-tap-highlight-color:transparent` - no grey flash on tap
- `100dvh` on the modal - correct height on mobile browsers with dynamic toolbars
- `prefers-reduced-motion` respected
- Zoom is **not** disabled (no `maximum-scale`) - blocking pinch-zoom is an
  accessibility failure

## Editing

**`script.js` is one file shared by all pages.** Every init module is guarded -
it checks whether its elements exist and returns quietly if not. That's why the
calculator code doesn't error on the commercial lending page. Verified: 0 JS
errors across all 11 pages.

Your blog posts, case studies, region data and rate history were carried over
intact - they live in the DATA section at the top of `script.js`.

**To change the nav, footer, or contact details:** edit `_source/generate.py`,
then run:

```bash
cd _source && python3 generate.py
```

This regenerates all 10 pages from one template. It exists because a static
multi-page site otherwise means the nav is copy-pasted into 10 files, and you'd
inevitably update 9 of them. Page copy lives in `_source/pages.py`.

To add a page: copy a block in `pages.py`, run the generator, add the URL to
`sitemap.xml`.

## Still to do before this is fully live

1. **Replace social placeholders** - search `YOUR-HANDLE` (8 instances across
   the generator; regenerate after editing)
2. **Replace the Calendly link** - search `YOUR-LINK-HERE` in `_source/generate.py`
3. **Verify the domain actually resolves** - as of the last check, an exact-match
   search for `"meetventure.ca"` returned no results for your site, so it may not
   be indexed or live yet. Nothing above matters until Google can crawl it.
4. **Google Business Profile** - still the highest-value local SEO lever
5. **Principal Broker review** - all public-facing material, per FSRA

## A note on the rate and market figures

`MARKET_DATA`, `GROWTH_RATES`, `BOC_MEETINGS` and `BOND_YIELDS` in `script.js`
were current when built and will go stale. The renewal page also references the
November 2024 stress-test change and the 2026-27 renewal wave. Re-verify these
against Bank of Canada, OSFI and CMHC sources before relying on them in client
conversations, and refresh quarterly.
