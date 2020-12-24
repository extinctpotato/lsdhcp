import argparse, configparser, sys
from pathlib import Path
from os import path
from lsdhcp import DhcpServer

CONF_PATH = path.join(str(Path.home()), ".config", "lsdhcp.ini")
CONFIG = configparser.ConfigParser()
CONFIG.read(CONF_PATH)

def default_func(arg):
    d = DhcpServer(
            server_ip=CONFIG['SSH']['IP'],
            user=CONFIG['SSH']['USER'],
            lease_file=CONFIG['SSH']['LEASE_FILE'],
            )
    d.pprint_leases()

def get_parser():
    parser = argparse.ArgumentParser()
    parser.set_defaults(func=default_func)
    return parser

def main():
    parser = get_parser()
    args = parser.parse_args()
    args.func(args)
