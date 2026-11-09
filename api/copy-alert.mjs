// Copy alert (Tim, 9 Nov 2026): the site's pages show an "Unlicensed copy" banner and ping this endpoint when they
// are opened anywhere other than AI Rocket's own addresses (Vercel links, jmelectric.airocket.pro, and after launch jmelectricsolutions.com).
// It reports only the web address the copy runs on. No visitor details are sent or stored.
// Needs RESEND_API_KEY and ALERT_FROM in Vercel (same shared variables as the proposal alerts). Emails Tim only.
const ALERT_TO = "tim@airocket.pro";
const DESIGN = "JM Electrical Solutions";
const seen = new Map(); // host -> last alert time, so one copy doesn't flood the inbox (per warm instance)

function eastern(d) {
  return d.toLocaleString("en-US", { timeZone: "America/New_York", dateStyle: "medium", timeStyle: "short" });
}

async function handle(request) {
  let body;
  try {
    body = JSON.parse(await request.text());
  } catch {
    return new Response(null, { status: 400 });
  }
  const clean = (v, n) => (typeof v === "string" ? v.replace(/[^\w.:\-\/ ()]/g, "").slice(0, n) : "");
  const host = clean(body.host, 120) || "(no web address: a saved copy opened from a computer)";
  const page = clean(body.page, 120);
  const now = Date.now();
  if (now - (seen.get(host) || 0) < 6 * 3600 * 1000) return new Response(null, { status: 204 });
  seen.set(host, now);

  const subject = `Your ${DESIGN} design was opened at ${host}`;
  const text = [
    `A copy of the ${DESIGN} site you built was opened at ${eastern(new Date())} ET.`,
    "",
    `Web address: ${host}`,
    page ? `Page: ${page}` : "",
    "",
    "This address is not one of your own preview links, so the page showed the \"Unlicensed copy\" banner.",
    "No visitor details were collected. Repeat alerts for the same address are held back for 6 hours.",
  ].filter((l, i, a) => l || a[i - 1]).join("\n");

  console.log(`[copy-alert] ${subject}`);
  const key = (process.env.RESEND_API_KEY || "").trim();
  const from = (process.env.ALERT_FROM || "").trim();
  if (key && from) {
    const r = await fetch("https://api.resend.com/emails", {
      method: "POST",
      headers: { Authorization: `Bearer ${key}`, "Content-Type": "application/json" },
      body: JSON.stringify({ from, to: [ALERT_TO], subject, text }),
    }).catch((e) => console.error("[copy-alert] email failed", e && e.name));
    if (r && !r.ok) console.error("[copy-alert] email failed", r.status, await r.text().catch(() => ""));
  } else console.error("[copy-alert] email skipped: RESEND_API_KEY or ALERT_FROM missing");
  return new Response(null, { status: 204, headers: { "Access-Control-Allow-Origin": "*" } });
}

export function POST(request) {
  return handle(request);
}
