import shutil
import os

import logging
logging.basicConfig(level = logging.DEBUG)
log = logging.getLogger(__name__)

from jinja2 import Environment, FileSystemLoader

def cleanup():
    log.debug('Cleaning public folder ...')
    shutil.rmtree('public/static', ignore_errors=True)
    shutil.copytree('site/static', 'public/static')

def generate_output(data):
    data.update(os.environ) # Expose env variables to template
    log.debug('Generating output ...')
    env = Environment(loader = FileSystemLoader(['./site/', '.']))
    for name in ['index', 'event']:
        template = env.get_template(f'site/{name}.html')
        template.stream(data).dump(f'public/{name}.html')


cleanup()

data = {
    "events": [
        {
            "title": "Kurz I. Hatha jóga a relaxace",
            "time": "16. 1. Pondělí 16:30 – 17:45",
            "place": "Yoga studio, Vinohradská 34, Praha 2",
            "instructor": {
                "name": "Katka",
                "photo": "/static/images/avatar.jpg"
            }
        },
        {
            "title": "Hatha jóga a relaxace",
            "time": "18. 1. Středa 18:00 – 19:30",
            "place": "Yoga studio, Vinohradská 34, Praha 2",
            "instructor": {
                "name": "Katka",
                "photo": "/static/images/avatar.jpg"
            }
        },
        {
            "title": "Kurz II. Hatha jóga a relaxace",
            "time": "20. 1. Pondělí 16:30 – 17:45",
            "place": "Yoga studio, Vinohradská 34, Praha 2",
            "instructor": {
                "name": "Katka",
                "photo": "/static/images/avatar.jpg"
            }
        },
    ]
}
generate_output(data)
