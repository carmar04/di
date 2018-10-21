print("Digame cuantas palabras tiene la lista")
numeroLineas = input()
numeroLineas = int(numeroLineas)
lista = []
indice = 0
flag = True
if numeroLineas > 0:
	flag = True
else:
	flag = False
if flag == True:
	while indice < numeroLineas:
		print("Digame la palabra "+str(indice+1)+": ")
		palabra = input()
		lista.append(palabra)
		indice = indice + 1
	print("La lista creada es: "+str(lista))
else:
	print("¡imposible!")

