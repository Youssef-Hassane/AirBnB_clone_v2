#!/usr/bin/python3

"""
Fabric script based on the file 2-do_deploy_web_static.py that creates and
distributes an archive to the web servers.

Usage: fab -f 3-deploy_web_static.py deploy -i ~/.ssh/id_rsa -u ubuntu
"""

from fabric.api import env, local, put, local
from datetime import datetime
from os.path import exists, isdir


# Define the host servers
env.hosts = ['54.173.82.140', '54.157.177.171']


def do_pack():
    """
    Creates an archive from the contents of the web_static folder.
    Returns the archive path if successful, otherwise returns None.
    """
    try:
        # Create an archive from the web_static folder
        file_name = "versions/web_static_{}.tgz".format(
            datetime.strftime("%Y%m%d%H%M%S"))
        if not isdir("versions"):
            # Create the versions directory if it doesn't exist
            local("mkdir versions")
        # Create the tgz archive
        local("tar -cvzf {} web_static".format(file_name))
        return file_name

    except Exception:
        return None


def do_deploy(archive_path):
    """
    Distributes an archive to the web servers.

    Parameters:
    archive_path (str): The path to the archive file to be distributed.

    Returns:
    bool: True if the deployment was successful, False otherwise.
    """
    if not exists(archive_path):
        return False

    try:
        # Extract the archive file name and its base name without extension
        archive_file = archive_path.split("/")[-1]
        base_name = archive_file.split(".")[0]
        release_path = "/data/web_static/releases/"

        # Upload the archive to the /tmp/ directory on the web server
        put(archive_path, '/tmp/')

        # Create the release directory on the web server
        local('mkdir -p {}{}'.format(release_path, base_name))

        # Uncompress the archive to the release directory
        local('tar -xzf /tmp/{} -C {}{}'.format(archive_file,
                                              release_path, base_name))

        # Remove the uploaded archive from /tmp/
        local('rm /tmp/{}'.format(archive_file))

        # Move the contents out of the web_static subdirectory
        local('mv {0}{1}/web_static/* {0}{1}/'.format(release_path, base_name))

        # Remove the now-empty web_static directory
        local('rm -rf {}{}/web_static'.format(release_path, base_name))

        # Remove the current symbolic link
        local('rm -rf /data/web_static/current')

        # Create a new symbolic link to the new release
        local('ln -s {}{}/ /data/web_static/current'.format(release_path,
                                                          base_name))

        return True
    except Exception:
        return False


def deploy():
    """
    Creates and distributes an archive to the web servers.

    Returns:
    bool: True if both the creation and deployment were successful,
    False otherwise.
    """
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
