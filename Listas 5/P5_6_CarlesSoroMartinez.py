#! /bin/usr/env python3
numeroLineas = input("Dígame cuantas palabras tiene la lista: ")
if numeroLineas.isdigit():
	lista = []
	# Creamos la lista gracias al bucle for
	for indice in range(0, numeroLineas):
		respuesta = input("Dígame la palabra " + str(indice + 1) + ":")
		#! Añadimos los elementos pasados por teclado
		lista.append(respuesta)
	# Mostramos la lista
	print("La lista creada es: " + str(lista))
	# Invertimos la lista y la mostramos
	print("La lista inversa es: " + str(lista[::-1]))
else:
	print("Debe introducir un numero")
