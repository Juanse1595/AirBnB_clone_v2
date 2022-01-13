#!/usr/bin/python3
"""Fabric script that distributes an archive to your web servers,
using the function do_deploy
"""
from datetime import datetime
from os.path import exists
from fabric.api import *
env.hosts = ['34.138.152.200', '3.85.201.247']
env.user = 'ubuntu'

def do_pack():
    """Fabric script that generates a .tgz archive from the contents of the
    web_static folder of your AirBnB Clone repo, using the function do_pack
    """
    local("mkdir -p versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    tgz_name = "web_static_" + date + ".tgz"
    archive_path = local("tar -cvzf versions/{} web_static".format(tgz_name))
    if archive_path.failed:
        return None
    return archive_path

def do_deploy(archive_path):
    """Fabric script that distributes an archive to your web servers,
    using the function do_deploy
    """
    if exists(archive_path) is False:
        return False
    start = archive_path.find("web_static")
    end = archive_path.find(".tgz")
    # Getting filename withouth extension
    filename_woe = archive_path[start:end]
    # Getting filename with extension
    filename_we = archive_path[start:]
    try:
        put(archive_path, "/tmp/")
        run("sudo mkdir -p /data/web_static/releases/{}/".format(filename_woe))
        run("sudo tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
            .format(filename_we, filename_woe))
        run("sudo rm -rf /tmp/{}".format(filename_we))
        run("sudo mv /data/web_static/releases/{}/web_static/* /data/\
web_static/releases/{}/".format(filename_woe, filename_woe))
        run("sudo rm -rf /data/web_static/releases/{}/web_static"
            .format(filename_woe))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(filename_woe))
        return True
    except Exception:
        return False

def deploy():
    """Fabric script that creates and distributes an archive to 
    your web servers, using the function deploy"""
    result_1 = do_pack()
    if result_1 is None:
        return False
    result_2 = do_deploy(result_1)
    return result_2

