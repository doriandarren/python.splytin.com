import os
import sys
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent

with open(PROJECT_DIR / "passenger_debug.log", "a") as f:
    f.write("START\n")
    f.write(f"PROJECT_DIR={PROJECT_DIR}\n")

sys.path.insert(0, str(PROJECT_DIR))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "main.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

with open(PROJECT_DIR / "passenger_debug.log", "a") as f:
    f.write("WSGI LOADED OK\n")
