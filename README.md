# lsdhcp - list DHCP leases over SSH

This is a tiny Python script for obtaining leases from a server running `dnsmasq` (although it was tested specifically with OpenWRT routers).

## Installation

To install, clone this repository and run `pip install .`.

## Usage

Create a configuration file at `$HOME/.config/lsdhcp.ini` with the following contents:

```toml
[SSH]
IP = "IP ADDRESS OF YOUR DHCP SERVER"
```
