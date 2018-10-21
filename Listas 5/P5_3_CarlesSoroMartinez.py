print("Dígame cuántas palabras tiene la lista: ")
numeroLineas = input()
numeroLineas = int(numeroLineas)
indice = 0
lista = []
while indice < numeroLineas:
	print("Dígame la palabra " + str(indice + 1) + ": ")
	respuesta = input()
	lista.append(respuesta)
	indice = indice + 1
print("La lista creada es: " + str(lista))
print("Sustituir la palabra: ")
buscador = input()
print("Por la palabra: ")
reemplazo = input()
indice2 = 0
while indice2 < len(lista):
	if lista[indice2] == buscador:
		lista[indice2] = reemplazo
	indice2 = indice2 + 1
print("La lista es ahora: " + str(lista))
