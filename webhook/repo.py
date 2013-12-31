from os import path
from webhook import app

def fullname_for(owner, name):
    return owner + '/' + name

def path_for(owner, name):
    return path.join(app.config['REPODIR'], owner, name)

def allow(owner, name):
    return fullname_for(owner, name) in app.config['REPOS']

def actions_for(owner, name):
    return app.config['REPOS'][fullname_for(owner, name)]
