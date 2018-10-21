checked = True
while checked == True:
	print("Dígame cuántas palabras tiene la lista:")
	numeroLineas = input()
	numeroLineas = int(numeroLineas)
	indice = 0
	lista = []
	while indice < numeroLineas:
		print("Digame la palabra "+str(indice + 1)+":")
		respuesta = input()
		lista.append(respuesta)
		indice = indice + 1
	print("La lista creada es: "+str(lista))
	print("Digame la palabra a buscar: ")
	buscador = input()
	if lista.count(buscador) > 0:
		if lista.count(buscador) == 1:
			print("La palabra \'"+str(buscador)+"\' aparece una vez en la lista")
		else:
			print("La palabra \'"+str(buscador)+"\' aparece "+str(lista.count(buscador))+" veces")
	else:
		print("La palabra \'"+str(buscador)+"\' no esta en la lista")
		checked = False
	
