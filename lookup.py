from socket import gethostbyname
from sys import argv
from re import search

name = search("[a-z]+[0-9]*\.[a-z]", argv[1])
if name:
    print(gethostbyname(argv[1]))
else:
    print("Fait un effort, fait au moins semblant de mettre un vrai site mec !")