#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-

# FUNZIONA SOLO CON L'INPUT DA PARTE DELL'UTENTE python mac_changer2_2.py -i enp2s0 -m 11:22:33:44:55:66

import subprocess
import optparse

parser = optparse.OptionParser()
# parser E' UN OGGETTO, UN'ISTANZA (VARIABILE) DELLA CLASSE/FUNZIONE OptionParser FORNITA DAL MODULO optparse.
# optparse.OptionParser() È UN COSTRUTTORE CHE CREA UN NUOVO OGGETTO ANALIZZATORE DI OPZIONI. QUESTO OGGETTO parser HA LO SCOPO DI DEFINIRE E 
# ANALIZZARE LE OPZIONI CHE POSSONO ESSERE PASSATE A UNO SCRIPT DA RIGA DI COMANDO.
# POSSO USARE IL METODO add_option() PER SPECIFICARE LE DIVERSE OPZIONI CHE LO SCRIPT ACCETTERÀ
# E IL METODO parse_args() DELL'OGGETTO parser PER PRENDERE GLI ARGOMENTI DALLA RIGA DI COMANDO E CONFRONTARLI CON LE OPZIONI DEFINITE PRIMA

# parser.add_option() RITORNA ALLA VARIABILE parser 2 SET DI INFORMAZIONI (SIA options CHE arguments)
parser.add_option("-i", "--interface", dest="interface", help="Interfaccia a cui cambiare MAC")
parser.add_option("-m", "--mac", dest="new_mac", help="Nuovo indirizzo MAC")
(options, arguments) = parser.parse_args()

interface = options.interface
# raw_input("interface > ")
new_mac = options.new_mac
# raw_input("new_MAC > ")

# SONO ENTRAMBE options

print ("[+] Cambio l'indirizzo MAC per l'interfaccia " + interface + " a " + new_mac)

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"]) 


