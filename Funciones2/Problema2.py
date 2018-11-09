#! /usr/bin/python3
def gcdIter(a, b):
	'''
	Definimos la función y creamos dos listas para guardar los exponentes
	Gracias a la transformación de de lista en conjuntos podemos aprovechas sus comparaciones
	'''
	lista1 = []
	lista2 = []
	resultado = 0
	for indice in range(1, a + 1):
		if a % indice == 0:
			lista1.append(indice)
	for indice in range(1, b + 1):
		if b % indice == 0:
			lista2.append(indice)
	conjunto1 = set(lista1)
	conjunto2 = set(lista2)
	conjunto3 = list(conjunto1 & conjunto2)
	resultado = conjunto3[len(conjunto3) - 1]
	return resultado
try:
	'''
	Comprobamos que los parametros pasados son numericos
	En caso de que no se introduzca un numero mostramos el mensaje
	En caso de que el exponete sea mayor que 0 lanzamos la función
	
	'''
	a = int(input("Introduzca el primer valor: "))
	b = int(input("Introduca el segundo valor: "))
	print("El maximo común divisor es: " + str(gcdIter(a,b)))
	
except:
	print("Debe introducir valores enteros")
