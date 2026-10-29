// E-signatures for the proposal (21 Oct 2026). POST saves a signature; GET ?id= returns one for the signed copy.
// Rows live in Supabase project "airocket", table proposal_signatures, reached only through two RPC functions.
// Needs SUPABASE_URL and SUPABASE_KEY (the project's publishable key) in this Vercel project.
const SHOP = "jm-electrical";
const VERSION = "v1 · 21 Oct 2026"; // must match build_proposal.py
const ALERT_TO = "tim@airocket.pro"; // Tim only, never the prospect

// Signed alert (28 Oct 2026). Uses the same RESEND_API_KEY and ALERT_FROM shared variables as track.mjs.
async function alertSigned(name, business, id, request) {
  const key = (process.env.RESEND_API_KEY || "").trim(), from = (process.env.ALERT_FROM || "").trim(); // the shared value has a stray line break
  if (!key || !from) return console.error("[proposal-sign] alert skipped: RESEND_API_KEY or ALERT_FROM missing");
  const link = `${new URL(request.url).origin}/agreement/?sig=${id}`;
  const when = new Date().toLocaleString("en-US", { timeZone: "America/New_York", dateStyle: "medium", timeStyle: "short" });
  const text = `${name} signed the agreement for ${business} at ${when} ET.\n\nSigned copy: ${link}\n\nNext: they are sent to the Stripe deposit page. Check Stripe for the payment.`;
  const r = await fetch("https://api.resend.com/emails", {
    method: "POST",
    headers: { Authorization: `Bearer ${key}`, "Content-Type": "application/json" },
    body: JSON.stringify({ from, to: [ALERT_TO], subject: `${name} signed the JM Electrical Solutions agreement`, text }),
  }).catch((e) => console.error("[proposal-sign] alert failed", e && e.name));
  if (r && !r.ok) console.error("[proposal-sign] alert failed", r.status, await r.text());
}

async function rpc(fn, args) {
  const url = process.env.SUPABASE_URL, key = process.env.SUPABASE_KEY;
  if (!url || !key) throw new Error("SUPABASE_URL or SUPABASE_KEY missing");
  const r = await fetch(`${url}/rest/v1/rpc/${fn}`, {
    method: "POST",
    headers: { apikey: key, Authorization: `Bearer ${key}`, "Content-Type": "application/json" },
    body: JSON.stringify(args),
  });
  if (!r.ok) throw new Error(`${fn} ${r.status} ${await r.text()}`);
  return r.json();
}

const json = (data, status = 200) =>
  new Response(JSON.stringify(data), { status, headers: { "Content-Type": "application/json", "Cache-Control": "no-store" } });

export async function POST(request) {
  let b;
  try { b = await request.json(); } catch { return json({ error: "bad request" }, 400); }
  const name = typeof b.name === "string" ? b.name.trim() : "";
  const business = typeof b.business === "string" ? b.business.trim() : "";
  if (b.agree !== true || name.length < 2 || business.length < 2 || name.length > 120 || business.length > 160)
    return json({ error: "Tick the box and type your full name and business name." }, 400);
  const ip = (request.headers.get("x-forwarded-for") || "").split(",")[0].trim();
  const ua = request.headers.get("user-agent") || "";
  try {
    const id = await rpc("sign_proposal_v3", {
      p_shop: SHOP, p_version: VERSION, p_name: name, p_business: business,
      p_pay_on_booking: typeof b.payOnBooking === "boolean" ? b.payOnBooking : null,
      p_code: typeof b.p === "string" ? b.p : null, p_ip: ip, p_ua: ua,
      p_package: b.package === "site" || b.package === "booking" ? b.package : null,
      p_domain: typeof b.domain === "string" && /^[a-z0-9.|\- ]{1,60}$/.test(b.domain) ? b.domain : null,
    });
    console.log(`[proposal-sign] ${SHOP} signed by ${name} for ${business} (${id})`);
    await alertSigned(name, business, id, request).catch((e) => console.error("[proposal-sign] alert failed", e && e.name));
    return json({ id });
  } catch (e) {
    console.error("[proposal-sign] save failed", e);
    return json({ error: "We couldn't save your signature. Please try again or text us." }, 502);
  }
}

export async function GET(request) {
  const id = new URL(request.url).searchParams.get("id") || "";
  if (!/^[0-9a-f-]{36}$/i.test(id)) return json({ error: "not found" }, 404);
  try {
    const rows = await rpc("get_proposal_signature_v3", { p_id: id });
    return rows && rows[0] ? json(rows[0]) : json({ error: "not found" }, 404);
  } catch (e) {
    console.error("[proposal-sign] lookup failed", e);
    return json({ error: "lookup failed" }, 502);
  }
}
