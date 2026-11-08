"""JM Electrical Solutions proposal, agreement and phone/computer view.

Edit this file, then run `python3 tools/build_proposal.py` from the repo root. It writes site/proposal/index.html,
site/agreement/index.html and site/preview/index.html. Copied from the PH Electric proposal (jobisgreat/phelectrical,
branch claude/ph-proposal, 28 Oct 2026), itself from Century Glass and Tint Me. JM facts from Tim's brief (28 Oct 2026),
jmelectricsolutions.com (checked 29 Oct 2026) and Tim. Never add a fact here that Tim or Jamie has not confirmed.
"""
import html
import os
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "site"

# ---- Fill these in before the proposal goes to Jamie. None shows a yellow "to confirm" mark. ----
SITE = os.environ.get("JM_SITE", "")  # the site is served from this same project, so links stay relative
PROPOSAL_HOST = "project-q2oxb.vercel.app"  # this project's Vercel address (Vercel project "jmelectrical")
DEPOSIT_LINK = None   # Stripe payment link for the $1,750 deposit (from Tim)
LEGAL_NAME = None     # exact legal entity on the Order Form (from Tim), e.g. "JM Electrical Solutions, LLC"
SIGNER = None         # signer's full name and title (from Tim)
LAUNCH = None         # launch promise (from Tim), e.g. "Within 14 days of receiving your deposit"
FORGE_LINE = None     # Forge's one-line promise for the top of the page (from Tim)
DOMAIN = "jmelectricsolutions.com"  # Jamie's current site (GoDaddy Website Builder), also on the vans
EMAIL_JM = "jmelectricsolutions@gmail.com"  # from the van lettering (Tim's photo, 28 Oct 2026)
PHONE_JM = "(978) 746-1993"
VERSION = "v1 · 21 Oct 2026"  # Tim's attorney-reviewed agreement text; must match api/sign.mjs

BUILD = 3500
DEPOSIT = BUILD // 2
MONTHLY = 150
PHONE_AIR = "(617) 499-0149"
CHECKED = "29 Oct 2026"
# Which photos are AI-made (skill rule: name them exactly). Tim to confirm the Jamie photo.
AI_NOTE = "The photo of your building and vans at the top of the page is AI-made, a stand-in until we have your own photo."

# One page list (skill: site standard 6). Name, address on the site. Order matches the site's sitemap.
SITE_PAGES = [
    ("Home", "/"),
    ("Services", "/services.html"),
    ("Panel Upgrades", "/panel-upgrades.html"),
    ("EV Charger Installation", "/ev-chargers.html"),
    ("Lighting & Ceiling Fans", "/lighting-ceiling-fans.html"),
    ("Home Rewiring", "/rewiring.html"),
    ("Generators", "/generators.html"),
    ("Smart Home Automation", "/smart-home.html"),
    ("Outlets & Switches", "/outlets-switches.html"),
    ("Emergency Electrical Service", "/emergency-electrician.html"),
    ("Reviews", "/reviews.html"),
    ("About", "/about.html"),
    ("Service Areas", "/service-areas.html"),
    ("Contact", "/contact.html"),
    ("Thank-you page", "/thank-you.html"),
]
PAGES = [n for n, _ in SITE_PAGES]
PAGE_LIST = f"{len(PAGES)} pages: " + ", ".join(PAGES[:-1]) + " and a " + PAGES[-1][0].lower() + PAGES[-1][1:] + " after the quote form"

# Word for word on the proposal (twice) and the agreement. Change it here only.
# JM has no Projects page, so the template's "new projects" line became new reviews (29 Oct 2026).
MONTHLY_SCOPE = [
    "Hosting, plus security and uptime monitoring, with fixes when something changes.",
    "Small text or photo changes, up to about an hour a month.",
    "New customer reviews added to your Reviews page when you send them.",
    "A check every month that your quote form still reaches you.",
    "Keyword updates every month: we check what customers search for and what changed in Google's latest updates, then adjust your page titles, descriptions and wording to match.",
]

# Tim's wording style for the chart section's "kept current" column (PH Electric, 28 Oct 2026). Same promises as MONTHLY_SCOPE.
CHART_KEPT = [
    "Hosting, security, and uptime monitoring. Fixes when something breaks.",
    "Small text or photo changes (about an hour a month).",
    "New customer reviews added to the Reviews page when you send them.",
    "A monthly check that the quote form still reaches you.",
    "Keyword and wording updates every month. AI scans never stop, so we check what customers are searching for and adjust titles, descriptions, and copy to match.",
]

BUILD_SCOPE = [
    f"Your new website, built from the working preview, with every fix in the table above: {PAGE_LIST}.",
    "Each of your eight services on its own page named with Dorchester and Boston: the signs to look for, what the work involves, a typical timeline, what to expect and common questions.",
    "Your real customer reviews on the home page and on a Reviews page.",
    "An About page with your photo, and a Service Areas page for Dorchester, South Boston and nearby neighborhoods.",
    f"{PHONE_JM} as a tap-to-call link on every page, plus a call bar that stays on screen on phones.",
    "Your logo, your Massachusetts license number (#22667) and 749 Dorchester Ave on every page.",
    "Search setup: a title and description on every page, and business and service details written in code Google reads.",
    "Your quote form connected, so every request reaches your inbox.",
    "Every fact on the site confirmed by you. Anything we could not confirm is marked on the preview and stays off the live site until you confirm it.",
    "jmelectricsolutions.com moved off GoDaddy Website Builder onto the new site, with your email left as it is, and Google allowed to list the site from launch day.",
    "Your Google Business Profile checked and cleaned up.",
    "Two rounds of revisions before launch, plus 30 days of fixes after launch.",
]

# Short version of BUILD_SCOPE for the price box at the top. Keep it in step with BUILD_SCOPE.
PRICE_BUILD = [
    f"The {len(PAGES)}-page website, built from the working preview.",
    "A page for each of your eight services, named with Dorchester and Boston.",
    "Your real customer reviews on the home page and a Reviews page.",
    f"Tap-to-call {PHONE_JM} on every page, plus a call bar on phones.",
    "Your license number and street address on every page.",
    "Search setup on every page, and your Google Business Profile cleaned up.",
    "Your quote form connected to your inbox.",
    "jmelectricsolutions.com moved onto the new site, with your email left as it is.",
    "Two rounds of revisions before launch, plus 30 days of fixes after launch.",
]

# Gaps: checked on jmelectricsolutions.com, 29 Oct 2026. Do not add a row that wasn't checked.
GAPS = [
    ("Only two pages",
     "The menu has Home and Photo Gallery, and a “More” menu that repeats the same two links. None of your services has its own page.",
     "Fifteen pages, including a page for each of your eight services, each named with Dorchester and Boston, so the page someone lands on matches what they searched for."),
    ("Almost no services named",
     "The home page names two jobs: “a small wiring fix” and smart home automation. Panel upgrades, EV chargers, lighting, rewiring and generators are not mentioned.",
     "A Services page and eight service pages: panel upgrades, EV chargers, lighting and ceiling fans, rewiring, generators, smart home, outlets and switches, and emergency service."),
    ("Your 4.9 stars don't show",
     "There are no reviews or star ratings anywhere on the site, though your Google listing shows a 4.9-star rating.",
     "Your real customer reviews on the home page and a Reviews page, with your Google rating at the top."),
    ("No license number or street address",
     "No Massachusetts license number appears on the site, and the address is only “Boston, MA”. No neighborhood, Dorchester or South Boston, is named.",
     "License #22667 and 749 Dorchester Ave on every page, and a Service Areas page that names the neighborhoods you work in."),
    ("Google gets little to go on",
     "The home page title is “Expert Electrician Services for Your Home”, with no business name and no city.",
     "A title and description written for every page with your name, the service and the area, plus business and service details in code Google reads."),
    ("The quote form asks for an email, not a phone number",
     "The Get a Quote form makes email required and leaves the phone number optional.",
     "A three-field quote form that asks for a name, a phone number and the job, so you can call people back."),
    ("The footer says 2018",
     "The copyright line reads “© 2018”, and the site runs on GoDaddy Website Builder. It tells a customer the site has not been touched in years.",
     "A current site, kept up every month on your monthly plan."),
]

SOURCES = [
    ("Electrician site, 10 pages, residential and commercial, freelancer", "$2,800–$5,500",
     "https://projectcostestimator.com/blog/electrician-website-cost-2026", "ProjectCostEstimator, electrician sites, June 2026"),
    ("Electrician site, US freelancer median", "$3,500",
     "https://projectcostestimator.com/cost/industry/electrician", "ProjectCostEstimator, electrician sites, July 2026"),
    ("Electrician site, US agency", "$5,800–$18,850",
     "https://projectcostestimator.com/cost/industry/electrician", "ProjectCostEstimator, electrician sites, July 2026"),
    ("Running an electrician site: hosting, tools and maintenance", "$30–$150 a month",
     "https://projectcostestimator.com/cost/industry/electrician", "ProjectCostEstimator, electrician sites, July 2026"),
]

NEEDS = [
    "Answers to the yellow “Confirm” items on the preview: your hours, financing (lender and terms), insurance details, typical timelines for each service, the neighborhoods you cover and whether you offer emergency service. Nothing goes live until you confirm it.",
    "Your own photos (you, your team, the vans and finished jobs), so we can replace the AI-made photo at the top of the page.",
    "First names for the reviews you're happy to show, or a yes to keep them unnamed.",
    "Your original logo file (SVG, PDF or AI), so it is sharp on every screen.",
    "The email address your quote form should go to.",
    "A login for jmelectricsolutions.com on GoDaddy (or the name of whoever manages it), so we can point it at the new site without touching your email.",
    "Add AI Rocket (tim@airocket.pro) as a manager on your Google listing, so we can clean it up and measure your before-and-after numbers.",
]


def money(n):
    return f"${n:,}"


def ph(text):
    """Visible mark for anything Tim still has to fill in."""
    return f'<mark class="ph">[To confirm: {html.escape(text)}]</mark>'


def val(v, label):
    return html.escape(v) if v else ph(label)


def ul(items, mark=""):
    return "\n".join(f"            <li>{mark}{html.escape(i)}</li>" for i in items)


FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Roboto+Slab:wght@800;900&family=Archivo:wght@400;500;600;700&display=swap" rel="stylesheet">'

# ---------------------------------------------------------------- proposal
PROPOSAL_CSS = """
:root {
  --ink: #0a0f22; --onink: #f2f5f7; --accent: #b5893a; --accent-lt: #d6ad62; --gold: #b5893a; --red: #a3262c;
  --bg: #0f1630; --alt: #131b39; --surface: #18224a; --fg: #eef2f8; --muted: #b9c4d6; --line: #2a3563;
  --display: "Roboto Slab", Georgia, serif; --body: "Archivo", system-ui, -apple-system, "Segoe UI", sans-serif;
  --gutter: clamp(16px, 4vw, 48px);
}
*, *::before, *::after { box-sizing: border-box; }
html { -webkit-text-size-adjust: 100%; scroll-behavior: smooth; }
body { margin: 0; background: var(--bg); color: var(--fg); font-family: var(--body); font-size: 17px; line-height: 1.55; }
a { color: inherit; }
img { display: block; max-width: 100%; }
h1, h2, .display { font-family: var(--display); font-weight: 900; text-transform: uppercase; line-height: 1.02; letter-spacing: 0; margin: 0; }
.wrap { max-width: 1152px; margin: 0 auto; padding: 0 var(--gutter); }
.ph { background: #ffe14d; color: #1a1400; padding: 0 4px; font-style: normal; overflow-wrap: anywhere; }
.topnav { display: flex; justify-content: space-between; align-items: center; gap: 12px; background: var(--ink); color: var(--onink); padding: 0 var(--gutter); min-height: 52px; border-bottom: 1px solid rgba(242,245,247,.15); }
.topnav span { font-weight: 600; font-size: 15px; color: rgba(242,245,247,.75); }
.topnav .navlinks { display: flex; flex-wrap: wrap; justify-content: flex-end; column-gap: 20px; }
@media (max-width: 480px) { .topnav > span:first-child { display: none; } .topnav { justify-content: center; } .topnav .navlinks { justify-content: center; } }
.topnav a { font-weight: 600; font-size: 16px; color: var(--accent-lt); text-decoration: underline; text-underline-offset: 4px; min-height: 44px; display: inline-flex; align-items: center; }
.banner { background: #ffe14d; color: #1a1400; text-align: center; font-size: 14px; padding: 8px var(--gutter); }
header { background: var(--ink); color: var(--onink); border-bottom: 3px solid var(--accent); box-shadow: 0 3px 0 var(--red); padding: 40px 0 36px; }
.eyebrow { font-size: 13px; text-transform: uppercase; letter-spacing: .14em; color: var(--accent); margin: 0 0 10px; font-weight: 700; }
header .eyebrow { color: var(--accent-lt); }
header .forge { font-size: 19px; font-weight: 600; margin: 0 0 10px; max-width: 46rem; }
header .tagline { font-family: var(--display); font-weight: 800; font-size: clamp(20px, 2.4vw, 28px); line-height: 1.2; color: var(--accent-lt); margin: 0 0 14px; max-width: 32ch; }
header img.shoplogo { width: min(560px, 100%); height: auto; margin: 0 0 26px; }
header h1 { font-size: clamp(36px, 5vw, 64px); max-width: 20ch; }
header .sub { margin: 16px 0 0; max-width: 44rem; font-size: 19px; color: rgba(242,245,247,.82); }
.shot { margin: 28px 0 0; max-width: 56rem; }
.shot .frame { background: #1b2550; padding: 26px 8px 8px; position: relative; box-shadow: 0 24px 50px rgba(0,0,0,.45); }
.shot .frame::before { content: ""; position: absolute; left: 12px; top: 9px; width: 9px; height: 9px; border-radius: 50%; background: #e06c5f; box-shadow: 15px 0 0 #e3b341, 30px 0 0 #58b368; }
.shot img { width: 100%; height: auto; }
.shot figcaption { margin-top: 10px; font-size: 14px; color: rgba(242,245,247,.65); }
.btns { display: flex; flex-wrap: wrap; gap: 12px; margin-top: 26px; }
.btn { display: inline-flex; align-items: center; justify-content: center; min-height: 48px; padding: 8px 22px; font-weight: 700; font-size: 17px; text-decoration: none; text-align: center; border-radius: 0; }
.btn.main { background: var(--accent); color: #0f1630; }
.btn.outline { border: 1px solid currentColor; }
.btn:hover { opacity: .9; } .btn.main:hover { background: #c4994a; opacity: 1; }
.findings { background: var(--ink); color: var(--onink); padding: 36px 0 56px; }
.findings h2 { font-size: clamp(30px, 4.5vw, 50px); }
table { width: 100%; border-collapse: collapse; margin-top: 22px; text-align: left; }
th { font-family: var(--display); font-weight: 800; text-transform: uppercase; font-size: 19px; padding: 10px 14px 10px 0; border-bottom: 2px solid var(--accent); }
td { padding: 14px 14px 14px 0; border-bottom: 1px solid rgba(242,245,247,.18); vertical-align: top; }
td.t { font-weight: 700; width: 24%; }
td.p { color: rgba(242,245,247,.74); width: 38%; }
.num { color: var(--accent-lt); font-weight: 700; }
.x { color: #f08a7e; font-weight: 700; margin-right: 8px; }
.ok { color: var(--accent-lt); font-weight: 700; margin-right: 8px; }
.cards { list-style: none; margin: 22px 0 0; padding: 0; display: none; }
.cards li { border: 1px solid rgba(242,245,247,.2); padding: 16px; margin-bottom: 12px; }
.cards p { margin: 0 0 8px; } .cards .p { color: rgba(242,245,247,.74); } .cards .t { font-weight: 700; }
.note { font-size: 14px; color: rgba(242,245,247,.6); margin-top: 16px; }
dl.summary { display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px; margin: 34px 0 0; }
dl.summary div { border-left: 4px solid var(--accent); background: rgba(242,245,247,.06); padding: 14px; }
dl.summary dt { font-size: 12px; text-transform: uppercase; letter-spacing: .14em; color: var(--accent-lt); font-weight: 700; }
dl.summary dd { margin: 4px 0 0; font-size: 17px; }
dl.summary div.pricecell { grid-column: 1 / -1; order: 1; }
dl.summary .pcols, dl.summary .pcols > div { border: 0; background: none; padding: 0; }
dl.summary .pcols { display: grid; grid-template-columns: 1fr 1fr; gap: 8px 28px; }
dl.summary .pcols p { margin: 6px 0; }
dl.summary .pcols ul { margin: 4px 0 8px; padding-left: 20px; font-size: 16px; }
dl.summary .pcols li { margin: 3px 0; }
section[data-slide] { padding: 64px 0; border-bottom: 1px solid var(--line); scroll-margin-top: 16px; }
section.alt { background: var(--alt); }
section[data-slide] h2 { font-size: clamp(32px, 5vw, 52px); max-width: 22ch; }
.lead { font-size: 19px; color: var(--muted); max-width: 46rem; margin: 18px 0 0; }
.grid3 { display: grid; grid-template-columns: repeat(3, 1fr); gap: 14px; list-style: none; padding: 0; margin: 24px 0 0; }
.grid3 li { background: var(--surface); border: 1px solid var(--line); border-top: 3px solid var(--accent); padding: 18px; }
.q { font-family: var(--display); font-weight: 800; font-size: 22px; margin: 0 0 6px; line-height: 1.15; }
.muted { color: var(--muted); margin: 0; }
.small { font-size: 14px; color: var(--muted); }
.pages { display: flex; flex-wrap: wrap; gap: 8px; list-style: none; padding: 0; margin: 22px 0 0; max-width: 56rem; }
.pages a { display: inline-flex; align-items: center; min-height: 44px; padding: 6px 14px; border: 1px solid var(--line); background: var(--surface); text-decoration: none; font-weight: 600; }
.pages a:hover { border-color: var(--accent); color: var(--accent-lt); }
.two { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-top: 24px; }
.box { background: var(--surface); border: 1px solid var(--line); border-top: 4px solid var(--accent); padding: 22px; }
.box h3 { font-family: var(--display); font-weight: 800; text-transform: uppercase; font-size: 23px; margin: 0 0 8px; }
.box ul { margin: 0; padding-left: 20px; } .box li { margin-bottom: 6px; }
#proposal { background: var(--alt); }
.price { font-family: var(--display); font-weight: 900; font-size: 46px; color: var(--accent-lt); line-height: 1; margin: 0; }
.price + p { font-family: var(--display); font-weight: 800; font-size: 23px; text-transform: uppercase; margin: 2px 0 0; }
.compare ul { list-style: none; padding: 0; margin: 8px 0 0; font-size: 15px; }
.compare li { display: flex; flex-wrap: wrap; justify-content: space-between; gap: 4px 12px; padding: 4px 0; border-bottom: 1px solid var(--line); }
.compare a { color: var(--muted); }
dl.terms div { padding: 8px 0; border-bottom: 1px solid var(--line); }
dl.terms dt { font-weight: 700; } dl.terms dd { margin: 2px 0 0; color: var(--muted); }
.dark { background: var(--ink); color: var(--onink); border-top-color: var(--gold); }
.dark ul { padding: 0; } .dark li { list-style: none; }
/* Funnel headline and steps (Tim's wording, 23 Oct 2026) */
.funnel { margin-top: 8px; background: var(--ink); border-top: 4px solid var(--gold); padding: 22px 20px; }
.funnel h2 { color: var(--accent-lt); font-family: var(--display); font-weight: 800; text-transform: none; font-size: clamp(26px, 3.4vw, 38px); line-height: 1.15; max-width: 30ch; }
.syshead { font-family: var(--display); font-weight: 800; font-size: 22px; margin: 28px 0 0; }
.sys { display: grid; grid-template-columns: repeat(3, 1fr); gap: 14px; margin: 14px 0 0; padding: 0; list-style: none; }
.sys li { border-left: 6px solid var(--gold); background: var(--surface); padding: 14px 16px; }
.sys b { display: block; font-family: var(--display); font-size: 21px; text-transform: uppercase; }
.keep { margin: 22px 0 0; max-width: 46rem; } .keep p { margin: 0; font-weight: 700; }
.keep ul { margin: 6px 0 0; padding-left: 20px; } .keep li { margin: 4px 0; }
.proof { margin: 16px 0 0; max-width: 46rem; }
.seochart{margin-top:28px;background:var(--ink);color:var(--onink);border-top:4px solid var(--gold);padding:16px;}
.seohead{display:flex;flex-wrap:wrap;justify-content:space-between;align-items:baseline;gap:8px 16px}
.seotitle{font-family:var(--display);font-weight:800;font-size:23px;color:#f0b13c;margin:0}
.seokey{list-style:none;padding:0;margin:0;display:flex;flex-wrap:wrap;gap:6px 16px;font-size:14px}
.seokey li{display:flex;align-items:center;gap:8px}
.seokey i{display:inline-block;width:24px} .seokey .k1{height:5px;background:#f0b13c;border-radius:3px} .seokey .k2{border-top:3px dashed #93a8b8} .seokey .k3{width:10px;height:10px;background:#f0b13c;transform:rotate(45deg);margin:0 7px}
.seoplot .beam text{font-weight:600;font-size:11px;fill:#f0b13c}
.seoplot{position:relative;margin-top:14px;padding-left:40px}
.seoplot svg{width:100%;height:auto;display:block}
.seoplot .grid{stroke:currentColor;stroke-opacity:.12} .seoplot .axis{stroke:currentColor;stroke-opacity:.4}
.seoplot .lineA{fill:none;stroke:#93a8b8;stroke-width:3;stroke-dasharray:9 7;stroke-linejoin:round}
.seoplot .lineB{fill:none;stroke:#f0b13c;stroke-width:5;stroke-linejoin:round;stroke-linecap:round}
.seoplot .dotA{fill:#93a8b8;stroke:var(--ink);stroke-width:2} .seoplot .dotB{fill:#f0b13c;stroke:var(--ink);stroke-width:2}
.seoplot .pulse{fill:none;stroke:#f0b13c;stroke-width:2;transform-box:fill-box;transform-origin:center;animation:seoPulse 1.8s ease-out infinite}
@keyframes seoPulse{0%{transform:scale(1);opacity:.9}100%{transform:scale(2.6);opacity:0}}
.seoplot .endl{transition:opacity .6s;font-weight:600;font-size:12px;fill:#f2f5f7} .seoplot .endl.b{fill:#f0b13c} .seoplot .endl.a{fill:#c4d0d8}
.seoplot .upd line{stroke:#f2f5f7;stroke-opacity:.35;stroke-dasharray:3 5} .seoplot .upd text{font-weight:500;font-size:10px;fill:#f2f5f7;fill-opacity:.8}
.seoplot .upd path{fill:#f0b13c} .seoplot .upd{transition:opacity .4s}
.seoplot .br{stroke:#f0b13c;stroke-width:2} .seoplot .gapt{font-weight:700;font-size:12px;fill:#f0b13c}
@media(max-width:640px){.seoplot .endl{font-size:17px} .seoplot #seoLB0{transform:translateY(-16px)} .seoplot .upd text{display:none} .xlabs .mid{display:none} .seoplot{padding-left:0} .ylab{display:none}}
.seoplot .mo{font:600 30px var(--display);fill:#f2f5f7;fill-opacity:.16}
.replay{margin-left:auto;background:transparent;border:1px solid rgba(242,245,247,.35);color:#f2f5f7;border-radius:0;padding:4px 12px;font-weight:500;font-size:13px;cursor:pointer}
.replay:hover{background:rgba(255,255,255,.08)}
@media(max-width:640px){.seoplot .beam text{display:none} .seoplot .mo{font-size:44px}}
.seoplot .xhair{stroke:#f2f5f7;stroke-opacity:.5;stroke-width:1}
.seoplot svg{cursor:crosshair;touch-action:pan-y}
@media (prefers-reduced-motion:reduce){.seoplot .pulse{animation:none;opacity:0}}
.ylab{position:absolute;left:0;font-size:13px;color:rgba(242,245,247,.7)} .ylab.top{top:0} .ylab.bot{bottom:44px}
.xlabs{position:relative;height:22px;font-size:13px;color:rgba(242,245,247,.7)} .xlabs span{position:absolute;top:2px;white-space:nowrap}
.seocap{margin:2px 0 0;font-size:13px;color:rgba(242,245,247,.55)}
.seonow{display:grid;gap:10px;margin-top:12px} @media(min-width:640px){.seonow{grid-template-columns:1fr 1fr}}
.seonow p{margin:0;padding:10px 12px;background:rgba(255,255,255,.05);border-left:4px solid var(--gold);font-size:15px;color:var(--onink)} .seonow p.a{border-left-color:rgba(242,245,247,.4)}
.seonow p.b b{color:#f0b13c}
.noguar{margin:14px 0 0;font-size:15px;font-weight:600;line-height:1.5}
.seonote{margin:14px 0 0;font-size:15px;line-height:1.5;color:#f2f5f7} @media(min-width:1160px){.seonote{font-size:14px}}
.ghead { font-family: var(--display); font-weight: 900; text-transform: uppercase; font-size: clamp(26px, 3.6vw, 40px); line-height: 1.1; margin: 48px 0 0; max-width: 24ch; }
.gstats { display: grid; grid-template-columns: repeat(3, 1fr); gap: 14px; list-style: none; padding: 0; margin: 20px 0 0; }
.gstats li { background: var(--ink); border-top: 4px solid var(--gold); padding: 18px; }
.gstats b { display: block; font-family: var(--display); font-weight: 900; font-size: clamp(34px, 4vw, 48px); line-height: 1; color: var(--accent-lt); }
.gstats span { display: block; margin-top: 8px; font-size: 16px; }
.gstats a { display: inline-block; margin-top: 8px; font-size: 14px; color: var(--muted); }
@media (max-width: 900px) { .gstats { grid-template-columns: 1fr; } }
.box.goldbox { border-top: 4px solid var(--gold); background: var(--surface); }
#seo .box ul { list-style: none; padding-left: 0; } #seo .box li { padding-left: 1.4em; text-indent: -1.4em; margin: 6px 0; }
.seoclose { margin: 24px 0 0; padding: 14px 16px; background: var(--ink); color: var(--onink); border-left: 8px solid var(--gold); font-family: var(--display); font-weight: 800; font-size: 21px; }
#seo mark.g { background: rgba(181,137,58,.35); color: inherit; padding: 0 3px; }
#accept { background: var(--ink); color: var(--onink); padding: 28px; margin-top: 32px; scroll-margin-top: 16px; }
#accept p { color: rgba(242,245,247,.82); }
.signbox { border: 1px solid rgba(242,245,247,.25); padding: 18px; margin: 16px 0; max-width: 40rem; }
.signbox a.agree { color: var(--onink); font-weight: 700; text-decoration: underline; text-underline-offset: 4px; display: inline-flex; min-height: 44px; align-items: center; }
.signbox label { display: block; margin: 12px 0 0; color: var(--onink); font-size: 16px; }
.signbox label.check { display: flex; gap: 10px; align-items: flex-start; }
.signbox input[type=checkbox] { width: 22px; height: 22px; flex: none; margin-top: 2px; accent-color: var(--accent); }
.signbox input[type=text] { display: block; width: 100%; margin-top: 6px; min-height: 48px; padding: 8px 12px; font: inherit; font-size: 17px; border: 1px solid rgba(242,245,247,.4); background: #fff; color: #111; border-radius: 0; }
.signbox button { margin-top: 16px; border: 0; cursor: pointer; font-family: inherit; }
.signbox button[disabled] { opacity: .45; cursor: not-allowed; }
#signmsg { margin: 12px 0 0; color: var(--onink); font-weight: 700; }
#signmsg a { color: var(--onink); }
.card { display: flex; align-items: center; gap: 28px; background: #000; color: var(--onink); padding: 28px; margin-top: 36px; flex-wrap: wrap; }
.card img.logo { width: 200px; height: auto; }
.card img.tim { width: 132px; height: 132px; object-fit: cover; box-shadow: 0 0 0 4px var(--accent); }
.card p { margin: 2px 0; }
.bar { display: none; }
@media (max-width: 900px) { dl.summary { grid-template-columns: 1fr 1fr; } .grid3, .two, .sys { grid-template-columns: 1fr; } }
@media (max-width: 640px) {
  table { display: none; } .cards { display: block; }
  dl.summary { grid-template-columns: 1fr; }
  dl.summary .pcols { grid-template-columns: 1fr; }
  .btn { width: 100%; }
  .bar { display: flex; position: fixed; left: 12px; right: 12px; bottom: 12px; z-index: 40; min-height: 52px; align-items: center; justify-content: space-between; padding: 0 16px; background: var(--ink); color: var(--onink); text-decoration: none; box-shadow: 0 6px 24px rgba(0,0,0,.35); margin-bottom: env(safe-area-inset-bottom); border-top: 3px solid var(--accent); }
  .bar b { font-family: var(--display); font-size: 19px; color: var(--accent-lt); }
  .bar[hidden] { display: none; }
  body { padding-bottom: 76px; }
}
@media print {
  @page { size: letter landscape; margin: .4in; } html { font-size: 10px; }
  .banner, .btns, .bar { display: none !important; }
  table { display: table !important; } .cards { display: none !important; }
  section[data-slide] { break-before: page; }
}
"""

SEO_CHART = """
        <div class="seochart" id="seochart">
          <div class="seohead"><p class="seotitle">Two sites, twelve months later</p><button type="button" class="replay" id="seoReplay" aria-label="Replay the chart">↻ Replay</button>
            <ul class="seokey"><li><i class="k1"></i>Kept current every month</li><li><i class="k2"></i>Built and left alone</li><li><i class="k3"></i>AI scans, nonstop</li></ul></div>
          <div class="seoplot" id="seoplot"><span class="ylab top">More</span><span class="ylab bot">Less</span>
            <svg viewBox="0 0 640 270" role="img" aria-label="Illustration: a site kept current every month climbs steadily over twelve months; a site built and left alone slides a little lower every month as AI keeps scanning, and the inbound leads gained between them grow.">
              <defs>
                <linearGradient id="gArea" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f0b13c" stop-opacity=".45"/><stop offset="1" stop-color="#f0b13c" stop-opacity="0"/></linearGradient>
                <pattern id="gGap" width="8" height="8" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="8" height="8" fill="#f0b13c" fill-opacity=".08"/><line x1="0" y1="0" x2="0" y2="8" stroke="#f0b13c" stroke-opacity=".28" stroke-width="2"/></pattern>
                <filter id="gGlow" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="5"/></filter>
              </defs>
              <line x1="4" x2="540" y1="200" y2="200" class="grid"/><line x1="4" x2="540" y1="140" y2="140" class="grid"/><line x1="4" x2="540" y1="80" y2="80" class="grid"/>
              <g id="seoUpd"></g>
              <g id="seoBeam" class="beam" aria-hidden="true"><defs><linearGradient id="gBeam" x1="0" x2="1"><stop offset="0" stop-color="#f0b13c" stop-opacity="0"/><stop offset="1" stop-color="#f0b13c" stop-opacity=".35"/></linearGradient></defs><rect id="seoBeamR" x="-30" y="22" width="30" height="230" fill="url(#gBeam)"/><line id="seoBeamL" x1="0" x2="0" y1="22" y2="252" stroke="#f0b13c" stroke-opacity=".8" stroke-width="1.5"/><text id="seoBeamT" x="8" y="17">AI scanning</text></g>
              <path id="seoArea" fill="url(#gArea)" d=""/>
              <path id="seoGap" fill="url(#gGap)" d=""/>
              <line x1="4" x2="540" y1="252" y2="252" class="axis"/><line x1="4" x2="4" y1="12" y2="252" class="axis"/>
              <path id="seoA" class="lineA" d=""/>
              <path id="seoBglow" class="lineB" d="" filter="url(#gGlow)" opacity=".7"/>
              <path id="seoB" class="lineB" d=""/>
              <g id="seoGapLab"><line id="seoBr" class="br"/><text id="seoGapT" class="gapt" dominant-baseline="middle"><tspan dy="-0.6em">Inbound</tspan><tspan dy="1.2em">Leads</tspan></text></g>
              <circle id="seoDA" r="6" class="dotA"/>
              <circle id="seoPulse" r="9" class="pulse"/><circle id="seoDB" r="8" class="dotB"/>
              <text id="seoLB0" class="endl b" x="12" y="144">Site That Climbs</text><text id="seoLB" class="endl b">Site That Climbs</text><text id="seoLA" class="endl a">Falling</text>
              <text id="seoMo" class="mo" x="22" y="48">Launch</text>
              <line id="seoX" class="xhair" y1="12" y2="252" opacity="0"/>
            </svg>
            <div class="xlabs" aria-hidden="true"><span style="left:0.6%">Launch</span><span class="mid" style="left:21.6%;transform:translateX(-50%)">3 mo</span><span style="left:42.5%;transform:translateX(-50%)">6 mo</span><span class="mid" style="left:63.4%;transform:translateX(-50%)">9 mo</span><span style="left:84.4%;transform:translateX(-50%)">12 mo</span></div>
            <p class="seocap">How easily nearby customers find you (illustration). Hover or tap to step through the year.</p>
          </div>
          <div class="seonow"><p class="b"><b id="seoM1">Month 12</b> · Kept current: <span id="seoT1">12 monthly rounds so far, keeping up with AI scans that never stop.</span></p><p class="a"><b id="seoM2">Month 12</b> · Left alone: <span id="seoT2">No changes since launch. AI keeps scanning, so it slips a little more every month.</span></p></div>
          <p class="seonote">Illustration of the usual pattern, not a forecast. No real numbers on the chart. AI scans run all the time; the marks show the pattern, not exact dates.</p>
          <p class="seonote more">Your real numbers come from the before-and-after check, starting from the baseline we save before the build.</p>
        </div>
"""

SEO_JS = """
    // SEO chart (from the DeVellis Zrein proposal, 27 Oct 2026): draws on a loop while on screen; hover or tap to scrub; holds still for reduced motion.
    (function () {
      // AI scans never stop (Tim, 28 Oct 2026): a mark every month, a scanning beam that rides the front of the gold line, and the left-alone line slips every month.
      var A = [30, 28.5, 26.5, 24, 21.5, 19, 16.5, 14, 11.5, 9, 6, 3, 0], B = [30, 33, 36, 40, 44, 47, 51, 55, 58, 62, 66, 69, 73], N = 12, UPD = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11];
      var box = document.getElementById("seochart"); if (!box) return;
      var svg = box.querySelector("svg"), $ = function (id) { return document.getElementById(id); };
      function x(m) { return 4 + (m / N) * 536; } function y(v) { return 252 - (v / 100) * 240; }
      function at(v, m) { var i = Math.floor(m); return i >= N ? v[N] : v[i] + (v[i + 1] - v[i]) * (m - i); }
      function line(v, t) { var p = []; for (var m = 0; m <= Math.floor(t); m++) p.push([x(m), y(v[m])]); if (t % 1) p.push([x(t), y(at(v, t))]); return p; }
      // Smooth curve through the points (Catmull-Rom as cubic Beziers).
      function curve(p, move) {
        var d = (move === false ? " L" : "M") + p[0][0] + "," + p[0][1];
        for (var i = 0; i < p.length - 1; i++) {
          var p0 = p[i - 1] || p[i], p1 = p[i], p2 = p[i + 1], p3 = p[i + 2] || p2;
          d += " C" + (p1[0] + (p2[0] - p0[0]) / 6) + "," + (p1[1] + (p2[1] - p0[1]) / 6) + " " + (p2[0] - (p3[0] - p1[0]) / 6) + "," + (p2[1] - (p3[1] - p1[1]) / 6) + " " + p2[0] + "," + p2[1];
        }
        return d;
      }
      var ns = "http://www.w3.org/2000/svg", ug = $("seoUpd"), marks = UPD.map(function (m) {
        var g = document.createElementNS(ns, "g"); g.setAttribute("class", "upd");
        g.innerHTML = '<line x1="' + x(m) + '" x2="' + x(m) + '" y1="22" y2="252"/><path d="M' + x(m) + ' 9l4 4-4 4-4-4z"/>';
        ug.appendChild(g); return g;
      });
      var phone = window.matchMedia("(max-width:640px)");
      function draw(t) {
        var pa = line(A, t), pb = line(B, t), ya = y(at(A, t)), yb = y(at(B, t)), xt = x(t), cb = curve(pb);
        $("seoA").setAttribute("d", curve(pa)); $("seoB").setAttribute("d", cb); $("seoBglow").setAttribute("d", cb);
        $("seoArea").setAttribute("d", cb + " L" + xt + ",252 L4,252 Z");
        $("seoGap").setAttribute("d", cb + curve(pa.slice().reverse(), false) + " Z");
        $("seoDA").setAttribute("cx", xt); $("seoDA").setAttribute("cy", ya);
        ["seoDB", "seoPulse"].forEach(function (id) { $(id).setAttribute("cx", xt); $(id).setAttribute("cy", yb); });
        var lb = $("seoLB"), la = $("seoLA"), right = t > 8.5;
        lb.setAttribute("x", right ? xt - 12 : xt + 12); lb.setAttribute("y", yb - 14); lb.setAttribute("text-anchor", right ? "end" : "start");
        la.setAttribute("x", right ? xt - 12 : xt + 12); la.setAttribute("y", ya > 225 ? ya - 12 : ya + 24); la.setAttribute("text-anchor", right ? "end" : "start");
        marks.forEach(function (g, i) { g.style.opacity = t >= UPD[i] - 0.3 ? 1 : 0; });
        // The "AI scanning" beam rides the front of the gold line and climbs with it (Tim, 28 Oct 2026).
        var by = yb + 9;
        $("seoBeam").setAttribute("transform", "translate(" + xt + ",0)");
        $("seoBeamR").setAttribute("y", by); $("seoBeamR").setAttribute("height", Math.max(0, 252 - by));
        $("seoBeamL").setAttribute("y1", by);
        // The label sits just right of the beam and above the line, clear of the "Site That Climbs" label at the start.
        $("seoBeamT").setAttribute("y", Math.min(yb - 30, 118));
        // "Falling" rides the dashed line the whole way, with no flashing tags (Tim, 28 Oct 2026).
        $("seoLB").style.opacity = t >= N - 0.05 ? 1 : 0; // the end label fades in when the line arrives
        // "Inbound Leads" rides the line ends and grows from small to big as the gap opens (Tim, 27 Oct 2026).
        var br = $("seoBr"); br.setAttribute("x1", xt + 16); br.setAttribute("x2", xt + 16); br.setAttribute("y1", yb + 6); br.setAttribute("y2", Math.max(ya - 6, yb + 6));
        var gt = $("seoGapT"), gsz = (7 + 13 * t / N) * (phone.matches ? 1.4 : 1);
        gt.setAttribute("x", xt + 22); gt.setAttribute("y", (ya + yb) / 2); gt.style.fontSize = gsz + "px";
        var tsp = gt.querySelectorAll("tspan"), len = 0; // two lines: "Inbound" over "Leads"
        for (var i = 0; i < tsp.length; i++) { tsp[i].setAttribute("x", xt + 22); len = Math.max(len, tsp[i].getComputedTextLength()); }
        var room = 636 - (xt + 22);
        if (len > room) gt.style.fontSize = gsz * room / len + "px";
        $("seoMo").textContent = t < 0.5 ? "Launch" : "Month " + Math.round(t);
        var mo = Math.round(t), lab = mo === 0 ? "Launch day" : "Month " + mo; $("seoM1").textContent = lab; $("seoM2").textContent = lab;
        $("seoT1").textContent = mo === 0 ? "the site goes live and the monthly work starts." : mo + " monthly round" + (mo > 1 ? "s" : "") + " so far, keeping up with AI scans that never stop.";
        $("seoT2").textContent = mo === 0 ? "the site goes live and the builder moves on." : "No changes since launch. AI keeps scanning, so it slips a little more every month.";
      }
      draw(N);
      var reduce = !("IntersectionObserver" in window) || window.matchMedia("(prefers-reduced-motion: reduce)").matches;
      var raf = 0, visible = false, scrubbing = false;
      function loop() { cancelAnimationFrame(raf); var start = performance.now(); (function step(now) { var f = Math.min(1, ((now - start) % 19000) / 14000), e = f < .5 ? 2 * f * f : 1 - Math.pow(-2 * f + 2, 2) / 2; draw(e * N); raf = requestAnimationFrame(step); })(start); }
      if (!reduce) new IntersectionObserver(function (es) { visible = es.some(function (e) { return e.isIntersecting; }); cancelAnimationFrame(raf); if (visible && !scrubbing) loop(); }, { threshold: 0.3 }).observe(box);
      function scrub(e) {
        var r = svg.getBoundingClientRect(), vx = ((e.clientX - r.left) / r.width) * 640, t = Math.max(0, Math.min(N, ((vx - 4) / 536) * N));
        scrubbing = true; cancelAnimationFrame(raf); draw(t);
        var xh = $("seoX"); xh.setAttribute("x1", x(t)); xh.setAttribute("x2", x(t)); xh.setAttribute("opacity", 1);
      }
      $("seoReplay").addEventListener("click", function () { scrubbing = false; $("seoX").setAttribute("opacity", 0); if (reduce) { var st = performance.now(); cancelAnimationFrame(raf); (function step(now) { var f = Math.min(1, (now - st) / 14000); draw(f * N); if (f < 1) raf = requestAnimationFrame(step); })(st); } else loop(); });
      svg.addEventListener("pointermove", scrub); svg.addEventListener("pointerdown", scrub);
      svg.addEventListener("pointerleave", function () { scrubbing = false; $("seoX").setAttribute("opacity", 0); if (reduce) draw(N); else if (visible) loop(); });
    })();
"""


def proposal():
    gap_rows = "\n".join(
        f'          <tr><td class="t">{html.escape(t)}</td><td class="p"><span class="x" aria-label="Gap">✕</span>{html.escape(p)}</td><td><span class="ok" aria-label="Solution">✓</span>{html.escape(s)}</td></tr>'
        for i, (t, p, s) in enumerate(GAPS, 1))
    gap_cards = "\n".join(
        f'        <li><p class="t">{html.escape(t)}</p><p class="p"><span class="x" aria-label="Gap">✕</span>{html.escape(p)}</p><p><span class="ok" aria-label="Solution">✓</span>{html.escape(s)}</p></li>'
        for i, (t, p, s) in enumerate(GAPS, 1))
    page_links = "\n".join(f'          <li><a href="{SITE}{s}" data-site="{s}" target="_blank" rel="noopener">{html.escape(n)}</a></li>'
                           for n, s in SITE_PAGES)
    compare = "\n".join(f'            <li><span>{html.escape(a)}</span><span><b>{b}</b> <a href="{u}">({html.escape(c)})</a></span></li>'
                        for a, b, u, c in SOURCES)
    pay = (f'<a class="btn main" id="paylink" href="{DEPOSIT_LINK}" hidden>Pay the {money(DEPOSIT)} deposit</a>'
           if DEPOSIT_LINK else '<span id="paylink-missing" hidden></span>')
    deposit_attr = DEPOSIT_LINK or ""
    launch = val(LAUNCH, "launch time")
    gap_n = len(GAPS)
    forge = html.escape(FORGE_LINE) if FORGE_LINE else ph("Forge's one-line promise")
    domain = html.escape(DOMAIN) if DOMAIN else "your domain " + ph("domain")

    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <title>JM Electrical Solutions · Not a brochure. A website that brings in work.</title>
  <meta name="description" content="The {gap_n} gaps we found on jmelectricsolutions.com, our fix for each, and our proposal.">
  <meta name="robots" content="noindex, nofollow">
  <meta property="og:type" content="website">
  <meta property="og:title" content="JM Electrical Solutions · Not a brochure. A website that brings in work.">
  <meta property="og:description" content="The {gap_n} gaps we found and how we fix each one. Your new website is built and ready to see.">
  <meta property="og:image" content="https://{PROPOSAL_HOST}/proposal/share.jpg">
  <meta property="og:image:width" content="1120">
  <meta property="og:image:height" content="630">
  <meta property="og:image:alt" content="Your proposal from AI Rocket for JM Electrical Solutions: see the {gap_n} gaps and fixes">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="icon" href="../assets/img/jm-icon.svg" type="image/svg+xml">
  <!-- Generated by build_proposal.py. Edit that file, not this one.
       Every gap comes from jmelectricsolutions.com as checked on {CHECKED}. Do not add rows that weren't checked. -->
  {FONTS}
  <style>{PROPOSAL_CSS}  </style>
</head>
<body>
  <nav class="topnav"><span>Your proposal</span><span class="navlinks"><a href="/preview/" data-prev>Phone &amp; computer view</a><a href="{SITE}/?from=proposal" data-site="/">View Your Website</a></span></nav>
  <div class="banner">Concept preview by <a href="https://airocket.pro">AI Rocket</a>, not the official JM Electrical Solutions website.</div>

  <header>
    <div class="wrap">
      <img class="shoplogo" src="jm-electrical-logo.webp" alt="JM Electrical Solutions logo, from your sign" width="919" height="303" onerror="this.onerror=null;this.src='jm-electrical-logo.png'">
      <p class="forge">{forge}</p>
      <p class="tagline">Not a brochure. A website that brings in work.</p>
      <h1>A website built to win you jobs.</h1>
      <p class="sub">Your new website is built and working now, made from your Google reviews, your own photos and the facts on jmelectricsolutions.com.</p>
      <figure class="shot">
        <div class="frame"><img src="site-home.jpg" alt="The new JM Electrical Solutions home page on a computer" width="1440" height="900"></div>
        <figcaption>Your new home page, as a homeowner sees it on a computer. {AI_NOTE}</figcaption>
      </figure>
      <div class="btns">
        <a class="btn main" href="#proposal">See your proposal</a>
        <a class="btn outline" href="{SITE}/?from=proposal" data-site="/">Explore your new website</a>
        <a class="btn outline" href="/preview/" data-prev>See it on a phone and a computer →</a>
      </div>
    </div>
  </header>

  <section class="findings" id="findings" data-slide>
    <div class="wrap">
      <h2>The gaps we found vs. our solutions</h2>
      <table>
        <thead><tr><th>Gap</th><th>✕ What we found</th><th>✓ Our solution</th></tr></thead>
        <tbody>
{gap_rows}
        </tbody>
      </table>
      <ol class="cards">
{gap_cards}
      </ol>
      <p class="note">jmelectricsolutions.com, checked {CHECKED}.</p>
      <dl class="summary">
        <div><dt>The gap</dt><dd>People who look you up find a two-page site with almost no services named, none of your 4.9-star reviews, no license number or street address, and a footer dated 2018.</dd></div>
        <div><dt>The fix</dt><dd>A website built to win you jobs: a {len(PAGES)}-page site for homeowners and businesses around Dorchester and Boston, with a page for each of your eight services, your real customer reviews and a clear way to call or ask for a quote. It is set up to be found on Google: each service on its own page named with Dorchester and Boston, search details on every page, and your Google Business Profile cleaned up. Your monthly plan keeps it current so you keep getting found. You can <a href="{SITE}/?from=proposal" data-site="/">open the working preview</a> now: the eight service pages, the Reviews page and the quote form are already built.</dd></div>
        <div class="pricecell"><dt>The price</dt><dd>
          <div class="pcols">
            <div><p><b>{money(BUILD)} website build</b>: {money(DEPOSIT)} deposit at signing, {money(BUILD - DEPOSIT)} at launch. It includes:</p>
            <ul>
{ul(PRICE_BUILD)}
            </ul></div>
            <div><p><b>{money(MONTHLY)} a month</b>, starting on launch day, not at signing. It includes:</p>
            <ul>
{ul(MONTHLY_SCOPE)}
            </ul>
            <p class="noguar">Results depend on your market and competition; we don't guarantee rankings, calls or revenue.</p>
            <p>You keep {domain} and your email. No domain fee.</p></div>
          </div></dd></div>
        <div><dt>Next step</dt><dd><a href="#accept">Sign the agreement and pay the deposit to start.</a></dd></div>
      </dl>
    </div>
  </section>

  <main>
    <section data-slide>
      <div class="wrap">
        <p class="eyebrow">Built for your customers</p>
        <h2>Built for the people who send you work</h2>
        <p class="lead">Before people let an electrician into their home or office, they check the reviews, the license and what the job involves. The site answers those questions before they pick up the phone.</p>
        <ul class="grid3">
          <li><p class="q">Homeowners</p><p class="muted">A page for each job they search for, from panel upgrades and EV chargers to recessed lighting and outlets, with the signs to look for, what the work involves, a typical timeline and common questions.</p></li>
          <li><p class="q">Businesses and offices</p><p class="muted">Your real reviews, including the interior design firm whose office remodel you wired, plus your Massachusetts license number on every page.</p></li>
          <li><p class="q">Anyone comparing electricians</p><p class="muted">Your 4.9-star rating, your customers' own words, Jamie's photo and a quote form that asks for a name, a phone number and the job.</p></li>
        </ul>
      </div>
    </section>

    <section class="alt" data-slide>
      <div class="wrap">
        <p class="eyebrow">Every page of your new site</p>
        <h2>{len(PAGES)} pages, ready to click through</h2>
        <p class="lead">Tap any page to open it on the working site. Facts we could not confirm are marked in yellow and stay off the live site until you confirm them.</p>
        <ul class="pages">
{page_links}
        </ul>
      </div>
    </section>

    <section id="seo" data-slide>
      <div class="wrap">
        <p class="eyebrow">Why the monthly plan keeps it working</p>
        <p class="lead">Your website should bring in jobs, not just look nice.</p>
        <div class="funnel"><h2>Anyone can build a pretty brochure website. We build the funnel system that turns visitors into clients.</h2></div>
        <p class="syshead">Your system, from search to phone call</p>
        <ul class="sys">
          <li><b>Found.</b>Homeowners and businesses searching for an electrician in Dorchester, South Boston and nearby Boston neighborhoods land on JM Electrical Solutions. Your Google listing is checked and cleaned up, and each of your eight services has its own page named with Dorchester and Boston, written with the title, description and business details those customers and AI search tools look for when they need that specific job done.</li>
          <li><b>Shown.</b>{html.escape(PAGE_LIST)}.</li>
          <li><b>Contacted.</b>When a customer is ready, they can reach you from any page. On a phone, one tap calls {PHONE_JM}, and the call bar stays on screen. The quote form on every page asks for their name, phone number and the job, and lands in your inbox.</li>
        </ul>
        <div class="keep"><p>Every month we keep it working:</p><ul>
{ul(MONTHLY_SCOPE)}
        </ul></div>
        <p class="proof"><b>The proof:</b> we save your Google numbers before the build and compare them at 30, 60 and 90 days after launch.</p>
        <p class="ghead">Google changes the rules every day. Your site should keep up.</p>
        <ul class="gstats">
          <li><b>4,000+</b><span>improvements Google made to Search in 2023 alone.</span><a href="https://www.google.com/intl/en_us/search/howsearchworks/how-search-works/rigorous-testing/">Google, How Search Works</a></li>
          <li><b>About 11 a day</b><span>That is the average: more than 4,000 changes over 365 days.</span><a href="https://www.google.com/intl/en_us/search/howsearchworks/how-search-works/rigorous-testing/">Google, How Search Works</a></li>
          <li><b>3</b><span>core updates to how Google ranks sites since December 2025, the latest in May 2026.</span><a href="https://status.search.google.com/summary">Google Search Status Dashboard, checked {CHECKED}</a></li>
        </ul>
        <p class="lead">Plenty of people can build a website. Most finish it, collect payment and move on. From that day the site starts to slip, because Google never stops changing how it ranks sites, and a site nobody touches falls behind the ones that keep up.</p>
        <p class="lead">SEO (search engine optimization) means the steady work that helps Google show JM Electrical Solutions when someone nearby searches something like “electrician Dorchester” or “EV charger installation Boston”. Every month we update your keywords: we check what customers are searching for and what changed in Google's latest updates, then adjust your page titles, descriptions and wording to match. Sites that sit still fall behind the ones that keep up. With your {money(MONTHLY)} a month, yours keeps up.</p>
{SEO_CHART}
        <div class="two" style="margin-top:28px">
          <div class="box"><h3>Built and left alone</h3><ul>
            <li><span aria-hidden="true">✕ </span>Finished on launch day and never touched again.</li>
            <li><span aria-hidden="true">✕ </span>AI scans never stop, and they change how sites rank. This one does not change with them.</li>
            <li><span aria-hidden="true">✕ </span>New reviews come in on Google. The site still shows the old ones.</li>
            <li><span aria-hidden="true">✕ </span>No one checks that quote requests still reach you.</li>
            <li><span aria-hidden="true">✕ </span>No one watches if the site goes down or the security certificate expires.</li>
          </ul></div>
          <div class="box goldbox"><h3>Your {money(MONTHLY)} a month: kept current</h3><ul>
{ul(CHART_KEPT, '<span aria-hidden="true">✓ </span>')}
          </ul></div>
        </div>
        <p class="seoclose">The build gets you a great site on launch day. The monthly plan is what keeps it working.</p>
      </div>
    </section>

    <section id="proposal" data-slide>
      <div class="wrap">
        <p class="eyebrow">Proposal</p>
        <h2>Your new website</h2>
        <p class="small">Prepared by AI Rocket for JM Electrical Solutions · October 2026</p>
        <div class="two">
          <div class="box">
            <p class="price">{money(BUILD)}</p>
            <p>Website build</p>
            <p class="small">{money(DEPOSIT)} deposit at signing, {money(BUILD - DEPOSIT)} at launch</p>
            <ul>
{ul(BUILD_SCOPE)}
            </ul>
            <p class="price" style="margin-top:24px">{money(MONTHLY)}/mo</p>
            <p>From launch day</p>
            <ul>
{ul(MONTHLY_SCOPE)}
            </ul>
            <p class="noguar">Results depend on your market and competition; we don't guarantee rankings, calls or revenue.</p>
            <p class="price" style="margin-top:24px;font-size:34px">$0</p>
            <p>Your domain and email</p>
            <ul>
            <li>You keep {domain}. We point it at the new site at launch.</li>
            <li>Your email stays exactly as it is.</li>
            </ul>
            <div class="compare" style="margin-top:20px;border:1px solid var(--line);padding:14px">
              <b>How the price compares</b>
              <ul>
{compare}
              </ul>
              <p class="small">Your build is {money(BUILD)}: inside the freelancer range for a 10-page electrician site and right at the freelancer median for electrician sites, well below agency prices, while your new site has {len(PAGES)} pages. {money(MONTHLY)} a month sits at the top of the hosting-and-maintenance range and covers the hands-on work listed above, including monthly keyword updates. Figures checked {CHECKED}.</p>
            </div>
          </div>
          <div>
            <div class="box dark">
              <h3 style="color:var(--gold)">What success looks like: goals we measure</h3>
              <ul>
            <li><span class="ok" aria-hidden="true">✓</span>Your own site shows up when people search “JM Electrical Solutions Dorchester” (we re-run the same searches 30 days after launch).</li>
            <li><span class="ok" aria-hidden="true">✓</span>Each of your eight services has its own page named with Dorchester and Boston.</li>
            <li><span class="ok" aria-hidden="true">✓</span>Address and phone match on your site and in your Google listing.</li>
            <li><span class="ok" aria-hidden="true">✓</span>Quote requests from the site land in your inbox, checked every month.</li>
              </ul>
            </div>
            <div class="box" style="margin-top:16px">
              <h3>How we prove it works: before and after</h3>
              <ul>
            <li>Before we build: we save your Google listing's numbers for the last 6 months (calls, directions, website clicks and the searches people use to find you).</li>
            <li>The same day, we record where you show up on Google for two or three key searches, such as “electrician Dorchester MA”.</li>
            <li>After launch: we compare the same numbers at 30, 60 and 90 days and send you a plain-English before-and-after.</li>
            <li>The 90-day check lands as your 3-month minimum ends, so you decide whether to stay on real numbers, not promises.</li>
              </ul>
            </div>
            <div class="box" style="margin-top:16px">
              <h3>Terms</h3>
              <dl class="terms">
            <div><dt>Build payment</dt><dd>{money(DEPOSIT)} deposit at signing and {money(BUILD - DEPOSIT)} at launch.</dd></div>
            <div><dt>Domain and email</dt><dd>You keep {domain} and your email. No domain fee.</dd></div>
            <div><dt>Launch</dt><dd>{launch}</dd></div>
            <div><dt>Monthly billing</dt><dd>{money(MONTHLY)} a month, starting on launch day, not at signing.</dd></div>
            <div><dt>Minimum term</dt><dd>3 months, then month to month.</dd></div>
            <div><dt>Cancelling</dt><dd>30 days' written notice after the first 3 months. You keep the site, and we hand over the files.</dd></div>
            <div><dt>How you accept</dt><dd>Sign the agreement and pay the {money(DEPOSIT)} deposit below. We invoice the second half and start the {money(MONTHLY)} monthly plan on launch day.</dd></div>
              </dl>
            </div>
          </div>
        </div>

        <div id="accept">
          <p class="display" style="font-size:32px;color:var(--onink)">Ready for a website that wins you jobs?</p>
          <p>Sign the agreement, then pay the deposit by secure Stripe checkout. Questions first? AI Rocket: <a href="tel:+16174990149"><b>{PHONE_AIR}</b></a>.</p>
          <!-- E-signature: the deposit unlocks only after the agreement is signed. Saved by /api/sign to Supabase. -->
          <form class="signbox" id="signform" novalidate>
            <p><a class="agree" href="/agreement/" data-agree target="_blank" rel="noopener">Read the Website Service Agreement and your Order Form →</a></p>
            <label class="check"><input type="checkbox" id="agree"> <span>I have read and agree to the Website Service Agreement and my Order Form, and I agree to sign electronically.</span></label>
            <label>Your full name<input type="text" id="signname" autocomplete="name" maxlength="120"></label>
            <label>Business name<input type="text" id="signbiz" autocomplete="organization" maxlength="160" value="{html.escape(LEGAL_NAME or 'JM Electrical Solutions')}"></label>
            <button type="submit" class="btn main" id="signbtn" disabled>Sign the agreement</button>
            <p id="signmsg" role="status" aria-live="polite"></p>
          </form>
          <div class="btns">
            <span id="paywrap" hidden>{pay}</span>
            <a class="btn outline" href="mailto:tim@airocket.pro?subject=JM%20Electrical%20proposal">Email us a question</a>
          </div>
        </div>
      </div>
    </section>

    <section data-slide>
      <div class="wrap">
        <p class="eyebrow">What we need from you</p>
        <h2>{len(NEEDS)} things only you can confirm</h2>
        <p class="lead">Nothing goes on your real site until you confirm it.</p>
        <ul style="font-size:18px;max-width:46rem">
{ul(NEEDS)}
        </ul>
        <div class="card">
          <img class="logo" src="airocket-logo.jpg" alt="AI Rocket" width="600" height="558">
          <img class="tim" src="tim-regan.jpg" alt="Tim Regan, founder of AI Rocket" width="400" height="400">
          <div>
            <p class="display" style="font-size:22px">Tim Regan · AI Rocket</p>
            <p class="small" style="color:rgba(242,245,247,.7)">Founder</p>
            <p><a href="mailto:tim@airocket.pro">tim@airocket.pro</a></p>
            <p><a href="tel:+16174990149">{PHONE_AIR}</a> · <a href="https://airocket.pro">airocket.pro</a></p>
          </div>
        </div>
      </div>
    </section>
  </main>

  <nav class="topnav botnav"><span>Your proposal</span><span class="navlinks"><a href="/preview/" data-prev>Phone &amp; computer view</a><a href="{SITE}/?from=proposal" data-site="/">View Your Website</a></span></nav>

  <a class="bar" id="bar" href="#proposal"><b>{money(BUILD)} + {money(MONTHLY)}/mo</b><span>See your proposal ↓</span></a>

  <script>
    // Links to the site carry the reader's ?p= code, so the site can offer a way back to this proposal.
    (function () {{
      var SITE = "{SITE}", p = new URLSearchParams(location.search).get("p");
      if (!p) return;
      document.querySelectorAll("a[data-site]").forEach(function (a) {{ a.href = SITE + a.getAttribute("data-site") + "?from=proposal&p=" + encodeURIComponent(p); }});
      document.querySelectorAll("a[data-prev]").forEach(function (a) {{ a.href = "/preview/?p=" + encodeURIComponent(p); }});
    }})();
  </script>
  <script>
    // Phone bar: jumps to the proposal, then to the signature; hides while the accept block is on screen.
    (function () {{
      var bar = document.getElementById("bar"), proposal = document.getElementById("proposal"), accept = document.getElementById("accept");
      if (!("IntersectionObserver" in window)) return;
      var at = false, vis = false;
      function draw() {{
        bar.hidden = vis;
        bar.href = at ? "#accept" : "#proposal";
        bar.lastChild.textContent = at ? "Sign and pay ↓" : "See your proposal ↓";
      }}
      new IntersectionObserver(function (es) {{ at = es[0].isIntersecting || es[0].boundingClientRect.top < 0; draw(); }}).observe(proposal);
      new IntersectionObserver(function (es) {{ vis = es[0].isIntersecting; draw(); }}).observe(accept);
      window.addEventListener("beforeprint", function () {{ bar.hidden = true; }});
    }})();
  </script>
  <script>
    // Sign, then pay: saves the signature through /api/sign, then shows (and opens) the Stripe deposit.
    (function () {{
      var SHOP = "jm-electrical", f = document.getElementById("signform"), btn = document.getElementById("signbtn"), msg = document.getElementById("signmsg");
      var agree = document.getElementById("agree"), nm = document.getElementById("signname"), biz = document.getElementById("signbiz");
      var wrap = document.getElementById("paywrap"), pay = document.getElementById("paylink");
      var p = new URLSearchParams(location.search).get("p");
      document.querySelectorAll("a[data-agree]").forEach(function (a) {{ if (p) a.href = "/agreement/?p=" + encodeURIComponent(p); }});
      function ok() {{ return agree.checked && nm.value.trim().length >= 2 && biz.value.trim().length >= 2; }}
      function check() {{ btn.disabled = !ok(); }}
      [agree, nm, biz].forEach(function (el) {{ el.addEventListener("input", check); el.addEventListener("change", check); }});
      function done(id, go) {{
        f.querySelectorAll("input,button").forEach(function (el) {{ el.disabled = true; }});
        var copy = "/agreement/?sig=" + encodeURIComponent(id) + (p ? "&p=" + encodeURIComponent(p) : "");
        msg.innerHTML = "";
        msg.appendChild(document.createTextNode("Signed. Thank you. "));
        var a = document.createElement("a"); a.href = copy; a.target = "_blank"; a.rel = "noopener"; a.textContent = "Your signed copy"; msg.appendChild(a);
        if (pay) {{ pay.hidden = false; wrap.hidden = false; if (go) setTimeout(function () {{ pay.click(); }}, 1200); }}
        else msg.appendChild(document.createTextNode(". We'll email you the deposit link."));
      }}
      var KEY = "signed-" + SHOP, saved = null;
      try {{ saved = localStorage.getItem(KEY); }} catch (e) {{}}
      if (saved) done(saved, false);
      f.addEventListener("submit", function (e) {{
        e.preventDefault();
        if (!ok()) return;
        btn.disabled = true; msg.textContent = "Saving your signature…";
        fetch("/api/sign", {{ method: "POST", headers: {{ "Content-Type": "application/json" }},
          body: JSON.stringify({{ agree: true, name: nm.value, business: biz.value, package: "site", p: p }}) }})
          .then(function (res) {{ return res.json().then(function (j) {{ return {{ ok: res.ok, j: j }}; }}); }})
          .then(function (x) {{
            if (!x.ok || !x.j.id) throw new Error(x.j.error || "save failed");
            try {{ localStorage.setItem(KEY, x.j.id); }} catch (e) {{}}
            done(x.j.id, true);
          }})
          .catch(function (err) {{ msg.textContent = (err && err.message) || "Something went wrong. Please try again or email us."; btn.disabled = !ok(); }});
      }});
    }})();
  </script>
  <script src="track.js" data-deposit="{deposit_attr}" defer></script>
  <script>{SEO_JS}  </script>
</body>
</html>
"""


# ---------------------------------------------------------------- agreement
# Tim's attorney-reviewed text, word for word from jobisgreat/tint-me agreement/index.html (v1 · 21 Oct 2026).
AGREEMENT_BODY = """<p>This agreement is between AI Rocket, 220 Forest Street, Waltham, MA 02452 (&quot;AI Rocket&quot;, &quot;we&quot;), and the business named in the Order Form (&quot;you&quot;). It starts on the date you sign it. The Order Form is part of this agreement. If the two disagree, the Order Form wins.</p>
<h3>1. What we build</h3><p>We build the website and any extras listed in your Order Form (the &quot;Build&quot;). The working preview you saw in your proposal shows the look and features. Before launch we replace the preview&#x27;s AI-made photos with your own photos, and we add only facts you have confirmed.</p>
<h3>2. Launch</h3><p>We launch within the time stated in your Order Form, counted from the day we receive your deposit. That time depends on you giving us, on time, what section 5 lists. Any wait for a third party you choose or need (such as a domain registrar, Google, or phone carriers approving a texting number) does not count against us.</p>
<h3>3. Monthly plan</h3><p>From launch day you pay the monthly fee in your Order Form. It covers what the Order Form lists for the monthly plan. Work outside that list is quoted first, in writing, and done only once you agree.</p>
<h3>4. Payment</h3><ul><li>You pay the deposit when you sign. We start work once it clears.</li><li>We invoice the rest of the Build fee, and any one-time items in the Order Form, on launch day. Payment is due within 7 days.</li><li>The monthly fee is charged on the same day each month, starting on launch day.</li><li>If a payment is more than 15 days late, we may pause the monthly work and take the site offline after giving you 7 days&#x27; written notice. We restore it once you are paid up.</li><li>Third-party fees are yours (for example Stripe card fees on payments your customers make). Fees already included in your price are named in your Order Form.</li></ul>
<h3>5. What you give us</h3><ul><li>Your own photos, prices, hours and business facts, and quick answers to our questions.</li><li>Access to your Google Business Profile, or an invitation as a manager.</li><li>You confirm that you own, or have the right to use, everything you give us, and that your prices and claims are accurate.</li></ul>
<h3>6. Term and cancelling</h3><p>The monthly plan has a 3-month minimum from launch day. After that it runs month to month. Either side may end it with 30 days&#x27; written notice; email or text counts. Either side may end this agreement at once if the other seriously breaks it and does not fix it within 15 days of written notice.</p>
<h3>7. What you keep when it ends</h3><p>Once you have paid the Build fee in full, you own your site&#x27;s content: your text, photos, prices and logo. When the plan ends we hand over the site files and move your domain to you. The deposit is not refunded once work has started. Monthly fees already paid are not refunded.</p>
<h3>8. Our tools</h3><p>We keep ownership of the general tools, templates and code we use for all clients. You get a permanent licence to use them as part of your site. We may show your site in our portfolio unless you tell us in writing not to.</p>
<h3>9. No promises about results</h3><p>We do the work listed in good faith. We cannot promise any search ranking, number of visitors, bookings or sales, because Google and your customers decide those. Third-party services (hosting, Google, Stripe, phone carriers) can change or go down, and we are not responsible for their outages.</p>
<h3>10. Limit of liability</h3><p>Neither side is liable for lost profits or indirect losses. Our total liability under this agreement is limited to the fees you paid us in the 3 months before the claim. This does not limit liability for fraud or wilful misconduct.</p>
<h3>11. Privacy</h3><p>We use customer details collected by your site (such as bookings) only to run your site, and we never sell them. You are responsible for any privacy notice your business needs, and we will add one to your site if you ask.</p>
<h3>12. Electronic signature and notices</h3><p>You agree to sign electronically. Typing your name and ticking &quot;I agree&quot; on the proposal page is your signature, and it has the same effect as signing on paper. Written notice may be given by email or text to the contacts in the Order Form.</p>
<h3>13. General</h3><p>Massachusetts law governs this agreement. Any dispute goes to the courts of Middlesex County, Massachusetts. This agreement and the Order Form are the whole deal between us; changes must be in writing and agreed by both sides. If a part is found unenforceable, the rest still stands.</p>"""


def agreement():
    client = f"{val(LEGAL_NAME, 'legal name')}, 749 Dorchester Ave, Boston, MA 02125"
    rows = [
        ("Client", client),
        ("Signer", val(SIGNER, "signer's full name")),
        ("Client contact", f"Jamie Maguire, {html.escape(EMAIL_JM)}; phone {PHONE_JM}"),
        ("Website build", money(BUILD)),
        ("Build payment", f"{money(DEPOSIT)} deposit at signing, {money(BUILD - DEPOSIT)} on launch day"),
        ("Domain and email", f"The client keeps {html.escape(DOMAIN) if DOMAIN else 'its domain ' + ph('domain')} and its email. We point the domain at the new site at launch. No domain or email fee"),
        ("Monthly plan", f"{money(MONTHLY)} a month from launch day; 3-month minimum, then month to month"),
        ("Launch time", val(LAUNCH, "launch time")),
        ("Revisions", "Two rounds of revisions before launch, plus 30 days of fixes after launch"),
        ("Proposal", f"{PROPOSAL_HOST}/proposal (the build scope listed there)"),
    ]
    table = "\n".join(f"<tr><th>{k}</th><td>{v}</td></tr>" for k, v in rows)
    build_text = html.escape(
        f"a website with {len(PAGES)} pages ({', '.join(PAGES[:-1])} and {PAGES[-1]}), built from the working preview; "
        "each of the eight services on its own page named with Dorchester and Boston (panel upgrades, EV charger installation, lighting and ceiling fans, home rewiring, generators, smart home automation, outlets and switches, and emergency electrical service), with the signs to look for, what the work involves, a typical timeline, what to expect and common questions; "
        "the client's real customer reviews on the home page and a Reviews page; an About page with the client's photo and a Service Areas page; "
        "tap-to-call on every page and a call bar on phones; the client's logo; the Massachusetts license number and street address on every page; "
        "a title and description on every page and business and service details in code Google reads; the quote form connected to the client's inbox; "
        "only facts the client has confirmed; the client's domain pointed at the new site with its email left as it is; "
        "and a Google Business Profile check and cleanup.")
    monthly_text = " ".join(html.escape(s) for s in MONTHLY_SCOPE)  # word for word, as on the proposal
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Website Service Agreement · JM Electrical Solutions</title>
  <meta name="robots" content="noindex, nofollow">
  <!-- Generated by build_proposal.py. Agreement {VERSION}. A ?sig=<id> link shows the signed record above the text. -->
  <style>
    :root {{ --ink:#141414; --muted:#5b5b5b; --line:#d5dde2; --bg:#ffffff; --ok:#1d6b3a; }}
    * {{ box-sizing: border-box; }}
    body {{ margin:0; background:var(--bg); color:var(--ink); font:17px/1.6 -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif; }}
    .wrap {{ max-width: 760px; margin: 0 auto; padding: 24px 16px 64px; }}
    nav {{ display:flex; flex-wrap:wrap; gap:8px 24px; padding:12px 0 20px; border-bottom:1px solid var(--line); margin-bottom:24px; }}
    nav a {{ color:var(--ink); font-weight:600; min-height:44px; display:inline-flex; align-items:center; }}
    h1 {{ font-size: 30px; line-height:1.2; margin: 0 0 4px; }}
    h2 {{ font-size: 22px; margin: 40px 0 8px; }}
    h3 {{ font-size: 18px; margin: 24px 0 4px; }}
    .muted {{ color: var(--muted); font-size: 15px; }}
    table {{ width:100%; border-collapse:collapse; margin: 12px 0 16px; font-size:16px; }}
    th, td {{ text-align:left; vertical-align:top; padding:10px 8px; border-bottom:1px solid var(--line); }}
    th {{ width: 34%; }}
    .ph {{ background:#ffe14d; color:#1a1400; padding:0 4px; }}
    .signed {{ border:2px solid var(--ok); background:#eef7f0; padding:14px 16px; border-radius:6px; margin-bottom:24px; }}
    .signed b {{ color: var(--ok); }}
    @media print {{ nav, .noprint {{ display:none; }} body {{ background:#fff; }} }}
  </style>
</head>
<body>
  <div class="wrap">
    <nav class="noprint"><a href="/proposal/" class="back">View Your Proposal</a><a href="#" onclick="window.print();return false">Print or save as PDF</a></nav>
    <div id="signed" class="signed" hidden></div>
    <h1>Website Service Agreement</h1>
    <p class="muted">AI Rocket and JM Electrical Solutions · Agreement {VERSION}</p>
{AGREEMENT_BODY}
    <h2>Order Form: JM Electrical Solutions</h2>
    <table>
{table}
    </table>
<p><b>The website build includes:</b> {build_text} Two rounds of revisions before launch, plus 30 days of fixes after launch.</p>
<p><b>The monthly plan includes:</b> {monthly_text}</p>
    <nav class="noprint" style="border-bottom:0;border-top:1px solid var(--line);margin:32px 0 0;padding-top:12px"><a href="/proposal/" class="back">View Your Proposal</a></nav>
  </div>
  <script>
    (function () {{
      var q = new URLSearchParams(location.search);
      var p = q.get("p");
      if (p) document.querySelectorAll("a.back").forEach(function (a) {{ a.href = "/proposal/?p=" + encodeURIComponent(p); }});
      var id = q.get("sig");
      if (!id) return;
      fetch("/api/sign?id=" + encodeURIComponent(id)).then(function (r) {{ return r.ok ? r.json() : null; }}).then(function (s) {{
        if (!s) return;
        var box = document.getElementById("signed");
        var when = new Date(s.signed_at).toLocaleString("en-US", {{ timeZone: "America/New_York", dateStyle: "long", timeStyle: "short" }});
        box.innerHTML = "<b>Signed electronically</b><br>";
        box.appendChild(document.createTextNode(s.signer_name + " for " + s.business_name + ", " + when + " (Eastern), agreement " + s.agreement_version + ". Website build: {money(BUILD)}."));
        box.hidden = false;
      }}).catch(function () {{}});
    }})();
  </script>
</body>
</html>
"""


# ---------------------------------------------------------------- preview
PREVIEW_PAGES = [("/", "Homepage"), ("/panel-upgrades.html", "A service page"), ("/reviews.html", "Reviews"),
                 ("/contact.html", "Contact")]


def preview():
    src = (ROOT / "tools" / "preview_template.html").read_text()
    buttons = "".join(
        f'<button type="button" data-page="{SITE}{path}" aria-pressed="{"true" if i == 0 else "false"}">{name}</button>'
        for i, (path, name) in enumerate(PREVIEW_PAGES))
    return (src.replace("{{SITE}}", SITE).replace("{{PAGEBUTTONS}}", buttons).replace("{{FONTS}}", FONTS))


if __name__ == "__main__":
    for d in ("proposal", "agreement", "preview"):
        (OUT / d).mkdir(exist_ok=True)
    (OUT / "proposal" / "index.html").write_text(proposal())
    (OUT / "agreement" / "index.html").write_text(agreement())
    (OUT / "preview" / "index.html").write_text(preview())
    print("wrote site/proposal/, site/agreement/, site/preview/")
