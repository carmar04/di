#! /bin/usr/env python3
numeroLineas = int(input("Dígame cuantas palabras tiene la lista: "))
if numeroLineas.isdigit():
	lista = []
	# Iniciamos el bucle for para perdir las palabras a añadir a la lista
	for indice in range(0, numeroLineas):
		respuesta = input("Dígame la palabra " + str(indice + 1) + ": ")
		lista.append(respuesta)
	print("La lista creada es: " + str(lista))
	# Pasamos la lista creada como conjunto, debido a que los metodos que incorpora son de gran 	utilidad
	conjunto1 = set(lista)
	conjunto2 = set(lista)
	# Gracias a la puerta OR podemos mostrar los elementos de la lista sin repeticiones
	conjunto3 = conjunto1 | conjunto2
	# Mostramos el conjunto
	print("La lista sin repeticiones es: " + str(conjunto3))
else:
	print("Debe introducir un numero")
