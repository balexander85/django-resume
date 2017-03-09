import sys, os
cwd = os.getcwd()
sys.path.append(cwd)
sys.path.append(cwd + '/public/resume')  # You must add your project here or 500

INTERP = os.path.expanduser("/home/baxe/briandanielalexander.com/env/bin/python")
if sys.executable != INTERP: os.execl(INTERP, INTERP, *sys.argv)

sys.path.insert(0, '$HOME/briandanielalexander.com/env/bin')
sys.path.insert(0, '$HOME/briandanielalexander.com/env/lib/python2.7/site-packages/django')
sys.path.insert(0, '$HOME/briandanielalexander.com/env/lib/python2.7/site-packages')

os.environ['DJANGO_SETTINGS_MODULE'] = "resume.settings"
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
