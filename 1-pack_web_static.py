#!/usr/bin/python3
"""
Fabric script to generate a tgz archive.
"""

from datetime import datetime
from fabric.api import local


def do_pack():
    """
    Creates an archive from the contents of the web_static folder.
    Returns the archive path if successful, otherwise returns None.
    """
    try:

        current_time = datetime.now()
        archive_name = 'web_static_' + \
            current_time.strftime("%Y%m%d%H%M%S") + '.tgz'

        # Create the versions directory if it doesn't exist
        local('mkdir -p versions')

        # Create the tgz archive
        result = local('tar -cvzf versions/{} web_static'.format(archive_name))

        # Check if the archive was created successfully
        if result.succeeded:
            return archive_name
        else:
            return None
    except Exception:
            return None
