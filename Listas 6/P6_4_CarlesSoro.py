#! /usr/bin/env python3
numero = input("Dígame un número: ")
if numero.isdigit():
	lista = []
	numero = int(numero)
	checker = True
	for indice in range(2, numero):
		if numero % indice == 0:
			checker = False
	if checker == True:
		print("El " + str(numero) + " es primo")
	else:
		print("El " + str(numero) + " no es primo")
