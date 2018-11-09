class Pais:
	# Creamos 
	def __init__(self, nombre, poblacion, area):
		self.nombre = nombre
		self.poblacion = poblacion
		self.area = area
	def masGrandeQue(self, object):
		return self.area > object.area
	def densidadDePoblacion(self):
		return self.poblacion / self.area

España = Pais("España", 46770000, 504645)
Francia = Pais("Francia", 66030000, 640679)
print("España es mas grande que Francia? " + str(España.masGrandeQue(Francia)))
print("Densidad de población de " + str(España.nombre) + ": " + str(España.densidadDePoblacion()))
print("Densidad de población de " + str(Francia.nombre) + ": " + str(Francia.densidadDePoblacion()))
