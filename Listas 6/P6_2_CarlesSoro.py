#! /usr/bin/env python3
numero = input("Dígame un numero: ")
lista = []
if numero.isdigit():
	numero = int(numero)
	for indice in range(1, numero + 1):
		if numero % indice == 0:
			lista.append(indice)
	print(str(numero) + " tiene " + str(len(lista)) + " divisores: " + str(lista))
