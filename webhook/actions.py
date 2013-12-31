from os import path
from subprocess import call
from webhook import repo, utils

def _call(*args):
    a = list(args)
    return call(a)

def do_pull(owner, name):
    utils.pushd(repo.path_for(owner, name))
    _call('git', 'pull')
    utils.popd()

def do_make_doc(owner, name):
    utils.pushd(path.join(repo.path_for(owner, name), 'build'))
    _call('make', 'doc')
    utils.popd()

def do(action, owner, name, *args, **kwargs):
    action_map = {
        'pull': do_pull,
        'make_doc': do_make_doc
    }
    action_map[action](owner, name, *args, **kwargs)
