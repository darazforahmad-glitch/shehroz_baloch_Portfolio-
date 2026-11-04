"""
=============================================================================
 THE ONLY FILE YOU NEED TO EDIT
=============================================================================

Every word on the website comes from this file. There is no database and no
admin panel -- change a value here, reload the page, and the site updates.

STATUS
  Complete and live. Name, headline, location, contact email, the Cloaked
  role and its delivery, skills, selected work, and the degree are all real.

  Optional additions, marked TODO below:
    * earlier roles, certifications, languages
    * a profile photo at static/img/profile.jpg
    * stat tiles and the "open to opportunities" badge, both off by default

Sections disappear by themselves when left empty, so the site never shows a
half-finished block. PROJECTS = [] removes the Work section and its nav link.

Optional files:
  static/img/profile.jpg    profile photo (a monogram shows if absent)
  static/files/resume.pdf   CV, then set PROFILE["resume_file"] below
=============================================================================
"""

# ---------------------------------------------------------------------------
# 1. PROFILE
# ---------------------------------------------------------------------------
PROFILE = {
    "name": "Shehroz Baloch",
    "headline": "Lifecycle, Support & Growth Ops @ Cloaked",
    "tagline": (
        "I work across lifecycle marketing, customer support and growth "
        "operations — building the campaigns, segments and reporting that "
        "connect a product to the people actually using it."
    ),
    "location": "Lahore, Punjab, Pakistan",
    # TODO: set to "Open to new opportunities" if that is true for you.
    # Left empty for now so the site does not claim it on your behalf.
    "availability": "",
    # Rotating words in the hero.
    "focus_areas": [
        "Lifecycle marketing",
        "CRM operations",
        "Growth ops",
        "Customer.io",
    ],
    "photo": "img/profile.jpg",
    "resume_file": "",  # e.g. "files/resume.pdf"
}

CONTACT = {
    "email": "shhrzblchh@gmail.com",
    "phone": "",
    "linkedin": "https://www.linkedin.com/in/shehroz-baloch-92910141b/",
    "github": "",
    "twitter": "",
    "website": "",
}

# ---------------------------------------------------------------------------
# 2. ABOUT
# ---------------------------------------------------------------------------
ABOUT = {
    "heading": "About me",
    "lead": (
        "I work at the intersection of lifecycle marketing, customer support "
        "and growth operations."
    ),
    "paragraphs": [
        "At Cloaked I work on lifecycle marketing and operational support — "
        "building and managing campaigns in Customer.io across email, SMS and "
        "push, segmenting audiences, and keeping day-to-day CRM operations "
        "running, with a focus on campaign performance and user engagement.",

        "Much of the work sits between teams. I developed a segment exclusion "
        "filter to address data sync issues, streamlined backend-triggered "
        "email workflows into Customer.io, and managed the Referral Gift Card "
        "program — collaborating cross-functionally to resolve bugs that were "
        "affecting users.",

        "I lean on A/B testing, holdout pool design and Snowflake data "
        "integration to measure what campaigns actually do, and on a "
        "background in Communication and Media Studies for how I approach "
        "messaging and audience. The through-line is aligning technical "
        "solutions to organisational goals.",
    ],
    "highlights": [
        "Lifecycle campaigns across email, SMS and push, built in Customer.io",
        "Audience segmentation and day-to-day CRM operations",
        "A/B testing, holdout pool design and campaign performance reporting",
        "Technical issue investigation alongside engineering and support",
        "Cross-functional stakeholder communication",
    ],
}

# TODO: add real figures if you want the stat tiles back, e.g.
#   {"value": "3+", "label": "Years in lifecycle marketing"}
# Left empty rather than showing invented numbers.
STATS = []

# ---------------------------------------------------------------------------
# 3. EXPERIENCE
# ---------------------------------------------------------------------------
EXPERIENCE = [
    {
        "role": "Lifecycle & Support Ops",
        "company": "Cloaked",
        "company_url": "",  # optional: link to cloaked.com
        "location": "Lahore, Punjab, Pakistan · Remote",
        "start": "Mar 2025",
        "end": "Present",
        "employment_type": "Full-time",
        "summary": (
            "Enhancing lifecycle marketing and operational support, with "
            "improvements in campaign performance and user engagement."
        ),
        "achievements": [
            "Developed a segment exclusion filter to resolve data sync "
            "issues, ensuring accurate user messaging.",
            "Led the migration of backend-triggered emails into Customer.io, "
            "streamlining communication workflows.",
            "Managed the Referral Gift Card program, coordinating "
            "cross-functional teams to resolve user-impacting bugs.",
        ],
        "skills": [
            "Lifecycle Marketing (Email, SMS & Push)",
            "Customer.io (CIO)",
            "A/B Testing & Holdout Pool Design",
            "Cross-functional Stakeholder Communication",
            "Audience Segmentation",
            "Snowflake",
        ],
    },
    # TODO: add earlier roles by copying the block above. Newest first.
]

# ---------------------------------------------------------------------------
# 4. SKILLS  (the five listed on your LinkedIn profile)
# ---------------------------------------------------------------------------
SKILL_GROUPS = [
    {
        "title": "Lifecycle & Campaigns",
        "icon": "spark",
        "skills": [
            "Lifecycle Marketing (Email, SMS & Push)",
            "Customer.io (CIO) Campaign Management",
            "Backend-triggered Email Workflows",
        ],
    },
    {
        "title": "Audience & CRM Operations",
        "icon": "users",
        "skills": [
            "Audience Segmentation & CRM Operations",
            "Holdout Pool Design",
            "Segment Exclusion Filtering",
        ],
    },
    {
        "title": "Analytics & Experimentation",
        "icon": "chart",
        "skills": [
            "Campaign Performance Reporting & Data Analysis",
            "A/B Testing",
            "Snowflake Data Integration",
        ],
    },
    {
        "title": "Support & Collaboration",
        "icon": "tools",
        "skills": [
            "Technical Issue Investigation & Cross-functional Collaboration",
            "Cross-functional Stakeholder Communication",
        ],
    },
]

# ---------------------------------------------------------------------------
# 5. PROJECTS / SELECTED WORK
# ---------------------------------------------------------------------------
# Drawn from the work at Cloaked. TODO: add results/numbers where you have
# them -- a figure in the description is what makes these land.
PROJECTS = [
    {
        "title": "Segment Exclusion Filter",
        "category": "CRM Operations",
        "period": "",
        "description": (
            "Built a segment exclusion filter to address data sync issues "
            "that were affecting campaign targeting, so audiences resolved "
            "correctly before a send went out."
        ),
        "tags": ["Audience Segmentation", "Data Sync", "Customer.io"],
        "url": "",
        "url_label": "",
        "featured": True,
    },
    {
        "title": "Customer.io Workflow Consolidation",
        "category": "Lifecycle Engineering",
        "period": "",
        "description": (
            "Streamlined backend-triggered email workflows into Customer.io, "
            "bringing delivery into one platform and making lifecycle "
            "messaging easier to manage and measure."
        ),
        "tags": ["Customer.io", "Email Automation"],
        "url": "",
        "url_label": "",
        "featured": False,
    },
    {
        "title": "Referral Gift Card Program",
        "category": "Growth",
        "period": "",
        "description": (
            "Managed the Referral Gift Card program end to end, working "
            "across engineering, support and growth to investigate and "
            "resolve user-impacting bugs."
        ),
        "tags": ["Referral", "Cross-functional", "Support"],
        "url": "",
        "url_label": "",
        "featured": False,
    },
]

# ---------------------------------------------------------------------------
# 6. EDUCATION, CERTIFICATIONS, LANGUAGES
# ---------------------------------------------------------------------------
EDUCATION = [
    {
        "degree": "Bachelor of Science, Communication and Media Studies",
        "institution": "International Islamic University, Islamabad",
        "location": "Islamabad, Pakistan",
        "start": "Feb 2013",
        "end": "Jan 2017",
        "detail": "Grade: A — Gold Medalist",
    },
]

# TODO: add any certifications, e.g. Customer.io or HubSpot credentials.
CERTIFICATIONS = []

# TODO: add languages and levels, e.g. {"name": "Urdu", "level": "Native"}.
LANGUAGES = []

TESTIMONIALS = []

# ---------------------------------------------------------------------------
# 7. SITE SETTINGS
# ---------------------------------------------------------------------------
SITE = {
    "base_url": "",
    "brand": "Shehroz Baloch",
    "nav_cta": "Get in touch",
    "footer_note": "Designed and built with Django.",
    "contact_heading": "Let's work together",
    "contact_blurb": (
        "Have a role, a project or a question in mind? Send a message and "
        "I will get back to you."
    ),
    "title_suffix": "Lifecycle & Growth Ops",
}
