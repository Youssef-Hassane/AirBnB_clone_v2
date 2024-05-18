#!/usr/bin/python3
"""
Fabric script to generate a tgz archive.
"""

from datetime import datetime
from fabric.api import *


def do_pack():
    """
    Creates an archive from the contents of the web_static folder.
    Returns the archive path if successful, otherwise returns None.
    """

    time = datetime.now()
    archive_name = 'web_static_' + time.strftime("%Y%m%d%H%M%S") + '.tgz'

    # Create the versions directory if it doesn't exist
    local('mkdir -p versions')

    # Create the tgz archive
    result = local('tar -cvzf versions/{} web_static'.format(archive_name))

    # Check if the archive was created successfully
    if result is not None:
        return archive_name
    else:
        return None
