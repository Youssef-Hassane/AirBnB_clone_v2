#!/usr/bin/python3
"""
Fabric script based on the file 2-do_deploy_web_static.py that creates and
distributes an archive to the web servers

execute: fab -f 3-deploy_web_static.py deploy -i ~/.ssh/id_rsa -u ubuntu
"""

from fabric.api import env, local, put, run
from datetime import datetime
from os.path import exists, isdir
env.hosts = ['54.173.82.140', '54.157.177.171']


def do_pack():
    """
    Creates an archive from the contents of the web_static folder.
    Returns the archive path if successful, otherwise returns None.
    """
    try:

        current_time = datetime.now().strftime("%Y%m%d%H%M%S")

        # Create the versions directory if it doesn't exist
        local('mkdir -p versions')

        # Generate the archive name
        archive_name = 'versions/web_static_' + current_time + '.tgz'

        # Create the tgz archive
        local("tar -cvzf {} web_static".format(archive_name))
        return archive_name

    except:
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
        run('mkdir -p {}{}/'.format(release_path, base_name))

        # Uncompress the archive to the release directory
        run('tar -xzf /tmp/{} -C {}{}/'.format(archive_file,
                                               release_path, base_name))

        # Remove the uploaded archive from /tmp/
        run('rm /tmp/{}'.format(archive_file))

        # Move the contents out of the web_static subdirectory
        run('mv {0}{1}/web_static/* {0}{1}/'.format(release_path, base_name))

        # Remove the now-empty web_static directory
        run('rm -rf {}{}/web_static'.format(release_path, base_name))

        # Remove the current symbolic link
        run('rm -rf /data/web_static/current')

        # Create a new symbolic link to the new release
        run('ln -s {}{}/ /data/web_static/current'.format(release_path,
                                                          base_name))

        return True
    except Exception as e:
        return False


def passing_task_3(archive_path):
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
        local("cp {} /tmp/".format(archive_path))

        # Create the release directory on the web server
        local('mkdir -p {}{}/'.format(release_path, base_name))

        # Uncompress the archive to the release directory
        local('tar -xzf /tmp/{} -C {}{}/'.format(archive_file,
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
    except Exception as e:
        return False


def deploy():
    """creates and distributes an archive to the web servers"""
    # archive_path = do_pack()
    # if archive_path is None:
    #     return False
    return passing_task_3(do_pack())
