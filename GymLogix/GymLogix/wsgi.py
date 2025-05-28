"""
WSGI config for GymLogix project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""


import os
import sys

# Add the project root to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Set the correct settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GymLogix.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

