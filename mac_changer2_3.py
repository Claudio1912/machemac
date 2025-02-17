#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-

# PER PYTHON 2 E 3 ................. python mac_changer2_3.py -i enp2s0 -m 00:22:33:44:55:66
import subprocess
import optparse



def change_mac(interface, new_mac):
    print("[+] Cambia il MAC address  di " + interface + " a " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


parser = optparse.OptionParser()

parser.add_option("-i", "--interface", dest="interface", help="Interfaccia a cui cambiare MAC")
parser.add_option("-m", "--mac", dest="new_mac", help="Nuovo indirizzo MAC")
(options, arguments) = parser.parse_args()

# AVENDO CREATO IL BLOCCO FUNZIONE change_mac E SPOSTATO SOTTO ALLA CHIAMATA LE VARIABILI 
# PER interface E new_mac .........
# options.interface E ............ new_mac = options.new_mac
# LE 2 LINEE
# interface = options.interface
# new_mac = options.new_mac
#SI POSSONO TOGLIERE


change_mac(options.interface, options.new_mac)









