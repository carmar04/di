#! /usr/bin/python3
st = input("Introduzca su orden: ")
'''
Definimos la funcion y buscamos si estan los substrings
dentro de la cadena pasada por parametro, en caso de que
sea así lo almacenamos en una variable que suma las coincidencias.

'''
def item_order(st):
	agua = st.count(str("agua"))
	hamburguesa = st.count(str("hamburguesa"))
	ensalada = st.count(str("ensalada"))
	print("Su pedido: ")
	print("Agua:        " + str(agua))
	print("Hamburguesa: " + str(hamburguesa))
	print("Ensalada:    " + str(ensalada))
	print("********************")

item_order(st)


