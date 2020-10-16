import socket
import time

from paramiko import BadHostKeyException, AuthenticationException, SSHException
from paramiko.client import SSHClient


def try_ssh(hostname: str, port: int = 22, username: str = 'root', password: str = 'toor', retries: int = 10):
    retry = 0
    connected = False

    if port is None:
        port = 22
    if username is None:
        username = 'root'
    if password is None:
        password = 'toor'

    ssh = SSHClient()
    ssh.load_system_host_keys()
    while retry < retries and not connected:
        try:
            print('Trying ssh connection to {} : {} out of {} retries'.format(hostname, retry, retries))
            ssh.connect(hostname, port=port, username=username, password=password)
            connected = True
        except (BadHostKeyException, AuthenticationException, SSHException, socket.error) as e:
            print(e)
            time.sleep(10)
        retry += 1

    if not connected:
        raise Exception('Unable to connect to the machine after {} tries'.format(retry))
    print('Connection to {} established after {} out of {} retries'.format(hostname, retry, retries))
