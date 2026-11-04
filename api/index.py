"""Vercel serverless entrypoint.

Vercel's Python runtime imports this module and looks for `app`. Every
request to the deployment is rewritten here by vercel.json, so a single
function serves the whole Django site.
"""

import os
import sys
from pathlib import Path

# The project root is one level up from /api -- put it on the import path
# so `config` and `portfolio` resolve inside the serverless bundle.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

from config.wsgi import application  # noqa: E402

app = application
