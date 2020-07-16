#UTF-8
import math

class Vector:
	def __init__(self,values):
		"""
		Recibe values(string) que contiene al vector con sus componentes separados por comas.
		"""
		self.vector = list(map(float, values.split(','))) 
		self.dimension = len(self.vector)


	def sumar(self,vector):
		"""
		Recibe vector(objeto) para sumar. Regresa la suma de los dos vectores (list)
		"""	
		list=[]
		if self.dimension == vector.dimension:
			for i in range(self.dimension):
				list.append(self.vector[i]+vector.vector[i])

			return list

		else:
			return 'No es posible sumar vetores'

	def restar(self,vector):
		"""
		Recibe otro vector(objeto) para restar.
		"""		
		list=[]
		if self.dimension == vector.dimension:
			for i in range(self.dimension):
				list.append(self.vector[i] - vector.vector[i])

			return list

		else:
			return '    No es posible restar vetores'

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
		if self.dimension == vector.dimension:
			modulo1 = self.modulo()
			modulo2 = vector.modulo()
			angulo = self.angulo(vector)
			return pow(modulo1**2 + modulo2**2 + 2*modulo1*modulo2*(math.cos(angulo)),0.5)
		else:
			return '    No es posible calcular el angulo entre vetores'	
		

	def angulo(self,vector):
		"""
		Recibe otro vector(objeto) para calcular el angulo entre ellos.
		"""	
		if self.dimension == vector.dimension:
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
		for i in range(self.dimension):
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
		for i in range(self.dimension):
			sumatoria += self.vector[i]**2

		return pow(sumatoria,0.5)						

		

def menu_principal():	
	print('-----------------*-------------')
	print('     Calculadora de vectores')
	print('\n \n        [1]Sumar vectores')
	print('        [2]Restar vectores')
	print('        [3]Multiplicar vector por escalar')
	print('        [4]Calcular resultante entre vectores')
	print('        [5]Calcular angulo entre dos vectores')
	return input('\n            => ')			

if __name__ == '__main__':

	texto = '    Ingresa vector separado por comas => '

	while True:
		opcion = menu_principal()
		if opcion == '1': # Suma
			print('\n\n-----------------*------------------')
			print('     [1]Sumar vectores\n')

			vector1 = Vector(input(texto))
			vector2 = Vector(input(texto)) 

			print('\n    Resultado:',vector1.sumar(vector2)) 
			break

		elif opcion == '2':# Resta
			print('\n\n-----------------*------------------')
			print('     [2]Restar vectores\n')

			vector1 = Vector(input(texto))
			vector2 = Vector(input(texto))  

			print('\n    Resultado:',vector1.restar(vector2)) 
			break

		elif opcion == '3':# Multi. por escalar
			print('\n\n-----------------*------------------')
			print('     [3]Multiplicar vector por escalar\n')

			vector1 = Vector(input(texto))
			escalar = input('    Ingresa escalar =>')

			print('\n    Resultado:',vector1.multiplicar(escalar)) 
			break

		elif opcion == '4':# Resultante
			print('\n\n-----------------*------------------')
			print('     [4]Calcular resultante entre vectores\n')

			vector1 = Vector(input(texto))
			vector2 = Vector(input(texto))
			print('\n    Resultado:',vector1.resultante(vector2))   
			break

		elif opcion == '5':# Angulo
			print('\n\n-----------------*------------------')
			print('     [5]Calcular angulo entre dos vectores\n')

			vector1 = Vector(input(texto))
			vector2 = Vector(input(texto)) 
			print('\n    Resultado:',vector1.angulo(vector2)) 
			break

		else:
			print('\n    Opcion iválida')
			print('        Selccione otra opcion: ')
			