import paramiko
from pathlib import Path
from os import path

class DhcpServer:
    def __init__(self, server_ip, user='root', key_path=None, lease_file='/tmp/dhcp.leases'):
        if key_path is None:
            key_path = path.join(Path.home(), '.ssh/id_rsa') 
        self.__key = paramiko.RSAKey.from_private_key_file(key_path)
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(server_ip, username=user, pkey=self.__key)
        self.lease_file = lease_file
        self.leases = []

    def get_leases(self):
        stdin, stdout, stderr = self.client.exec_command(f'cat {self.lease_file}')
        for line in stdout:
            l = line.strip('\n').split(" ")
            one_lease = {'until': l[0], 'mac': l[1], 'ip': l[2], 'hostname': l[3]}
            self.leases.append(one_lease)
