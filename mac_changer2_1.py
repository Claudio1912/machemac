#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-

import subprocess

# CREO LE VARIABILI interface E new_mac 
interface = raw_input("interface > ")
new_mac = raw_input("new_MAC > ")
# input SE UTILIZZO Python 3

print ("[+] Cambio l'indirizzo MAC per l'interfaccia " + interface + " a " + new_mac)

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"]) 


