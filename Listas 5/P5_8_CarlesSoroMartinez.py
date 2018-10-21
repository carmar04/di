#! /bin/usr/env python3
numeroLineas1 = input("Dígame cuántas palabras tiene la primera lista: ")
if numeroLineas1.isdigit():
	lista1 = []
	# Iniciamos el bucle para rellenar la 1ª lista con los datos pasados por teclado
	for indice in range(0, numeroLineas1):
		respuesta1 = input("Digame la palabra " + str(indice + 1) + ": ")
		lista1.append(respuesta1)
	print("La primera lista es: " + str(lista1))
	numeroLineas2 = input("Dígame cuántas palabras tiene la primera lista: ")
	if numeroLineas2.isdigit() and numeroLineas1.isdigit():
		lista2 = []
		# Iniciamos el bucle para rellenar la 2ª lista con los datos pasados por teclado
		for indice in range(0, numeroLineas2):
			respuesta2 = input("Digame la palabra " + str(indice + 1) + ": ")
			lista2.append(respuesta2)
		print("La segunda lista es: " + str(lista2))
		# Pasamos las listas a conjuntos, ya que es más facil compararlas de esta manera
		conjunto1 = set(lista1)
		conjunto2 = set(lista2)
		# Mostramos los valores que coinciden en ambos conjuntos gracias a la puerta AND
		print("Palabras que aparecen en las dos listas " + str(conjunto1 & conjunto2))
		# Mostramos los valores que sean genuinos del primer conjunto gracias a la resta
		print("Palabras que solo aparecen en la primera lista: " + str(conjunto1 - conjunto2))
		# Mostramos los valores que sean genuinos del segundo conjunto gracias a la resta
		print("Palabras que solo aparecen en la segunda lista: " + str(conjunto2 - conjunto1))
		# Mostramos todos los valores sin repeticiones gracias a la puerta OR
		print("Todas las palabras: " + str(conjunto1 | conjunto2))


