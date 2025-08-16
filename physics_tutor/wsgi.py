import os
import sys

# مسیر پروژه
project_home = '/home/abtinphs/physics_tutor'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# تنظیمات Django
os.environ['DJANGO_SETTINGS_MODULE'] = 'physics_tutor.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
