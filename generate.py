#!/usr/bin/env python3
"""
meetventure.ca page generator
=============================
WHY THIS EXISTS: this is a plain static site (GitHub Pages, no build tool).
Multi-page static sites normally mean the nav bar and footer are copy-pasted
into every single HTML file - so changing one nav link means editing 11 files
and inevitably missing one.

This script keeps the nav, footer, contact strip and all SEO boilerplate in
ONE place and stamps out every page from it.

TO CHANGE THE NAV OR FOOTER: edit NAV_ITEMS / footer_html() below, then run
    python3 generate.py
and every page is rebuilt consistently.

TO ADD A PAGE: add an entry to PAGES, run the script, then add the URL to
sitemap.xml.
"""
import os, json, html, datetime

OUT = os.environ.get("OUT_DIR", "/home/claude/rebuild/site")
SITE = "https://meetventure.ca"
TODAY = "2026-08-12"

NAME   = "Meet Patel"
TITLE  = "Mortgage Agent Level 1"
LIC    = "M25002923"
BROKER = "Pegasus Mortgage Lending Center Inc."
FSRA   = "11479"
PHONE_DISPLAY = "226-978-8858"
PHONE_TEL = "+12269788858"
EMAIL  = "meetventure@gmail.com"
CALENDLY = "https://calendly.com/YOUR-LINK-HERE"

SOCIAL = {
    "instagram": "https://instagram.com/YOUR-HANDLE",
    "tiktok":    "https://tiktok.com/@YOUR-HANDLE",
    "linkedin":  "https://linkedin.com/in/YOUR-HANDLE",
    "facebook":  "https://facebook.com/YOUR-HANDLE",
}

# Primary nav. slug "" == homepage.
NAV_ITEMS = [
    ("mortgage-renewal-ontario",        "Renewals"),
    ("first-time-home-buyer-ontario",   "First-Time Buyers"),
    ("self-employed-mortgage",          "Self-Employed"),
    ("pre-construction-mortgage",       "Pre-Construction"),
    ("mortgage-affordability-calculator","Calculators"),
]

# ---------------------------------------------------------------- icons
IC_PHONE = ('<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
  'stroke-width="2.2" aria-hidden="true"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 '
  '19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.127.96.362 1.903.7 '
  '2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.907.338 1.85.573 2.81.7A2 '
  '2 0 0 1 22 16.92z"/></svg>')
IC_MAIL = ('<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
  'stroke-width="2.2" aria-hidden="true"><path d="M22 6l-10 7L2 6"/><rect x="2" y="4" width="20" height="16" rx="2"/></svg>')

def big(icon, size=20):
    return icon.replace('width="14" height="14"', f'width="{size}" height="{size}"')

SVG_IG = ('<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
  'aria-hidden="true"><rect x="2" y="2" width="20" height="20" rx="5"/><circle cx="12" cy="12" r="4"/>'
  '<circle cx="17.5" cy="6.5" r="1" fill="currentColor" stroke="none"/></svg>')
SVG_TT = ('<svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M16.6 '
  '5.82c-.9-.78-1.47-1.9-1.6-3.15h-3.03v13.44c0 1.63-1.33 2.96-2.96 2.96a2.96 2.96 0 0 1-2.96-2.96 2.96 2.96 0 0 '
  '1 2.96-2.96c.27 0 .53.04.78.1V9.9a6.1 6.1 0 0 0-.78-.05A6.1 6.1 0 0 0 3 16a6.1 6.1 0 0 0 6.01 6.1A6.1 6.1 0 0 '
  '0 15.02 16V8.86a8.5 8.5 0 0 0 4.98 1.6V7.4c-1.2 0-2.35-.4-3.4-1.58z"/></svg>')
SVG_LI = ('<svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M20.45 '
  '20.45h-3.56v-5.57c0-1.33-.02-3.04-1.85-3.04-1.85 0-2.14 1.45-2.14 2.94v5.67H9.34V9h3.41v1.56h.05c.48-.9 '
  '1.64-1.85 3.38-1.85 3.6 0 4.27 2.37 4.27 5.46v6.28zM5.34 7.43a2.07 2.07 0 1 1 0-4.13 2.07 2.07 0 0 1 0 '
  '4.13zM7.12 20.45H3.56V9h3.56v11.45z"/></svg>')
SVG_FB = ('<svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M22 '
  '12a10 10 0 1 0-11.56 9.88v-6.99H7.9V12h2.54V9.8c0-2.5 1.49-3.89 3.78-3.89 1.1 0 2.24.2 2.24.2v2.46H15.2c-1.24 '
  '0-1.63.77-1.63 1.56V12h2.78l-.44 2.89h-2.34v6.99A10 10 0 0 0 22 12z"/></svg>')
SOCIAL_SVG = {"instagram":SVG_IG,"tiktok":SVG_TT,"linkedin":SVG_LI,"facebook":SVG_FB}


def url_for(slug):
    return f"{SITE}/" if slug == "" else f"{SITE}/{slug}/"

def href(slug, current):
    """Root-relative links so they work identically from / and /subfolder/."""
    return "/" if slug == "" else f"/{slug}/"


# ---------------------------------------------------------------- schema
def schema_business():
    return {
      "@type": "FinancialService",
      "@id": f"{SITE}/#business",
      "name": f"{NAME} - Mortgage Agent",
      "description": ("Licensed Mortgage Agent Level 1 serving Brampton, Mississauga, "
                      "Toronto and the Greater Toronto Area. Renewals, first-time buyers, "
                      "self-employed and newcomer mortgages."),
      "url": SITE,
      "telephone": PHONE_TEL,
      "email": EMAIL,
      "image": f"{SITE}/images/image.jpg",
      "priceRange": "Free consultation",
      "areaServed": [{"@type":"City","name":c} for c in
                     ["Brampton","Mississauga","Toronto","Caledon","Milton","Oakville",
                      "Kitchener","Waterloo","Cambridge","Hamilton","Burlington","Oshawa"]],
      "parentOrganization": {
        "@type":"Organization","name":BROKER,
        "identifier":f"FSRA Licence #{FSRA}"
      },
      "sameAs": list(SOCIAL.values())
    }

def schema_person():
    return {
      "@type":"Person",
      "@id": f"{SITE}/#person",
      "name": NAME,
      "jobTitle": TITLE,
      "identifier": f"FSRA Licence #{LIC}",
      "telephone": PHONE_TEL,
      "email": EMAIL,
      "worksFor": {"@type":"Organization","name":BROKER},
      "url": SITE
    }

def schema_breadcrumb(page):
    items = [{"@type":"ListItem","position":1,"name":"Home","item":f"{SITE}/"}]
    if page["slug"]:
        items.append({"@type":"ListItem","position":2,"name":page["crumb"],
                      "item":url_for(page["slug"])})
    return {"@type":"BreadcrumbList","itemListElement":items}

def schema_faq(faqs):
    return {
      "@type":"FAQPage",
      "mainEntity":[{"@type":"Question","name":q,
        "acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faqs]
    }

def schema_webpage(page):
    return {
      "@type":"WebPage",
      "@id": url_for(page["slug"]) + "#webpage",
      "url": url_for(page["slug"]),
      "name": page["title"],
      "description": page["desc"],
      "isPartOf":{"@type":"WebSite","@id":f"{SITE}/#website","name":f"{NAME} - Mortgage Agent","url":SITE},
      "about":{"@id":f"{SITE}/#business"},
      "inLanguage":"en-CA"
    }

def build_schema(page):
    graph = [schema_business(), schema_person(), schema_webpage(page), schema_breadcrumb(page)]
    if page.get("faqs"):
        graph.append(schema_faq(page["faqs"]))
    return json.dumps({"@context":"https://schema.org","@graph":graph},
                      indent=2, ensure_ascii=False)


# ---------------------------------------------------------------- chrome
def head_html(page):
    canonical = url_for(page["slug"])
    og_img = f"{SITE}/images/image.jpg"
    return f"""<!DOCTYPE html>
<html lang="en-CA">
<head>
<meta charset="UTF-8">
<!-- Viewport: without this, phones render at ~980px wide and shrink the page,
     forcing pinch-zoom. Do not remove. No maximum-scale/user-scalable=no here
     on purpose - blocking zoom is an accessibility failure. -->
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="theme-color" content="#090F15">
<meta name="format-detection" content="telephone=yes">

<title>{html.escape(page["title"])}</title>
<meta name="description" content="{html.escape(page["desc"])}">
<link rel="canonical" href="{canonical}">
<meta name="robots" content="index,follow,max-image-preview:large">
<meta name="author" content="{NAME}">
<meta name="geo.region" content="CA-ON">
<meta name="geo.placename" content="Brampton, Ontario">

<!-- Open Graph / Twitter: controls how the link looks when shared on
     Facebook, LinkedIn, WhatsApp, iMessage, Slack. Without these you get a
     blank grey box. -->
<meta property="og:type" content="website">
<meta property="og:site_name" content="{NAME} - Mortgage Agent">
<meta property="og:locale" content="en_CA">
<meta property="og:title" content="{html.escape(page["og_title"])}">
<meta property="og:description" content="{html.escape(page["desc"])}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{og_img}">
<meta property="og:image:alt" content="{NAME}, Mortgage Agent Level 1">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{html.escape(page["og_title"])}">
<meta name="twitter:description" content="{html.escape(page["desc"])}">
<meta name="twitter:image" content="{og_img}">

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="/style.css">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/images/image.jpg">

<!-- Structured data: tells Google exactly who you are, where you serve, and
     (on service pages) your FAQs, which can earn expanded search results. -->
<script type="application/ld+json">
{build_schema(page)}
</script>
</head>
<body>
<a href="#main" class="sr-only">Skip to main content</a>
"""

def nav_html(page):
    cur = page["slug"]
    desk = "\n".join(
        f'      <a href="{href(s,cur)}"{" aria-current=\"page\"" if s==cur else ""}>{html.escape(l)}</a>'
        for s,l in NAV_ITEMS)
    mob = "\n".join(
        f'    <a href="{href(s,cur)}"{" aria-current=\"page\"" if s==cur else ""}>{html.escape(l)}</a>'
        for s,l in NAV_ITEMS)
    home_extra = '' if cur=="" else f'    <a href="/">Home</a>\n'
    return f"""
<div class="nav-contact-bar">
  <a href="tel:{PHONE_TEL}">{IC_PHONE}{PHONE_DISPLAY}</a>
  <a href="mailto:{EMAIL}">{IC_MAIL}{EMAIL}</a>
</div>

<nav class="site-nav" aria-label="Main navigation">
  <div class="wrap nav-row">
    <a class="brand" href="/" aria-label="{NAME} - home">
      <span class="brand-mark" aria-hidden="true">M</span>
      <span class="brand-text">
        <span class="name">{NAME}</span>
        <span class="role">{TITLE}</span>
      </span>
    </a>
    <div class="nav-links">
{desk}
    </div>
    <a class="btn gold nav-cta" href="#book">Book a Call</a>
    <button class="nav-toggle" id="nav-toggle" aria-label="Open menu"
            aria-expanded="false" aria-controls="mobile-nav">
      <span></span><span></span><span></span>
    </button>
  </div>
  <div class="mobile-nav" id="mobile-nav">
    <div class="mn-contact">
      <a href="tel:{PHONE_TEL}">{IC_PHONE}&nbsp;{PHONE_DISPLAY}</a>
      <a href="mailto:{EMAIL}">{IC_MAIL}&nbsp;{EMAIL}</a>
    </div>
{home_extra}{mob}
    <a class="btn gold" href="#book">Book a Call</a>
  </div>
</nav>
"""

def crumb_html(page):
    if not page["slug"]:
        return ""
    return f"""
<div class="wrap breadcrumb">
  <nav aria-label="Breadcrumb"><ol>
    <li><a href="/">Home</a></li>
    <li aria-current="page">{html.escape(page["crumb"])}</li>
  </ol></nav>
</div>
"""

def contact_strip_html():
    socials = "\n".join(
      f'      <a href="{u}" target="_blank" rel="noopener" aria-label="{k.title()}">{SOCIAL_SVG[k]}</a>'
      for k,u in SOCIAL.items())
    return f"""
<section class="contact-strip" aria-label="Contact">
  <div class="wrap contact-strip-inner">
    <a class="cs-item" href="tel:{PHONE_TEL}">
      <span class="cs-icon">{big(IC_PHONE)}</span>
      <span><span class="cs-label">Call or text</span><span class="cs-value mono">{PHONE_DISPLAY}</span></span>
    </a>
    <a class="cs-item" href="mailto:{EMAIL}">
      <span class="cs-icon">{big(IC_MAIL)}</span>
      <span><span class="cs-label">Email</span><span class="cs-value mono">{EMAIL}</span></span>
    </a>
    <div class="cs-social">
{socials}
    </div>
  </div>
</section>
"""

def book_html():
    return f"""
<section id="book">
  <div class="wrap">
    <div class="book-card">
      <h2>Let's talk for 15 minutes.</h2>
      <p>No forms, no pressure - just a quick call to figure out what actually applies to your situation.</p>
      <!-- Replace with your real Calendly / Cal.com link -->
      <a class="btn gold" href="{CALENDLY}" target="_blank" rel="noopener">Book a 15-Minute Call</a>
    </div>
  </div>
</section>
"""

def related_html(page):
    rel = page.get("related") or []
    if not rel: return ""
    cards = "\n".join(
      f'      <a class="link-card" href="{href(s,page["slug"])}">{html.escape(l)}</a>' for s,l in rel)
    return f"""
<section class="alt">
  <div class="wrap">
    <div class="sec-head"><h2>Keep reading</h2></div>
    <div class="link-grid">
{cards}
    </div>
  </div>
</section>
"""

def footer_html(page):
    socials = "\n".join(
      f'        <a href="{u}" target="_blank" rel="noopener" aria-label="{k.title()}">{SOCIAL_SVG[k]}</a>'
      for k,u in SOCIAL.items())
    links = "\n".join(
      f'        <a href="{href(s,page["slug"])}">{html.escape(l)}</a>' for s,l in NAV_ITEMS)
    return f"""
<footer>
  <div class="wrap">
    <div class="f-grid">
      <div class="f-col">
        <strong>{NAME}</strong>
        {TITLE} · Licence #{LIC}<br>
        <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a><br>
        <a href="mailto:{EMAIL}">{EMAIL}</a>
      </div>
      <div class="f-col">
        <strong>Brokerage</strong>
        {BROKER}<br>FSRA Licence #{FSRA}
      </div>
      <div class="f-col">
        <strong>Pages</strong>
        <div class="f-links">
{links}
        </div>
      </div>
      <div class="f-col">
        <strong>Follow</strong>
        <div class="f-social">
{socials}
        </div>
      </div>
    </div>
    <hr class="f-rule">
    <p class="disclaimer">
      All figures and tools on this site are simplified estimates for educational purposes only and do not
      constitute a mortgage pre-approval, quote, or financial advice. Actual rates, CMHC premiums,
      qualification criteria and payments depend on your individual application, lender, and market
      conditions at the time of application. Market and rate figures are directional estimates and may not
      reflect current conditions - contact {NAME} directly for up-to-date, personalized numbers.
      {TITLE}, licensed with {BROKER}, FSRA Licence #{FSRA}.
    </p>
  </div>
</footer>

<div class="modal-overlay" id="modal-overlay" role="dialog" aria-modal="true" aria-labelledby="modal-title">
  <div class="modal-box" id="modal-box">
    <button class="modal-close" id="modal-close" aria-label="Close">&times;</button>
    <span class="tag" id="modal-tag"></span>
    <h3 id="modal-title"></h3>
    <p class="modal-meta" id="modal-meta"></p>
    <div class="modal-content" id="modal-content"></div>
  </div>
</div>

<script src="/script.js" defer></script>
</body>
</html>
"""

def faq_section(faqs):
    if not faqs: return ""
    items = "\n".join(f"""      <details>
        <summary>{html.escape(q)}</summary>
        <div class="faq-body"><p>{a}</p></div>
      </details>""" for q,a in faqs)
    return f"""
<section id="faq">
  <div class="wrap">
    <div class="sec-head">
      <p class="eyebrow">Common questions</p>
      <h2>Questions people actually ask</h2>
    </div>
    <div class="faq">
{items}
    </div>
  </div>
</section>
"""

def render(page):
    parts = [head_html(page), nav_html(page), crumb_html(page),
             '<main id="main">', page["body"], "</main>",
             faq_section(page.get("faqs")), contact_strip_html(),
             book_html(), related_html(page), footer_html(page)]
    return "".join(parts)


def write(page):
    out = os.path.join(OUT, page["slug"]) if page["slug"] else OUT
    os.makedirs(out, exist_ok=True)
    path = os.path.join(out, "index.html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(render(page))
    return path


if __name__ == "__main__":
    from pages import PAGES
    os.makedirs(OUT, exist_ok=True)
    for p in PAGES:
        print("wrote", write(p))
    print(f"\n{len(PAGES)} pages generated into {OUT}")
