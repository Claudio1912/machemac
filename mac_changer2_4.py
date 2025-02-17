#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-

# PER PYTHON 2 E 3 ................. python mac_changer2_4.py -i enp2s0 -m 00:00:03:04:05:66
import subprocess
import optparse


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New Mac address")
    (options, arguments) = parser.parse_args()

    
# CAMBIO QUESTA RIGA   return options  CON return parser.parse_args() RIASSEGNANDO NEL MOMENTO DELLA CHIAMATA DELLA FUNZIONE get_arguments()
# in fondo, IL RISULTATO DEL return ALLE STESSE VARIABILI options E arguments

   #return parser.parse_args()
    if not options.interface:
        parser.error("[+] Prego, specificare una interfaccia, usare --help per maggiori info.")
    elif not options.new_mac:
        parser.error("[+] Prego, specificare una nuova MAC, usare --help per maggiori info.")
    return options

def change_mac(interface, new_mac):
    print("[+] Cambia il MAC address  di " + interface + " a " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


parser = optparse.OptionParser()

parser.add_option("-i", "--interface", dest="interface", help="Interfaccia a cui cambiare MAC")
parser.add_option("-m", "--mac", dest="new_mac", help="Nuovo indirizzo MAC")
(options, arguments) = parser.parse_args()


# get_arguments() LO CAMBIO IN (options, arguments) = get_arguments()
# MA POI DEVO PORTARE (options, arguments) SOPRA AL POSTO DI return ... (options, arguments) = parser.parse_args()
# INSERIRE LA VARIABILE options E RIMETTERE SOPRA return options PRECEDUTO DA TUTTE LE POSSIBILITA' DI INSERIMENTO DATI SBAGLIATO ...
options = get_arguments()
change_mac(options.interface, options.new_mac)









