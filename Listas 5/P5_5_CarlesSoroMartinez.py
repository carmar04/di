print("Dígame cuántas palabras tiene la lista: ")
numeroLineas = int(input())
lista = []
for indice in range(numeroLineas):
	print("Dígame la palabra " + str(indice) + ":")
	respuesta = input()
	lista.append(respuesta)
print("La lista creada es: " + str(lista))

print("Dígame cuantas palabras tiene la lista de palabras a eliminar: ")
numeroLineas2 = int(input())
lista2 = []
for indice in range(numeroLineas2):
	print("Dígame la palabra " + str(indice) + ":")
	respuesta2 = input()
	lista2.append(respuesta2)
print("La lista de palabras a eliminar es: " + str(lista2))

lista = set(lista)
lista2 = set(lista2)
lista3 = lista - lista2
print("La lista es ahora: " + str(lista3))
