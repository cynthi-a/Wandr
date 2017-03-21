import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wandr_project.settings')
import django
django.setup()
from wandr.models import *