"""Cuenta palabras en frases"""
PALABRAS = "palabras.txt"
FRASES = "frases.txt"
archivo = open(PALABRAS, "r")
palabras = []
for linea in archivo:
    palabras[linea.stip()] = []
print("Lista de palabras: \n", palabras)

archivo = open(FRASES, "r")
