#! /usr/bin/python3
string = input("Introduzca una letra: ")
# Definimos la función
def isVowel(char):
	# Iniciamos el flag
	checker = False
	# En caso de introducir más de un caracter mostrará mensaje
	if len(char) > 1:
		print("Debe introducir solo un caracter, ha introducido " + str(len(char)) + " caracteres")
	else:
		if char == 'a' or char == 'e' or char == 'i' or char =='o' or char == 'u' or char == 'A' or char == 'E' or char == 'I' or char =='O' or char == 'U':
			checker = True
	if checker == True:
		# En caso verdadero
		return True
	else:
		# En caso falso
		return False
# Imprimos el resultado
print("Devuelve: " + str(isVowel(string)))
