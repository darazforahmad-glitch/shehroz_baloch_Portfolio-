"""Views for the portfolio site.

The site is a single scrolling page plus a few small utility endpoints.
Nothing here touches a database.
"""

import logging

from django.conf import settings
from django.core.mail import EmailMessage
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.decorators.http import require_GET, require_http_methods

from portfolio import content
from portfolio.forms import ContactForm
from portfolio.utils import base_url

logger = logging.getLogger(__name__)


def _render_home(request, form, *, status=200, sent=False):
    return render(
        request,
        "portfolio/home.html",
        {"form": form, "contact_sent": sent},
        status=status,
    )


@require_GET
def home(request):
    """The portfolio page."""
    return _render_home(request, ContactForm())


@require_http_methods(["POST"])
def contact(request):
    """Handle the contact form.

    Posts come from the form on the home page. The response re-renders the
    page so validation errors appear in place; a successful submit redirects
    back to the anchor so a refresh cannot resend the message.
    """
    form = ContactForm(request.POST)

    if not form.is_valid():
        return _render_home(request, form, status=400)

    if form.looks_like_spam:
        return redirect(f"{reverse('home')}?sent=1#contact")

    data = form.cleaned_data
    subject = data.get("subject") or "New message from your portfolio site"
    body = (
        f"From: {data['name']} <{data['email']}>\n"
        f"Subject: {subject}\n"
        f"{'-' * 56}\n\n"
        f"{data['message']}\n"
    )
    recipient = content.CONTACT.get("email", "")

    if settings.CONTACT_EMAIL_BACKEND_READY and recipient:
        try:
            EmailMessage(
                subject=f"[Portfolio] {subject}",
                body=body,
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[recipient],
                reply_to=[data["email"]],
            ).send(fail_silently=False)
        except Exception:
            # Never show a stack trace to a visitor: log it and tell them
            # plainly that the message did not go through.
            logger.exception("Contact form delivery failed")
            form.add_error(
                None,
                "Something went wrong sending the message. "
                f"Please email {recipient} directly.",
            )
            return _render_home(request, form, status=500)
    else:
        # No SMTP configured -- the message is recorded in the logs so it is
        # not silently lost while the site is still being set up.
        logger.info("Contact form submission (email not configured):\n%s", body)

    return redirect(f"{reverse('home')}?sent=1#contact")


@require_GET
def resume(request):
    """Printable, single-column CV view of the same content."""
    return render(request, "portfolio/resume.html")


@require_GET
def robots_txt(request):
    lines = [
        "User-agent: *",
        "Allow: /",
        "",
        f"Sitemap: {base_url(request)}/sitemap.xml",
        "",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain; charset=utf-8")


@require_GET
def sitemap_xml(request):
    root = base_url(request)
    urls = [f"{root}/", f"{root}/resume/"]
    body = "".join(f"<url><loc>{url}</loc><changefreq>monthly</changefreq></url>" for url in urls)
    xml = (
        '<?xml version="1.0" encoding="UTF-8"?>'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
        f"{body}"
        "</urlset>"
    )
    return HttpResponse(xml, content_type="application/xml")


@require_GET
def healthz(request):
    """Trivial endpoint for uptime checks."""
    return JsonResponse({"status": "ok"})


# --------------------------------------------------------------------------
# Error handlers
# --------------------------------------------------------------------------

def page_not_found(request, exception=None):
    return render(request, "portfolio/404.html", status=404)


def server_error(request):
    return render(request, "portfolio/500.html", status=500)
