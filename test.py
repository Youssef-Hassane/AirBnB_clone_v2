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

        # Create -- a new symbolic link to the new release
        local('ln -s {}{}/ /data/web_static/current'.format(release_path,
                                                            base_name))

        return True
    except Exception as e:
        return False
