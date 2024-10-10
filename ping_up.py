from os import system
from sys import argv
from ipaddress import IPv4Address

try :
    IPv4Address(argv[1])
    return_code = system(f"ping {argv[1]} > null 2>&1")

    if return_code == 0 :
        print("UP !")

    else :
        print("DOWN !")
except :
    print("Bah frérot, faut mettre une adresse ip valide !")