"""Small helpers shared by the views and context processor."""

from functools import lru_cache

from django.contrib.staticfiles import finders


@lru_cache(maxsize=64)
def static_exists(relative_path: str) -> bool:
    """True when `relative_path` resolves to a real file in the static dirs.

    Lets the templates degrade gracefully: a missing profile photo falls back
    to a monogram instead of rendering a broken image.
    """
    if not relative_path:
        return False
    return finders.find(relative_path) is not None


def initials(name: str) -> str:
    """"Shehroz Baloch" -> "SB". Used for the monogram fallback."""
    parts = [part for part in (name or "").split() if part]
    if not parts:
        return "?"
    if len(parts) == 1:
        return parts[0][:2].upper()
    return (parts[0][0] + parts[-1][0]).upper()


def base_url(request) -> str:
    """Absolute site root, e.g. https://example.vercel.app (no trailing /)."""
    from portfolio import content

    configured = (content.SITE.get("base_url") or "").rstrip("/")
    if configured:
        return configured
    return f"{request.scheme}://{request.get_host()}"
