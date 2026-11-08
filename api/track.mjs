// Proposal read alerts (copied from the EAS build, 20 Oct 2026), as a plain Vercel function for this static site.
// The page is /proposal/; send each person their own /proposal/?p=<code> link. Edit only the PROPOSAL block.
// Needs RESEND_API_KEY and ALERT_FROM in Vercel (link the shared variables). Emails Tim only, never the prospect.
const PROPOSAL = {
  business: "JM Electrical Solutions",
  depositLabel: "Pay the $1,750 deposit", // button text the deposit alert quotes
  prospects: {
    // link code -> name shown in the alert. Send each person their own ?p= link.
    // Add one code per person once Tim names them, e.g. jamie: "Jamie Maguire (JM Electrical Solutions)".
    jamie: "Jamie Maguire (JM Electrical Solutions)",
    test: "Test visit (Tim)",
  },
};
const ALERT_TO = "tim@airocket.pro";

function fmt(sec) {
  const s = Math.max(0, Math.round(sec));
  return s >= 60 ? `${Math.floor(s / 60)} min ${s % 60} s` : `${s} s`;
}

function eastern(d) {
  return d.toLocaleString("en-US", { timeZone: "America/New_York", dateStyle: "medium", timeStyle: "short" });
}

async function handle(request) {
  let body;
  try {
    body = await request.json();
  } catch {
    return new Response(null, { status: 400 });
  }
  const who = typeof body.p === "string" ? PROPOSAL.prospects[body.p] : undefined;
  if (!who) return new Response(null, { status: 204 });

  const kind = body.kind === "open" || body.kind === "deposit" || body.kind === "leave" ? body.kind : null;
  if (!kind) return new Response(null, { status: 400 });

  const when = eastern(new Date());
  const ua = request.headers.get("user-agent") ?? "";
  const device = /iPhone|Android|Mobile/i.test(ua) ? "phone" : "computer";
  const city = request.headers.get("x-vercel-ip-city");
  const where = city ? decodeURIComponent(city) : null;
  const name = PROPOSAL.business;

  let subject;
  let text;
  if (kind === "open") {
    subject = `${who} opened your proposal`;
    text = `${who} opened the ${name} proposal at ${when} ET on a ${device}${where ? ` near ${where}` : ""}.`;
  } else if (kind === "deposit") {
    subject = `${who} clicked the deposit button`;
    text = `${who} clicked "${PROPOSAL.depositLabel}" at ${when} ET. Check Stripe to see whether payment went through.`;
  } else {
    const rows = Array.isArray(body.sections)
      ? body.sections
          .filter((r) => Array.isArray(r) && typeof r[0] === "string" && typeof r[1] === "number")
          .filter(([, sec]) => sec >= 2)
          .slice(0, 30)
      : [];
    const total = typeof body.seconds === "number" ? body.seconds : rows.reduce((a, [, s]) => a + s, 0);
    subject = `${who} read your proposal for ${fmt(total)}`;
    text = [
      `${who} left the ${name} proposal at ${when} ET after ${fmt(total)} on the page (${device}).`,
      "",
      "Time on each section:",
      ...(rows.length ? rows.map(([title, sec]) => `- ${title.slice(0, 120)}: ${fmt(sec)}`) : ["- (no section read for 2 seconds or more)"]),
    ].join("\n");
  }

  console.log(`[proposal-track] ${subject}\n${text}`);

  const key = (process.env.RESEND_API_KEY || "").trim(); // the shared value has a stray line break
  const from = (process.env.ALERT_FROM || "").trim();
  if (key && from) {
    const r = await fetch("https://api.resend.com/emails", {
      method: "POST",
      headers: { Authorization: `Bearer ${key}`, "Content-Type": "application/json" },
      body: JSON.stringify({ from, to: [ALERT_TO], subject, text }),
    }).catch((e) => console.error("[proposal-track] email failed", e && e.name));
    if (r && !r.ok) console.error("[proposal-track] email failed", r.status, await r.text().catch(() => ""));
  } else console.error("[proposal-track] email skipped: RESEND_API_KEY or ALERT_FROM missing");
  return new Response(null, { status: 204 });
}

export function POST(request) {
  return handle(request);
}
