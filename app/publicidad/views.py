# from Flask
from flask import render_template, request, redirect, url_for, flash

# from APP
from . import publicidad

from paramiko import SSHClient
from scp import SCPClient
from pathlib import Path

import tempfile, re

@publicidad.route('/', methods=['POST', 'GET'])
def main_view():

    if request.method == 'POST':
        for data in request.files.getlist("file"):
            match request.form['sala']:
                case "Cubatta":
                    ip = '172.20.20.213'
                    userName = 'pi'
                    pword = 'PubliCuba'
                    portN = 22

                case "Tribeca":
                    ip = '172.20.21.186'
                    userName = 'pi'
                    pword = 'PubliSala'
                    portN = 22

                case "Montreal":
                    ip = '172.20.22.184'
                    userName = 'pi'
                    pword = 'PubliSala'
                    portN = 22

                case "Kavari":
                    ip = '172.20.23.186'
                    userName = 'pi'
                    pword = 'PubliSala'
                    portN = 22

                case "Siete":
                    ip = '172.20.24.184'
                    userName = 'pi'
                    pword = 'PubliSala'
                    portN = 22

                case "Magia":
                    ip = '172.20.25.225'
                    userName = 'pi'
                    pword = 'PubliSala'
                    portN = 9000

                case "Cassino":
                    ip = '172.20.26.182'
                    userName = 'pi'
                    pword = 'PubliSala'
                    portN = 22

                case "Proceres":
                    ip = '172.20.23.43'
                    userName = 'pi'
                    pword = 'PubliSala'
                    portN = 22

                case "Huacho":
                    ip = '172.20.24.43'
                    userName = 'pi'
                    pword = 'PubliSala'
                    portN = 22

                case "Huarmey":
                    ip = '172.20.25.34'
                    userName = 'pi'
                    pword = 'PubliSala'
                    portN = 22

                case "Casma":
                    ip = '172.20.26.33'
                    userName = 'pi'
                    pword = 'PubliSala'
                    portN = 22

            if request.form['event']:
                send_event(data, ip, userName, pword, portN, request)
            else:
                send_update(data, ip, userName, pword, portN, request)

    return render_template('video.html')

def send_update(request, ip, userName, pword, portN, local):
    ssh = SSHClient()
    ssh.load_system_host_keys()

    ssh.connect(ip,username=userName,password=pword,port=portN, timeout=900)
    scp = SCPClient(ssh.get_transport())
    with tempfile.TemporaryDirectory() as tmpdir:
        temp_file = Path(tmpdir) / request.filename
        request.save(temp_file)
        remote_path = '/home/pi/' + local.form['sala'] + '.mp4'
        scp.put(temp_file, remote_path)

        scp.close()
        if local.form['sala'] == 'Montreal':
            ssh.exec_command("sshpass -p 'PubliSala' scp Montreal.mp4 pi@172.20.22.185:~/")
        # ssh.exec_command("sudo reboot")
        ssh.close()

    flash(f'Se ha actualizado {local.form["sala"]}')
    return redirect(url_for('publicidad.main_view'))

def send_event(request, ip, userName, pword, portN, local):
    ssh = SSHClient()
    ssh.load_system_host_keys()
    fecha = re.split(r'-|T|:', local.form['date'])

    ssh.connect(ip,username=userName,password=pword,port=portN, timeout=900)
    scp = SCPClient(ssh.get_transport())
    with tempfile.TemporaryDirectory() as tmpdir:
        temp_file = Path(tmpdir) / request.filename
        request.save(temp_file)
        remote_path = '/home/pi/prueba/' + fecha[2] + '.mp4'
        scp.put(temp_file, remote_path)
        scp.close()
        # ssh.exec_command(f'sshpass -p "PubliCuba" crontab -l | {{ cat; echo "{fecha[4]} {fecha[3]} {fecha[2]} {fecha[1]} * /usr/bin/cp ~/prueba/{fecha[2]}.mp4 ~/prueba1/evento2.mp4"; }} | crontab -')
        ssh.exec_command(f'echo "{fecha[4]} {fecha[3]} {fecha[2]} {fecha[1]} * /usr/bin/cp ~/prueba/{fecha[2]}.mp4 ~/prueba1/evento2.mp4" > ~/mycron && crontab ~/mycron')
        ssh.close()

    flash(f'Se ha agregado el evento en la sala {local.form["sala"]}')
    return redirect(url_for('publicidad.main_view'))
