#!/usr/bin/env python3
"""Builds the JM Electrical Solutions static site.

Every page shares one header, footer, form and schema block, so business facts
(phone, address, license) live in ONE place below. Edit, then run:
    python3 build.py
Output goes to ../jm-electrical-site/
"""
import json, os, html

OUT = os.environ.get("OUT_DIR") or os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "jm-electrical-site")
# PREVIEW=1 keeps search engines out while sample reviews and placeholders are still on the site
PREVIEW = os.environ.get("PREVIEW") == "1"

# ---------------------------------------------------------------- facts (source: Tim's brief, 28 Oct 2026)
SITE_URL = "https://www.YOUR-DOMAIN.com"   # TODO: real domain before launch
BIZ = "JM Electrical Solutions"
OWNER = "Jamie Maguire"
STREET, CITY, REGION, ZIP = "749 Dorchester Ave", "Boston", "MA", "02125"
ADDRESS = f"{STREET}, {CITY}, {REGION} {ZIP}"
PHONE = "(978) 746-1993"
TEL = "tel:+19787461993"
LICENSE = "22667"
RATING, REVIEWS = "4.9", "100+"
GOOGLE_REVIEWS_URL = "#"   # TODO: paste the Google Business Profile reviews link
MAPS_URL = "https://www.google.com/maps/search/?api=1&query=749+Dorchester+Ave+Boston+MA+02125"

# ---------------------------------------------------------------- icons
I_PHONE = '<svg aria-hidden="true" viewBox="0 0 24 24" fill="currentColor"><path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.25 11.4 11.4 0 0 0 3.6.57 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.25.2 2.45.57 3.57a1 1 0 0 1-.25 1L6.6 10.8z"/></svg>'
I_CHECK = '<svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><path d="M5 12l5 5L20 7"/></svg>'
I_STAR = '<svg aria-hidden="true" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2l3.1 6.3 6.9 1-5 4.9 1.2 6.8L12 17.8 5.8 21l1.2-6.8-5-4.9 6.9-1z"/></svg>'

def esc(s): return html.escape(s, quote=True)

# ---------------------------------------------------------------- services
# Timelines are typical for this kind of work, not JM-specific; each page shows a
# "confirm" tag until Jamie signs off.
SERVICES = [
  dict(
    slug="panel-upgrades", name="Panel Upgrades", nav="Panel Upgrades", financing=True,
    card="Replace an old fuse box or undersized panel so you can add an EV charger, heat pump or new kitchen safely.",
    title="Electrical Panel Upgrades in Dorchester & Boston | JM Electrical Solutions",
    meta="Licensed panel upgrades and fuse box replacements in Dorchester, South Boston and Boston. MA License #22667. 4.9★ from 100+ Google reviews. Clear quotes, clean work.",
    h1="Electrical Panel Upgrades in Dorchester & Boston",
    intro="A lot of Boston homes, from Dorchester triple-deckers to South Boston row houses, are still running on panels sized for a few lights and a fridge. If you're adding an EV charger, a heat pump, central air or a new kitchen, the panel is usually the first thing that needs to change. We'll tell you plainly whether you need an upgrade, why, and what it costs before any work starts.",
    signs=["You still have a fuse box, or breakers trip when two appliances run at once",
           "Your panel is a brand electricians flag as a known hazard (Federal Pacific Stab-Lok or Zinsco)",
           "You're planning an EV charger, heat pump, central A/C, or kitchen or bath renovation",
           "There's no room left in the panel, or you see double-tapped breakers and tandem breakers everywhere",
           "Lights dim when the A/C or microwave kicks on, or the panel feels warm or buzzes",
           "An insurer or home inspector has flagged your panel"],
    involved=[("Load assessment", "We look at what's on your panel today and what you plan to add, then size the new panel and service (commonly 100 to 200 amps) to fit. No upselling: if your current panel can handle it, we'll say so."),
              ("Permit and utility coordination", "Panel and service upgrades in Boston need an electrical permit and a city inspection. When the service size changes, the utility also has to disconnect and reconnect power. We handle the paperwork and scheduling so you're not chasing anyone."),
              ("The swap", "Power goes off, the old panel comes out, and a new panel with new breakers goes in. Every circuit is labeled so you know what each breaker controls."),
              ("Inspection and walkthrough", "After the inspector signs off, we walk you through the new panel, show you the labeling, and leave the area cleaner than we found it.")],
    timeline=[("Visit and written quote", "Usually within a few days of your call."),
              ("Permit and utility scheduling", "Often one to three weeks, depending on the city and the utility."),
              ("Installation day", "Most straightforward panel swaps are done in one working day, with power off for part of it."),
              ("Inspection", "Scheduled with the city after the work is complete.")],
    expect=["A clear written quote with what's included, before any work starts",
            "A heads-up on how long the power will be off, so you can plan around it",
            "Drop cloths down, dust kept contained, old equipment hauled away",
            "Neatly labeled breakers and a walkthrough at the end"],
    benefits=["Room to add an EV charger, heat pump or new appliances without nuisance tripping",
              "Modern breakers, including AFCI and GFCI protection where code calls for it",
              "Fewer flags from insurers and home inspectors when you refinance or sell",
              "A properly sized service that's ready for the next 20+ years of electrical load"],
    faqs=[("How do I know if I need a panel upgrade or just a few new circuits?", "Not every home needs a full upgrade. We do a load calculation based on what you have and what you're adding. Sometimes a few new breakers or a subpanel does the job, and we'll tell you if that's the case."),
          ("Will my power be off all day?", "Power is off for part of the installation day while the old panel is removed and the new one is connected. We'll give you a realistic window ahead of time so you can plan for the fridge, work-from-home, and anyone on medical equipment."),
          ("Do you pull the permit?", "Yes. Panel and service work requires a permit and inspection in Massachusetts. We file it under our license (#22667) and schedule the inspection."),
          ("I'm thinking about an EV charger or heat pump. Should I upgrade first?", "Often, yes, but not always. Tell us everything you're planning and we'll size the panel once, so you're not paying for two upgrades."),
          ("Is financing available for a panel upgrade?", "Ask us about financing options when we quote the job. We'll walk you through what's available.")],
    related=["ev-chargers", "rewiring", "generators", "emergency-electrician"],
    photos=[("Photo: a newly installed 200-amp panel with every breaker neatly labeled in Jamie's handwriting, cover off, wires dressed straight.", "New panel, every circuit labeled."),
            ("Photo: before-and-after of an old fuse box in a Dorchester basement next to the new breaker panel that replaced it.", "Before and after: fuse box to modern panel.")],
  ),
  dict(
    slug="ev-chargers", name="EV Charger Installation", nav="EV Chargers", financing=True,
    card="Level 2 home charging installed safely, with an honest check on whether your panel can handle it.",
    title="EV Charger Installation in Dorchester & Boston | JM Electrical Solutions",
    meta="Level 2 EV charger installation for Boston homes, driveways and garages. Licensed MA electrician #22667, 4.9★ from 100+ Google reviews. Clear quote before work starts.",
    h1="EV Charger Installation in Dorchester & Boston",
    intro="A Level 2 charger turns overnight charging from a trickle into a full battery by morning. The charger itself is the easy part. What matters is whether your panel can carry the load, how far the wire has to run to your driveway or garage, and that it's installed to code. We check all three up front and give you a straight answer.",
    signs=["You just bought or are about to buy an EV or plug-in hybrid",
           "Charging from a regular wall outlet is too slow for your commute",
           "You have a charger in the box and need it installed properly",
           "You want an outdoor charger at a driveway, garage or parking spot behind a triple-decker"],
    involved=[("Panel and load check", "We look at your panel's size and how much load it already carries. If there's capacity, we add a dedicated 240-volt circuit. If not, we'll explain your options, from a load-managing charger to a panel upgrade, and what each costs."),
              ("Choosing the location", "We plan the shortest safe route from the panel to where you park, and talk through hardwired vs. plug-in (NEMA 14-50) setups and outdoor-rated equipment."),
              ("Installation", "We run the circuit, mount and connect the charger, and set it to the correct amperage for the circuit. Wiring is secured and protected, not left draped along the wall."),
              ("Permit, test and handoff", "We file the permit, test the charger with your car if it's home, and show you how to use it.")],
    timeline=[("Quote", "Often done from photos of your panel and parking spot, or a short site visit."),
              ("Installation", "A straightforward install near the panel is often done in a few hours to a day. Long runs or a panel upgrade add time."),
              ("Inspection", "Scheduled with the city after the work is done.")],
    expect=["An honest answer on whether your panel can handle a charger as-is",
            "A clear quote that separates the charger install from any panel work",
            "Neat, protected wiring runs, and holes sealed where we go through walls",
            "A test charge and a quick walkthrough before we leave"],
    benefits=["Wake up to a full battery instead of planning around public chargers",
              "A dedicated circuit sized correctly for your charger, so nothing overheats or trips",
              "Outdoor-rated equipment and connections that hold up to New England winters",
              "A permitted, inspected install, which matters for insurance and resale"],
    faqs=[("Do I need a panel upgrade for an EV charger?", "Not always. Many homes have enough capacity for a dedicated circuit. We check your panel's load first. If it's tight, a load-managing charger can sometimes avoid a full upgrade. We'll show you both options."),
          ("Should I buy the charger, or do you supply it?", "Either works. If you already have one, we'll install it. If you haven't bought one yet, call first and we'll tell you what amperage your home can support, so you don't buy the wrong unit."),
          ("Can you install a charger at a triple-decker or condo?", "Often, yes. The main questions are which meter and panel serve your parking spot and how far the run is. Condo installs may also need association approval. We'll help you figure out what's needed."),
          ("How long does installation take?", "A simple install close to the panel is often done in a few hours to a day. Longer runs or a panel upgrade add time, and we'll tell you up front."),
          ("Is financing available?", "Ask us about financing options when we quote, especially if the job includes a panel upgrade.")],
    related=["panel-upgrades", "generators", "smart-home", "outlets-switches"],
    photos=[("Photo: a wall-mounted Level 2 charger on the side of a garage in Dorchester, conduit run straight and strapped, cable coiled neatly.", "Outdoor Level 2 charger with a clean conduit run."),
            ("Photo: Nic connecting a new 60-amp breaker for an EV circuit inside an open panel, area covered with a drop cloth.", "Dedicated EV circuit going in.")],
  ),
  dict(
    slug="lighting-ceiling-fans", name="Lighting & Ceiling Fans", nav="Lighting & Fans", financing=False,
    card="Recessed lights, fixture swaps, under-cabinet and outdoor lighting, and ceiling fans hung on the right box.",
    title="Lighting & Ceiling Fan Installation in Dorchester & Boston | JM Electrical",
    meta="Recessed lighting, fixture replacement, outdoor lighting and ceiling fan installation in Dorchester and Boston. Licensed electrician #22667. Clean, careful work.",
    h1="Lighting & Ceiling Fan Installation in Dorchester & Boston",
    intro="Good lighting changes how a room feels and how you use it. Whether it's a single fixture swap or a full set of recessed lights in a renovated kitchen, we do it carefully, keep the dust down in finished rooms, and make sure fans are mounted on a box rated to hold them.",
    signs=["Dark kitchens, hallways or basements", "Old fixtures you want replaced", "A ceiling fan that wobbles or was hung on a light-fixture box", "Outdoor lighting for a porch, stairs or yard"],
    involved=[("Plan the layout", "We talk through where you want light, how bright, and how you want to control it (dimmers, switches, smart controls)."),
              ("Install", "For new recessed lights or fans we cut cleanly, fish wire through existing walls and ceilings where possible, and install fan-rated boxes where needed."),
              ("Finish", "Fixtures go up, dimmers are set, everything is tested, and we vacuum up before we go.")],
    timeline=[("Fixture swaps and fans", "Usually a few hours."), ("Recessed lighting for a room", "Often a day, depending on access.")],
    expect=["A clear price before we start", "Drop cloths in finished rooms and dust kept to a minimum", "Fans balanced and tested on every speed", "Cleanup before we leave"],
    benefits=["Brighter, more usable rooms", "Efficient LED fixtures that cut bulb changes", "Fans mounted securely on rated boxes", "Dimmer and smart-control options"],
    faqs=[("Can you add recessed lights without opening up the whole ceiling?", "In many cases, yes. We fish wire between fixture openings. Access depends on joists and what's above, and we'll tell you before we start if any extra openings are needed."),
          ("Can a ceiling fan go where my light fixture is now?", "Usually, but the box has to be rated for a fan. Many older boxes aren't. We swap it for a fan-rated box so the fan is secure and doesn't wobble."),
          ("Do you supply the fixtures?", "You can buy your own and we'll install them, or we can recommend fixtures that fit the space and your budget.")],
    related=["smart-home", "outlets-switches", "rewiring"],
    photos=[("Photo: a finished kitchen with evenly spaced LED recessed lights and under-cabinet lighting on, counters clear and clean.", "Recessed and under-cabinet lighting in a renovated kitchen."),
            ("Photo: a ceiling fan freshly installed in a South Boston bedroom, ladder folded, floor covered with a drop cloth.", "Ceiling fan on a fan-rated box.")],
  ),
  dict(
    slug="rewiring", name="Home Rewiring", nav="Rewiring", financing=True,
    card="Replace knob-and-tube, ungrounded or damaged wiring in older Boston homes with as little wall damage as possible.",
    title="Home Rewiring in Dorchester & Boston | Knob-and-Tube Replacement | JM Electrical",
    meta="Whole-home and partial rewiring for older Boston homes, including knob-and-tube replacement. Licensed MA electrician #22667. Clear plan, careful work, clean job sites.",
    h1="Home Rewiring in Dorchester & Boston",
    intro="Much of Boston's housing was built long before modern electrical loads. Knob-and-tube, cloth-insulated wire and ungrounded two-prong outlets are common in older Dorchester and South Boston homes. Rewiring is a bigger job, so we lay out the plan, the phases and the price clearly before anyone touches a wall.",
    signs=["Knob-and-tube or cloth-covered wiring in the basement or attic", "Mostly two-prong outlets with no ground", "Flickering lights, warm outlets or switch plates, or a burning smell", "An insurer or inspector has flagged your wiring", "You're renovating and walls are already open"],
    involved=[("Inspection and plan", "We trace what's there, identify what needs replacing now and what can wait, and give you a written plan. Partial rewiring is often an option."),
              ("Phased work", "We work room by room where possible so you can keep living in the house. We fish new wire through existing walls to limit openings, and tell you up front where openings are needed."),
              ("Permit and inspection", "Rewiring is permitted work. We file it and schedule rough and final inspections as required."),
              ("Wrap-up", "New outlets, switches and grounding in place, a labeled panel, and a clean house.")],
    timeline=[("Assessment and quote", "One visit, with a written plan to follow."), ("Partial rewiring", "Often a few days."), ("Whole-home rewiring", "Typically one to several weeks depending on the size of the house and access.")],
    expect=["A written, phased plan and price", "Honest guidance on what's urgent vs. what can wait", "Clear agreement on wall openings and patching before we start", "Daily cleanup and a working power plan so you're not left in the dark"],
    benefits=["Lower fire risk from aging or damaged wiring", "Grounded outlets for computers, appliances and surge protection", "Fewer insurance and home-sale headaches", "Wiring that can support modern loads like EV chargers and heat pumps"],
    faqs=[("Do I have to move out during a rewire?", "Usually not. We work in phases so most of the house stays powered. We'll plan around your schedule."),
          ("How much wall damage will there be?", "We fish wire through existing cavities wherever possible. Some openings are usually needed, and we'll show you where before starting and agree up front on patching."),
          ("Is knob-and-tube wiring dangerous?", "It was installed well for its time, but much of it is now 80 to 100 years old, ungrounded, and often has been modified or buried in insulation. Many insurers won't cover it. We'll assess yours and tell you honestly how urgent it is."),
          ("Can I rewire in stages?", "Yes. Many homeowners start with the most-used rooms or the riskiest circuits. We'll help you prioritize."),
          ("Is financing available?", "Ask us about financing options when we quote. For larger rewires it can make sense to phase the work too.")],
    related=["panel-upgrades", "outlets-switches", "lighting-ceiling-fans"],
    photos=[("Photo: old knob-and-tube wiring in an exposed joist bay next to new Romex runs, stapled neatly.", "Knob-and-tube replaced with modern cable."),
            ("Photo: a small, clean access hole in a plaster wall with a drop cloth below, used to fish new wire.", "Small access openings instead of torn-out walls.")],
  ),
  dict(
    slug="generators", name="Generators", nav="Generators", financing=True,
    card="Standby generators and safe portable-generator hookups so a storm doesn't knock out your heat or sump pump.",
    title="Generator Installation in Dorchester & Boston | JM Electrical Solutions",
    meta="Standby generator installation and portable generator transfer switches and interlocks for Boston homes. Licensed MA electrician #22667. 4.9★ from 100+ reviews.",
    h1="Generator Installation in Dorchester & Boston",
    intro="Nor'easters and summer storms take power out at the worst times. A generator keeps the heat, fridge, sump pump and medical equipment running. We'll help you decide between a standby unit and a portable generator with a proper transfer switch or interlock, and size it to what you actually need to keep on.",
    signs=["You lose heat, a sump pump or a fridge full of food when the power goes out", "Someone at home relies on medical equipment", "You use a portable generator with extension cords (which is risky) and want a safe hookup", "You work from home and can't afford downtime"],
    involved=[("Decide what to power", "We go through what you need on during an outage and size the system to match, so you're not overbuying."),
              ("Choose the setup", "A portable generator with an inlet and interlock or transfer switch is the budget option. A permanently installed standby generator starts automatically. We'll explain both."),
              ("Install", "We install the transfer switch or interlock, inlet and wiring. For standby units on natural gas or propane, the gas connection must be made by a licensed gas fitter; we'll tell you exactly what's needed."),
              ("Permit and test", "We file the electrical permit, test a full switchover, and show you how it works.")],
    timeline=[("Portable generator hookup", "Often done in a day."), ("Standby generator", "Several days of work, plus lead time for the unit and permits.")],
    expect=["A sizing recommendation based on what you actually need powered", "A clear quote that separates electrical work, equipment and gas work", "A full test and a walkthrough you'll remember during a storm"],
    benefits=["Heat, fridge and sump pump stay on during outages", "No dangerous extension cords or backfeeding the grid", "Automatic start with a standby unit", "Peace of mind for anyone on medical equipment"],
    faqs=[("Standby or portable: which do I need?", "If you want the house to switch over by itself and power a lot of circuits, standby. If you're comfortable rolling out a generator and powering essentials, a portable unit with a proper interlock or transfer switch is much cheaper."),
          ("Can I just plug my generator into an outlet?", "No. Backfeeding through an outlet is dangerous to you and to utility workers. An inlet with an interlock or transfer switch is the safe, code-compliant way."),
          ("Do you handle the gas line?", "Gas connections must be done by a licensed gas fitter. We handle all the electrical work and will be clear about what the gas work involves."),
          ("Is financing available?", "Ask us about financing options when we quote, especially for standby units.")],
    related=["panel-upgrades", "emergency-electrician", "ev-chargers"],
    photos=[("Photo: a standby generator on a level pad beside a Dorchester home, conduit and disconnect neatly mounted on the siding.", "Standby generator, cleanly installed."),
            ("Photo: a generator interlock kit installed on a residential panel with a labeled inlet box on the exterior wall.", "Safe portable-generator hookup.")],
  ),
  dict(
    slug="smart-home", name="Smart Home Automation", nav="Smart Home", financing=False,
    card="Smart switches, dimmers, doorbells and thermostats wired properly so they actually work reliably.",
    title="Smart Home Installation in Dorchester & Boston | JM Electrical Solutions",
    meta="Smart switches, dimmers, video doorbells, smart thermostats and lighting control installed by a licensed Boston electrician (#22667). Clean installs, clear explanations.",
    h1="Smart Home Installation in Dorchester & Boston",
    intro="Smart devices are only as good as the wiring behind them. Many smart switches need a neutral wire that older Boston homes don't always have in the switch box. We figure out what will work in your house, install it properly, and make sure you know how to use it before we leave.",
    signs=["You want lights you can control from your phone or on a schedule", "A smart switch you bought doesn't fit or won't power on", "You want a video doorbell or smart thermostat hardwired", "You're renovating and want to plan for smart lighting"],
    involved=[("Check compatibility", "We check your switch boxes, neutrals and existing wiring, and recommend devices that will actually work in your house."),
              ("Install and connect", "We install switches, dimmers, doorbells and thermostats and get them on your Wi-Fi and app."),
              ("Show you how", "We walk you through the app and basic schedules so it's useful from day one.")],
    timeline=[("A few devices", "Usually a few hours."), ("Whole-home lighting control", "Often a day or more depending on the number of devices.")],
    expect=["Honest advice on which devices fit your wiring", "Neat installs with no loose wires stuffed in boxes", "A quick training session before we leave"],
    benefits=["Control lighting from your phone or by schedule", "Wired doorbells and thermostats that don't need battery changes", "Lighting scenes and dimming that make rooms more usable", "Devices that work reliably because the wiring is right"],
    faqs=[("My smart switch needs a neutral wire. What if I don't have one?", "Some older boxes don't. We can run a neutral where practical, or recommend no-neutral devices that work with your setup."),
          ("Do you supply the devices?", "You can buy your own and we'll install them, or we can recommend devices that work well together."),
          ("Can you install a smart thermostat?", "Yes, for most common systems. We'll confirm your heating and cooling wiring is compatible first.")],
    related=["lighting-ceiling-fans", "outlets-switches", "ev-chargers"],
    photos=[("Photo: a row of new smart dimmers in a hallway, faceplates level, homeowner's phone showing the lighting app.", "Smart dimmers installed and connected."),
            ("Photo: a hardwired video doorbell on a Boston triple-decker front door frame.", "Hardwired video doorbell.")],
  ),
  dict(
    slug="outlets-switches", name="Outlets & Switches", nav="Outlets & Switches", financing=False,
    card="Dead outlets, GFCI and USB outlets, two-prong upgrades and new switches. Small jobs welcome.",
    title="Outlet & Switch Repair and Installation in Dorchester & Boston | JM Electrical",
    meta="Outlet repair, GFCI and USB outlets, two-prong to three-prong upgrades and new switches in Dorchester and Boston. Small jobs welcome. Licensed electrician #22667.",
    h1="Outlet & Switch Repair and Installation in Dorchester & Boston",
    intro="No job is too small. Whether it's one dead outlet, GFCI protection in the kitchen and bath, USB outlets, or swapping out two-prong outlets, we show up on time, fix it properly, and don't make you feel like a small job is a bother.",
    signs=["An outlet or switch stopped working", "Outlets are warm, loose, scorched or spark when you plug in", "No GFCI protection in kitchens, baths, basements or outside", "Two-prong outlets you want upgraded", "You need an outlet where there isn't one"],
    involved=[("Find the cause", "A dead outlet is often a tripped GFCI elsewhere or a loose connection. We find the actual cause instead of just swapping parts."),
              ("Repair or install", "We replace or add outlets and switches, add GFCI and AFCI protection where needed, and ground two-prong outlets properly or protect them to code."),
              ("Test", "Every device we touch gets tested before we leave.")],
    timeline=[("Most outlet and switch jobs", "An hour or two."), ("Adding new circuits or many outlets", "Often half a day to a day.")],
    expect=["On-time arrival and a clear price", "Fixes for the cause, not just the symptom", "No attitude about small jobs", "Clean-up before we go"],
    benefits=["Safer outlets in kitchens, baths and basements", "Grounded outlets for electronics and appliances", "USB-C and USB-A outlets where you charge devices", "Fewer extension cords and power strips"],
    faqs=[("Do you take small jobs like one outlet?", "Yes. Customers tell us they appreciate that we treat small jobs with the same care as big ones."),
          ("Can I just swap a two-prong outlet for a three-prong one?", "Not without a ground. Putting a three-prong outlet on an ungrounded circuit is a code violation and a safety risk. We can add a ground or install GFCI protection labeled correctly."),
          ("Why does my outlet feel warm?", "Warm outlets usually mean a loose connection or an overloaded circuit. Stop using it and call us. It's worth checking soon.")],
    related=["lighting-ceiling-fans", "rewiring", "smart-home", "emergency-electrician"],
    photos=[("Photo: a new GFCI outlet installed on a kitchen backsplash, faceplate straight and caulk line clean.", "GFCI protection at the kitchen counter."),
            ("Photo: a scorched old outlet held next to its replacement after a repair call.", "A scorched outlet we replaced.")],
  ),
  dict(
    slug="emergency-electrician", name="Emergency Electrical Service", nav="Emergency Service", financing=False,
    card="Power out to part of the house, a burning smell, sparking outlets or storm damage. Call now.",
    title="Emergency Electrician in Dorchester & Boston | JM Electrical Solutions",
    meta="Emergency electrical service in Dorchester, South Boston and Boston: partial power loss, burning smells, sparking outlets, storm damage. Call (978) 746-1993. MA License #22667.",
    h1="Emergency Electrician in Dorchester & Boston",
    intro="When something electrical goes wrong, you want someone who picks up, shows up and explains what happened. Call us directly. For emergencies, the phone is faster than the form.",
    signs=["Power is out to part of the house but neighbors have power", "A burning smell from an outlet, switch or panel", "Sparking, buzzing or scorched outlets or switches", "A breaker that keeps tripping or won't reset", "Water got into an outlet, fixture or panel", "Storm damage to the service mast or wires to your house"],
    involved=[("Call us", f"Call {PHONE} and tell us what you're seeing. We'll tell you what to do right now to stay safe."),
              ("Make it safe", "On site, our first job is to make the situation safe and stop the immediate problem."),
              ("Explain and fix", "We explain what caused it, what we fixed, and whether anything else needs attention later, with a clear price.")],
    timeline=[("First step", "Call and tell us what you're seeing."), ("On site", "We make it safe first. Any larger repair gets a clear quote before we do it.")],
    expect=["A real person who explains what's happening", "Safety first, then a clear explanation", "Honest pricing, even in an emergency", "A clean work area after the repair"],
    benefits=["Fast help from a licensed local electrician", "Clear explanations, not jargon", "Fair pricing when you're under pressure", "Follow-up recommendations so it doesn't happen again"],
    faqs=[("What should I do right now?", "If there's smoke, fire or a strong burning smell, get everyone out and call 911. If it's safe to do so, turn off the breaker for the affected circuit. Then call us."),
          ("A power line is down outside. Who do I call?", "Stay well away from it, keep others away, and call 911 and Eversource right away. Once the utility has made it safe, we can repair damage to your service mast, meter socket or panel."),
          ("Half my house has no power. Is that an emergency?", "Often, yes. Partial power loss can mean a failing main breaker or a problem with the service connection. Call us and we'll help you figure out if it's urgent."),
          ("Should I use the form for emergencies?", "No. Please call. The form is for non-urgent jobs.")],
    related=["panel-upgrades", "outlets-switches", "generators", "rewiring"],
    photos=[("Photo: Dan inspecting a scorched breaker with a flashlight inside an open panel during a service call.", "Diagnosing a failed breaker."),
            ("Photo: a storm-damaged service mast on a Dorchester triple-decker being repaired.", "Storm damage repair.")],
  ),
]
SVC = {s["slug"]: s for s in SERVICES}

PAGES_NAV = [("index.html", "Home"), ("services.html", "Services"), ("reviews.html", "Reviews"),
             ("about.html", "About"), ("service-areas.html", "Service Areas"), ("contact.html", "Contact")]

AREAS = {
  "Dorchester": ["Savin Hill", "Fields Corner", "Ashmont", "Adams Village", "Neponset", "Lower Mills", "Codman Square", "Uphams Corner", "Meeting House Hill", "Polish Triangle"],
  "South Boston": ["City Point", "Andrew Square", "West Broadway", "D Street area", "Seaport edge"],
  "Nearby Boston neighborhoods": ["Roxbury", "South End", "Jamaica Plain", "Mattapan", "Roslindale", "Hyde Park", "West Roxbury"],
}

# Review excerpts are SAMPLES written from themes in JM's real reviews. Each one
# is tagged on the page. Replace with verbatim Google review text before launch.
REVIEWS_SAMPLE = [
  ("Clean job site", "They put down drop cloths, cleaned up every bit of dust, and left the basement cleaner than before they arrived."),
  ("Clear explanations", "Jamie took the time to explain exactly what was wrong with our panel and what our options were. No pressure, no jargon."),
  ("Fair pricing", "The quote was fair and the final bill matched it. No surprises."),
  ("Punctual & responsive", "Called back the same day, showed up when they said they would, and kept us updated the whole way."),
  ("Small jobs, no attitude", "We only needed a couple of outlets fixed and they treated it like it mattered. We'll call them for the big stuff too."),
  ("Professional technicians", "Nic and Dan were professional, careful in our home and clearly knew what they were doing."),
]

# ---------------------------------------------------------------- shared parts
def business_schema():
    return {
      "@context": "https://schema.org", "@type": "Electrician", "@id": SITE_URL + "/#business",
      "name": BIZ, "url": SITE_URL + "/", "logo": SITE_URL + "/assets/img/jm-logo-horizontal.svg", "telephone": "+1-978-746-1993",
      "address": {"@type": "PostalAddress", "streetAddress": STREET, "addressLocality": CITY,
                  "addressRegion": REGION, "postalCode": ZIP, "addressCountry": "US"},
      "areaServed": [{"@type": "Place", "name": n + ", Boston, MA"} for n in ["Dorchester", "South Boston"]] + [{"@type": "City", "name": "Boston, MA"}],
      "hasCredential": {"@type": "EducationalOccupationalCredential", "credentialCategory": "license",
                        "name": "Massachusetts Electrical License " + LICENSE},
      "employee": [{"@type": "Person", "name": OWNER, "jobTitle": "Owner"}],
      "hasOfferCatalog": {"@type": "OfferCatalog", "name": "Electrical services",
                          "itemListElement": [{"@type": "Offer", "itemOffered": {"@type": "Service", "name": s["name"], "url": f"{SITE_URL}/{s['slug']}.html"}} for s in SERVICES]},
    }

def ld(obj): return '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False) + "</script>"

def head(title, desc, path, schemas=(), noindex=False):
    canon = SITE_URL + "/" + ("" if path == "index.html" else path)
    robots = '<meta name="robots" content="noindex">' if (noindex or PREVIEW) else ""
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
{robots}
<link rel="canonical" href="{canon}">
<meta property="og:type" content="website">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{canon}">
<meta name="theme-color" content="#0f2a44">
<link rel="icon" href="assets/img/jm-icon.svg" type="image/svg+xml">
<link rel="stylesheet" href="assets/css/styles.css">
{ld(business_schema())}
{''.join(ld(s) for s in schemas)}
</head>
<body>
<a class="skip-link" href="#main">Skip to main content</a>"""

def header(current):
    links = []
    for href, label in PAGES_NAV:
        cur = ' aria-current="page"' if href == current else ""
        links.append(f'<li><a href="{href}"{cur}>{label}</a></li>')
        if href == "services.html":
            for s in SERVICES:
                c2 = ' aria-current="page"' if s["slug"] + ".html" == current else ""
                links.append(f'<li class="sub"><a href="{s["slug"]}.html"{c2}>{s["nav"]}</a></li>')
    return f"""
<div class="topbar"><div class="container">
  <span>MA Electrical License #{LICENSE} · {ADDRESS}</span>
  <span><span class="stars" aria-hidden="true">★★★★★</span> {RATING} from {REVIEWS} Google reviews</span>
</div></div>
<header class="site-header">
  <div class="container header-inner">
    <a class="brand" href="index.html"><img src="assets/img/jm-logo-van.svg" alt="{BIZ} home" width="196" height="64"></a>
    <a class="header-call" href="{TEL}">{I_PHONE}<span>{PHONE}</span></a>
    <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="site-nav">Menu</button>
  </div>
  <nav id="site-nav" class="site-nav" aria-label="Main"><div class="container"><ul>{''.join(links)}</ul></div></nav>
</header>"""

def lead_form(pid, heading="Get a clear quote", note="Tell us what you need. We'll call you back to talk it through.", button="Request my quote", tag="h2"):
    return f"""<form class="lead-form js-lead" id="{pid}-form" action="thank-you.html" method="post" novalidate aria-labelledby="{pid}-title">
  <{tag} id="{pid}-title">{heading}</{tag}>
  <p class="form-note">{note}</p>
  <div class="field"><label for="{pid}-name">Name</label>
    <input id="{pid}-name" name="name" type="text" autocomplete="name" required>
    <p class="field-error" role="alert"></p></div>
  <div class="field"><label for="{pid}-phone">Phone</label>
    <input id="{pid}-phone" name="phone" type="tel" autocomplete="tel" inputmode="tel" required>
    <p class="field-error" role="alert"></p></div>
  <div class="field"><label for="{pid}-job">What do you need done?</label>
    <textarea id="{pid}-job" name="job" required placeholder="e.g. Replace an old fuse box, install an EV charger, outlet stopped working"></textarea>
    <p class="field-error" role="alert"></p></div>
  <div class="visually-hidden" aria-hidden="true"><label for="{pid}-company">Leave blank</label><input id="{pid}-company" name="company" tabindex="-1" autocomplete="off"></div>
  <button class="btn btn--primary btn--block" type="submit">{button}</button>
  <p class="form-status" aria-live="polite"></p>
  <p class="form-alt">Prefer to talk? <a href="{TEL}"><strong>Call {PHONE}</strong></a></p>
</form>"""

def trustbar():
    items = ["Licensed (MA #" + LICENSE + ")", "Insured", "Clean Work", "Fair Pricing", f"{RATING}★ ({REVIEWS} reviews)"]
    return '<section class="trustbar" aria-label="Why homeowners choose us"><div class="container"><ul>' + "".join(f"<li>{I_CHECK}{i}</li>" for i in items) + "</ul></div></section>"

def review_cards(items):
    out = []
    for topic, text in items:
        out.append(f"""<figure class="review"><span class="topic">{topic}</span>
<blockquote><p>“{text}”</p></blockquote>
<figcaption><span class="stars" aria-label="5 out of 5 stars">★★★★★</span> Google review <span class="ph-tag">Sample: swap for verbatim review</span></figcaption></figure>""")
    return '<div class="reviews">' + "".join(out) + "</div>"

def review_showcase(items, heading_tag="h2", more_link=True):
    """Dark 'Customer Reviews' panel over the office photo: rating card + review cards."""
    bg = ""
    if os.path.exists(os.path.join(OUT, "assets/img/office-sign.webp")):
        bg = ('<picture class="rs-bg"><source media="(max-width: 700px)" srcset="assets/img/office-sign-800.webp">'
              '<img src="assets/img/office-sign.webp" alt="" width="1600" height="744" loading="lazy" decoding="async"></picture>')
    cards = "".join(f"""<figure class="rs-card"><div class="rs-stars" aria-label="5 out of 5 stars">★★★★★</div>
<p class="rs-topic">{topic}</p><blockquote><p>{text}</p></blockquote>
<figcaption>Google review <span class="ph-tag">Sample: swap for verbatim review</span></figcaption></figure>""" for topic, text in items)
    more = f'<a class="rs-link" href="reviews.html">Read more reviews</a>' if more_link else ""
    return f"""<section class="review-show" aria-labelledby="rs-title">
  {bg}
  <div class="container rs-inner">
    <{heading_tag} id="rs-title" class="rs-title">Customer Reviews</{heading_tag}>
    <p class="rs-sub">Trusted by Dorchester &amp; Boston homeowners</p>
    <div class="rs-grid">
      <div class="rs-score">
        <div class="rs-score-top"><span class="rs-big">{RATING}</span>
          <div><div class="rs-stars rs-stars--big" aria-label="{RATING} out of 5 stars">★★★★★</div>
          <p class="rs-count">{REVIEWS} Google reviews</p></div></div>
        <a class="rs-btn" href="{GOOGLE_REVIEWS_URL}" rel="noopener">Write a review</a>
        <a class="rs-link" href="{GOOGLE_REVIEWS_URL}" rel="noopener">See all reviews on Google</a>
        {more}
      </div>
      <div class="rs-list">{cards}</div>
    </div>
  </div>
</section>"""

def photo(desc, caption):
    return f'<figure class="photo"><div class="ph" role="img" aria-label="{esc(caption)}">{esc(desc)}</div><figcaption>{esc(caption)} <span class="ph-tag">Photo placeholder</span></figcaption></figure>'

def real_photo(src, alt, caption, w, h):
    if not os.path.exists(os.path.join(OUT, src)):   # photo not uploaded yet: show the placeholder box
        return photo("Photo: " + alt + ".", caption)
    return f'<figure class="photo"><img src="{src}" alt="{esc(alt)}" width="{w}" height="{h}" loading="lazy" decoding="async"><figcaption>{esc(caption)}</figcaption></figure>'

JAMIE = ("assets/img/jamie-maguire-van.jpg", "Jamie Maguire standing beside the JM Electrical Solutions work van with ladders on the roof rack", "Owner Jamie Maguire with the JM Electrical van.", 520, 293)

def financing_box():
    return f"""<aside class="financing" aria-label="Financing">
<h3>Financing options available</h3>
<p>Bigger jobs like panel upgrades, EV chargers, rewiring and generators don't have to be paid for all at once. Ask about financing when we quote your job and we'll walk you through the options.</p>
<p><span class="ph-tag">Confirm lender, terms and wording with Jamie</span></p>
<a class="btn btn--call" href="{TEL}">{I_PHONE} Ask about financing: {PHONE}</a>
</aside>"""

def footer():
    svc = "".join(f'<li><a href="{s["slug"]}.html">{s["nav"]}</a></li>' for s in SERVICES)
    return f"""
<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div>
        <h2>{BIZ}</h2>
        <p>{STREET}<br>{CITY}, {REGION} {ZIP}<br><a href="{TEL}">{PHONE}</a></p>
        <p>Massachusetts Electrical License #{LICENSE}<br>Owner: {OWNER}</p>
        <p><span class="stars" aria-hidden="true">★★★★★</span> {RATING} from {REVIEWS} Google reviews</p>
      </div>
      <div><h2>Services</h2><ul>{svc}</ul></div>
      <div><h2>Company</h2><ul>
        <li><a href="about.html">About</a></li><li><a href="reviews.html">Reviews</a></li>
        <li><a href="service-areas.html">Service Areas</a></li><li><a href="contact.html">Contact</a></li></ul></div>
      <div><h2>Service Area</h2><p>Dorchester, South Boston and surrounding Boston neighborhoods.</p>
        <p><a href="{MAPS_URL}" rel="noopener">Get directions</a></p></div>
    </div>
    <div class="footer-legal">© <span id="year">2026</span> {BIZ}. All rights reserved.</div>
  </div>
</footer>
<div class="mobile-callbar">
  <a class="btn btn--call" href="{TEL}">{I_PHONE} Call now</a>
  <a class="btn btn--primary" href="#quote">Get a quote</a>
</div>
<script src="assets/js/main.js" defer></script>
</body>
</html>"""

def breadcrumbs(trail):
    lis = "".join(f'<li><a href="{h}">{t}</a></li>' if h else f'<li aria-current="page">{t}</li>' for t, h in trail)
    schema = {"@context": "https://schema.org", "@type": "BreadcrumbList",
              "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": t, **({"item": f"{SITE_URL}/{h}"} if h else {})} for i, (t, h) in enumerate(trail)]}
    return f'<nav class="breadcrumbs" aria-label="Breadcrumb"><ol>{lis}</ol></nav>', schema

def call_cta(text="Call now"):
    return f'<a class="btn btn--call" href="{TEL}">{I_PHONE} {text}: {PHONE}</a>'

def write(name, body):
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        f.write(body)

# ---------------------------------------------------------------- homepage
def hero_img():
    # Brand image behind the homepage hero; skipped if the file isn't deployed
    if not os.path.exists(os.path.join(OUT, "assets/img/hero-fleet.webp")):
        return ""
    return ('<picture class="hero-bg"><source media="(max-width: 700px)" srcset="assets/img/hero-fleet-800.webp">'
            '<img src="assets/img/hero-fleet.webp" alt="" width="1600" height="900" fetchpriority="high" decoding="async"></picture>')

def home():
    HERO_IMG = hero_img()
    cards = "".join(f'<article class="card"><h3><a href="{s["slug"]}.html">{s["name"]}</a></h3><p>{s["card"]}</p><a class="more" href="{s["slug"]}.html" aria-label="Learn more about {s["name"]}">Learn more</a></article>' for s in SERVICES)
    body = head("Licensed Electrician in Dorchester & Boston, MA | JM Electrical Solutions",
                f"JM Electrical Solutions: licensed residential electrician in Dorchester, South Boston and Boston. Panel upgrades, EV chargers, lighting, rewiring. {RATING}★ from {REVIEWS} Google reviews. Call {PHONE}.",
                "index.html")
    body += header("index.html")
    body += f"""
<main id="main">
<section class="hero{' hero--photo' if HERO_IMG else ''}">
  {HERO_IMG}
  <div class="container hero-grid">
    <div>
      <p class="eyebrow"><span class="stars" aria-hidden="true">★★★★★</span> {RATING} from {REVIEWS} Google reviews</p>
      <h1>Licensed Electrician Serving Dorchester &amp; Boston</h1>
      <p class="hero-sub">Panel upgrades, EV chargers, lighting, rewiring and repairs for Boston homeowners. We show up on time, explain everything clearly, quote fairly, and clean up before we leave.</p>
      <a class="hero-phone" href="{TEL}">{I_PHONE}{PHONE}</a>
      <ul class="badges">
        <li class="badge"><span class="stars" aria-hidden="true">★</span> {RATING}★ · {REVIEWS} Google reviews</li>
        <li class="badge">{I_CHECK.replace('<svg', '<svg width="16" height="16"')} MA License #{LICENSE}</li>
        <li class="badge badge--owner">Owner-operated by {OWNER}</li>
      </ul>
      <p class="lead hide-sm" style="font-size:1rem">Based at {STREET}. Serving Dorchester, South Boston and surrounding Boston neighborhoods.</p>
    </div>
    <div id="quote">{lead_form("hero", heading="Get a clear quote", note="Three quick fields. We'll call you back to talk it through.")}</div>
  </div>
</section>
{trustbar()}
{review_showcase([REVIEWS_SAMPLE[0], REVIEWS_SAMPLE[1], REVIEWS_SAMPLE[2]])}

<section class="section" aria-labelledby="process-title">
  <div class="container">
    <h2 id="process-title" class="center">How it works</h2>
    <p class="lead center">No runaround and no surprises. Just four straightforward steps.</p>
    <ol class="steps">
      <li><h3>Call</h3><p>Call or send the form. Tell us what's going on and we'll set up a time.</p></li>
      <li><h3>Diagnose</h3><p>We find the actual cause and explain it in plain English, with options when there are options.</p></li>
      <li><h3>Clear quote</h3><p>You get a clear price before work starts. The bill matches the quote.</p></li>
      <li><h3>Clean finish</h3><p>Work done to code, tested, and the area cleaned up. Drop cloths down, dust gone.</p></li>
    </ol>
  </div>
</section>

<section class="section section--soft" aria-labelledby="services-title">
  <div class="container">
    <h2 id="services-title">Residential electrical services</h2>
    <p class="lead">Small fixes and big projects, handled with the same care. We also take on light commercial work.</p>
    <div class="cards">{cards}</div>
  </div>
</section>



<section class="section section--soft" aria-labelledby="bigjob-title">
  <div class="container">
    <div class="bigjob">
      <h2 id="bigjob-title">Planning a bigger project?</h2>
      <p>Panel upgrades, EV chargers, generators and whole-home rewiring are investments. We'll give you a written plan and a clear quote, size the work once so you don't pay twice, and handle the permits and inspection.</p>
      <ul>
        <li>Panel upgrades sized for EV chargers, heat pumps and renovations</li>
        <li>Level 2 EV chargers with an honest panel check first</li>
        <li>Whole-home and partial rewiring for older Boston homes</li>
      </ul>
      <p><strong>Financing options available.</strong> Ask when we quote. <span class="ph-tag">Confirm lender &amp; terms</span></p>
      <div class="btn-row">
        <a class="btn btn--call" href="{TEL}">{I_PHONE} Talk through your project: {PHONE}</a>
        <a class="btn btn--ghost" href="panel-upgrades.html">Panel upgrades</a>
        <a class="btn btn--ghost" href="ev-chargers.html">EV chargers</a>
      </div>
    </div>
  </div>
</section>

<section class="section" aria-labelledby="team-title">
  <div class="container layout">
    <div>
      <h2 id="team-title">A local electrician who explains the work</h2>
      <p>{BIZ} is run by {OWNER} out of {STREET} in Dorchester. Jamie and technicians Nic and Dan are the people who show up at your door. Reviewers mention them by name for being professional, punctual and easy to deal with.</p>
      <ul class="checklist">
        <li>Licensed Massachusetts electrician, license #{LICENSE}</li>
        <li>Small jobs and big projects, without attitude</li>
        <li>Clear explanations and a quote before work starts</li>
        <li>Clean, careful work in your home</li>
      </ul>
      <p><a href="about.html"><strong>More about us</strong></a> · <a href="service-areas.html"><strong>Where we work</strong></a></p>
    </div>
    <div>{real_photo(*JAMIE)}</div>
  </div>
</section>

<section class="section section--navy center" aria-labelledby="final-title">
  <div class="container">
    <h2 id="final-title">Need an electrician in Dorchester or Boston?</h2>
    <p class="lead">Call now, or send three quick details and we'll call you back.</p>
    <div style="display:flex;flex-wrap:wrap;gap:12px;justify-content:center">
      {call_cta("Call")}
      <a class="btn btn--ghost" href="#quote">Request a quote</a>
    </div>
  </div>
</section>
</main>"""
    body += footer()
    write("index.html", body)

# ---------------------------------------------------------------- service pages
def service_page(s):
    path = s["slug"] + ".html"
    crumbs_html, crumbs_schema = breadcrumbs([("Home", "index.html"), ("Services", "services.html"), (s["name"], None)])
    service_schema = {"@context": "https://schema.org", "@type": "Service", "name": s["name"], "serviceType": s["name"],
                      "provider": {"@id": SITE_URL + "/#business"}, "url": f"{SITE_URL}/{path}",
                      "areaServed": ["Dorchester, Boston, MA", "South Boston, Boston, MA", "Boston, MA"], "description": s["meta"]}
    faq_schema = {"@context": "https://schema.org", "@type": "FAQPage",
                  "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in s["faqs"]]}
    involved = "".join(f"<li><h3>{t}</h3><p>{d}</p></li>" for t, d in s["involved"])
    timeline = "".join(f"<div><strong>{t}</strong>{d}</div>" for t, d in s["timeline"])
    faqs = "".join(f"<details><summary>{q}</summary><div><p>{a}</p></div></details>" for q, a in s["faqs"])
    related = "".join(f'<li><a href="{r}.html">{SVC[r]["name"]}</a></li>' for r in s["related"])
    signs = "".join(f"<li>{x}</li>" for x in s["signs"])
    expect = "".join(f"<li>{x}</li>" for x in s["expect"])
    benefits = "".join(f"<li>{x}</li>" for x in s["benefits"])
    is_emergency = s["slug"] == "emergency-electrician"
    form_note = "Not urgent? Send three quick details and we'll call you back. For emergencies, please call." if is_emergency else "Three quick fields. We'll call you back to talk it through."
    review_pick = [REVIEWS_SAMPLE[0], REVIEWS_SAMPLE[1]] if not is_emergency else [REVIEWS_SAMPLE[3], REVIEWS_SAMPLE[1]]

    body = head(s["title"], s["meta"], path, [service_schema, faq_schema, crumbs_schema])
    body += header(path)
    body += f"""
<main id="main">
<section class="page-hero">
  <div class="container">
    {crumbs_html}
    <h1>{s["h1"]}</h1>
    <p class="hero-sub">{s["intro"]}</p>
    <div style="display:flex;flex-wrap:wrap;gap:12px;align-items:center;margin-top:12px">
      {call_cta("Call now" if is_emergency else "Call")}
      <a class="btn btn--ghost" href="#quote" style="color:var(--navy)">Get a quote</a>
    </div>
    <ul class="badges" style="margin-top:16px">
      <li class="badge"><span class="stars" aria-hidden="true">★</span> {RATING}★ · {REVIEWS} Google reviews</li>
      <li class="badge">MA License #{LICENSE}</li>
      <li class="badge">Known for clean job sites</li>
    </ul>
  </div>
</section>
{trustbar()}
<div class="section">
  <div class="container layout">
    <article class="content">
      <h2>{"Signs you need help now" if is_emergency else "When homeowners call us for this"}</h2>
      <ul class="checklist">{signs}</ul>

      <h2>What's involved</h2>
      <ol class="steps" style="grid-template-columns:1fr">{involved}</ol>

      <div class="cards" style="grid-template-columns:repeat(auto-fit,minmax(240px,1fr))">
        {photo(*s["photos"][0])}
        {photo(*s["photos"][1])}
      </div>

      <h2>Typical timeline <span class="ph-tag">Confirm timing with Jamie</span></h2>
      <div class="timeline">{timeline}</div>

      <h2>What to expect from us</h2>
      <ul class="checklist">{expect}</ul>

      <h2>Benefits</h2>
      <ul class="checklist">{benefits}</ul>

      {financing_box() if s["financing"] else ""}

      <h2>Why Dorchester and Boston homeowners choose {BIZ}</h2>
      <p>Licensed Massachusetts electrician (#{LICENSE}), {RATING}★ from {REVIEWS} Google reviews, and a reputation for leaving every job site clean. Owner {OWNER} and technicians Nic and Dan explain the work clearly and quote fairly.</p>
      {review_cards(review_pick)}

      <section class="faq" aria-labelledby="faq-title">
        <h2 id="faq-title">{s["name"]} FAQ</h2>
        {faqs}
      </section>

      <h2>Related services</h2>
      <ul class="related">{related}</ul>
    </article>
    <aside class="sidebar" id="quote">
      {lead_form("svc", heading=("Non-urgent request" if is_emergency else f"Get a quote: {s['name']}"), note=form_note, tag="h2")}
      <div class="trust-box">
        <ul class="checklist">
          <li>MA Electrical License #{LICENSE}</li>
          <li>{RATING}★ from {REVIEWS} Google reviews</li>
          <li>Clean work, clear quotes</li>
          <li>{STREET}, {CITY}</li>
        </ul>
      </div>
    </aside>
  </div>
</div>
</main>"""
    body += footer()
    write(path, body)

# ---------------------------------------------------------------- other pages
def simple_page(path, title, desc, h1, intro, content, crumb, form_heading="Get a clear quote", schemas=(), noindex=False, form=True, feature=""):
    crumbs_html, crumbs_schema = breadcrumbs([("Home", "index.html"), (crumb, None)])
    body = head(title, desc, path, [crumbs_schema, *schemas], noindex=noindex)
    body += header(path)
    side = f'<aside class="sidebar" id="quote">{lead_form("pg", heading=form_heading)}</aside>' if form else ""
    body += f"""
<main id="main">
<section class="page-hero"><div class="container">
  {crumbs_html}
  <h1>{h1}</h1>
  <p class="hero-sub">{intro}</p>
  {call_cta("Call")}
</div></section>
{feature or trustbar()}
<div class="section"><div class="container layout"><div class="content">{content}</div>{side}</div></div>
</main>"""
    body += footer()
    write(path, body)

def services_index():
    cards = "".join(f'<article class="card"><h3><a href="{s["slug"]}.html">{s["name"]}</a></h3><p>{s["card"]}</p><a class="more" href="{s["slug"]}.html" aria-label="Learn more about {s["name"]}">Learn more</a></article>' for s in SERVICES)
    content = f"""<h2>Everything electrical for your home</h2>
<div class="cards" style="grid-template-columns:repeat(auto-fit,minmax(220px,1fr))">{cards}</div>
<h2>Light commercial work</h2>
<p>We also handle light commercial electrical work for small shops and offices in the area. Call to talk through your project.</p>"""
    simple_page("services.html", "Electrical Services in Dorchester & Boston | JM Electrical Solutions",
                f"Residential electrical services in Dorchester and Boston: panel upgrades, EV chargers, lighting, rewiring, generators, smart home, outlets and emergency service. License #{LICENSE}.",
                "Electrical Services in Dorchester &amp; Boston", "From a single dead outlet to a full panel upgrade, here's what we do for Boston homeowners.", content, "Services")

def about():
    content = f"""<h2>Who we are</h2>
<p>{BIZ} is a licensed Massachusetts electrical contractor (license #{LICENSE}) based at {STREET} in Dorchester. Owner {OWNER} runs the business and is on the tools, along with technicians Nic and Dan.</p>
<p><span class="ph-tag">Add Jamie's background: years in the trade, how JM started, any certifications</span></p>
{real_photo(*JAMIE)}
<h2>How we work</h2>
<p>Our reviews keep coming back to the same few things, and they're the things we care about most:</p>
<ul class="checklist">
  <li><strong>Clean job sites.</strong> Drop cloths down, dust contained, and we clean up before we leave.</li>
  <li><strong>Clear explanations.</strong> We tell you what's wrong, what your options are, and what we recommend, in plain English.</li>
  <li><strong>Fair pricing.</strong> You get a clear quote before work starts.</li>
  <li><strong>Punctual and responsive.</strong> We return calls and show up when we say we will.</li>
  <li><strong>No job too small.</strong> One outlet or a full rewire, same care and no attitude.</li>
</ul>
<h2>The team</h2>
<div class="cards" style="grid-template-columns:repeat(auto-fit,minmax(200px,1fr))">
  <article class="card"><h3>Jamie</h3><p>Owner. <span class="ph-tag">Add a line about Jamie</span></p></article>
  <article class="card"><h3>Nic</h3><p>Technician. <span class="ph-tag">Add a line about Nic</span></p></article>
  <article class="card"><h3>Dan</h3><p>Technician. <span class="ph-tag">Add a line about Dan</span></p></article>
</div>
<h2>Licensed and accountable</h2>
<p>Massachusetts Electrical License #{LICENSE}. We pull permits for work that requires them and schedule inspections. <span class="ph-tag">Confirm insurance details</span></p>
<p><a href="reviews.html"><strong>Read what customers say</strong></a> · <a href="services.html"><strong>See our services</strong></a></p>"""
    simple_page("about.html", f"About {BIZ} | Licensed Electrician in Dorchester, Boston",
                f"Meet {OWNER} and the team at {BIZ}, a licensed Massachusetts electrician (#{LICENSE}) at {ADDRESS}. Clean work, clear explanations, fair pricing.",
                f"About {BIZ}", f"A Dorchester-based electrical contractor run by {OWNER}. Known for clean work, clear explanations and fair prices.", content, "About")

def reviews():
    content = f"""<h2><span class="stars" aria-hidden="true">★★★★★</span> {RATING} out of 5 from {REVIEWS} Google reviews</h2>
<p>These are the themes that come up most often in our reviews. <a href="{GOOGLE_REVIEWS_URL}" rel="noopener"><strong>Read every review on Google</strong></a>.</p>
{review_cards(REVIEWS_SAMPLE)}
<h2>Worked with us?</h2>
<p>Reviews help other Boston homeowners find a good electrician. <a href="{GOOGLE_REVIEWS_URL}" rel="noopener">Leave us a Google review</a>.</p>
<p><span class="ph-tag">Before launch: replace each sample with a verbatim Google review (first name + last initial, with permission)</span></p>"""
    simple_page("reviews.html", f"Reviews | {RATING}★ Electrician in Dorchester & Boston | {BIZ}",
                f"{BIZ} has {RATING}★ from {REVIEWS} Google reviews. Homeowners in Dorchester and Boston mention clean job sites, clear explanations and fair pricing.",
                "Reviews from Boston Homeowners", f"{RATING}★ from {REVIEWS} Google reviews. Here's what keeps coming up.", content, "Reviews",
                feature=review_showcase(REVIEWS_SAMPLE[:3], more_link=False))

def contact():
    content = f"""<h2>Call or send a quick request</h2>
<p><a class="hero-phone" href="{TEL}">{I_PHONE}{PHONE}</a></p>
<p><strong>{BIZ}</strong><br>{STREET}<br>{CITY}, {REGION} {ZIP}<br><a href="{MAPS_URL}" rel="noopener">Get directions</a></p>
<p><strong>Hours:</strong> <span class="ph-tag">Add business hours</span></p>
<p><strong>Electrical emergency?</strong> Please call rather than using the form. If there's smoke or fire, call 911 first.</p>
<h2>Service area</h2>
<p>Dorchester, South Boston and surrounding Boston neighborhoods. <a href="service-areas.html">See the full list</a>.</p>"""
    simple_page("contact.html", f"Contact {BIZ} | Electrician in Dorchester, Boston | {PHONE}",
                f"Contact {BIZ} at {PHONE} or {ADDRESS}. Licensed electrician #{LICENSE} serving Dorchester, South Boston and Boston.",
                f"Contact {BIZ}", "Call us, or send three quick details and we'll call you back.", content, "Contact", form_heading="Send a quick request")

def service_areas():
    blocks = "".join(f'<h2>{area}</h2><ul class="areas">' + "".join(f"<li>{n}</li>" for n in subs) + "</ul>" for area, subs in AREAS.items())
    svc_links = "".join(f'<li><a href="{s["slug"]}.html">{s["name"]}</a></li>' for s in SERVICES)
    content = f"""<p>We're based at {STREET} in Dorchester, so we're close to most of our customers in Dorchester and South Boston, and we work across surrounding Boston neighborhoods.</p>
<p><span class="ph-tag">Confirm the neighborhood list with Jamie</span></p>
{blocks}
<h2>Services in your neighborhood</h2>
<ul class="related">{svc_links}</ul>
<p>Not sure if you're in our area? <a href="{TEL}">Call {PHONE}</a> and ask.</p>"""
    simple_page("service-areas.html", f"Service Areas: Dorchester, South Boston & Boston | {BIZ}",
                f"{BIZ} serves Dorchester, South Boston and surrounding Boston neighborhoods from {ADDRESS}. Licensed electrician #{LICENSE}.",
                "Electrician Serving Dorchester, South Boston &amp; Boston", "Local, licensed and close by.", content, "Service Areas")

def thank_you():
    content = f"""<h2>What happens next</h2>
<ol><li>We read your request.</li><li>We call you back to ask a couple of questions and set up a time.</li><li>You get a clear quote before any work starts.</li></ol>
<p>Need us sooner? <a href="{TEL}"><strong>Call {PHONE}</strong></a>.</p>
<p><a href="index.html">Back to home</a></p>"""
    simple_page("thank-you.html", f"Thanks, we got your request | {BIZ}", "Thanks for contacting JM Electrical Solutions.",
                "Thanks. We got your request.", "We'll call you back to talk it through.", content, "Thank you", noindex=True, form=False)

def seo_files():
    pages = ["", "services.html"] + [s["slug"] + ".html" for s in SERVICES] + ["reviews.html", "about.html", "service-areas.html", "contact.html"]
    urls = "".join(f"<url><loc>{SITE_URL}/{p}</loc></url>" for p in pages)
    write("sitemap.xml", f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n')
    write("robots.txt", "User-agent: *\nDisallow: /\n" if PREVIEW else f"User-agent: *\nAllow: /\nSitemap: {SITE_URL}/sitemap.xml\n")


# Logo + favicon (same output as logo.py, embedded so the site builds without fontTools)
LOGO_SVG = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 516 186" width="516" height="186" role="img" aria-label="JM Electrical Solutions"><title>JM Electrical Solutions</title><defs><linearGradient id="jmg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1f6fd1"/><stop offset=".75" stop-color="#0f2a44"/></linearGradient></defs><g transform="translate(40,20)"><g transform="skewX(-12)"><path d="M0 60H16V82H24V0H140V100H122V18H91L88 58H106L72 142L78 84H63L73 18H42V100H0Z" fill="url(#jmg)"/></g></g><g fill="#0f2a44"><path transform="translate(190,64)" d="M0.1 0H24.1L25.3 -7.3H10.4L11.3 -13.3H25.1L26.3 -20.5H12.5L13.5 -26.1H28.5L29.7 -33.5H5.6ZM30.5 0H53.1L54.3 -7.3H40.8L45.1 -33.5H36.1ZM58.4 0H82.4L83.6 -7.3H68.7L69.6 -13.3H83.4L84.6 -20.5H70.8L71.8 -26.1H86.8L88 -33.5H63.9ZM104.8 0.4C114.4 0.4 120.3 -6.5 121.7 -12.2H112.5C111.5 -9.4 109 -7.5 105.4 -7.5C101.9 -7.5 100 -9.4 100 -13.4C100 -19.1 103 -26 109.4 -26C112.6 -26 114 -24.1 113.9 -21.2H123.1C123.6 -29.4 118 -33.9 109.6 -33.9C98.1 -33.9 90.8 -24.5 90.8 -13.3C90.8 -4.4 96.5 0.4 104.8 0.4ZM128.5 -26.1H138.5L134.2 0H143.2L147.6 -26.1H157.6L158.8 -33.5H129.7ZM158.5 0H167.6L169.4 -11.1H172.5L176.6 0H186.5L181.7 -12.5C185.6 -14.2 188.3 -17.5 189 -22.1C190.2 -29.2 185.9 -33.5 178.5 -33.5H164ZM170.6 -18.1 171.9 -26.2H175.1C178.3 -26.2 180 -25 179.5 -22.1C179.1 -19.2 177 -18.1 173.7 -18.1ZM205.7 -33.5H196.6L191.1 0H200.1ZM222.3 0.4C231.8 0.4 237.7 -6.5 239.1 -12.2H229.9C229 -9.4 226.4 -7.5 222.9 -7.5C219.4 -7.5 217.5 -9.4 217.5 -13.4C217.5 -19.1 220.5 -26 226.9 -26C230 -26 231.5 -24.1 231.4 -21.2H240.6C241.1 -29.4 235.4 -33.9 227 -33.9C215.6 -33.9 208.3 -24.5 208.3 -13.3C208.3 -4.4 214 0.4 222.3 0.4ZM241.4 0H251.9L254.8 -6.4H265.1L266 0H275.9L270.2 -33.5H257.8ZM257.9 -13.2C259.7 -17.3 261.4 -21.7 263 -26C263.3 -21.7 263.7 -17.3 264.2 -13.2ZM280.9 0H303.5L304.8 -7.3H291.2L295.6 -33.5H286.5Z"/><path transform="translate(190,120)" d="M14.2 0.4C22.6 0.4 27.8 -3.3 28.9 -9.9C29.7 -15 27.2 -18.5 20.1 -20.1L17.5 -20.7C14.4 -21.4 13.2 -22.3 13.5 -23.9C13.7 -25.4 15.2 -26.5 18 -26.5C20.9 -26.5 22.1 -25.2 21.9 -23H30.6C31.6 -29.6 26.8 -33.9 18.7 -33.9C10.7 -33.9 5 -29.6 3.9 -23.3C3.1 -18 6.2 -15.1 11.9 -13.8L15.1 -13.1C18.7 -12.3 19.9 -11.4 19.6 -9.9C19.4 -8.2 17.6 -7.1 14.7 -7.1C11.2 -7.1 9.4 -8.7 9.8 -11.8H1.2C-0.2 -3.4 5.4 0.4 14.2 0.4ZM48.6 0.4C60.1 0.4 67.5 -8.8 67.5 -20C67.5 -29 61.6 -33.9 53.4 -33.9C41.9 -33.9 34.5 -24.6 34.5 -13.4C34.5 -4.5 40.4 0.4 48.6 0.4ZM49 -7.5C45.5 -7.5 43.8 -9.5 43.8 -13.3C43.8 -19 46.5 -26 53 -26C56.5 -26 58.3 -24 58.3 -20.1C58.3 -14.5 55.6 -7.5 49 -7.5ZM70.1 0H92.7L93.9 -7.3H80.4L84.7 -33.5H75.6ZM112.8 0.4C121.1 0.4 127.5 -4.1 128.8 -11.7L132.4 -33.5H123.3L119.9 -13.1C119.4 -10 116.5 -7.5 113.2 -7.5C110.3 -7.5 108.6 -9.4 109.1 -12.5L112.6 -33.5H103.5L100 -12.3C98.7 -4.7 103.9 0.4 112.8 0.4ZM136.4 -26.1H146.4L142.1 0H151.2L155.5 -26.1H165.5L166.7 -33.5H137.6ZM181 -33.5H172L166.4 0H175.5ZM197.7 0.4C209.2 0.4 216.6 -8.8 216.6 -20C216.6 -29 210.7 -33.9 202.5 -33.9C191 -33.9 183.6 -24.6 183.6 -13.4C183.6 -4.5 189.5 0.4 197.7 0.4ZM198.1 -7.5C194.6 -7.5 192.8 -9.5 192.8 -13.3C192.8 -19 195.6 -26 202.1 -26C205.6 -26 207.4 -24 207.4 -20.1C207.4 -14.5 204.7 -7.5 198.1 -7.5ZM219.2 0H228.5L230.5 -12.2C230.9 -14.4 231.3 -18.1 231.6 -21.9C232.7 -18.2 233.5 -15.6 235 -12.2L240.4 0H250.3L255.8 -33.5H246.5L244.4 -21.2C244 -18.8 243.6 -14.6 243.3 -11.2C242.5 -15 241.6 -17.6 240.4 -20.3L234.6 -33.5H224.7ZM270.5 0.4C279 0.4 284.1 -3.3 285.2 -9.9C286.1 -15 283.6 -18.5 276.5 -20.1L273.8 -20.7C270.8 -21.4 269.6 -22.3 269.9 -23.9C270.1 -25.4 271.5 -26.5 274.3 -26.5C277.3 -26.5 278.5 -25.2 278.3 -23H287C288 -29.6 283.1 -33.9 275 -33.9C267.1 -33.9 261.3 -29.6 260.3 -23.3C259.4 -18 262.5 -15.1 268.2 -13.8L271.5 -13.1C275.1 -12.3 276.2 -11.4 276 -9.9C275.7 -8.2 274 -7.1 271.1 -7.1C267.6 -7.1 265.8 -8.7 266.1 -11.8H257.5C256.2 -3.4 261.8 0.4 270.5 0.4Z"/></g><rect x="190" y="78" width="307" height="5" fill="#f2a900"/></svg>\n'
ICON_SVG = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="200" height="200" role="img" aria-label="JM Electrical Solutions"><title>JM Electrical Solutions</title><defs><linearGradient id="jmg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1f6fd1"/><stop offset=".75" stop-color="#0f2a44"/></linearGradient></defs><rect width="200" height="200" rx="36" fill="#0f2a44"/><g transform="translate(42,34) scale(.92)"><g transform="skewX(-12)"><path d="M0 60H16V82H24V0H140V100H122V18H91L88 58H106L72 142L78 84H63L73 18H42V100H0Z" fill="#ffffff"/></g></g></svg>\n'

def write_logos():
    os.makedirs(os.path.join(OUT, "assets", "img"), exist_ok=True)
    for name, data in (("jm-logo-horizontal.svg", LOGO_SVG), ("jm-icon.svg", ICON_SVG)):
        path = os.path.join(OUT, "assets", "img", name)
        if not os.path.exists(path):
            write(os.path.join("assets", "img", name), data)

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    write_logos()
    home(); services_index()
    for s in SERVICES: service_page(s)
    about(); reviews(); contact(); service_areas(); thank_you(); seo_files()
    print("built", len(os.listdir(OUT)), "entries in", os.path.abspath(OUT))
