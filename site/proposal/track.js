// Proposal read alerts, ported from the EAS build's useReadTracking (20 Oct 2026) for a static page.
// Reports open / time per section / deposit click to /api/track when the URL has ?p=<code>.
// Sections = the page <header> plus every element with data-slide (title = its first <h2>). No cookies.
(function () {
  var p = new URLSearchParams(window.location.search).get("p");
  if (!p) return;
  var depositLinks = ((document.currentScript && document.currentScript.getAttribute("data-deposit")) || "").split(" ").filter(Boolean);
  function send(data, beacon) {
    data.p = p;
    var body = JSON.stringify(data);
    if (beacon && navigator.sendBeacon) navigator.sendBeacon("/api/track", new Blob([body], { type: "application/json" }));
    else fetch("/api/track", { method: "POST", headers: { "Content-Type": "application/json" }, body: body, keepalive: true }).catch(function () {});
  }
  send({ kind: "open" });

  var sections = Array.prototype.slice.call(document.querySelectorAll("header, [data-slide]"));
  function title(el) {
    if (el.tagName === "HEADER") return "Top of the page";
    var h = el.querySelector("h2");
    return h ? h.textContent : el.id || "Section";
  }
  var seconds = new Map();
  var start = Date.now();
  var active = 0;
  // Each second, credit the section crossing the middle of the screen.
  var tick = window.setInterval(function () {
    if (document.visibilityState !== "visible") return;
    active += 1;
    var mid = window.innerHeight / 2;
    var el = sections.find(function (s) {
      var r = s.getBoundingClientRect();
      return r.top <= mid && r.bottom > mid;
    });
    if (el) seconds.set(el, (seconds.get(el) || 0) + 1);
  }, 1000);

  var sent = false;
  function leave() {
    if (sent || Date.now() - start < 3000) return;
    sent = true;
    window.clearInterval(tick);
    var rows = sections.filter(function (el) { return seconds.has(el); }).map(function (el) { return [title(el), seconds.get(el)]; });
    send({ kind: "leave", seconds: active, sections: rows }, true);
  }
  document.addEventListener("visibilitychange", function () { if (document.visibilityState === "hidden") leave(); });
  window.addEventListener("pagehide", leave);
  document.addEventListener("click", function (e) {
    var a = e.target && e.target.closest ? e.target.closest("a") : null;
    if (a && depositLinks.indexOf(a.getAttribute("href")) >= 0) send({ kind: "deposit" }, true);
  });
})();
