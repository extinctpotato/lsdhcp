import paramiko, datetime
from pathlib import Path
from prettytable import PrettyTable
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
        self.get_leases()

    def get_leases(self):
        self.leases = []
        stdin, stdout, stderr = self.client.exec_command(f'cat {self.lease_file}')
        for line in stdout:
            l = line.strip('\n').split(" ")
            dt = datetime.datetime.fromtimestamp(int(l[0])).strftime('%c')
            one_lease = {'until': dt, 'mac': l[1], 'ip': l[2], 'hostname': l[3]}
            self.leases.append(one_lease)

    def pprint_leases(self):
        ptable = PrettyTable()
        ptable.field_names = list(self.leases[0].keys())

        for lease in self.leases:
            values = list(lease.values())
            ptable.add_row(values)

        print(ptable)
