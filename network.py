from psutil import net_if_addrs
from socket import gethostbyname
from sys import argv
from re import search
from os import system
from ipaddress import IPv4Address

def lookup(arg):
    name = search("[a-z]+[0-9]*\.[a-z]", arg)
    if name:
        return gethostbyname(arg)
    else:
        return "Fait un effort, fait au moins semblant de mettre un vrai site mec !"
    
def ping(arg):
    try :
        IPv4Address(arg)
        return_code = system(f"ping {arg} > null 2>&1")

        if return_code == 0 :
            return "UP !"

        else :
            return "DOWN !"
    except :
        return "Bah frérot, faut mettre une adresse ip valide !"


def ip():
    trop_dinfos = net_if_addrs()
    wifi = trop_dinfos['Wi-Fi'].pop(1)
    address_wifi = wifi.address
    mask_wifi = wifi.netmask

    binary_address = ''
    for byte in mask_wifi.split("."):
        binary_byte = bin(int(byte))
        binary_address += binary_byte

    dispos = 2**(32-binary_address.count("1"))
    affichage = str(address_wifi + "\n" + str(dispos))

    return affichage

if argv[1] == "lookup":
    result = lookup(argv[2])
elif argv[1] == "ping":
    result = ping(argv[2])
elif argv[1] == "ip":
    result = str(ip())
else:
    result = "Vérifie mieux ta commande chef, elle existe pas celle là !"

print(result)