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

Once you've configured the IP and made sure that you can ssh into that server, execute ``lsdhcp``.
You should see something like this (MAC addresses have been removed in this example):

```shell
+--------------------------+-------------------+--------------+-----------------+------------------------------+
|          until           |        mac        |      ip      |     hostname    |            vendor            |
+--------------------------+-------------------+--------------+-----------------+------------------------------+
| Thu Aug  6 06:16:02 2020 | xx:xx:xx:xx:xx:xx | 192.168.1.34 |        *        |   Raspberry Pi Trading Ltd   |
| Thu Aug  6 05:56:23 2020 | xx:xx:xx:xx:xx:xx | 192.168.1.15 |        *        |       Intel Corporate        |
| Thu Aug  6 10:49:03 2020 | xx:xx:xx:xx:xx:xx | 192.168.1.19 | DESKTOP-LIVINGR |          Dell Inc.           |
| Thu Aug  6 09:19:02 2020 | xx:xx:xx:xx:xx:xx | 192.168.1.14 |     verycool    |  Flextronics International   |
| Thu Aug  6 10:41:42 2020 | xx:xx:xx:xx:xx:xx | 192.168.1.17 |    somephone1   | Xiaomi Communications Co Ltd |
| Thu Aug  6 06:43:17 2020 | xx:xx:xx:xx:xx:xx | 192.168.1.56 |    somephone2   | Xiaomi Communications Co Ltd |
+--------------------------+-------------------+--------------+-----------------+------------------------------+
```

Vendor name is obtained from the [OUI database](http://standards-oui.ieee.org/oui.txt).
