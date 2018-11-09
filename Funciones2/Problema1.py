#! /usr/bin/python3
def iterPower(base, exp):
	'''
	base: int or float.
	exp int >= 0
	return int or float.

	'''
	resultado = base
	for indice in range(1,exp):
		resultado = resultado * base
	return resultado
try:
	'''
	Comprobamos que los parametros pasados son numericos
	En caso de que no se introduzca un numero mostramos el mensaje
	En caso de que el exponete sea mayor que 0 lanzamos la función
	
	'''
	base = float(input("Introduzca la base: "))
	exp = int(input("introduca el exponente: "))
	if exp < 0:
		print("El exponente es menor que 0")
	else:
		print("El resultado es: " + str(iterPower(base, exp)))
except:
	print("Debe introducir valores enteros")

