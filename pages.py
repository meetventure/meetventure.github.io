"""
PAGE CONTENT
============
One dict per page. Add a new page by copying a block, then rerun generate.py
and add the URL to sitemap.xml.

Fields:
  slug      - folder name. "" is the homepage. URL becomes /slug/
  crumb     - breadcrumb label
  title     - <title>. Format: "Primary Keyword | Secondary | Name". Aim <60 chars.
  og_title  - shorter title for social shares
  desc      - meta description. Aim 140-160 chars. Write for a human clicking.
  body      - page HTML (goes inside <main>)
  faqs      - list of (question, answer) -> renders an accordion AND FAQPage
              schema, which can earn expanded Google results
  related   - internal links; internal linking spreads ranking strength
"""

# ---------------------------------------------------------------- shared blocks

HERO_CALC = """
      <div class="calc-card">
        <p class="label">Home price</p>
        <p class="calc-big mono" id="hp-display">$650,000</p>

        <div class="slider-row">
          <div class="slider-top"><span>Purchase price</span><span class="val mono" id="hp-val">$650,000</span></div>
          <input type="range" id="hp-slider" min="300000" max="2000000" step="5000" value="650000"
                 aria-label="Purchase price">
        </div>
        <div class="slider-row">
          <div class="slider-top"><span>Down payment</span><span class="val mono" id="dp-val">10% · $65,000</span></div>
          <input type="range" id="dp-slider" min="5" max="35" step="1" value="10"
                 aria-label="Down payment percentage">
        </div>
        <div class="slider-row">
          <div class="slider-top">
            <span>Interest rate (5-yr fixed)<span class="rate-badge" id="rate-suggested-badge">suggested</span></span>
            <span class="val mono" id="rate-val">3.99%</span>
          </div>
          <input type="range" id="rate-slider" min="3" max="7" step="0.05" value="3.99"
                 aria-label="Interest rate">
        </div>

        <div class="calc-result">
          <span class="l">Est. monthly payment</span>
          <span class="v mono" id="hero-monthly">$3,187</span>
        </div>
        <p class="calc-note" id="hero-cmhc-note">Includes CMHC insurance premium (financed) · 25-yr amortization</p>

        <div class="stat-rows">
          <div class="stat-row"><span>Down payment</span><strong class="mono" id="hero-down-amt">$65,000</strong></div>
          <div class="stat-row"><span>CMHC insurance premium</span><strong class="mono" id="hero-cmhc-amt">$18,135</strong></div>
          <div class="stat-row"><span>Total mortgage</span><strong class="mono" id="hero-total-mortgage">$603,135</strong></div>
        </div>
      </div>
"""

AFFORD_CALC = """
      <div class="calc-card">
        <p class="label">What you could afford</p>
        <p class="calc-big mono" id="af-max-price">$540,000</p>
        <p class="calc-note" style="margin-bottom:1.5rem">Estimated maximum purchase price</p>

        <div class="slider-row">
          <div class="slider-top"><span>Household income (yearly)</span><span class="val mono" id="af-income-val">$110,000</span></div>
          <input type="range" id="af-income" min="40000" max="350000" step="2500" value="110000" aria-label="Household income">
        </div>
        <div class="slider-row">
          <div class="slider-top"><span>Other monthly debts</span><span class="val mono" id="af-debt-val">$450/mo</span></div>
          <input type="range" id="af-debt" min="0" max="3000" step="25" value="450" aria-label="Other monthly debt payments">
        </div>
        <div class="slider-row">
          <div class="slider-top"><span>Down payment saved</span><span class="val mono" id="af-down-val">$50,000</span></div>
          <input type="range" id="af-down" min="10000" max="400000" step="5000" value="50000" aria-label="Down payment saved">
        </div>
        <div class="slider-row">
          <div class="slider-top"><span>Qualifying rate</span><span class="val mono" id="af-rate-val">5.25%</span></div>
          <input type="range" id="af-rate" min="4" max="8" step="0.05" value="5.25" aria-label="Qualifying rate">
        </div>

        <div style="height:8px;background:var(--line);border-radius:4px;overflow:hidden;margin:1.25rem 0 .5rem">
          <div id="af-meter" style="height:100%;width:40%;background:var(--green);transition:width .2s ease"></div>
        </div>
        <p class="calc-note">How much of your allowable debt room you're using</p>

        <div class="stat-rows">
          <div class="stat-row"><span>Max housing budget</span><strong class="mono" id="af-max-housing">$3,575/mo</strong></div>
          <div class="stat-row"><span>Max mortgage</span><strong class="mono" id="af-max-mortgage">$490,000</strong></div>
        </div>
        <p class="calc-note" id="af-bound" style="margin-top:.85rem"></p>
      </div>
"""

RVB_CALC = """
      <div class="calc-card">
        <p class="label">Rent vs buy</p>
        <p class="calc-big mono" id="rvb-equity">$0</p>
        <p class="calc-note" style="margin-bottom:1.5rem">Equity you'd have built by the end</p>

        <div class="slider-row">
          <div class="slider-top"><span>Current rent</span><span class="val mono" id="rvb-rent-val">$2,400/mo</span></div>
          <input type="range" id="rvb-rent" min="1200" max="4500" step="50" value="2400" aria-label="Current monthly rent">
        </div>
        <div class="slider-row">
          <div class="slider-top"><span>Purchase price</span><span class="val mono" id="rvb-price-val">$650,000</span></div>
          <input type="range" id="rvb-price" min="300000" max="1500000" step="5000" value="650000" aria-label="Purchase price">
        </div>
        <div class="slider-row">
          <div class="slider-top"><span>Rate</span><span class="val mono" id="rvb-rate-val">4.14%</span></div>
          <input type="range" id="rvb-rate" min="3" max="7" step="0.05" value="4.14" aria-label="Interest rate">
        </div>
        <div class="slider-row">
          <div class="slider-top"><span>Time horizon</span><span class="val mono" id="rvb-years-val">10 yrs</span></div>
          <input type="range" id="rvb-years" min="3" max="25" step="1" value="10" aria-label="Years">
        </div>

        <div class="stat-rows">
          <div class="stat-row"><span>Your mortgage payment</span><strong class="mono" id="rvb-payment">$3,150/mo</strong></div>
          <div class="stat-row"><span>Total rent paid</span><strong class="mono" id="rvb-rent-total">$293,760</strong></div>
          <div class="stat-row"><span>Total ownership carry</span><strong class="mono" id="rvb-own-total">$456,000</strong></div>
        </div>
        <p class="calc-note">Assumes 20% down. Ownership carry includes estimated property tax and upkeep. Illustrative, not a forecast.</p>
      </div>
"""

SERVICES = [
  ("&#127968;", "First-Time Buyers", "Pre-approval, down payment strategy, and a plain-language walkthrough of your first purchase."),
  ("&#128260;", "Renewals", "Your current lender's offer isn't the only one. I check the market before you sign anything."),
  ("&#128176;", "Refinancing", "Access equity or restructure your mortgage around your current goals."),
  ("&#128188;", "Self-Employed", "Financing built around business income, not just a T4 - I know which lenders work with it."),
  ("&#127760;", "Newcomers to Canada", "Mortgage programs for new permanent residents and eligible work permit holders."),
  ("&#128200;", "Investment Properties", "Financing for rental and investment purchases, with your portfolio goals in mind."),
  ("&#127970;", "Commercial Lending", "Retail, office, industrial and mixed-use property purchases or refinances."),
  ("&#128202;", "Business Financing", "Working capital, equipment and expansion financing built around how your business runs."),
]

def services_grid():
    cards = "\n".join(
      f'      <article class="card service-card"><div class="icon" aria-hidden="true">{i}</div>'
      f'<h3>{t}</h3><p>{d}</p></article>' for i,t,d in SERVICES)
    return f'<div class="grid-auto">\n{cards}\n    </div>'

JOURNEY = [
  ("15-Min Call", "We talk through your situation - no forms, no pressure."),
  ("Your Real Options", "I lay out the scenarios that actually apply to you, numbers included."),
  ("Talk It Through", "We go over each option together - no rush, no pressure to decide on the spot."),
  ("Pre-Approval", "Once you've picked a direction: documents gathered, application submitted, firm number in hand."),
  ("Closing &amp; Beyond", "I stay in the loop through closing - and for the renewal after that."),
]

def journey_grid():
    steps = "\n".join(
      f'      <div class="journey-step"><div class="journey-num">{n+1}</div><h4>{t}</h4><p>{d}</p></div>'
      for n,(t,d) in enumerate(JOURNEY))
    return f'<div class="journey">\n{steps}\n    </div>'


# ---------------------------------------------------------------- pages

PAGES = []

# ============================== HOME ==============================
PAGES.append(dict(
  slug="", crumb="Home",
  title="Mortgage Agent Brampton & GTA | Meet Patel",
  og_title="Meet Patel - Mortgage Agent, Brampton & the GTA",
  desc=("Licensed mortgage agent in Brampton serving Mississauga, Toronto and the GTA. "
        "Free consultation on renewals, first-time buyers and self-employed mortgages."),
  related=[("mortgage-renewal-ontario","Mortgage renewals in Ontario"),
           ("first-time-home-buyer-ontario","First-time buyer guide"),
           ("mortgage-affordability-calculator","Affordability calculator")],
  faqs=[
    ("Do I have to renew my mortgage with my current bank?",
     "No. You can move your mortgage to a different lender at renewal. Since a policy change in "
     "November 2024, a straight switch - same balance, same amortization - generally does not require "
     "you to pass the federal stress test again, which used to keep many people locked in with their "
     "existing lender."),
    ("How much down payment do I need to buy a home in Ontario?",
     "The minimum is 5% on the first $500,000 of the purchase price, with a higher percentage required "
     "on the portion above that, and 20% is generally required to avoid mortgage default insurance. "
     "Under 20% down, CMHC or a private insurer premium applies and is usually added to your mortgage."),
    ("What does a mortgage agent cost me?",
     "For most standard residential mortgages, the lender pays the brokerage, so there is typically no "
     "direct fee to you. If any fee would ever apply to your situation, it must be disclosed to you in "
     "writing before you commit to anything."),
    ("Which areas do you serve?",
     "Brampton, Mississauga, Toronto and the wider GTA, plus Kitchener-Waterloo-Cambridge, "
     "Hamilton-Burlington, Halton, York, Durham and Niagara. Licensed across Ontario."),
  ],
  body=f"""
<section class="hero">
  <div class="wrap hero-grid">
    <div>
      <p class="eyebrow">Your mortgage, explained plainly</p>
      <h1>Know the numbers <span>before you sign anything.</span></h1>
      <p class="lead">Drag the sliders - price, down payment, even the rate. Watch the real cost of a home
        move in real time, the same way I break it down for clients before we ever talk paperwork.</p>
      <div class="actions">
        <a class="btn gold" href="#tools">Play with the numbers</a>
        <a class="btn ghost" href="#book">Book a 15-min call</a>
      </div>
    </div>
{HERO_CALC}
  </div>
</section>

<section id="about" class="alt">
  <div class="wrap">
    <div class="hero-grid">
      <div>
        <img src="/images/image.jpg" alt="Meet Patel, Mortgage Agent Level 1 in Brampton, Ontario"
             width="843" height="1180" loading="eager"
             style="width:min(220px,50vw);border-radius:50%;aspect-ratio:1;object-fit:cover;box-shadow:var(--shadow-lg)">
      </div>
      <div class="prose">
        <h2>Hi, I'm Meet - a mortgage agent in Brampton serving the GTA</h2>
        <p>Yes, "Meet" - like the verb. I've heard every joke ("nice to Meet you, Meet") and I still laugh
          every single time, so feel free.</p>
        <p>I got into mortgages because I love the moment a client's face changes from "I have no idea what
          any of this means" to "oh - <em>that's</em> how it works." That little lightbulb moment is
          basically my whole personality at work.</p>
        <p>I like people, I like numbers, and I really like combining the two without anyone losing their
          mind in the process. If you want an agent who actually picks up the phone and explains things
          like a human being, let's talk.</p>
        <p><strong>{'Mortgage Agent Level 1 · Licence #M25002923 · Pegasus Mortgage Lending Center Inc. (FSRA #11479)'}</strong></p>
      </div>
    </div>
  </div>
</section>

<section id="services">
  <div class="wrap">
    <div class="sec-head">
      <p class="eyebrow">What I help with</p>
      <h2>Mortgages, for wherever you're starting from</h2>
      <p>Whether this is your first home or your fifth mortgage renewal, the approach is the same:
        understand your real situation, then find the option that actually fits it.</p>
    </div>
    {services_grid()}
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="sec-head">
      <p class="eyebrow">How it works</p>
      <h2>The journey, start to close</h2>
    </div>
    {journey_grid()}
  </div>
</section>

<section id="tools">
  <div class="wrap">
    <div class="sec-head">
      <p class="eyebrow">Financial literacy tools</p>
      <h2>Three ways to understand your mortgage</h2>
      <p>These are the exact conversations I have with clients - turned into something you can play with
        yourself, before we ever get on a call.</p>
    </div>

    <div class="tabs" role="tablist" aria-label="Calculators">
      <button class="tab" data-panel="afford" role="tab" aria-selected="true">What can you afford?</button>
      <button class="tab" data-panel="rvb" role="tab" aria-selected="false">Rent vs. buy</button>
    </div>

    <div data-panel-id="afford" role="tabpanel">
      <div class="grid-2">
{AFFORD_CALC}
        <div class="prose">
          <h3>How lenders decide what you can afford</h3>
          <p>Two ratios do most of the work. <strong>GDS</strong> (gross debt service) looks at housing
            costs against your income. <strong>TDS</strong> (total debt service) adds your other debts -
            car loans, credit cards, student loans.</p>
          <p>The common conventional guidelines are roughly 39% GDS and 44% TDS, though exact thresholds
            vary by lender and by whether your mortgage is insured.</p>
          <p>This is why paying down a car loan can sometimes raise your buying power more than saving
            another few thousand for a down payment.</p>
        </div>
      </div>
    </div>

    <div data-panel-id="rvb" role="tabpanel" hidden>
      <div class="grid-2">
{RVB_CALC}
        <div class="prose">
          <h3>The honest version of this comparison</h3>
          <p>Renting isn't "throwing money away" and buying isn't automatically the better financial move.
            It depends on how long you stay, what happens to prices, and what you'd have done with the
            money otherwise.</p>
          <p>What ownership does reliably give you is <strong>forced equity</strong> - a portion of every
            payment reduces what you owe. Rent builds none.</p>
          <p>What renting gives you is flexibility and no exposure to a furnace dying in February.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<section id="market" class="alt">
  <div class="wrap">
    <div class="sec-head">
      <p class="eyebrow">Where I work</p>
      <h2>Ontario coverage areas and local price context</h2>
      <p>Tap a region to see typical price points in that market.</p>
    </div>
    <div class="map-grid">
      <div>
        <svg id="ontario-map" viewBox="0 0 620 480" role="img"
             aria-label="Map of Ontario regions served"></svg>
      </div>
      <div class="card" id="map-detail"></div>
    </div>
    <p class="market-note">Regional figures are directional estimates compiled from board and public
      reporting and may not reflect current conditions. Cities marked "est." are modelled from regional
      averages and nearby comparables rather than a confirmed board benchmark. Ask me for current numbers
      before making a decision.</p>

    <div style="margin-top:clamp(2rem,1.5rem+2vw,3rem)">
      <h3>Bank of Canada rate history and bond yields</h3>
      <p class="calc-note" style="margin:.5rem 0 1rem">Tap a legend item to toggle a series.</p>
      <div class="legend">
        <button id="legend-boc" type="button"><span class="dot" style="background:var(--ink)"></span>Bank of Canada policy rate</button>
        <button id="legend-bond" type="button"><span class="dot" style="background:var(--accent)"></span>5-yr bond yield</button>
      </div>
      <div class="chart-wrap">
        <svg id="rate-chart" class="chart" viewBox="0 0 900 340" role="img"
             aria-label="Chart of Bank of Canada policy rate and 5-year bond yields over time"></svg>
      </div>
      <p class="market-note">Rate history compiled from Bank of Canada announcements and financial press
        reporting. Confirm exact figures at bankofcanada.ca before relying on them.</p>
    </div>
  </div>
</section>

<section id="cases">
  <div class="wrap">
    <div class="sec-head">
      <p class="eyebrow">The Mortgage Diaries</p>
      <h2>Real situations, real numbers</h2>
      <p>Dramatizations based on common client scenarios. Details and figures changed.</p>
    </div>
    <div class="grid-2" id="case-grid"></div>
    <div class="pagination" id="case-pagination"></div>
  </div>
</section>

<section id="blog" class="alt">
  <div class="wrap">
    <div class="sec-head">
      <p class="eyebrow">From the blog</p>
      <h2>Mortgage questions, answered plainly</h2>
    </div>
    <div class="blog-scroll" id="blog-grid"></div>
  </div>
</section>
"""))


# ============================== RENEWAL ==============================
PAGES.append(dict(
  slug="mortgage-renewal-ontario", crumb="Mortgage Renewals",
  title="Mortgage Renewal Ontario | Before You Sign",
  og_title="Mortgage Renewal in Ontario - What to Know Before You Sign",
  desc=("Renewing in Ontario? Your bank's letter is an opening offer, not your only option. "
        "How switching lenders works and the 2024 stress test change explained."),
  related=[("first-time-home-buyer-ontario","First-time buyer guide"),
           ("self-employed-mortgage","Self-employed mortgages"),
           ("mortgage-affordability-calculator","Affordability calculator")],
  faqs=[
    ("Do I need to pass the stress test to switch lenders at renewal?",
     "Generally no, if it's a straight switch. Since November 2024, moving your existing mortgage to a new "
     "lender without increasing the balance or extending the amortization does not require re-qualifying "
     "under the federal minimum qualifying rate. If you increase the balance or refinance, the stress test "
     "does still apply."),
    ("When should I start shopping for my renewal?",
     "About four to six months before your term ends. Lenders typically mail a renewal offer 90 to 120 days "
     "out, and rate holds usually run 90 to 130 days - so starting early means you're comparing with time "
     "on your side rather than negotiating against a deadline."),
    ("What happens if I do nothing at renewal?",
     "Most lenders will automatically renew you, often into a posted rate that is rarely their most "
     "competitive offer. It's a valid outcome, just usually an expensive one."),
    ("Can I negotiate my renewal rate?",
     "Yes. The most effective approach is getting a competing quote in writing first, then taking it to "
     "your current lender's retention team. Keeping an existing client is usually cheaper for a lender "
     "than acquiring a new one."),
    ("What documents do I need to renew?",
     "For a straight renewal or switch, usually your current mortgage statement, government ID, and often "
     "recent proof of income. It's substantially lighter than a purchase application."),
  ],
  body="""
<section class="hero">
  <div class="wrap">
    <p class="eyebrow">Mortgage renewals</p>
    <h1>Your renewal letter is an <span>opening offer</span> - not your only option.</h1>
    <p class="lead" style="margin-top:1rem">A large share of Canadian mortgages are renewing through 2026
      and 2027, many of them off pandemic-era rates near 2%. If that's you, the gap between signing the
      first letter and actually shopping around can be worth thousands.</p>
    <div class="actions" style="margin-top:1.5rem">
      <a class="btn gold" href="#book">Have me check your renewal letter</a>
      <a class="btn ghost" href="tel:+12269788858">Call 226-978-8858</a>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap prose" style="max-width:75ch">
    <h2>Why the 2026-2027 renewal wave matters</h2>
    <p>Mortgages signed during the ultra-low-rate period are now coming up for renewal into a very
      different rate environment. For many households that means a real monthly increase, even with the
      Bank of Canada holding its policy rate steady.</p>
    <p>Here's the part that gets missed: <strong>the size of that increase isn't fixed.</strong> You don't
      control the Bank of Canada, but you do control which lender you renew with, what term you choose,
      whether you negotiate, and whether anyone actually shopped your file.</p>

    <h2>The rule change most homeowners still haven't heard about</h2>
    <p>Before November 2024, switching lenders at renewal meant re-qualifying under the federal stress
      test at your contract rate plus 2% (or 5.25%, whichever was higher). Plenty of people couldn't pass
      it at current rates - so they were effectively stuck accepting whatever their existing lender offered.</p>
    <p>That changed. For a <strong>straight switch</strong> - same mortgage balance, same amortization -
      you generally no longer need to pass the stress test to move to a new lender. If you're increasing
      your balance or refinancing, the stress test still applies.</p>
    <p>Practically: your bank has meaningfully less leverage over you at renewal than it used to, and
      you may not know it.</p>

    <h2>What a 1% difference actually costs</h2>
    <p>People hear "one percent" and mentally file it as small. On a $450,000 remaining balance, roughly a
      one-point difference in rate can mean over $200 a month - which is more than $12,000 across a
      five-year term. That's not a rounding error.</p>
    <p><em>Illustrative example. Your actual figures depend on your balance, amortization and the rates
      available to you at the time.</em></p>

    <h2>What to compare beyond the rate</h2>
    <ul>
      <li><strong>Prepayment privileges</strong> - can you pay extra without a penalty, and how much?</li>
      <li><strong>Penalty structure</strong> - what happens if you need to break the term early? The
        calculation method varies a lot between lenders.</li>
      <li><strong>Fixed vs. variable</strong> - which one actually matches your tolerance for change.</li>
      <li><strong>Portability</strong> - can the mortgage move with you if you sell before the term ends?</li>
    </ul>
    <p>Two mortgages at an identical rate can behave very differently three years in.</p>

    <h2>The renewal timeline</h2>
    <ul>
      <li><strong>4-6 months out:</strong> start comparing, before anything arrives in the mail</li>
      <li><strong>90-120 days out:</strong> your lender typically sends its official renewal offer</li>
      <li><strong>30-120 days out:</strong> competing rate holds get locked in around here</li>
      <li><strong>Term end date:</strong> new terms take effect - or you're auto-renewed by default</li>
    </ul>

    <h2>Already been auto-renewed?</h2>
    <p>It's not permanent. Depending on your mortgage type and how far into the term you are, switching or
      renegotiating mid-term may be possible, sometimes with a penalty and sometimes without. Penalties
      are generally smaller earlier in a term, so checking sooner is better than checking later.</p>
  </div>
</section>
"""))


# ============================== FIRST-TIME BUYER ==============================
PAGES.append(dict(
  slug="first-time-home-buyer-ontario", crumb="First-Time Buyers",
  title="First-Time Home Buyer Mortgage Ontario | Guide",
  og_title="First-Time Home Buyer Guide - Ontario",
  desc=("First-time buyer in Ontario? Down payment minimums, CMHC insurance, closing "
        "costs and land transfer tax rebates, explained in plain language."),
  related=[("mortgage-affordability-calculator","How much can you afford?"),
           ("rent-vs-buy-calculator","Rent vs buy calculator"),
           ("pre-construction-mortgage","Buying pre-construction")],
  faqs=[
    ("What is the minimum down payment in Ontario?",
     "5% on the first $500,000 of the purchase price, then 10% on the portion between $500,000 and "
     "$1,500,000. Above that threshold, insured financing is generally not available and 20% down is "
     "typically required."),
    ("Do I need 20% down to buy a home?",
     "No. You can buy with as little as 5% down, but under 20% you'll need mortgage default insurance "
     "(CMHC or a private insurer), and that premium is added to your mortgage in most cases."),
    ("What is the FHSA and should I use it?",
     "The First Home Savings Account combines an RRSP-style tax deduction on contributions with TFSA-style "
     "tax-free withdrawals for a qualifying first home purchase. For most first-time buyers saving a down "
     "payment it is worth understanding before defaulting to a regular savings account. Talk to a tax "
     "professional about your specific situation."),
    ("What closing costs should I budget for?",
     "Commonly 1.5% to 4% of the purchase price on a resale home - land transfer tax (plus a second "
     "municipal tax in Toronto), legal fees, title insurance, home inspection, and adjustments. "
     "First-time buyers may qualify for land transfer tax rebates."),
    ("How long does a pre-approval last?",
     "Typically 90 to 120 days, and up to about 130 with some lenders. If it expires before you buy, it "
     "can be redone with updated documents and a new credit check."),
  ],
  body="""
<section class="hero">
  <div class="wrap">
    <p class="eyebrow">First-time buyers</p>
    <h1>Buying your first home in Ontario, <span>without the guesswork.</span></h1>
    <p class="lead" style="margin-top:1rem">Nobody hands you a manual for this. Here's the whole picture -
      what you need saved, what it actually costs to close, and what lenders are really looking at.</p>
    <div class="actions" style="margin-top:1.5rem">
      <a class="btn gold" href="#book">Book a 15-min call</a>
      <a class="btn ghost" href="/mortgage-affordability-calculator/">See what you can afford</a>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap prose" style="max-width:75ch">
    <h2>How much down payment you actually need</h2>
    <p>Canada's minimums are tiered, not a flat percentage:</p>
    <ul>
      <li><strong>5%</strong> on the first $500,000 of the purchase price</li>
      <li><strong>10%</strong> on the portion from $500,000 to $1,500,000</li>
      <li>Above roughly $1.5M, insured financing generally isn't available - expect 20%+</li>
    </ul>
    <p>So on a $650,000 home: 5% of the first $500,000 ($25,000) plus 10% of the remaining $150,000
      ($15,000) = <strong>$40,000 minimum</strong>.</p>

    <h2>CMHC insurance: what it is and who it protects</h2>
    <p>Put down less than 20% and you'll need mortgage default insurance. Worth being clear about: it
      protects <em>the lender</em> if you stop paying, not you. It's what makes low-down-payment lending
      possible at all.</p>
    <p>The premium is a percentage of your mortgage that rises as your down payment shrinks, and it's
      normally added to your mortgage rather than paid in cash - which means you pay interest on it too.</p>
    <p>If you're buying a newly built energy-efficient home, look into <strong>CMHC Eco Plus</strong>,
      which can refund up to 25% of the premium you paid. Note that's 25% of the insurance premium, not
      of the home price. Confirm current criteria directly with CMHC.</p>

    <h2>Closing costs nobody warns you about</h2>
    <ul>
      <li><strong>Land transfer tax</strong> - provincial, plus a second municipal one inside Toronto.
        First-time buyer rebates may apply.</li>
      <li><strong>Legal fees</strong> - typically $1,500-$2,500 including disbursements</li>
      <li><strong>Title insurance</strong>, <strong>home inspection</strong>, and
        <strong>adjustments</strong> for prepaid property tax</li>
    </ul>
    <p>Budget roughly 1.5% to 4% of the purchase price on top of your down payment.</p>

    <h2>What lenders are actually assessing</h2>
    <p>Income stability, credit history, your down payment and where it came from, and your debt ratios.
      That last one surprises people: <strong>paying off a car loan can raise your buying power more than
      saving another $5,000</strong>, because it frees up monthly debt room.</p>

    <h2>Pre-approval vs. pre-qualification</h2>
    <p>A pre-qualification is an estimate. A pre-approval is a conditional commitment with a real credit
      check and a rate hold, usually 90-120 days. Neither is final approval - that still depends on the
      property appraising and your finances staying stable.</p>
    <p>One warning: don't take on new debt between pre-approval and closing. A new car loan or financed
      furniture can change your ratios enough to affect the deal.</p>
  </div>
</section>
"""))


# ============================== SELF-EMPLOYED ==============================
PAGES.append(dict(
  slug="self-employed-mortgage", crumb="Self-Employed",
  title="Self-Employed Mortgage Ontario | Beyond the T4",
  og_title="Self-Employed Mortgages - Ontario",
  desc=("Turned down while self-employed? Your write-offs may be the issue, not your "
        "income. How lenders assess business owners and which programs fit."),
  related=[("mortgage-renewal-ontario","Renewals"),
           ("commercial-lending","Commercial lending"),
           ("business-financing","Business financing")],
  faqs=[
    ("Why do banks decline self-employed borrowers with good income?",
     "Many lenders assess self-employed income using your net income after business write-offs, as shown "
     "on your Notice of Assessment. Legitimate deductions that reduce your taxable income also reduce the "
     "income a lender will count - so a healthy business can read as low income on paper."),
    ("How many years self-employed do I need?",
     "Two years of business history is the common benchmark, since lenders usually want two years of tax "
     "documents to average. Some lenders will consider shorter histories, particularly where there's "
     "relevant prior experience in the same field."),
    ("What documents will I need?",
     "Typically two years of T1 General returns and Notices of Assessment, business financial statements, "
     "business registration or articles of incorporation, and often 6-12 months of business bank "
     "statements. Programs that assess gross revenue lean more heavily on the bank statements."),
    ("Can I get a mortgage if I write off a lot of income?",
     "Often yes, through lenders offering self-employed or business-for-self programs that consider gross "
     "business revenue and cash flow rather than only net taxable income. Terms vary and a larger down "
     "payment is sometimes required."),
  ],
  body="""
<section class="hero">
  <div class="wrap">
    <p class="eyebrow">Self-employed</p>
    <h1>A "no" from your bank <span>isn't the whole market.</span></h1>
    <p class="lead" style="margin-top:1rem">If you're self-employed and got declined, the issue is usually
      how one lender reads your income - not whether you can actually carry a mortgage.</p>
    <div class="actions" style="margin-top:1.5rem">
      <a class="btn gold" href="#book">Talk through your situation</a>
      <a class="btn ghost" href="tel:+12269788858">Call 226-978-8858</a>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap prose" style="max-width:75ch">
    <h2>The write-off paradox</h2>
    <p>Good accounting minimises your taxable income. Mortgage qualification often rewards showing high
      taxable income. Those two goals pull in opposite directions, and most self-employed borrowers only
      discover it at a bank branch.</p>
    <p>A contractor grossing $180,000 who writes down to $70,000 net looks like a $70,000 earner to a
      lender reading line 15000 - even though the business is strong and the cash flow is real.</p>

    <h2>What actually changes the outcome</h2>
    <ul>
      <li><strong>Lenders who assess differently.</strong> Business-for-self programs consider gross
        revenue, bank statement deposits and cash flow rather than only net taxable income.</li>
      <li><strong>Add-backs.</strong> Some deductions - depreciation, home office, certain one-time
        expenses - can sometimes be added back into qualifying income when documented properly.</li>
      <li><strong>Timing.</strong> If you're planning to buy in 18 months, how you file this year matters.
        That's a conversation to have with your accountant <em>and</em> me, ideally in the same month.</li>
      <li><strong>Down payment size.</strong> A larger down payment opens more programs.</li>
    </ul>

    <h2>Where a broker matters more for you than for a salaried buyer</h2>
    <p>A bank employee can offer you that bank's products. If your file doesn't match their template, the
      answer is no and the conversation ends. Working across multiple lenders means the question becomes
      "which lender's guidelines fit this file" rather than "does this file fit this one lender."</p>

    <h2>Document checklist</h2>
    <ul>
      <li>Two years of T1 General returns and Notices of Assessment</li>
      <li>Business financial statements, ideally accountant-prepared</li>
      <li>Business registration or articles of incorporation</li>
      <li>6-12 months of business bank statements</li>
      <li>Any contracts or invoices showing forward revenue</li>
    </ul>
    <p>Get these organised early. Self-employed files ask more questions, and having answers ready is
      often the difference between a smooth approval and a stalled one.</p>
  </div>
</section>
"""))


# ============================== NEWCOMER ==============================
PAGES.append(dict(
  slug="newcomer-mortgage-canada", crumb="Newcomers",
  title="Newcomer Mortgage Canada | No Credit History?",
  og_title="Newcomer Mortgages - Canada",
  desc=("New to Canada and want to buy? Newcomer mortgage programs can work without "
        "Canadian credit history. What lenders accept instead."),
  related=[("first-time-home-buyer-ontario","First-time buyer guide"),
           ("self-employed-mortgage","Self-employed mortgages"),
           ("mortgage-affordability-calculator","Affordability calculator")],
  faqs=[
    ("Can I get a mortgage as a new permanent resident?",
     "Often yes. Several lenders run newcomer programs specifically for people without an established "
     "Canadian credit file, using alternative documentation to assess creditworthiness."),
    ("Do I need Canadian credit history?",
     "Not always. Lenders may accept an international credit report, a reference letter from your bank in "
     "your country of origin, or other evidence such as 12 months of rent and utility payment history."),
    ("Can I buy on a work permit?",
     "Some programs are available to non-permanent residents legally authorised to work in Canada, though "
     "requirements are stricter and a larger down payment is often needed. Eligibility depends on your "
     "permit type and the lender."),
    ("How long do I need to be in Canada first?",
     "There's no universal waiting period. Some newcomer programs are designed for people who arrived "
     "within the last five years, and some clients qualify well inside their first two years."),
    ("Are there restrictions on foreign buyers?",
     "Canada has had restrictions on residential property purchases by non-Canadians, with exemptions "
     "including permanent residents and certain temporary residents. Rules have changed over time, so "
     "confirm current requirements for your specific status before making an offer."),
  ],
  body="""
<section class="hero">
  <div class="wrap">
    <p class="eyebrow">Newcomers to Canada</p>
    <h1>New here? You may qualify <span>sooner than you think.</span></h1>
    <p class="lead" style="margin-top:1rem">"I need years of Canadian credit history first" is one of the
      most common assumptions newcomers make - and one of the most commonly wrong.</p>
    <div class="actions" style="margin-top:1.5rem">
      <a class="btn gold" href="#book">Find out what you qualify for</a>
      <a class="btn ghost" href="tel:+12269788858">Call 226-978-8858</a>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap prose" style="max-width:75ch">
    <h2>The credit history gap</h2>
    <p>Credit scores don't transfer between countries. You can have a spotless twenty-year record abroad
      and arrive in Canada with essentially no file at all. Standard underwriting struggles with that -
      not because you're a risk, but because the usual data point is missing.</p>
    <p>Newcomer programs exist precisely to fill that gap.</p>

    <h2>What lenders accept instead</h2>
    <ul>
      <li><strong>International credit reports</strong> from your country of origin</li>
      <li><strong>Reference letters</strong> from your previous financial institution</li>
      <li><strong>Rental and utility payment history</strong> - typically 12 months, showing you pay
        housing costs reliably</li>
      <li><strong>Employment letters and pay stubs</strong> confirming current Canadian income</li>
      <li><strong>Proof of down payment</strong>, including funds transferred from abroad - keep clear
        records of the transfer trail</li>
    </ul>

    <h2>Practical things that help before you apply</h2>
    <ul>
      <li>Open a Canadian bank account and get a secured or entry-level credit card early - even small
        activity starts building a file</li>
      <li>Keep every rent receipt and utility statement</li>
      <li>Document any large deposit. Lenders must trace your down payment, and an unexplained lump sum
        is one of the most common reasons a file stalls</li>
      <li>Avoid changing jobs right before applying if you can help it</li>
    </ul>

    <h2>Down payment expectations</h2>
    <p>Permanent residents can often access the same minimum down payment rules as Canadian citizens.
      Non-permanent residents on work permits typically face higher requirements, commonly starting around
      20% depending on the lender and program.</p>

    <h2>Rules change - check before you commit</h2>
    <p>Restrictions on residential purchases by non-Canadians have been introduced and amended over recent
      years, with various exemptions. Before making an offer, confirm what currently applies to your exact
      immigration status. I'd rather check that with you upfront than have it surface at the lawyer's office.</p>
  </div>
</section>
"""))


# ============================== PRE-CONSTRUCTION ==============================
PAGES.append(dict(
  slug="pre-construction-mortgage", crumb="Pre-Construction",
  title="Pre-Construction Mortgage Ontario | What to Know",
  og_title="Pre-Construction Mortgages - Ontario",
  desc=("Buying pre-construction? Deposit schedules, why your pre-approval expires "
        "before closing, occupancy fees and the CMHC Eco Plus refund."),
  related=[("first-time-home-buyer-ontario","First-time buyer guide"),
           ("mortgage-affordability-calculator","Affordability calculator"),
           ("mortgage-renewal-ontario","Renewals")],
  faqs=[
    ("How long is a mortgage pre-approval valid for a pre-construction purchase?",
     "Usually 90 to 120 days, sometimes up to about 130. Since pre-construction closings can be one to "
     "four years out, your original pre-approval will almost certainly expire well before closing. Plan to "
     "arrange financing again as your real closing date approaches."),
    ("How do pre-construction deposits work in Ontario?",
     "Builders collect deposits in instalments during construction, commonly totalling around 15% to 20% "
     "of the purchase price - for example 5% on signing, 5% at 30 days, 5% at 180 days and 5% at "
     "occupancy. Structures vary by builder, so check your Agreement of Purchase and Sale."),
    ("Are my deposits protected if the builder fails?",
     "Ontario's Tarion new home warranty program includes deposit protection, but with limits that depend "
     "on the type of home and your agreement. It's not automatically 100% of everything you've paid. "
     "Confirm your specific coverage limit with Tarion and your real estate lawyer."),
    ("What is interim occupancy?",
     "For many condo purchases you can move in once your unit is ready but before the building is legally "
     "registered. During that period you pay occupancy fees to the builder. Those aren't mortgage "
     "payments and don't build equity - your mortgage begins at final closing."),
    ("Can I get money back for an energy-efficient new build?",
     "CMHC Eco Plus can refund up to 25% of your CMHC mortgage insurance premium on a qualifying newly "
     "built energy-efficient home. Lower efficiency tiers may qualify for a smaller refund. Applications "
     "are generally filed within two years of closing. Confirm current criteria with CMHC."),
    ("Is there a cooling-off period?",
     "Ontario provides a 10-day statutory cooling-off period for new freehold homes. Condominium "
     "purchases have their own rescission rights under condo legislation. Ask your lawyer what applies to "
     "your agreement."),
  ],
  body="""
<section class="hero">
  <div class="wrap">
    <p class="eyebrow">Pre-construction</p>
    <h1>You sign years before <span>you ever get a mortgage.</span></h1>
    <p class="lead" style="margin-top:1rem">That gap is where pre-construction buyers get blindsided -
      expired pre-approvals, deposit schedules they didn't plan for, and occupancy fees nobody mentioned
      at the sales centre.</p>
    <div class="actions" style="margin-top:1.5rem">
      <a class="btn gold" href="#book">Review my agreement with me</a>
      <a class="btn ghost" href="tel:+12269788858">Call 226-978-8858</a>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap prose" style="max-width:75ch">
    <h2>The timing trap: 120 days vs. 3 years</h2>
    <p>A standard pre-approval holds your rate for roughly 90 to 120 days. Pre-construction closings
      routinely land one to four years after signing. Those two numbers don't line up, and nothing at the
      sales centre will point that out - selling the unit and managing your mortgage timeline are two
      different jobs.</p>
    <p>Treat pre-approval as something you revisit near closing, not a box ticked once at the beginning.</p>

    <h2>Your finances get re-examined at closing</h2>
    <p>At final closing, your lender verifies your income, credit, employment and down payment source
      essentially from scratch. If you changed jobs, moved from salary to contract work, or took on a car
      loan somewhere in those years, that's the moment it surfaces.</p>
    <p>None of that has to be a problem - but it needs lead time. Finding out four months before closing
      is manageable. Finding out four weeks before is not.</p>

    <h2>Deposit schedules</h2>
    <p>Instead of one down payment, builders collect staged instalments, commonly totalling 15% to 20%
      before closing. A typical GTA structure looks like 5% on signing, 5% at 30 days, 5% at 180 days and
      5% at occupancy - but every builder differs, so read your own agreement.</p>
    <p>Plan cash flow around those dates. Money you'll need in eight months shouldn't be somewhere you
      can't reach it.</p>

    <h2>Interim occupancy</h2>
    <p>Many condo purchases include an occupancy period: you have keys and can live there, but the
      building isn't registered, so you don't legally own it and your mortgage hasn't started. You pay
      occupancy fees to the builder during this window. They feel like rent, they don't build equity, and
      they need to be in your budget.</p>

    <h2>Incentives: get it in writing</h2>
    <p>Free appliance packages, design credits, capped development charges - these are real and often
      negotiable. But "included" sometimes means a specific limited list, and a verbal promise from a
      sales rep isn't enforceable. If it isn't in the Agreement of Purchase and Sale, treat it as not
      guaranteed.</p>

    <h2>Energy-efficient builds and CMHC Eco Plus</h2>
    <p>If your build meets recognised energy-efficiency standards, CMHC Eco Plus can refund up to 25% of
      your mortgage insurance premium. To be precise about what that means: it's a percentage of the
      <em>insurance premium you paid</em>, not of the purchase price. Lower efficiency tiers can qualify
      for a smaller refund. You generally have up to two years after closing to apply, and it isn't
      automatic - someone has to file it.</p>

    <h2>Before you sign anything</h2>
    <ul>
      <li>Confirm the full deposit schedule and total percentage in writing</li>
      <li>Understand your Tarion deposit protection limit for this specific agreement</li>
      <li>Get every incentive written into the agreement itself</li>
      <li>Know your estimated closing date and count backward to when financing needs arranging</li>
      <li>Ask whether interim occupancy applies, and what the fees will be</li>
      <li>Check whether the build may qualify for energy-efficiency refunds</li>
      <li><strong>Have a real estate lawyer review the agreement before you sign</strong></li>
    </ul>
  </div>
</section>
"""))


# ============================== AFFORDABILITY CALC ==============================
PAGES.append(dict(
  slug="mortgage-affordability-calculator", crumb="Affordability Calculator",
  title="Mortgage Affordability Calculator | Ontario",
  og_title="Mortgage Affordability Calculator - Ontario",
  desc=("Free Ontario mortgage affordability calculator. See your maximum purchase "
        "price from income, debts and down payment, with GDS and TDS explained."),
  related=[("rent-vs-buy-calculator","Rent vs buy calculator"),
           ("first-time-home-buyer-ontario","First-time buyer guide"),
           ("mortgage-renewal-ontario","Renewals")],
  faqs=[
    ("How much mortgage can I afford on my income?",
     "Lenders generally cap housing costs around 39% of gross income (GDS) and total debt payments around "
     "44% (TDS), though thresholds vary by lender and insurance status. Your down payment and other debts "
     "then determine the purchase price those ratios support."),
    ("What are GDS and TDS ratios?",
     "Gross Debt Service is your housing costs - mortgage payment, property tax, heat, and half of any "
     "condo fees - as a percentage of gross income. Total Debt Service adds all your other debt payments. "
     "Both must fit within lender limits."),
    ("Does this calculator guarantee approval?",
     "No. It's an educational estimate. Real approval depends on your full application, credit, income "
     "documentation, the property, and the individual lender's guidelines."),
    ("Why does paying off debt increase how much I can borrow?",
     "Because TDS counts your other monthly payments against the same income. Clearing a $450 car payment "
     "frees that room for housing costs, which can raise your maximum mortgage by considerably more than "
     "the loan balance you paid off."),
  ],
  body=f"""
<section class="hero">
  <div class="wrap">
    <p class="eyebrow">Calculator</p>
    <h1>How much house can you <span>actually afford?</span></h1>
    <p class="lead" style="margin-top:1rem">Drag the sliders. This runs the same debt-ratio math lenders
      use, so you get a realistic range instead of a guess.</p>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="grid-2">
{AFFORD_CALC}
      <div class="prose">
        <h2>How the math works</h2>
        <p>Two ratios decide most of it.</p>
        <p><strong>GDS (Gross Debt Service)</strong> - your housing costs as a share of gross income:
          mortgage payment, property tax, heating, and typically half of any condo fees. Common ceiling
          around 39%.</p>
        <p><strong>TDS (Total Debt Service)</strong> - GDS plus every other monthly debt payment: car
          loans, credit card minimums, student loans, lines of credit. Common ceiling around 44%.</p>
        <p>Whichever limit you hit first is your constraint.</p>

        <h3>Why your debts matter so much</h3>
        <p>A $450 monthly car payment doesn't just cost $450. It removes $450 of room from your TDS
          calculation - which at typical rates can reduce your maximum mortgage by roughly $70,000 to
          $90,000. Paying it off is sometimes the single fastest way to increase buying power.</p>

        <h3>What this calculator can't see</h3>
        <p>Your credit score, how your income is documented, whether you're self-employed, the specific
          property, and each lender's own overlays. Treat the output as a realistic starting range, then
          let's confirm it properly against actual lender guidelines.</p>
      </div>
    </div>
    <p class="market-note">Educational estimate only. Not a pre-approval, quote, or commitment to lend.</p>
  </div>
</section>
"""))


# ============================== RENT VS BUY CALC ==============================
PAGES.append(dict(
  slug="rent-vs-buy-calculator", crumb="Rent vs Buy Calculator",
  title="Rent vs Buy Calculator | Canada",
  og_title="Rent vs Buy Calculator - Canada",
  desc=("Free rent vs buy calculator. Compare total rent paid against ownership "
        "carrying costs and the equity you would build over your time horizon."),
  related=[("mortgage-affordability-calculator","Affordability calculator"),
           ("first-time-home-buyer-ontario","First-time buyer guide"),
           ("mortgage-renewal-ontario","Renewals")],
  faqs=[
    ("Is renting really throwing money away?",
     "No. Renting buys you housing plus flexibility and zero maintenance exposure. What it doesn't do is "
     "build equity. Whether buying comes out ahead depends mostly on how long you stay and what you would "
     "have done with the money otherwise."),
    ("How long do I need to own before buying beats renting?",
     "There's no universal number, but transaction costs - land transfer tax, legal fees, eventually "
     "realtor commission - mean short holding periods favour renting. Longer horizons give equity "
     "accumulation time to outweigh those one-time costs."),
    ("Does this calculator account for home price appreciation?",
     "The equity figure reflects mortgage paydown plus a modest assumed appreciation. Nobody can reliably "
     "predict future prices, so treat it as illustrative rather than a forecast."),
    ("What costs do renters avoid?",
     "Property tax, maintenance and repairs, condo special assessments, and the transaction costs of "
     "buying and selling. Those are real and often left out of casual comparisons."),
  ],
  body=f"""
<section class="hero">
  <div class="wrap">
    <p class="eyebrow">Calculator</p>
    <h1>Rent vs. buy, <span>done honestly.</span></h1>
    <p class="lead" style="margin-top:1rem">Most versions of this comparison are built to make buying look
      obvious. This one includes the costs renters genuinely avoid.</p>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="grid-2">
{RVB_CALC}
      <div class="prose">
        <h2>What the numbers show</h2>
        <p>Ownership almost always costs more month to month than renting an equivalent place. The
          difference is that part of your payment reduces what you owe - <strong>forced savings you can't
          easily skip.</strong></p>

        <h3>The case for renting</h3>
        <ul>
          <li>No property tax, maintenance, or special assessments</li>
          <li>Full mobility - job changes and life changes cost you a moving truck, not a sale</li>
          <li>Your capital stays liquid and can be invested elsewhere</li>
        </ul>

        <h3>The case for buying</h3>
        <ul>
          <li>Equity from paydown, plus any appreciation</li>
          <li>A fixed mortgage payment doesn't climb with the rental market</li>
          <li>Stability and control over your space</li>
        </ul>

        <h3>What no calculator can price</h3>
        <p>Not worrying that your landlord will sell. Painting a wall without asking. Those matter to
          people, and they don't show up in a spreadsheet - which is fine, as long as you're honest about
          which factors are actually driving your decision.</p>
      </div>
    </div>
    <p class="market-note">Illustrative comparison, not a forecast or investment advice. Assumes 20% down.</p>
  </div>
</section>
"""))


# ============================== COMMERCIAL ==============================
PAGES.append(dict(
  slug="commercial-lending", crumb="Commercial Lending",
  title="Commercial Mortgage Ontario | DSCR Explained",
  og_title="Commercial Lending - Ontario",
  desc=("Commercial mortgages in Ontario for retail, office, industrial and mixed-use "
        "property. How DSCR works and what lenders actually review."),
  related=[("business-financing","Business financing"),
           ("self-employed-mortgage","Self-employed mortgages")],
  faqs=[
    ("How is a commercial mortgage different from a residential one?",
     "Commercial lending focuses on the property's income rather than mainly your personal income. "
     "Lenders assess debt service coverage ratio, lease quality and tenant strength, and typically "
     "require larger down payments with shorter terms and amortizations."),
    ("What is DSCR?",
     "Debt Service Coverage Ratio compares the property's net operating income to its annual debt "
     "payments. A DSCR of 1.25 means the property generates 25% more income than needed to cover the "
     "mortgage. Most commercial lenders want to see a comfortable cushion above 1.0."),
    ("How much down payment do I need for commercial property?",
     "Commonly 25% to 35% or more, varying by property type, tenant profile and lender. Owner-occupied "
     "commercial can sometimes access more favourable structures than pure investment purchases."),
    ("Do you handle mixed-use properties?",
     "Yes - a building with retail below and apartments above is common and financeable, though the mix "
     "of residential to commercial space affects which lenders and programs apply."),
  ],
  body="""
<section class="hero">
  <div class="wrap">
    <p class="eyebrow">Commercial lending</p>
    <h1>Financing that follows <span>the property's income.</span></h1>
    <p class="lead" style="margin-top:1rem">Commercial deals are underwritten differently from homes. The
      building has to carry itself - and the way that gets measured decides your terms.</p>
    <div class="actions" style="margin-top:1.5rem">
      <a class="btn gold" href="#book">Discuss a commercial deal</a>
      <a class="btn ghost" href="tel:+12269788858">Call 226-978-8858</a>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap prose" style="max-width:75ch">
    <h2>What lenders look at</h2>
    <p>On a home, the main question is whether <em>you</em> can pay. On commercial property, the main
      question is whether <em>the building</em> can pay - and you're the backup.</p>
    <ul>
      <li><strong>Net operating income</strong> - rental income less operating expenses</li>
      <li><strong>Debt service coverage ratio</strong> - NOI divided by annual debt payments</li>
      <li><strong>Lease quality</strong> - term length, tenant covenant strength, renewal risk</li>
      <li><strong>Property type and location</strong> - industrial, retail, office and mixed-use each
        carry different lender appetite</li>
      <li><strong>Your experience</strong> - track record with similar assets genuinely matters</li>
    </ul>

    <h2>Understanding DSCR</h2>
    <p>If a property nets $120,000 a year and the mortgage costs $96,000 a year, DSCR is 1.25 - the
      property produces 25% more than it needs. Lenders use that cushion to size the loan. Push the loan
      higher and DSCR falls; fall too close to 1.0 and the deal stops working for them.</p>
    <p>Practically, DSCR often caps your loan amount before the appraised value does.</p>

    <h2>What to expect on structure</h2>
    <ul>
      <li>Larger down payments than residential - commonly 25-35%+</li>
      <li>Shorter terms and often shorter amortizations</li>
      <li>Appraisal, environmental assessment and sometimes a building condition report</li>
      <li>Longer timelines - commercial due diligence takes real time, so build it into your offer</li>
    </ul>

    <h2>Before you make an offer</h2>
    <p>Get the rent roll, current leases and two years of operating statements early. Commercial
      financing conversations go much faster when the property's actual numbers are on the table rather
      than estimated.</p>
    <p class="calc-note">Commercial and business lending scope depends on licensing category and
      brokerage arrangements. Let's confirm fit for your specific deal on a call.</p>
  </div>
</section>
"""))


# ============================== BUSINESS FINANCING ==============================
PAGES.append(dict(
  slug="business-financing", crumb="Business Financing",
  title="Business Financing Ontario | Capital & Equipment",
  og_title="Business Financing - Ontario",
  desc=("Ontario business financing: working capital, equipment loans, expansion "
        "funding and the Canada Small Business Financing Program."),
  related=[("commercial-lending","Commercial lending"),
           ("self-employed-mortgage","Self-employed mortgages")],
  faqs=[
    ("What types of business financing are available?",
     "Term loans for equipment and expansion, operating lines of credit for working capital, equipment "
     "leasing, and government-backed options such as the Canada Small Business Financing Program. The "
     "right structure depends on whether you're funding an asset or a cash flow gap."),
    ("What is the Canada Small Business Financing Program?",
     "A federal program where the government shares risk with lenders to help small businesses access "
     "financing for things like equipment and leasehold improvements. Eligibility and limits are set by "
     "the program, so confirm current terms before planning around it."),
    ("What do lenders want to see from my business?",
     "Typically two years of financial statements, recent business bank statements, a clear explanation of "
     "what the funds are for and how they'll be repaid, and personal financial information from the "
     "owners. Newer businesses lean more heavily on projections and personal credit."),
    ("Can I get financing for a business less than two years old?",
     "It's harder but not impossible. Options narrow, personal credit and any available security carry "
     "more weight, and government-backed programs sometimes help bridge the gap."),
  ],
  body="""
<section class="hero">
  <div class="wrap">
    <p class="eyebrow">Business financing</p>
    <h1>Funding built around <span>how your business actually runs.</span></h1>
    <p class="lead" style="margin-top:1rem">Matching the financing structure to the actual need matters
      more than chasing the lowest headline rate.</p>
    <div class="actions" style="margin-top:1.5rem">
      <a class="btn gold" href="#book">Talk through your financing need</a>
      <a class="btn ghost" href="tel:+12269788858">Call 226-978-8858</a>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap prose" style="max-width:75ch">
    <h2>Match the structure to the need</h2>
    <p>The most common expensive mistake is funding the wrong thing with the wrong product - covering a
      seasonal cash flow gap with a five-year term loan, or buying a $200,000 machine on a line of credit.</p>
    <ul>
      <li><strong>Working capital gaps</strong> - operating line of credit. You draw and repay as cash
        flow moves.</li>
      <li><strong>Equipment purchases</strong> - term loan or lease, amortized over the asset's useful
        life.</li>
      <li><strong>Expansion or leasehold improvements</strong> - term loan, sometimes with government
        program support.</li>
      <li><strong>Property purchase</strong> - that's a commercial mortgage.
        <a href="/commercial-lending/">See commercial lending</a>.</li>
    </ul>

    <h2>Government-backed options</h2>
    <p>The Canada Small Business Financing Program lets the federal government share lender risk, which
      can open doors for businesses that wouldn't clear conventional criteria alone. It's particularly
      relevant for equipment and leasehold improvements. Program limits and eligibility change over time,
      so confirm current details before building a plan around it.</p>

    <h2>What to have ready</h2>
    <ul>
      <li>Two years of financial statements, accountant-prepared where possible</li>
      <li>6-12 months of business bank statements</li>
      <li>A specific use of funds - "$85,000 for a CNC machine that adds capacity" beats "some working
        capital"</li>
      <li>Repayment logic tied to real revenue, not optimism</li>
      <li>Personal financial information for the owners</li>
    </ul>

    <h2>If your business is young</h2>
    <p>Under two years of history narrows options rather than eliminating them. Personal credit, available
      security, and government-backed programs all carry more weight. Being realistic about that upfront
      saves you from a string of declines that quietly damage your credit file.</p>
    <p class="calc-note">Commercial and business lending scope depends on licensing category and
      brokerage arrangements. Let's confirm fit for your specific situation on a call.</p>
  </div>
</section>
"""))
