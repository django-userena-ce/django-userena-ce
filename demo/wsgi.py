import os
import sys

import django.core.handlers.wsgi

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "demo"))
)
os.environ["DJANGO_SETTINGS_MODULE"] = "demo.settings"
application = django.core.handlers.wsgi.WSGIHandler()
