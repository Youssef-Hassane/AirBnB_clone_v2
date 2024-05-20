#!/usr/bin/python3
import os
from fabric.api import *

env.hosts = ['54.173.82.140', '54.157.177.171']


def do_clean(number=0):
    """
    Delete out-of-date archives.

    Parameters:
    number (int): The number of archives to keep.
    If number is 0 or 1, keeps only the most recent archive.

    If number is 2, keeps the most and second-most
    recent archives, etc.
    """
    # Ensure at least one archive is kept
    number = 1 if int(number) == 0 else int(number)

    # Clean local archives
    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    # Clean remote archives
    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]
