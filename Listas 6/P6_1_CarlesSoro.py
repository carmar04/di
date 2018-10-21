#! /usr/bin/env python3
numeroLineas = input("Dígame cuantas palabras tiene la lista: ")
lista = []
if numeroLineas.isdigit():
	for indice in range(int(numeroLineas)):
		respuesta = input("Dígame la palabra " + str(indice + 1) + " : ")
		lista.append(respuesta)
	print("La lista creada es: " + str(lista))
	print("La lista ordenada es: " + str(sorted(lista)))
else:
	print("Debe introducir un numero.")
