print("Dígame cuántas palabras tiene la lista: ")
numeroLineas = input()
numeroLineas = int(numeroLineas)
lista = []
indice = 0
while indice < numeroLineas:
	print("Dígame la palabra " + str(indice + 1) + ":")
	respuesta = input()
	lista.append(respuesta)
	indice = indice + 1
print("La lista creada es: " + str(lista))
print("Palabra a eliminar: ")
respuesta2 = input()
if lista.count(respuesta2) > 0:
	indice2 = 0
	while indice2 < len(lista):
		if lista[indice2] == respuesta:
			lista.remove(respuesta)
		indice2 = indice2 + 1
	print("La lista es ahora " + str(lista))
else:
	print("Ese elemento no esta en la lista")


