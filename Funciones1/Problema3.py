#! /usr/bin/python3
string = input("Introduzca un caracter para ver si es alguna vocal: ")
# Definimos la función
def isVowel(char):
	# Iniciamos el flag
	checker = False
	# En caso de introducir más de un caracter mostrará mensaje
	if len(char) > 1:
		print("Debe introducir solo un caracter, ha introducido " + str(len(char)) + " caracteres")
	else:
		if char in "aeiouAEIOU":
			checker = True
	# En caso verdadero
	if checker == True:
		return True
	# En caso falso
	else:
		return False
# Imprimimos el resultado
print("Devuelve: " + str(isVowel(string)))
