/* =====================================================================
   MOBILE NAV (hamburger menu)
   Below 920px width, the hamburger icon (#nav-toggle) in the nav bar shows
   up instead of the desktop link row. Tapping it calls toggleMobileNav(),
   which slides #mobile-nav open/closed and swaps the icon to an X. Tapping
   any link inside closes it again via closeMobileNav() (see the onclick on
   each <a> in index.html's #mobile-nav block).
===================================================================== */
function toggleMobileNav(){
  const menu = document.getElementById('mobile-nav');
  const toggle = document.getElementById('nav-toggle');
  const isOpen = menu.classList.toggle('open');
  toggle.classList.toggle('open', isOpen);
  toggle.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
}
function closeMobileNav(){
  document.getElementById('mobile-nav').classList.remove('open');
  document.getElementById('nav-toggle').classList.remove('open');
  document.getElementById('nav-toggle').setAttribute('aria-expanded', 'false');
}
// Safety net: if someone has the mobile menu open and rotates their phone
// or resizes past the point where the hamburger switches back to the full
// desktop nav (920px), force the menu closed so it can't get stuck open.
window.addEventListener('resize', ()=>{ if(window.innerWidth > 920) closeMobileNav(); });

/* =====================================================================
   BLOG POSTS - add a new object here to add a post. Nothing else to edit.
===================================================================== */
const BLOG_POSTS = [
  { tag: "First-Time Buyers", title: "You Don't Need 20% Down - Here's What You Actually Need", date: "July 2026",
    excerpt: "The single biggest myth stopping first-time buyers from starting the process - and what the real minimums look like.",
    content: [
      "If I had a dollar for every buyer who told me they're 'not ready yet' because they don't have 20% down, I could probably make a dent in my own mortgage. Possibly buy a very small shed.",
      "The real minimum in Canada is as little as 5% down on homes under $1.5 million. Putting down less than 20% means you'll need CMHC mortgage default insurance, which adds a premium - but it does not lock you out of buying.",
      "The right down payment for you depends on your monthly cash flow, how long you plan to stay in the home, and how comfortable you are with a slightly higher payment versus a slightly bigger cheque today.",
      "Try the Down Payment Dial above to see what 5%, 10%, 15%, and 20% actually look like side by side before you rule anything out. It's oddly satisfying to drag, like a very expensive fidget toy."
    ]},
  { tag: "Renewals", title: "Your Mortgage Renewal Isn't Automatic - And That's a Good Thing", date: "July 2026",
    excerpt: "That renewal letter from your bank isn't the only offer on the table. Here's what to do 4-6 months before it arrives.",
    content: [
      "A lot of homeowners treat their mortgage renewal letter like a bill - sign it, send it back, move on. But that renewal offer is just one lender's opening number, not the market.",
      "Rates and terms genuinely vary between lenders, and your current bank has no real incentive to give you their best offer automatically - you have to ask, or have someone ask on your behalf. Banks are not in the business of volunteering you a better deal, shocking absolutely no one.",
      "My rule of thumb: start looking 4-6 months before your renewal date. That gives enough time to compare options without feeling rushed into whatever envelope shows up in your mailbox.",
      "If your renewal is coming up in the next year, send me a message - I'll check the market for you at no cost before you sign anything, and I promise not to judge you for almost auto-signing it."
    ]},
  { tag: "Self-Employed", title: "Self-Employed and Buying a Home? Here's How Lenders Actually See You", date: "June 2026",
    excerpt: "Being self-employed doesn't disqualify you from a mortgage - it just changes what paperwork you'll need to gather.",
    content: [
      "The most common thing I hear from self-employed clients is some version of 'I probably can't qualify because I don't have a T4.' Understandable - but not quite true.",
      "Lenders assess self-employed income differently than salaried income, usually looking at 2 years of Notices of Assessment and tax returns, or using alternative documentation.",
      "The trade-off is usually preparation time. The more organized your paperwork is going in, the smoother the process goes - this is the one time in life where being 'that person' with a labeled folder system actually pays off.",
      "Check the Documents section above for the full self-employed checklist, or reach out and I'll walk through exactly what your situation needs."
    ]},
  { tag: "Government Policy", title: "The GST/HST New Housing Rebate: Who Actually Gets Money Back", date: "July 2026",
    excerpt: "A real rebate exists for new builds and major renovations - and most buyers have no idea it applies to them.",
    content: [
      "If you're buying a newly built home, a substantially renovated home, or building your own, there's a decent chance the GST/HST New Housing Rebate applies to you - and a lot of buyers walk right past it because 'rebate' sounds like a scam email.",
      "The rebate returns a portion of the GST or the federal part of HST paid on a new home, and for owner-built homes it can also apply to substantial renovations. The amount depends on the purchase price and whether it's your primary residence or a rental.",
      "The rules get genuinely fussy about deadlines, ownership structure, and occupancy timelines, so this is one of those areas where 'I'll figure it out after closing' can quietly cost you real money.",
      "I'm not an accountant, and this isn't tax advice - but I flag it for every new-build client early, because 'wait, I could have gotten thousands back?' is not a sentence I ever want to hear after the fact."
    ]},
  { tag: "Savings Strategy", title: "RRSP Home Buyers' Plan vs. FHSA: Why Not Both?", date: "June 2026",
    excerpt: "Two government programs, one goal, and most first-time buyers are only using half of what's available to them.",
    content: [
      "The RRSP Home Buyers' Plan (HBP) lets you withdraw up to $60,000 from your RRSP, tax-free, to put toward a first home - as long as you pay it back over 15 years. The First Home Savings Account (FHSA) lets you contribute up to $8,000/year (lifetime max $40,000), get a tax deduction going in, and withdraw it completely tax-free for a home, with no repayment required.",
      "Here's the part people miss: these aren't either/or. A first-time buyer can use both the HBP and the FHSA on the same purchase, meaning a couple could realistically bring well over $150,000 of tax-advantaged down payment money to closing.",
      "The FHSA is the newer, arguably better deal for money you haven't saved yet, since you never have to pay it back. The HBP is great for money already sitting in an RRSP that would otherwise just sit there judging you.",
      "This is genuinely one of the highest-leverage conversations I have with first-time buyers, and one of the most under-used. Ask me about it before you assume your only options are 'save for a decade' or 'ask your parents.'"
    ]},
  { tag: "Home Insurance", title: "Home Insurance Isn't One-Size-Fits-All: Condo vs. Townhouse vs. Detached", date: "July 2026",
    excerpt: "Your lender requires proof of insurance before closing - but what you actually need to buy depends heavily on the property type.",
    content: [
      "For a condo, you typically need a 'condo/HO-6' policy, which covers your unit's interior, contents, and liability - the building's exterior and common areas are covered by the condo corporation's master policy. Skip this distinction and you can end up paying twice for the same walls or, worse, not covered for the ones that matter.",
      "For a townhouse in a gated community or condo-style townhouse complex, check whether there's a shared master policy (common in condo-titled townhomes) or whether you're fully responsible for the structure yourself (common in freehold townhomes) - these look similar from the driveway and are completely different on paper.",
      "For a detached home, you're insuring the whole structure yourself: roof, foundation, plumbing, the works, plus contents and liability. This is usually the most expensive policy of the three, but also the most straightforward.",
      "Whatever the property type, your lender will want proof of insurance naming them as loss payee before funds are released on closing day - this is not optional paperwork, it's a 'closing does not happen without it' item. Get quotes early; insurance brokers are not known for their same-day turnaround."
    ]},
  { tag: "Stress Test", title: "The Mortgage Stress Test: What It Actually Tests (Spoiler: Not You)", date: "June 2026",
    excerpt: "You have to qualify at a higher rate than you'll actually pay. Here's why, and what it means for how much you can borrow.",
    content: [
      "Federally regulated lenders must qualify you at the higher of your contract rate plus 2%, or a minimum benchmark rate - meaning if your actual rate is 4.14%, you might need to prove you can handle payments closer to 6.14%.",
      "This isn't a test of your character, your budgeting skills, or your commitment to the relationship - it's a buffer built into the system so that a future rate increase doesn't immediately put you underwater.",
      "The practical effect: your approved mortgage amount is usually meaningfully lower than what your actual monthly payment would suggest you could afford. This surprises almost everyone the first time they hear it.",
      "It's frustrating in the moment, but it's also part of why Canada's mortgage system held up better than some others during rate spikes. Small comfort when you're staring at a smaller pre-approval number, I know."
    ]},
  { tag: "Government Policy", title: "The 30-Year Amortization Is Back (For Some People)", date: "May 2026",
    excerpt: "First-time buyers purchasing new builds can now access 30-year insured amortizations. Here's who actually qualifies.",
    content: [
      "As of the December 2024 rule change, eligible first-time homebuyers purchasing a newly built home can access a 30-year amortization on an insured mortgage, instead of the previous 25-year maximum - for a small rate surcharge.",
      "The math is straightforward: stretching the same mortgage over 30 years instead of 25 lowers your monthly payment, at the cost of paying more interest over the life of the loan. It's a real trade-off, not a free lunch, but it can be the difference between qualifying and not.",
      "The eligibility rules are specific - first-time buyer status and new construction are both required - so this isn't a universal option yet, despite what you might see in a catchy Instagram caption (possibly one of mine).",
      "If you're eyeing a new-build and the 25-year payment feels tight, this is worth a conversation before you assume it's off the table."
    ]},
  { tag: "News", title: "Bank of Canada Holds Again: What 'Stable Rates' Actually Means For You", date: "August 2026",
    excerpt: "Six consecutive holds at 2.25%. Here's what that streak does - and doesn't - tell you about your own mortgage decision.",
    content: [
      "The Bank of Canada has now held its policy rate at 2.25% for six consecutive decisions, after a rapid tightening cycle peaked at 5.00% in mid-2023 and nine subsequent cuts brought it down to today's level.",
      "'Stable' doesn't mean 'guaranteed to stay put forever' - it means the Bank currently sees the rate as appropriately balanced against inflation and growth. Fixed mortgage rates, meanwhile, are driven more by bond yields than the overnight rate directly, which is why they don't always move in lockstep.",
      "For anyone renewing or buying in this window, stability is generally good news: it makes budgeting easier and reduces the odds of an unpleasant surprise mid-process.",
      "That said, 'the Bank held again' is not, on its own, a reason to rush a decision - or delay one. Check the Rates & Bond Yields chart above for the actual trend, not just this month's headline."
    ]}
];

/* =====================================================================
   DOCUMENT CHECKLIST - add/remove a scenario by adding/removing a key
   below. Add/remove a required document by adding/removing a line in
   its array. That's it - the tabs, list, and progress bar all update
   automatically.
===================================================================== */
const DOC_SCENARIOS = {
  "First-Time Buyer": [
    "Government-issued photo ID",
    "Proof of employment (recent pay stubs or employment letter)",
    "2 most recent T4s or Notices of Assessment",
    "90 days of bank statements showing down payment funds",
    "Void cheque or pre-authorized debit form",
    "Signed purchase agreement (once you have one)"
  ],
  "Self-Employed": [
    "2 years of personal Notices of Assessment (NOA)",
    "2 years of T1 General tax returns",
    "Business financial statements or business license",
    "Proof of business ownership (articles of incorporation / registration)",
    "90+ days of business & personal bank statements",
    "Statement of business activities (T2125)"
  ],
  "Newcomer to Canada": [
    "Permanent Resident card, work permit, or study permit",
    "Valid passport",
    "Proof of employment or a signed employment offer letter",
    "Canadian or international credit history (if available)",
    "Down payment proof (funds typically need to be in Canada 30-90 days)",
    "Confirmation of Permanent Residence (COPR), if applicable"
  ],
  "Renewing": [
    "Current mortgage statement",
    "Renewal letter from your current lender",
    "Updated proof of income (if switching lenders)",
    "Recent property tax statement",
    "Updated government-issued ID"
  ],
  "Refinancing": [
    "Current mortgage statement & payout amount",
    "Updated home appraisal (often ordered by the lender)",
    "Proof of income (pay stubs, T4s, or NOA)",
    "Recent property tax statement",
    "Purpose of refinance details (e.g., list of debts if consolidating)",
    "Updated ID & void cheque"
  ],
  "Investment Property": [
    "Proof of personal income (plus rental income if you own other properties)",
    "Down payment proof (typically 20%+ required)",
    "Mortgage statements for any existing properties",
    "Lease agreements / rental income documentation (if applicable)",
    "Property tax statements for existing properties"
  ]
};

/* =====================================================================
   CASE STUDIES - add a new object to add a card. `stats` shows 2-3
   quick numbers on the card; `content` is the full expanded story.
===================================================================== */
const CASE_STUDIES = [
  { tag:"First-Time Buyers", title:"The $815,000 Home: Three Ways to Get There",
    preview:"A family compared 10%, 15%, and 20% down side by side before deciding - spreadsheets at the dinner table and everything.",
    stats:[["Price","$815,000"],["Best fit","15% down"],["Monthly","$3,742"]],
    content:[
      "A family found their home in the Ontario market at $815,000 and asked a question every buyer eventually asks: how much should we actually put down?",
      "I ran the real math on three scenarios: 10% down ($81,500, requiring a $22,738 CMHC premium and landing at ~$3,974/month), 15% down ($122,250, a smaller $19,397 premium, ~$3,742/month), and 20% down ($163,000, no insurance required, ~$3,479/month but $168,400 needed at closing).",
      "They chose 15% - enough to meaningfully lower the CMHC premium and monthly payment, without draining their cash reserves the way 20% would have.",
      "There's no universally right answer here. The right down payment is the one that fits your cash flow and your comfort level, not just the smallest monthly number - though I did have to physically stop them from putting down 20% 'for the vibes.'"
    ]},
  { tag:"Single Parents", title:"One Income, One Kid, One Very Determined Buyer",
    preview:"Proof that 'household income' doesn't have to mean two paycheques - just one very organized one.",
    stats:[["Income","$78,000/yr"],["Price range","$430,000"],["Program","5% down, insured"]],
    content:[
      "A single mom came in convinced that buying on one income, in this market, with a kid in daycare, was basically a fantasy. Spoiler: it wasn't.",
      "On $78,000/year with $300/month in existing debt, the real numbers landed on roughly $430,000 of affordability at 5% down - modest, but enough for a solid townhouse in the right area, and a lot more than 'not possible.'",
      "We leaned on a longer amortization to keep the monthly payment comfortable, and timed the closing around her daycare subsidy renewal so nothing collided at once.",
      "She texted me a photo of the front door with the caption 'we did this ourselves.' We did not correct her about the mortgage part. She earned that one."
    ]},
  { tag:"Business + Job", title:"The 9-to-5-er Who Also Ran a Weekend Empire",
    preview:"Full-time job by day, thriving Etsy business by night. Two income streams, one very confused first lender.",
    stats:[["T4 income","$64,000/yr"],["Side business","$31,000/yr"],["Result","Combined qualified"]],
    content:[
      "A client had a stable full-time job and a genuinely profitable side business selling custom furniture on weekends - but their bank only wanted to look at the T4 and treated the rest as 'hobby money.'",
      "It's not hobby money if it shows up on two years of tax returns. We packaged both income sources properly - T4 plus net business income from the Statement of Business Activities - and found a lender who actually counts both.",
      "Combined, that pushed their qualifying income up by about 40% compared to using the job alone, which was the difference between a condo and an actual house with a yard.",
      "Moral of the story: if the CRA taxes it, a good broker should be able to use it. Don't let anyone tell you your side hustle doesn't count just because it doesn't come with a lanyard."
    ]},
  { tag:"Self-Employed", title:"The Business Owner Refinance",
    preview:"Two years of inconsistent income didn't have to mean a higher rate - just a smarter application.",
    stats:[["Situation","Refinance"],["Income type","Self-employed"],["Outcome","Equity access"]],
    content:[
      "A self-employed contractor wanted to refinance to access equity for a business expansion, but was worried that fluctuating year-to-year income would work against them.",
      "We built the application around 2 years of Notices of Assessment and a clear statement of business activities, rather than trying to force a salaried-income narrative onto a self-employed file.",
      "The result: approved with a mainstream lender at a competitive rate, with enough equity released to fund the expansion without touching personal savings.",
      "The lesson: self-employed income needs a different application strategy, not a worse one - and no, 'trust me, business is good' is not, in fact, a financial document."
    ]},
  { tag:"Dual Self-Employed", title:"Two Freelancers, Zero T4s, One Nervous Couple",
    preview:"When both partners are self-employed, lenders get twice as curious. We got twice as organized.",
    stats:[["Household income","$142,000/yr"],["NOAs collected","4 years, 2 people"],["Outcome","Approved, 10% down"]],
    content:[
      "A couple - one freelance graphic designer, one independent consultant - assumed that with zero T4s between them, they'd be laughed out of every bank in the GTA.",
      "Two self-employed incomes just means twice the paperwork, not double the risk, as long as it's documented properly: 2 years of NOAs each, business registration, and clean, boring, well-organized bank statements.",
      "We used their averaged 2-year income (a very normal lender practice for self-employed applicants) and got them approved at 10% down with a mainstream lender - no private lending required, despite what a well-meaning uncle at Thanksgiving had warned them about.",
      "They now refer to their mortgage file as 'the most organized folder either of us has ever produced.' I consider that a professional compliment."
    ]},
  { tag:"Newcomers", title:"The First Mortgage, Six Months After Landing",
    preview:"No Canadian credit history yet - but a clear plan (and a very good spreadsheet) made it work.",
    stats:[["Situation","Newcomer"],["Time in Canada","6 months"],["Outcome","Approved"]],
    content:[
      "A newly landed permanent resident had a strong job offer and healthy savings, but no Canadian credit history - the thing most people assume will block a mortgage entirely.",
      "We used a newcomer-specific mortgage program, supplementing the missing Canadian credit file with proof of foreign income history and a larger down payment.",
      "Approved within a few weeks of the application going in, well before their first Canadian tax return would have even existed.",
      "Being new to Canada changes the paperwork, not the possibility - and yes, I did have to explain what a 'void cheque' was, because that phrase means nothing outside this country and honestly it's a weird thing to ask for."
    ]},
  { tag:"Renewals", title:"The Renewal That Almost Cost $400/Month Extra",
    preview:"Their bank's renewal letter wasn't the best offer available - it was just the first one to show up in the mail.",
    stats:[["Situation","Renewal"],["Lenders compared","4"],["Monthly saved","~$400"]],
    content:[
      "A homeowner was about to sign their bank's renewal letter as-is, assuming it was simply how renewals worked. Sign here, carry on, never question it.",
      "We compared their bank's offer against three other lenders. Two came back meaningfully better once we accounted for the full rate and term structure, not just the headline number.",
      "Switching saved them roughly $400/month compared to the original renewal offer - with the entire process handled before their existing term even expired.",
      "Your renewal letter is a starting offer, not a final one. Treat it the way you'd treat a first offer on a used car: politely, and with deep suspicion."
    ]},
  { tag:"Investors", title:"The Landlord With a Spreadsheet Problem (Complimentary)",
    preview:"Three rental properties in, and the math finally needed a professional instead of a napkin.",
    stats:[["Properties owned","3"],["New purchase","20%+ down"],["Outcome","4th property financed"]],
    content:[
      "A client with three existing rental properties wanted a fourth, and had been tracking every mortgage, tenant, and property tax bill in a single, increasingly terrifying spreadsheet.",
      "We pulled together a portfolio summary - mortgage statements, lease agreements, and rental income across all three properties - so the lender could see the full, profitable picture instead of three disconnected files.",
      "Because the existing properties were cash-flow positive, that rental income actually helped qualify for the new purchase rather than working against it.",
      "The spreadsheet has since been retired to a ceremonial, framed printout on his office wall. As it should be."
    ]}
];

/* =====================================================================
   LOCAL MARKET DATA - GROWTH_RATES models the year-over-year GTA-wide
   price change (used to back-calculate history from each city's 2026
   anchor price). Update anchor prices periodically from local boards.
===================================================================== */
const YEARS = [2020,2021,2022,2023,2024,2025,2026];
const GROWTH_RATES = [0.1854, 0.0872, -0.0524, -0.0097, -0.0468, -0.0086]; // 2020->21 ... 2025->26

function buildHistory(anchor2026){
  const vals = new Array(YEARS.length);
  vals[YEARS.length-1] = anchor2026;
  for(let i=GROWTH_RATES.length-1; i>=0; i--){ vals[i] = Math.round(vals[i+1] / (1+GROWTH_RATES[i])); }
  return vals;
}

/* REGIONS: one entry per bubble on the Ontario map (Coverage Areas section).
   cx/cy = center point, r = circle radius, all in SVG user-units against the
   viewBox set on <svg id="ontario-map"> in index.html (currently "0 0 620 480").
   IMPORTANT: if you add/move a region or resize any r, make sure cx-r, cx+r,
   cy-r, and cy+r+30 (extra 30 for the label text under the circle) all stay
   inside the viewBox, or that region will get visually clipped/cut off at
   the edge. Safe usable area with current viewBox: x 20-600, y 25-450. */
const REGIONS = [
  { id:"waterloo", name:"Waterloo Region", cx:110, cy:250, r:46, color:"#262E36",
    cities:[ {name:"Kitchener-Waterloo", anchor:642000, est:false}, {name:"Cambridge", anchor:671000, est:false} ] },
  { id:"halton", name:"Halton Region", cx:225, cy:270, r:44, color:"#C79A55",
    cities:[ {name:"Oakville", anchor:1454094, est:false}, {name:"Burlington", anchor:1149952, est:false}, {name:"Milton", anchor:980000, est:true} ] },
  { id:"hamiltonniagara", name:"Hamilton-Niagara", cx:190, cy:365, r:44, color:"#9C7A45",
    cities:[ {name:"Hamilton", anchor:746245, est:false}, {name:"Niagara Falls / St. Catharines", anchor:620000, est:true} ] },
  { id:"peel", name:"Peel Region", cx:315, cy:245, r:44, color:"#B98D4E",
    cities:[ {name:"Brampton", anchor:966024, est:false}, {name:"Mississauga", anchor:1190000, est:false}, {name:"Caledon", anchor:1250000, est:true} ] },
  { id:"toronto", name:"Toronto / GTA Core", cx:390, cy:265, r:42, color:"#090F15",
    cities:[ {name:"Toronto (City)", anchor:1081375, est:false}, {name:"Scarborough", anchor:984627, est:false} ] },
  { id:"york", name:"York Region", cx:370, cy:170, r:44, color:"#C29A5C",
    cities:[ {name:"Markham", anchor:1240000, est:false}, {name:"Vaughan", anchor:1330000, est:false}, {name:"Newmarket", anchor:1050000, est:true} ] },
  { id:"durham", name:"Durham Region", cx:480, cy:250, r:44, color:"#4A5058",
    cities:[ {name:"Oshawa", anchor:724000, est:false}, {name:"Ajax", anchor:880000, est:true}, {name:"Pickering", anchor:920000, est:true}, {name:"Whitby", anchor:900000, est:true} ] },
  { id:"simcoe", name:"Simcoe County", cx:330, cy:85, r:40, color:"#5C6570",
    cities:[ {name:"Barrie", anchor:780000, est:true} ] },
  { id:"ncr", name:"National Capital Region", cx:560, cy:140, r:40, color:"#404953",
    cities:[ {name:"Ottawa", anchor:734000, est:false}, {name:"Gatineau, QC", anchor:545000, est:true} ] },
  { id:"essex", name:"Essex County", cx:70, cy:410, r:40, color:"#454E58",
    cities:[ {name:"Windsor", anchor:565000, est:false}, {name:"LaSalle", anchor:620000, est:true} ] },
  { id:"middlesex", name:"Middlesex County", cx:180, cy:140, r:42, color:"#37404A",
    cities:[ {name:"London", anchor:640886, est:false}, {name:"St. Thomas", anchor:520000, est:true}, {name:"Middlesex Centre", anchor:746000, est:false} ] }
];

function fmt(v){ return '$' + Math.round(v).toLocaleString('en-CA'); }
function fmtK(v){ return '$' + Math.round(v/1000) + 'K'; }

/* ---- draw the stylized Ontario region map ---- */
const mapSvg = document.getElementById('ontario-map');
let activeMapRegion = "waterloo";
function renderMap(){
  mapSvg.innerHTML = '';
  REGIONS.forEach(r=>{
    const g = document.createElementNS('http://www.w3.org/2000/svg','g');
    const circle = document.createElementNS('http://www.w3.org/2000/svg','circle');
    circle.setAttribute('cx', r.cx); circle.setAttribute('cy', r.cy); circle.setAttribute('r', r.r);
    circle.setAttribute('fill', r.color); circle.setAttribute('opacity', r.id===activeMapRegion ? '1' : '0.55');
    circle.setAttribute('class','region-blob');
    circle.addEventListener('click', ()=>{ activeMapRegion = r.id; renderMap(); renderMapDetail(); });
    g.appendChild(circle);
    const label = document.createElementNS('http://www.w3.org/2000/svg','text');
    label.setAttribute('x', r.cx); label.setAttribute('y', r.cy + r.r + 16);
    label.setAttribute('text-anchor','middle');
    label.setAttribute('class','region-label' + (r.id===activeMapRegion ? ' active-label' : ''));
    label.textContent = r.name;
    g.appendChild(label);
    mapSvg.appendChild(g);
  });
}

function renderMapDetail(){
  const region = REGIONS.find(r=>r.id===activeMapRegion);
  const detail = document.getElementById('map-detail');
  const histories = region.cities.map(c=>({...c, history: buildHistory(c.anchor)}));
  const allVals = histories.flatMap(h=>h.history);
  const maxV = Math.max(...allVals) * 1.08;
  const minV = Math.min(...allVals) * 0.92;
  const colors = ["#262E36","#6C6D74","#8F4A42","#4F6E5C","#090F15"];

  const chartW = 460, chartH = 220, padL=44, padB=28, padT=14;
  const plotW = chartW - padL - 14, plotH = chartH - padB - padT;
  function xPos(i){ return padL + (plotW * i/(YEARS.length-1)); }
  function yPos(v){ return padT + plotH - ((v-minV)/(maxV-minV))*plotH; }

  let svgLines = '';
  histories.forEach((h, idx)=>{
    const color = colors[idx % colors.length];
    let pathD = h.history.map((v,i)=> (i===0?'M':'L') + xPos(i).toFixed(1) + ',' + yPos(v).toFixed(1)).join(' ');
    svgLines += `<path class="chart-line" d="${pathD}" stroke="${color}"/>`;
    h.history.forEach((v,i)=>{ svgLines += `<circle class="chart-dot" cx="${xPos(i).toFixed(1)}" cy="${yPos(v).toFixed(1)}" fill="${color}"/>`; });
  });
  YEARS.forEach((y,i)=>{ svgLines += `<text class="chart-axis-label" x="${xPos(i).toFixed(1)}" y="${chartH-6}" text-anchor="middle">${y}</text>`; });
  [minV, (minV+maxV)/2, maxV].forEach(v=>{ svgLines += `<text class="chart-axis-label" x="4" y="${yPos(v).toFixed(1)+3}">${fmtK(v)}</text>`; });

  const legendHtml = histories.map((h,idx)=>`<div class="chip"><span class="dot" style="background:${colors[idx%colors.length]}"></span>${h.name}${h.est?' (estimated)':''} · ${fmt(h.anchor)}</div>`).join('');

  detail.innerHTML = `
    <h4>${region.name}</h4>
    <div class="sub">Average price trend, 2020-2026</div>
    <div class="city-legend">${legendHtml}</div>
    <svg class="chart" viewBox="0 0 ${chartW} ${chartH}">${svgLines}</svg>
  `;
}

/* ---- BoC rate + bond yield combined chart ---- */
const BOC_MEETINGS = [
  ["2023-01-25",4.50,"hike"],["2023-03-08",4.50,"hold"],["2023-04-12",4.50,"hold"],["2023-06-07",4.75,"hike"],
  ["2023-07-12",5.00,"hike"],["2023-09-06",5.00,"hold"],["2023-10-25",5.00,"hold"],["2023-12-06",5.00,"hold"],
  ["2024-01-24",5.00,"hold"],["2024-03-06",5.00,"hold"],["2024-04-10",5.00,"hold"],["2024-06-05",4.75,"cut"],
  ["2024-07-24",4.50,"cut"],["2024-09-04",4.25,"cut"],["2024-10-23",3.75,"cut"],["2024-12-11",3.25,"cut"],
  ["2025-01-29",3.00,"cut"],["2025-03-12",2.75,"cut"],["2025-04-16",2.75,"hold"],["2025-06-04",2.75,"hold"],
  ["2025-07-30",2.50,"cut"],["2025-09-17",2.50,"hold"],["2025-10-29",2.25,"cut"],["2025-12-10",2.25,"hold"],
  ["2026-01-28",2.25,"hold"],["2026-03-18",2.25,"hold"],["2026-04-29",2.25,"hold"],["2026-06-10",2.25,"hold"],
  ["2026-07-15",2.25,"hold"]
];
// Approximate quarterly 5-yr GoC bond yield, anchored to confirmed readings (Apr 2026: 3.12%, Jul 2026: 3.26%)
const BOND_YIELDS = [
  ["2023-01-01",3.40],["2023-04-01",3.85],["2023-07-01",4.30],["2023-10-01",4.05],
  ["2024-01-01",3.55],["2024-04-01",3.65],["2024-07-01",3.30],["2024-10-01",2.95],
  ["2025-01-01",2.80],["2025-04-01",2.75],["2025-07-01",2.85],["2025-10-01",2.95],
  ["2026-01-01",3.05],["2026-04-01",3.12],["2026-07-01",3.26]
];

let showBoc = true, showBond = true;
function renderRateChart(){
  const svg = document.getElementById('rate-chart');
  const tooltip = document.getElementById('rate-tooltip');
  const W=900,H=340, padL=50,padR=20,padT=20,padB=36;
  const plotW=W-padL-padR, plotH=H-padT-padB;
  const startTime = new Date("2023-01-01").getTime();
  const endTime = new Date("2026-07-15").getTime();
  function xPos(dateStr){ const t=new Date(dateStr).getTime(); return padL + plotW*(t-startTime)/(endTime-startTime); }
  const minRate=2.0, maxRate=5.2;
  function yPos(v){ return padT + plotH - ((v-minRate)/(maxRate-minRate))*plotH; }

  let html = '';
  [2,3,4,5].forEach(v=>{ html += `<line x1="${padL}" y1="${yPos(v)}" x2="${W-padR}" y2="${yPos(v)}" stroke="#B3B7BA" stroke-width="1"/><text class="chart-axis-label" x="6" y="${yPos(v)+3}">${v}%</text>`; });

  if(showBoc){
    let bocPath = '';
    BOC_MEETINGS.forEach((m,i)=>{
      const x = xPos(m[0]), y = yPos(m[1]);
      if(i===0){ bocPath += `M${x},${y}`; } else {
        const prevY = yPos(BOC_MEETINGS[i-1][1]);
        bocPath += ` L${x},${prevY} L${x},${y}`;
      }
    });
    html += `<path class="chart-line" d="${bocPath}" stroke="#262E36" stroke-width="3"/>`;
  }
  if(showBond){
    let bondPath = '';
    BOND_YIELDS.forEach((b,i)=>{ const x=xPos(b[0]), y=yPos(b[1]); bondPath += (i===0?'M':'L')+x+','+y+' '; });
    html += `<path class="chart-line" d="${bondPath}" stroke="#8C959E" stroke-width="2.5"/>`;
  }

  ["2023-01-01","2024-01-01","2025-01-01","2026-01-01"].forEach(d=>{
    html += `<text class="chart-axis-label" x="${xPos(d)}" y="${H-10}" text-anchor="middle">${d.slice(0,4)}</text>`;
  });

  // invisible larger hit targets + visible dots, added after paths so they sit on top
  if(showBoc){
    BOC_MEETINGS.forEach(m=>{
      const x=xPos(m[0]), y=yPos(m[1]);
      const c = m[2]==="hike" ? "#8F4A42" : m[2]==="cut" ? "#4F6E5C" : "#262E36";
      html += `<circle cx="${x}" cy="${y}" r="3.5" fill="${c}"/>`;
      html += `<circle class="chart-hit" data-kind="boc" data-date="${m[0]}" data-val="${m[1]}" data-type="${m[2]}" cx="${x}" cy="${y}" r="9" fill="transparent"/>`;
    });
  }
  if(showBond){
    BOND_YIELDS.forEach(b=>{
      const x=xPos(b[0]), y=yPos(b[1]);
      html += `<circle cx="${x}" cy="${y}" r="3" fill="#6C6D74"/>`;
      html += `<circle class="chart-hit" data-kind="bond" data-date="${b[0]}" data-val="${b[1]}" cx="${x}" cy="${y}" r="9" fill="transparent"/>`;
    });
  }

  svg.innerHTML = html;

  svg.querySelectorAll('.chart-hit').forEach(el=>{
    el.addEventListener('mousemove', (e)=>{
      const rect = svg.getBoundingClientRect();
      const parentRect = svg.parentElement.getBoundingClientRect();
      const kind = el.dataset.kind;
      const dateLabel = new Date(el.dataset.date).toLocaleDateString('en-CA', {year:'numeric', month:'short', day:'numeric'});
      const val = parseFloat(el.dataset.val).toFixed(2);
      let label = kind === 'boc'
        ? `BoC Overnight Rate: ${val}% <span style="opacity:.7">(${el.dataset.type})</span>`
        : `5-Yr Bond Yield: ~${val}%`;
      tooltip.innerHTML = `<div class="tt-date">${dateLabel}</div>${label}`;
      tooltip.style.opacity = '1';
      tooltip.style.left = (e.clientX - parentRect.left + 14) + 'px';
      tooltip.style.top = (e.clientY - parentRect.top - 34) + 'px';
    });
    el.addEventListener('mouseleave', ()=>{ tooltip.style.opacity = '0'; });
  });
}

document.getElementById('legend-boc').addEventListener('click', ()=>{
  showBoc = !showBoc;
  document.getElementById('legend-boc').classList.toggle('off', !showBoc);
  renderRateChart();
});
document.getElementById('legend-bond').addEventListener('click', ()=>{
  showBond = !showBond;
  document.getElementById('legend-bond').classList.toggle('off', !showBond);
  renderRateChart();
});

document.querySelectorAll('.market-tab-btn').forEach(btn=>{
  btn.addEventListener('click', ()=>{
    document.querySelectorAll('.market-tab-btn').forEach(b=>b.classList.remove('active'));
    document.querySelectorAll('.market-view').forEach(v=>v.classList.remove('active'));
    btn.classList.add('active');
    document.getElementById('view-'+btn.dataset.view).classList.add('active');
  });
});
renderMap(); renderMapDetail(); renderRateChart();

/* =====================================================================
   SHARED MORTGAGE MATH
   These three functions are used everywhere on the site that shows a
   monthly payment number (hero calculator, down payment dial, rent vs
   buy, affordability check). If you need to update CMHC premium rates
   or the "suggested" starting rate shown to visitors, this is the ONE
   place to change it - every calculator on the site will pick it up
   automatically since they all call these same functions.
===================================================================== */

/* CMHC mortgage default insurance premium, as a % of the loan amount,
   based on down payment size. These are the standard CMHC tiers as of
   this build - if CMHC changes their rate schedule, update the numbers
   below (they're percentages written as decimals, e.g. 0.031 = 3.1%). */
function cmhcRate(pct){ if(pct>=20) return 0; if(pct>=15) return 0.028; if(pct>=10) return 0.031; return 0.04; }

/* The rate shown by default before a visitor drags the rate slider
   themselves. Update these two numbers whenever current mortgage rates
   move meaningfully - this is a "suggested starting point" for the
   calculator, not a real quote, so it doesn't need to be exact to the
   decimal, just roughly current. */
function suggestedRate(pct){ return pct>=20 ? 4.14 : 3.99; }

/* Standard Canadian mortgage payment formula, using semi-annual
   compounding (that "Math.pow(1+annualRate/2, 2/12) - 1" line converts
   the annual rate into an equivalent monthly rate the Canadian way -
   Canadian mortgages compound semi-annually by law, which is different
   from how US mortgages are calculated, so don't swap in a generic
   "mortgage calculator formula" from elsewhere without checking this). */
function monthlyPayment(principal, annualRatePct, years){
  const annualRate = annualRatePct/100;
  const n = years*12;
  const i = Math.pow(1+annualRate/2, 2/12) - 1;
  return principal * (i*Math.pow(1+i,n)) / (Math.pow(1+i,n)-1);
}

/* =====================================================================
   HERO TICKER
   The big "drag the sliders" calculator right under the headline at the
   top of the page. Three sliders (price, down payment, rate) all call
   updateHero() on every drag, which recalculates and rewrites the
   numbers shown. The rate slider auto-fills a suggested value (from
   suggestedRate() above) until the visitor drags it themselves, at
   which point rateTouchedByUser flips to true and it stops auto-filling.
===================================================================== */
const hpSlider = document.getElementById('hp-slider');
const dpSlider = document.getElementById('dp-slider');
const rateSlider = document.getElementById('rate-slider');
let rateTouchedByUser = false;
rateSlider.addEventListener('input', ()=>{ rateTouchedByUser = true; document.getElementById('rate-suggested-badge').style.display='none'; updateHero(); });

function updateHero(){
  const price = parseFloat(hpSlider.value);
  const pct = parseFloat(dpSlider.value);
  if(!rateTouchedByUser){ rateSlider.value = suggestedRate(pct); }
  const rate = parseFloat(rateSlider.value);
  const down = price*pct/100;
  const base = price - down;
  const cRate = cmhcRate(pct);
  const cmhc = base*cRate;
  const total = base + cmhc;
  const m = monthlyPayment(total, rate, 25);

  document.getElementById('hp-display').textContent = fmt(price);
  document.getElementById('hp-val').textContent = fmt(price);
  document.getElementById('dp-val').textContent = pct + '% · ' + fmt(down);
  document.getElementById('rate-val').textContent = rate.toFixed(2) + '%';
  document.getElementById('hero-monthly').textContent = fmt(m) + '/mo';
  document.getElementById('hero-cmhc-note').textContent = pct>=20
    ? 'No CMHC insurance required (20%+ down) · 25-yr amortization'
    : 'Includes CMHC insurance premium (financed) · 25-yr amortization';
}
[hpSlider, dpSlider].forEach(el=>el.addEventListener('input', updateHero));
updateHero();

/* =====================================================================
   TABS (games) - switches between the three "games" panels (Down
   Payment Dial / Rent vs Buy / Affordability). Matches each tab to its
   panel via the data-panel="..." attribute on the tab in index.html,
   which must match the end of that panel's id ("panel-XXX"). If you add
   a fourth game, give its tab a new data-panel value and its panel an
   id of "panel-" + that same value, and this code will handle the rest.
===================================================================== */
document.querySelectorAll('.game-tab').forEach(tab=>{
  tab.addEventListener('click', ()=>{
    document.querySelectorAll('.game-tab').forEach(t=>t.classList.remove('active'));
    document.querySelectorAll('.game-panel').forEach(p=>p.classList.remove('active'));
    tab.classList.add('active');
    document.getElementById('panel-'+tab.dataset.panel).classList.add('active');
  });
});

/* =====================================================================
   THE DOWN PAYMENT DIAL (one of the three interactive "games")
   Same math as the Hero Ticker above (reuses cmhcRate/suggestedRate/
   monthlyPayment so it stays in sync with the rest of the site), but
   drawn as a semicircular gauge instead of plain numbers, and it pulls
   the home price from the Hero Ticker's price slider (hpSlider) rather
   than having its own - so changing the price up top also updates this.

   The gauge arc: ARC_LEN (315) is NOT the literal path length (the actual
   drawn arc path measures ~345.6 units via getTotalLength() - you can
   check this yourself in a browser console with
   document.getElementById('dial-arc').getTotalLength()). 315 is instead
   a deliberately-chosen slightly-smaller number so the gauge visually
   stops a little short of wrapping all the way around, which looks
   better than a perfect full sweep. If you redraw the arc path in
   index.html with a different shape/size, you'll likely want to
   re-measure with getTotalLength() and pick a new ARC_LEN a bit below
   that new full length, the same way this one was chosen.
   The "frac" line below assumes the down payment slider's range is
   5%-30% (i.e. (pct-5)/25 - the 25 is the span from 5 to 30). If you
   ever change the slider's min/max in index.html, update those two
   numbers here to match, or the gauge will fill incorrectly.
===================================================================== */
const dialSlider = document.getElementById('dial-slider');
const dialRateSlider = document.getElementById('dial-rate-slider');
const dialArc = document.getElementById('dial-arc');
const ARC_LEN = 315;
let dialRateTouched = false;
dialRateSlider.addEventListener('input', ()=>{ dialRateTouched = true; updateDial(); });

function updateDial(){
  const pct = parseFloat(dialSlider.value);
  const price = parseFloat(hpSlider.value);
  if(!dialRateTouched){ dialRateSlider.value = suggestedRate(pct); }
  const rate = parseFloat(dialRateSlider.value);
  const down = price*pct/100;
  const base = price - down;
  const cRate = cmhcRate(pct);
  const cmhc = base*cRate;
  const total = base + cmhc;
  const m = monthlyPayment(total, rate, 25);

  document.getElementById('dial-pct').textContent = pct + '%';
  document.getElementById('dial-rate-val').textContent = rate.toFixed(2) + '%';
  document.getElementById('dial-price').textContent = fmt(price);
  document.getElementById('dial-down').textContent = fmt(down);
  document.getElementById('dial-cmhc').textContent = cmhc>0 ? fmt(cmhc) : '$0 - not required';
  document.getElementById('dial-total').textContent = fmt(total);
  document.getElementById('dial-monthly').textContent = fmt(m) + '/mo';
  document.getElementById('dial-required').textContent = pct>=20 ? 'No - 20%+ down' : 'Yes - under 20% down';

  // (pct-5)/25 assumes the slider's range is 5 to 30 - see note above
  const frac = Math.min(1, Math.max(0,(pct-5)/25));
  dialArc.setAttribute('stroke-dasharray', (frac*ARC_LEN) + ' 600');
}
dialSlider.addEventListener('input', updateDial);
hpSlider.addEventListener('input', updateDial);
updateDial();

/* =====================================================================
   RENT VS BUY (second of the three interactive "games")
   Compares the running total cost of renting vs. buying over a chosen
   number of years. Two growth assumptions are baked directly into the
   math below rather than pulled from named constants - both currently
   hardcoded as 1.03 (3% per year):
     - line with "r *= 1.03"          -> annual rent increase assumption
     - line with "Math.pow(1.03,years)" -> annual home appreciation assumption
   If you want to change either assumption, you have to edit the 1.03
   directly at each of those two spots (they're intentionally separate
   in case rent growth and home appreciation ever need different rates -
   right now they happen to both be 3%, which is a coincidence of the
   current assumptions, not a rule). This is a simplified illustrative
   comparison, not a real investment projection - the on-page copy
   already says as much to visitors.
===================================================================== */
const rvbRent = document.getElementById('rvb-rent');
const rvbPrice = document.getElementById('rvb-price');
const rvbYears = document.getElementById('rvb-years');
const rvbRate = document.getElementById('rvb-rate');
function updateRVB(){
  const rent0 = parseFloat(rvbRent.value);
  const price = parseFloat(rvbPrice.value);
  const years = parseFloat(rvbYears.value);
  const rate = parseFloat(rvbRate.value);

  document.getElementById('rvb-rent-val').textContent = fmt(rent0)+'/mo';
  document.getElementById('rvb-price-val').textContent = fmt(price);
  document.getElementById('rvb-years-val').textContent = years + ' years';
  document.getElementById('rvb-rate-val').textContent = rate.toFixed(2) + '%';

  let totalRent = 0; let r = rent0;
  for(let y=0;y<years;y++){ totalRent += r*12; r *= 1.03; } // 1.03 = assumed 3%/yr rent growth

  const down = price*0.20; // assumes 20% down (no CMHC) for this comparison specifically
  const mtg = price - down;
  const m = monthlyPayment(mtg, rate, 25); // 25 = years, i.e. a 25-year amortization
  const i = Math.pow(1+(rate/100)/2,2/12)-1;
  let bal = mtg; let principalPaid = 0;
  const totalMonths = Math.min(years*12, 25*12); // caps at 25 years even if the slider asks for more
  for(let mo=0; mo<totalMonths; mo++){ const interest=bal*i; const princ=m-interest; bal-=princ; principalPaid+=princ; }
  const appreciation = price*(Math.pow(1.03,years)-1); // 1.03 = assumed 3%/yr home appreciation
  const equity = down + principalPaid + appreciation;

  document.getElementById('rvb-buy-val').textContent = fmt(equity);
  document.getElementById('rvb-rent-total').textContent = fmt(totalRent);
  const maxV = Math.max(equity, totalRent, 1);
  document.getElementById('rvb-buy-bar').style.height = Math.max(6,(equity/maxV*100)) + '%';
  document.getElementById('rvb-rent-bar').style.height = Math.max(6,(totalRent/maxV*100)) + '%';
  const diff = equity - totalRent;
  document.getElementById('rvb-summary').textContent = diff>=0
    ? `Buying builds ~${fmt(diff)} more in equity than the rent paid over ${years} years (before costs like maintenance & closing).`
    : `Over ${years} years, rent paid is ~${fmt(-diff)} more than the equity built - factor in flexibility & maintenance savings too.`;
}
[rvbRent, rvbPrice, rvbYears, rvbRate].forEach(el=>el.addEventListener('input', updateRVB));
updateRVB();

/* =====================================================================
   AFFORDABILITY (third of the three interactive "games")
   Estimates a rough maximum home price based on income and existing
   debt, using the two debt-service ratios Canadian lenders commonly use
   to qualify borrowers:
     - GDS (Gross Debt Service): housing costs shouldn't exceed 39% of
       gross monthly income (the 0.39 below)
     - TDS (Total Debt Service): housing costs PLUS all other debt
       payments shouldn't exceed 44% of gross monthly income (the 0.44
       below, minus whatever debt the visitor entered)
   The lower of the two limits wins (maxHousing = the smaller number),
   same as how lenders actually calculate it. These 39%/44% figures are
   the commonly-cited conventional lending benchmarks - if guidelines
   change, or if you want to show insured-mortgage limits instead
   (which can differ), update the 0.39 and 0.44 here.

   This is a simplified pre-qualification gut-check, not an actual
   approval calculation - real lenders also weigh credit score, income
   type/stability, property type, and their own specific policies.
===================================================================== */
const afIncome = document.getElementById('af-income');
const afDebt = document.getElementById('af-debt');
const afDown = document.getElementById('af-down');
const afRate = document.getElementById('af-rate');
function updateAfford(){
  const income = parseFloat(afIncome.value);
  const debt = parseFloat(afDebt.value);
  const down = parseFloat(afDown.value);
  const qualifyRate = parseFloat(afRate.value);

  document.getElementById('af-income-val').textContent = fmt(income)+'/yr';
  document.getElementById('af-debt-val').textContent = fmt(debt)+'/mo';
  document.getElementById('af-down-val').textContent = fmt(down);
  document.getElementById('af-rate-val').textContent = qualifyRate.toFixed(2) + '%';

  const monthlyIncome = income/12;
  const maxGDS = monthlyIncome*0.39;
  const maxTDS = monthlyIncome*0.44 - debt;
  const maxHousing = Math.max(0, Math.min(maxGDS, maxTDS));

  const n = 25*12;
  const i = Math.pow(1+(qualifyRate/100)/2,2/12)-1;
  const maxMortgage = maxHousing * (Math.pow(1+i,n)-1) / (i*Math.pow(1+i,n));
  const maxPrice = maxMortgage + down;

  document.getElementById('af-max-housing').textContent = fmt(maxHousing)+'/mo';
  document.getElementById('af-max-mortgage').textContent = fmt(maxMortgage);
  document.getElementById('af-max-price').textContent = fmt(maxPrice);
  document.getElementById('af-meter').style.width = Math.min(100, (maxPrice/1500000)*100) + '%';
}
[afIncome, afDebt, afDown, afRate].forEach(el=>el.addEventListener('input', updateAfford));
updateAfford();

/* =====================================================================
   DOCUMENT CHECKLIST - rendering logic. The actual list of scenarios and
   required documents lives in DOC_SCENARIOS near the top of this file
   (search for "DOC_SCENARIOS" if you want to add/edit a scenario or
   document - that's the only place you need to touch for that).
   Everything below just draws tabs from its keys, draws a checklist from
   the active tab's array, and tracks which boxes are checked per-tab in
   checkedState so switching tabs and back doesn't lose your progress.
===================================================================== */
const docTabsEl = document.getElementById('doc-tabs');
const docListEl = document.getElementById('doc-list');
const checkedState = {};
let currentScenario = Object.keys(DOC_SCENARIOS)[0];

function renderDocTabs(){
  docTabsEl.innerHTML = '';
  Object.keys(DOC_SCENARIOS).forEach(name=>{
    const tab = document.createElement('div');
    tab.className = 'doc-tab' + (name===currentScenario ? ' active' : '');
    tab.textContent = name;
    tab.onclick = ()=>{ currentScenario = name; renderDocTabs(); renderDocList(); };
    docTabsEl.appendChild(tab);
  });
}
function renderDocList(){
  docListEl.innerHTML = '';
  const items = DOC_SCENARIOS[currentScenario];
  if(!checkedState[currentScenario]) checkedState[currentScenario] = new Array(items.length).fill(false);
  items.forEach((text, idx)=>{
    const row = document.createElement('div');
    row.className = 'doc-item' + (checkedState[currentScenario][idx] ? ' checked' : '');
    row.innerHTML = `<div class="doc-check">${checkedState[currentScenario][idx] ? '&#10003;' : ''}</div><div class="doc-text">${text}</div>`;
    row.onclick = ()=>{ checkedState[currentScenario][idx] = !checkedState[currentScenario][idx]; renderDocList(); };
    docListEl.appendChild(row);
  });
  const doneCount = checkedState[currentScenario].filter(Boolean).length;
  const countEl = document.getElementById('doc-count');
  countEl.textContent = `${doneCount} / ${items.length} ready`;
  countEl.classList.toggle('complete', doneCount === items.length);
  document.getElementById('doc-meter').style.width = (doneCount/items.length*100) + '%';
}
renderDocTabs(); renderDocList();

/* ===================== CASE STUDIES (Mortgage Diaries) =====================
   Shows CASES_PER_PAGE cards at a time with numbered page buttons underneath,
   instead of dumping every case study on screen at once. To change how many
   show per page, just edit CASES_PER_PAGE below - everything else (page
   count, button rendering, which cases show) recalculates on its own. */
const caseGrid = document.getElementById('case-grid');
const casePagination = document.getElementById('case-pagination');
const CASES_PER_PAGE = 4;
let currentCasePage = 1;

function renderCases(){
  const totalPages = Math.ceil(CASE_STUDIES.length / CASES_PER_PAGE);
  const startIdx = (currentCasePage - 1) * CASES_PER_PAGE;
  const pageItems = CASE_STUDIES.slice(startIdx, startIdx + CASES_PER_PAGE);

  caseGrid.innerHTML = '';
  pageItems.forEach((c, i)=>{
    const idx = startIdx + i; // real index into CASE_STUDIES, for the modal lookup
    const card = document.createElement('div');
    card.className = 'case-card';
    const statsHtml = c.stats.map(s=>`<div><strong>${s[1]}</strong>${s[0]}</div>`).join('');
    card.innerHTML = `<div class="tag">${c.tag}</div><h3>${c.title}</h3><p>${c.preview}</p><div class="stat-preview">${statsHtml}</div>`;
    card.onclick = ()=>openCaseModal(idx);
    caseGrid.appendChild(card);
  });

  // build the numbered page buttons (1, 2, 3...) below the grid
  casePagination.innerHTML = '';
  if(totalPages > 1){
    for(let p=1; p<=totalPages; p++){
      const btn = document.createElement('button');
      btn.className = 'case-page-btn' + (p===currentCasePage ? ' active' : '');
      btn.textContent = p;
      btn.setAttribute('aria-label', 'Show page ' + p + ' of mortgage diaries');
      btn.onclick = ()=>{ currentCasePage = p; renderCases(); document.getElementById('case-grid').scrollIntoView({behavior:'smooth', block:'start'}); };
      casePagination.appendChild(btn);
    }
  }
}
function openCaseModal(idx){
  const c = CASE_STUDIES[idx];
  document.getElementById('modal-tag').textContent = c.tag;
  document.getElementById('modal-title').textContent = c.title;
  document.getElementById('modal-meta').textContent = 'Case Study';
  const statsHtml = `<div class="case-stats">${c.stats.map(s=>`<div><strong>${s[1]}</strong>${s[0]}</div>`).join('')}</div>`;
  document.getElementById('modal-content').innerHTML = statsHtml + c.content.map(p=>`<p>${p}</p>`).join('');
  document.getElementById('modal-overlay').classList.add('active');
}
renderCases();

/* =====================================================================
   BLOG - rendering logic. The actual posts live in BLOG_POSTS at the
   very top of this file (search "BLOG_POSTS" to add/edit a post) - this
   section just draws a card for each one and wires up the click-to-open
   modal. Unlike the paginated Mortgage Diaries section, this one shows
   every post at once in a horizontal scroller (see .blog-grid /
   .blog-scroll-btn in style.css) rather than paging - if you'd rather
   paginate the blog the same way the case studies are paginated, you
   could copy the renderCases() pattern above and adapt it here.
===================================================================== */
const blogGrid = document.getElementById('blog-grid');
function renderBlog(){
  blogGrid.innerHTML = '';
  BLOG_POSTS.forEach((post, idx)=>{
    const card = document.createElement('div');
    card.className = 'blog-card';
    card.innerHTML = `<div class="tag">${post.tag}</div><h3>${post.title}</h3><p>${post.excerpt}</p><div class="meta">${post.date}</div>`;
    card.onclick = ()=>openBlogModal(idx);
    blogGrid.appendChild(card);
  });
}
function openBlogModal(idx){
  const post = BLOG_POSTS[idx];
  document.getElementById('modal-tag').textContent = post.tag;
  document.getElementById('modal-title').textContent = post.title;
  document.getElementById('modal-meta').textContent = post.date;
  document.getElementById('modal-content').innerHTML = post.content.map(p=>`<p>${p}</p>`).join('');
  document.getElementById('modal-overlay').classList.add('active');
}
function closeModal(){ document.getElementById('modal-overlay').classList.remove('active'); }
document.getElementById('modal-overlay').addEventListener('click', (e)=>{ if(e.target.id==='modal-overlay') closeModal(); });
renderBlog();