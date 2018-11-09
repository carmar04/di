#! /usr/bin/python3
# Definimos la función
def comparador(var1, var2):
		# Comparamos las casuísticas posibles
		if var1 > var2:
			print("var1 es mayor que var2")
		elif var1 == var2:
			print("var1 y var2 son iguales")
		elif var1 < var2:
			print("var1 es mas pequeño que var2")
# Comprobamos para que se introduzca valores númericos
try:
	var1 = int(input("Introduzca el valor de var1: "))
	var2 = int(input("Introduzca el valor de var2: "))
	comparador(var1, var2)
# Capturamos el error
except:
	print("Es una cadena")




