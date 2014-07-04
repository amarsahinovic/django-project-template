from fabric.api import env, run, cd, local, prefix, lcd

PROJECT_PATH = '/srv/webapps/{{ project_name }}_project/{{ project_name }}/'

env.hosts = ['SERVER IP']
env.user = 'root'
env.port = '22'
env.key_filename = '~/.ssh/{{ project_name }}'

ENV_ACTIVATE = 'source ./env/bin/activate'

COMMANDS = [
    'git pull',
    'pip install --upgrade -r requirements.txt',
    './manage.py syncdb --settings {{ project_name }}.settings.production',
    './manage.py migrate --settings {{ project_name }}.settings.production',
    './manage.py collectstatic --noinput --settings {{ project_name }}.settings.production',
    'chown -R www-data:www-data .',
    'service {{ project_name }} restart',
    'service {{ project_name }}-celery restart',
    'service {{ project_name }}-celery-beat restart',
]

def get_commands():
    global COMMANDS
    for c in COMMANDS:
        yield c

def test():
    with lcd("./{{ project_name }}"):
        local("./manage.py test --settings {{ project_name }}.settings.testing")

def deploy():
    with cd(PROJECT_PATH), prefix(ENV_ACTIVATE):
        for command in get_commands():
            run(command)
        
