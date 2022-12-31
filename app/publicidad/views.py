# from Flask
from flask import render_template, request, redirect, url_for, flash

# from APP
# from app.models import db, Ludopatia_db, no_access
from . import publicidad

from paramiko import SSHClient
from scp import SCPClient
from pathlib import Path

import tempfile

@publicidad.route('/', methods=['POST', 'GET'])
def main_view():

    if request.method == 'POST':
        ssh = SSHClient()
        ssh.load_system_host_keys()

        match request.files["file"].filename:
            case "Cubatta.mp4":
                ssh.connect('172.20.20.203',username='pi',password='PubliCuba',port=9000)
                scp = SCPClient(ssh.get_transport())
                with tempfile.TemporaryDirectory() as tmpdir:
                    temp_file = Path(tmpdir) / request.files['file'].filename
                    request.files['file'].save(temp_file)
                    scp.put(temp_file, remote_path='/home/pi/')
                return redirect(url_for('publicidad.main_view'))
            case "Tribeca.mp4":
                ssh.connect('172.20.21.186',username='pi',password='PubliSala')
                scp = SCPClient(ssh.get_transport())
                with tempfile.TemporaryDirectory() as tmpdir:
                    temp_file = Path(tmpdir) / request.files['file'].filename
                    request.files['file'].save(temp_file)
                    scp.put(temp_file, remote_path='/home/pi/')
                return redirect(url_for('publicidad.main_view'))
            case "Montreal":
                pass
            case "Kavari":
                pass
            case "Siete":
                pass
            case "Magia":
                pass
            case "Cassino":
                pass

        scp.close()
        ssh.close()

    return render_template('video.html')
