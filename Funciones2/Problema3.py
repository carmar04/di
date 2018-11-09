#! /usr/bin/python3
'''
Buscamos las coincidencias gracias a la función .count()
'''
st = input("Introduzca la cadena: ")
st2 = input("Introduzca las subacadena que desea buscar: ")
print("Numero de veces que aparece la cadena " + "'" + str(st2) + "'" + " : " +str(st.count(str(st2))))

