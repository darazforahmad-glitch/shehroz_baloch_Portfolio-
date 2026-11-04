"""Makes the content file available to every template."""

from portfolio import content
from portfolio.utils import initials, static_exists


def site_context(request):
    profile = content.PROFILE
    contact = content.CONTACT

    resume_file = profile.get("resume_file", "")

    # Only advertise the social links that have actually been filled in.
    social_links = [
        link
        for link in (
            {
                "name": "LinkedIn",
                "url": contact.get("linkedin", ""),
                "icon": "linkedin",
            },
            {"name": "GitHub", "url": contact.get("github", ""), "icon": "github"},
            {"name": "X", "url": contact.get("twitter", ""), "icon": "twitter"},
            {"name": "Website", "url": contact.get("website", ""), "icon": "globe"},
        )
        if link["url"]
    ]

    # "https://www.linkedin.com/in/shehroz-baloch-92910141b/" -> the slug,
    # so the contact row shows something readable rather than a long URL.
    linkedin_handle = ""
    if linkedin := contact.get("linkedin", ""):
        linkedin_handle = linkedin.rstrip("/").rsplit("/", 1)[-1]

    nav_items = [
        {"label": "About", "anchor": "about"},
        {"label": "Experience", "anchor": "experience"},
        {"label": "Skills", "anchor": "skills"},
    ]
    if content.PROJECTS:
        nav_items.append({"label": "Work", "anchor": "work"})
    nav_items.append({"label": "Education", "anchor": "education"})
    nav_items.append({"label": "Contact", "anchor": "contact"})

    return {
        "site": content.SITE,
        "profile": profile,
        "contact": contact,
        "about": content.ABOUT,
        "stats": content.STATS,
        "experience": content.EXPERIENCE,
        "skill_groups": content.SKILL_GROUPS,
        "projects": content.PROJECTS,
        "education": content.EDUCATION,
        "certifications": content.CERTIFICATIONS,
        "languages": content.LANGUAGES,
        "testimonials": content.TESTIMONIALS,
        "social_links": social_links,
        "linkedin_handle": linkedin_handle,
        "nav_items": nav_items,
        "has_resume": static_exists(resume_file),
        "resume_path": resume_file,
        "monogram": initials(profile.get("name", "")),
    }
