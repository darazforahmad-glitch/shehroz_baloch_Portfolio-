"""
=============================================================================
 THE ONLY FILE YOU NEED TO EDIT
=============================================================================

Every word, link, job, skill and project on the website comes from this file.
There is no database and no admin panel -- change a value here, reload the
page, and the site updates.

!! IMPORTANT !!
The values below are PLACEHOLDERS. The LinkedIn profile could not be read
automatically (LinkedIn blocks automated access), so nothing here is real
profile data. Replace anything wrapped in <angle brackets> or marked TODO
with the real details before sharing the site.

Quick start:
  1. PROFILE  -- name, headline, location, contact links
  2. ABOUT    -- the summary paragraphs and the stat tiles
  3. EXPERIENCE / EDUCATION / CERTIFICATIONS
  4. SKILLS   -- grouped skill chips
  5. PROJECTS -- featured work cards
  6. Drop a photo at  static/img/profile.jpg  and a CV at
     static/files/resume.pdf  (both optional; the site works without them)
=============================================================================
"""

# ---------------------------------------------------------------------------
# 1. PROFILE
# ---------------------------------------------------------------------------
PROFILE = {
    "name": "Shehroz Baloch",
    # Shown under the name in the hero. Keep it short and specific.
    "headline": "<Your professional headline, e.g. Business Development Manager>",
    # One punchy line used in the hero paragraph and as the meta description.
    "tagline": (
        "<One or two sentences describing what you do and the value you bring. "
        "This is the first thing a visitor reads, so make it count.>"
    ),
    "location": "<City, Country>",
    "availability": "Open to new opportunities",  # set to "" to hide the badge
    # Rotating words in the hero typing animation. Keep 2-5 short items.
    "focus_areas": [
        "<Focus area one>",
        "<Focus area two>",
        "<Focus area three>",
    ],
    # Optional: static/img/profile.jpg -- leave as-is; a lettered monogram is
    # shown automatically if the file is missing.
    "photo": "img/profile.jpg",
    # Optional: static/files/resume.pdf -- the Resume button hides if unset.
    "resume_file": "",  # e.g. "files/resume.pdf"
}

CONTACT = {
    "email": "<you@example.com>",
    "phone": "",  # optional, e.g. "+92 300 0000000"
    "linkedin": "https://www.linkedin.com/in/shehroz-baloch-92910141b/",
    "github": "",     # optional
    "twitter": "",    # optional
    "website": "",    # optional
}

# ---------------------------------------------------------------------------
# 2. ABOUT
# ---------------------------------------------------------------------------
ABOUT = {
    "heading": "About me",
    "lead": "<A single strong opening sentence about who you are professionally.>",
    "paragraphs": [
        "<Paragraph one: your background, the kind of work you do, and the "
        "industries or teams you have worked with.>",
        "<Paragraph two: how you work, what you are especially good at, and "
        "the sort of problems you enjoy solving.>",
    ],
    # Short, factual highlights. Delete any you do not want to show.
    "highlights": [
        "<A concrete strength or specialism>",
        "<Another strength>",
        "<A third strength>",
    ],
}

# Stat tiles in the hero. Use 2-4. Set to [] to hide the row entirely.
STATS = [
    {"value": "<N>+", "label": "Years of experience"},
    {"value": "<N>+", "label": "Projects delivered"},
    {"value": "<N>+", "label": "Clients served"},
]

# ---------------------------------------------------------------------------
# 3. EXPERIENCE
# ---------------------------------------------------------------------------
# Newest role first. `end` can be "Present".
EXPERIENCE = [
    {
        "role": "<Job title>",
        "company": "<Company name>",
        "company_url": "",
        "location": "<City, Country>",
        "start": "<Mon YYYY>",
        "end": "Present",
        "employment_type": "Full-time",
        "summary": "<One sentence on the scope of the role.>",
        "achievements": [
            "<An achievement with a number in it where you can.>",
            "<A responsibility that shows the scale you operate at.>",
            "<Something you improved, built or led.>",
        ],
        "skills": ["<Skill>", "<Skill>", "<Skill>"],
    },
    {
        "role": "<Previous job title>",
        "company": "<Previous company>",
        "company_url": "",
        "location": "<City, Country>",
        "start": "<Mon YYYY>",
        "end": "<Mon YYYY>",
        "employment_type": "Full-time",
        "summary": "<One sentence on the scope of the role.>",
        "achievements": [
            "<An achievement.>",
            "<Another achievement.>",
        ],
        "skills": ["<Skill>", "<Skill>"],
    },
]

# ---------------------------------------------------------------------------
# 4. SKILLS
# ---------------------------------------------------------------------------
# Grouped so the section reads as a capability map rather than a word cloud.
SKILL_GROUPS = [
    {
        "title": "<Group one, e.g. Core expertise>",
        "icon": "spark",  # spark | layers | chart | users | tools | globe
        "skills": ["<Skill>", "<Skill>", "<Skill>", "<Skill>"],
    },
    {
        "title": "<Group two, e.g. Tools & platforms>",
        "icon": "tools",
        "skills": ["<Skill>", "<Skill>", "<Skill>", "<Skill>"],
    },
    {
        "title": "<Group three, e.g. Ways of working>",
        "icon": "users",
        "skills": ["<Skill>", "<Skill>", "<Skill>"],
    },
]

# ---------------------------------------------------------------------------
# 5. PROJECTS / SELECTED WORK
# ---------------------------------------------------------------------------
# Set to [] to remove the whole section from the page and the navigation.
PROJECTS = [
    {
        "title": "<Project name>",
        "category": "<Category, e.g. Client engagement>",
        "period": "<YYYY>",
        "description": (
            "<What the project was, what you did on it, and what the outcome "
            "was. Two or three sentences is plenty.>"
        ),
        "tags": ["<Tag>", "<Tag>"],
        "url": "",          # optional link
        "url_label": "View project",
        "featured": True,   # featured cards get the wider layout
    },
    {
        "title": "<Second project>",
        "category": "<Category>",
        "period": "<YYYY>",
        "description": "<Short description of the work and its result.>",
        "tags": ["<Tag>", "<Tag>"],
        "url": "",
        "url_label": "View project",
        "featured": False,
    },
    {
        "title": "<Third project>",
        "category": "<Category>",
        "period": "<YYYY>",
        "description": "<Short description of the work and its result.>",
        "tags": ["<Tag>"],
        "url": "",
        "url_label": "View project",
        "featured": False,
    },
]

# ---------------------------------------------------------------------------
# 6. EDUCATION, CERTIFICATIONS, LANGUAGES
# ---------------------------------------------------------------------------
EDUCATION = [
    {
        "degree": "<Degree, e.g. BBA (Hons) Marketing>",
        "institution": "<University name>",
        "location": "<City, Country>",
        "start": "<YYYY>",
        "end": "<YYYY>",
        "detail": "<Optional: honours, specialisation, notable coursework.>",
    },
]

CERTIFICATIONS = [
    {
        "name": "<Certification name>",
        "issuer": "<Issuing organisation>",
        "year": "<YYYY>",
        "url": "",
    },
]

LANGUAGES = [
    {"name": "English", "level": "<Professional / Native / Fluent>"},
    {"name": "Urdu", "level": "<Native>"},
]

# Optional social proof. Set to [] to hide the section.
TESTIMONIALS = [
    # {
    #     "quote": "<What a manager, client or colleague said about working with you.>",
    #     "author": "<Name>",
    #     "role": "<Title, Company>",
    # },
]

# ---------------------------------------------------------------------------
# 7. SITE SETTINGS
# ---------------------------------------------------------------------------
SITE = {
    # Used for absolute URLs in meta tags and sitemap.xml. No trailing slash.
    # Leave "" to have it derived from the incoming request.
    "base_url": "",
    "brand": "Shehroz Baloch",
    "nav_cta": "Get in touch",
    "footer_note": "Designed and built with Django.",
    "contact_heading": "Let's work together",
    "contact_blurb": (
        "Have a role, a project or a question in mind? Send a message and "
        "I will get back to you."
    ),
    # Shown in the <title> after the name.
    "title_suffix": "Portfolio",
}
