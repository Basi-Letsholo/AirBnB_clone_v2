#!/usr/bin/python3
"""Generates a .tgz archive."""

from fabric.api import task, local
from datetime import datetime


@task
def do_pack():
    """
    Do pack function.
    """
    format_datetime = datetime.now().strftime('%Y%m%d%H%M%S')
    mkdir = 'mkdir -p versions'
    path = 'versions/web_static_{}.tgz'.format(format_datetime)

    print('Packing web_static to {}'.format(path))
    if local('{} && tar -cvzf {} web_static'.format(mkdir, path)).succeeded:
        return path

    return None
