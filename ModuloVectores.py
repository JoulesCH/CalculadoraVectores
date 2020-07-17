import math

class Vector:
	def __init__(self,values):
		"""
		Recibe values(string) que contiene al vector con sus componentes separados por comas.
		"""
		self.vector = list(map(float, values.split(',')))
		self.__dimension = len(self.vector) #Abstracción: Encapsulamiento.


	def sumar(self,vector):
		"""
		Recibe vector(objeto) para sumar. Regresa la suma de los dos vectores (list)
		"""
		list=[]
		if self.__dimension == vector.__dimension:
			for i in range(self.__dimension):
				list.append(self.vector[i]+vector.vector[i])

			return list

		else:
			return 'No es posible sumar esos vetores'

	def restar(self,vector):
		"""
		Recibe otro vector(objeto) para restar.
		"""
		list=[]
		if self.__dimension == vector.__dimension:
			for i in range(self.__dimension):
				list.append(self.vector[i] - vector.vector[i])

			return list

		else:
			return '    No es posible restar esos vetores'

	def multiplicar(self,escalar):
		"""
		Recibe un escalar(float) para multiplicar.
		"""
		try:
			escalar = float(escalar)
		except:
			return '    El escalar ingresado no es válido'
		else:
			return [x*escalar for x in self.vector ] #Se utlizó lis comprohension

	def resultante(self,vector):
		"""
		Recibe otro vector(objeto) para calcular la resultante entre ellos.
		"""
		if self.__dimension == vector.__dimension:
			modulo1 = self.modulo()
			modulo2 = vector.modulo()
			angulo_radianes = math.radians(self.angulo(vector))

			return pow(modulo1**2 + modulo2**2 + 2*modulo1*modulo2*(math.cos(angulo_radianes)),0.5)
		else:
			return '    No es posible calcular el angulo entre vetores'


	def angulo(self,vector):
		"""
		Recibe otro vector(objeto) para calcular el angulo entre ellos.
		"""
		if self.__dimension == vector.__dimension:
			numerador = self.producto_punto(vector)
			denominador = self.producto_modulos(vector)

			return math.degrees(math.acos(numerador/denominador))

		else:
			return '    No es posible calcular el angulo entre vetores'

	def producto_punto(self,vector):
		"""
		Recibe otro vector (objeto) y regresa su producto punto
		"""
		sumatoria = 0
		for i in range(self.__dimension):
			sumatoria += self.vector[i]*vector.vector[i]
		return sumatoria

	def producto_modulos(self,vector):
		"""
		Recibe otro vector (objeto) y regresa el producto de sus modulos.
		"""
		return self.modulo()*vector.modulo()

	def modulo(self):
		"""
		Regresa el modulo del vector propio.
		"""
		sumatoria = 0
		for i in range(self.__dimension):
			sumatoria += self.vector[i]**2

		return pow(sumatoria,0.5)
