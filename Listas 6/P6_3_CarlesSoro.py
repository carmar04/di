#! /usr/bin/env python3
numero = input("Dígame un número: ")
if numero.isdigit():
	lista = [1]
	numero = int(numero)
	checker = True
	for indice1 in range(2, numero + 1):
		for indice2 in range(2, indice1):
			if indice1 % indice2 == 0:
				checker = False
		if checker == True:
			lista.append(indice1)
		checker = True
	print("Primos hasta " + str(numero) + ": " + str(lista))
				
