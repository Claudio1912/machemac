#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-

# python mac_changer2_5.py -i enp2s0 -m 11:00:03:04:05:66

import subprocess
import optparse
import re

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New Mac address")
    (options, arguments) = parser.parse_args()
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

# LA VARIABILE DELLA FUNZIONE SOTTO NON SARA' options.interface MA interface .. E ANCHE 1 RIGA SOTTO SOTTO
def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
    if mac_address_search_result:
      # print(mac_address_search_result.group(0)) LO CANCELLO PERCHE' LO PRINTO IN FONDO ALLA CHIAMATA IN BASSO ***
      # QUI DEVE SOLO RITORNARE CON return 
        return mac_address_search_result.group(0)
    else:
        print("[-] Non posso leggere il MAC address")


# CHIAMIAMO LA FUNZIONE get_current_mac(........) PER VEDERE LA MAC DELL'INTERFACCIA
options = get_arguments()
current_mac = get_current_mac(options.interface)
print("MAC corrente = " + str(current_mac))
# INVECE DI print("MAC corrente = " + current_mac)
# DEVO FARE IL CASTING TRATTANDO current_mac COME STRINGA str(current_mac) E QUESTO SE L'INTERFACCIA NON ESISTE

# QUESTA CHIAMATA SOTTO CAMBIA LA MAC UNA VOLTA IMMESSA LA NUOVA DALL'UTENTE
change_mac(options.interface, options.new_mac)

# LA CHIAMATA SOTTO RACCOGLIE LA CURRENT MAC DOPO IL CAMBIAMENTO AVVENUTO CON LA FUNZIONE PRECEDENTE E IL RISULTATO SI IMMAGAZZINA
# NELLA VARIABILE current_mac (CHE E' UGUALE A QUELLA POCO SOPRA SOLO CHE QUI IMMAGAZZINA IL DATO DOPO IL CAMBIO FATTO DALL'UTENTE) E'
# SOVRASCRITTO IL VALORE PRECEDENTE (IN PYTHON SI PUO' FARE)
current_mac = get_current_mac(options.interface)
if current_mac == options.new_mac:
    print("[+] Il MAC address è stato cambiato con successo a: " + current_mac)
else:
    print("[-] Il MAC address NON RISULTA CAMBIATO!")















