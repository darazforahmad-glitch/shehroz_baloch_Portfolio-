# Shehroz Baloch — Portfolio

A professional one-page portfolio built with **Django 5.2**, designed to deploy
on **Vercel's free tier**.

The design is monochrome by intent: a matte charcoal wall, near-black panels and
a single warm spotlight falling from the upper right. There is no accent colour —
the only "accent" is light.

---

## ⚡ The one file you need to edit

Everything on the site — name, headline, jobs, skills, projects, education,
contact details — lives in **`portfolio/content.py`**.

There is no database and no admin panel. Change a value in that file, reload the
page, and the site updates.

> **The content is currently placeholder text.** LinkedIn blocks automated
> readers, so no real profile data could be imported. Anything written as
> `<like this>` needs replacing before you share the site.

Optional extras:

| What | Where to put it |
|---|---|
| Profile photo | `static/img/profile.jpg` (a lettered monogram shows if absent) |
| CV / résumé PDF | `static/files/resume.pdf`, then set `resume_file` in `content.py` |

Sections disappear on their own when you empty them — set `PROJECTS = []` and the
Work section and its nav link vanish.

---

## 🖥 Run it locally

```bash
python -m venv .venv && source .venv/bin/activate
```

```bash
pip install -r requirements.txt
```

```bash
DEBUG=True python manage.py runserver
```

Open <http://127.0.0.1:8000>. On Windows use `.venv\Scripts\activate` and set the
variable with `set DEBUG=True` first.

No `migrate` step — the project has no database.

---

## 🚀 Deploy to Vercel (free)

### 1. Push this repository to GitHub

### 2. Import it on Vercel

Go to <https://vercel.com/new>, pick the repository, and press **Deploy**.
Vercel detects `vercel.json` and needs no framework preset, no build command and
no output directory — leave all of those blank.

### 3. Add the environment variables

**Project → Settings → Environment Variables.** Generate the key with:

```bash
python -c "from django.core.management.utils import get_random_secret_key as k; print(k())"
```

| Name | Value |
|---|---|
| `SECRET_KEY` | the generated string |
| `DEBUG` | `False` |
| `ALLOWED_HOSTS` | `.vercel.app` (add your custom domain, comma separated) |

Redeploy after adding them, so the new values are picked up.

### 4. Done

Your site is live at `https://<project>.vercel.app`.

### Custom domain

Add it under **Settings → Domains**, then append it to `ALLOWED_HOSTS`
(for example `ALLOWED_HOSTS=.vercel.app,shehrozbaloch.com,www.shehrozbaloch.com`)
and redeploy.

---

## ✉️ Contact form

The form validates and responds out of the box. Without SMTP credentials it
writes submissions to the application log rather than emailing them — so nothing
is lost while you are still setting things up, and no visitor ever sees an error.

To receive messages by email, add these variables in Vercel. All four are
required; set fewer and the form quietly stays in log-only mode.

| Name | Example |
|---|---|
| `EMAIL_HOST` | `smtp.gmail.com` |
| `EMAIL_HOST_USER` | `you@gmail.com` |
| `EMAIL_HOST_PASSWORD` | a Gmail **App Password**, not your normal password |
| `DEFAULT_FROM_EMAIL` | `you@gmail.com` |

Messages are delivered to the address in `CONTACT["email"]` with the sender's
address set as `Reply-To`, so replying from your inbox just works.

Gmail App Passwords require 2-Step Verification and are created at
<https://myaccount.google.com/apppasswords>.

A hidden honeypot field catches most bots. A bot that fills it gets the normal
success page while the message is silently discarded.

---

## 🗂 Project structure

```
config/              Django project (settings, urls, wsgi)
portfolio/
  content.py         ← ALL site content lives here
  views.py           page + contact + robots/sitemap/healthz
  forms.py           contact form with validation and honeypot
  context_processors.py  exposes content.py to every template
  templates/portfolio/   base, home, resume, 404, 500
static/
  css/site.css       the full design system
  js/site.js         scroll reveal, nav, mobile menu, word rotator
api/index.py         Vercel serverless entrypoint
vercel.json          routes every request to that entrypoint
```

### Routes

| Path | Purpose |
|---|---|
| `/` | the portfolio |
| `/resume/` | printable résumé view of the same content |
| `/contact/` | form handler (POST only) |
| `/robots.txt`, `/sitemap.xml` | SEO |
| `/healthz` | uptime check |

---

## 🔧 Notes on how it is built

**No database.** `auth`, `sessions` and `admin` are deliberately not installed.
Serverless functions get a read-only filesystem, so a SQLite file would be lost on
every cold start anyway.

**No build step.** WhiteNoise serves assets through Django's staticfiles finders
(`WHITENOISE_USE_FINDERS`), so `collectstatic` is not needed. Run it only if you
later move assets to a CDN.

**Security.** With `DEBUG=False` the project sets HSTS, `X-Frame-Options: DENY`,
nosniff, a referrer policy and HTTPS redirect. `SECURE_PROXY_SSL_HEADER` is set so
Django reads Vercel's TLS termination correctly instead of looping redirects.

**Accessibility and performance.** Semantic landmarks, a skip link, visible focus
rings, labelled form fields, `prefers-reduced-motion` support, no horizontal
scroll at 390px, and a print stylesheet. The only external request is Google
Fonts; everything else is inline or local.
