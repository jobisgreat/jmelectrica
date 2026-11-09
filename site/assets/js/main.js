/* JM Electrical Solutions — the only script on the site (~2 KB).
   1) Mobile menu toggle  2) Lead-form validation + submit  3) Footer year */
(function () {
  // 1) Mobile menu
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.getElementById('site-nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('is-open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }

  // 2) Lead forms. Set FORM_ENDPOINT to your form service URL (e.g. Formspree,
  //    Basin, Netlify Forms). Until then, forms validate and go to thank-you.html.
  var FORM_ENDPOINT = ''; // TODO: e.g. 'https://formspree.io/f/xxxxxxx'

  function setError(field, msg) {
    var wrap = field.closest('.field');
    var err = wrap.querySelector('.field-error');
    wrap.classList.toggle('has-error', !!msg);
    field.setAttribute('aria-invalid', msg ? 'true' : 'false');
    if (err) err.textContent = msg || '';
  }

  function validate(form) {
    var ok = true, first = null;
    var name = form.elements.name, phone = form.elements.phone, job = form.elements.job;
    var digits = (phone.value || '').replace(/\D/g, '');
    [[name, name.value.trim().length < 2 ? 'Please enter your name.' : ''],
     [phone, digits.length < 10 ? 'Please enter a 10-digit phone number.' : ''],
     [job, job.value.trim().length < 3 ? 'Briefly tell us what you need done.' : '']
    ].forEach(function (pair) {
      setError(pair[0], pair[1]);
      if (pair[1]) { ok = false; first = first || pair[0]; }
    });
    if (first) first.focus();
    return ok;
  }

  document.querySelectorAll('form.js-lead').forEach(function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (form.elements.company && form.elements.company.value) return; // spam trap
      if (!validate(form)) return;
      var status = form.querySelector('.form-status');
      var btn = form.querySelector('button[type="submit"]');
      btn.disabled = true;
      if (status) status.textContent = 'Sending…';
      if (!FORM_ENDPOINT) { window.location.href = 'thank-you.html'; return; }
      fetch(FORM_ENDPOINT, { method: 'POST', body: new FormData(form), headers: { Accept: 'application/json' } })
        .then(function (r) {
          if (!r.ok) throw new Error();
          window.location.href = 'thank-you.html';
        })
        .catch(function () {
          btn.disabled = false;
          if (status) status.textContent = 'That didn’t go through. Please call (978) 746-1993.';
        });
    });
  });

  // 3) Footer year
  var y = document.getElementById('year');
  if (y) y.textContent = new Date().getFullYear();
})();

// "View Your Proposal" bar: only when the site was opened from the proposal (?from=proposal), so the public never sees it.
(function () {
  var q = new URLSearchParams(location.search), p = q.get('p'), on = q.get('from') === 'proposal';
  try {
    if (on) sessionStorage.setItem('jm-proposal', p || '');
    else if (sessionStorage.getItem('jm-proposal') !== null) { on = true; p = sessionStorage.getItem('jm-proposal'); }
  } catch (e) {}
  if (!on || window.top !== window.self) return; // never inside the phone/computer frames on /preview/
  var bar = document.createElement('div');
  bar.className = 'proposal-bar';
  var a = document.createElement('a');
  a.href = '/proposal/' + (p ? '?p=' + encodeURIComponent(p) : '');
  a.textContent = 'View Your Proposal →';
  bar.appendChild(a);
  document.body.insertBefore(bar, document.body.firstChild);
})();

// Preview mark (AI Rocket): on any web address other than AI Rocket's own preview links, show an
// "Unlicensed copy" banner and tell AI Rocket which address it is on. No visitor details are sent.
// At launch, after payment: add jmelectricsolutions.com and www.jmelectricsolutions.com to the allowed list.
(function () {
  try {
    var h = location.hostname || '';
    if (/(^|\.)localhost$|^127\.0\.0\.1$|-jobisgreat-3165s-projects\.vercel\.app$|^project-q2oxb\.vercel\.app$|^jmelectric\.airocket\.pro$/.test(h)) return;
    var b = document.createElement('div');
    b.setAttribute('role', 'alert');
    b.style.cssText = 'position:fixed;left:0;right:0;bottom:0;z-index:2147483647;background:#7a1010;color:#fff;font:700 15px/1.4 system-ui,sans-serif;text-align:center;padding:12px 16px';
    b.textContent = 'Unlicensed copy of a website design by AI Rocket (airocket.pro). Not for public use.';
    document.body.appendChild(b);
    document.body.style.paddingBottom = '64px';
    var k = 'jm-copy-' + h;
    try { if (localStorage.getItem(k)) return; localStorage.setItem(k, '1'); } catch (e) {}
    var d = JSON.stringify({ host: h, page: h ? location.pathname : '' }), u = 'https://jmelectric.airocket.pro/api/copy-alert';
    if (navigator.sendBeacon) navigator.sendBeacon(u, d); else fetch(u, { method: 'POST', mode: 'no-cors', body: d });
  } catch (e) {}
})();
