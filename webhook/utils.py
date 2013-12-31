from netaddr import IPAddress, IPNetwork
from os import chdir, getcwd

def in_cidrs(addr, cidrs):
    ip = IPAddress(addr)
    for cidr in cidrs:
        if ip in IPNetwork(cidr):
            return True
    return False

_dir_stack = []

def pushd(path):
    cwd = getcwd()
    try:
        chdir(path)
    finally:
        _dir_stack.append(cwd)

def popd():
    if not len(_dir_stack) == 0:
        chdir(_dir_stack.pop())
