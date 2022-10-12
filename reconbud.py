#!/usr/bin/env python
#
# ReconBud - Linux tool for automating reconnaissance
#
# Description:
#   This script will automate common pentest reconnaissance phases like Nmap scan,
#   directory busting and whois directory lookup.
#
#   For instructions on how to use this script, run the script (like -> python reconbud.py) 
#   and choose the "Instructions" option.
#
# Author:
#   Johith Iype (@laser3y3s)
#

import subprocess as sp
print(""" 

██████╗ ███████╗ ██████╗ ██████╗ ███╗   ██╗██████╗ ██╗   ██╗██████╗ 
██╔══██╗██╔════╝██╔════╝██╔═══██╗████╗  ██║██╔══██╗██║   ██║██╔══██╗
██████╔╝█████╗  ██║     ██║   ██║██╔██╗ ██║██████╔╝██║   ██║██║  ██║
██╔══██╗██╔══╝  ██║     ██║   ██║██║╚██╗██║██╔══██╗██║   ██║██║  ██║
██║  ██║███████╗╚██████╗╚██████╔╝██║ ╚████║██████╔╝╚██████╔╝██████╔╝

** https://github.com/laser3y3s/reconbud  **

""")

print( """ ReconBud has 4 levels of scan intensity

    Level 1 - Highest
    Level 2 - High
    Level 3 - Low
    Level 4 - Lowest
	""" )

# recon_lvl = input("Enter Recon Level of your choice. Enter 1 for Highest or 4 for lowest \n")

target_ip = input("Enter target IP address")


nmap_command = f"nmap {target_ip}; exec bash"


bash_command = f""" gnome-terminal --tab -e 'bash -c \"{nmap_command}"' \
--tab -e 'bash -c \"echo second; echo bar; exec bash\"'
"""

sp.Popen(bash_command, shell=True)

