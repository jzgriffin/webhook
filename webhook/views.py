from webhook import actions, app, github, repo, utils
from flask import abort, redirect, request
import json

@app.route('/')
def index():
    app.logger.debug('Redirecting to INDEX')
    return redirect(app.config['INDEX'])

@app.route('/webhook', methods=['POST'])
def webhook():
    if not utils.in_cidrs(request.remote_addr, github.hook_cidrs()):
        app.logger.warning('POST from unrecognized address ' + request.remote_addr)
        abort(403)

    payload = request.get_json()
    owner = payload['repository']['owner']['name']
    name = payload['repository']['name']

    fullname = repo.fullname_for(owner, name)
    app.logger.debug('Payload for repository ' + fullname)
    if not repo.allow(owner, name):
        app.logger.warning('Payload for unrecognized repository ' + fullname)
        abort(403)

    action_list = repo.actions_for(owner, name)
    for action in action_list:
        app.logger.debug('Performing action (' + action + ') on ' + fullname)
        actions.do(action, owner, name)
    return 'OK'
