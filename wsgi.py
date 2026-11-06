import os
import sys

# Add inner clinic folder to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'clinic'))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'clinic.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()