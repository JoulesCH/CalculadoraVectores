
from Menu import Menu_princial #Modulacion
from ModuloVectores import Vector #Modulacion

class Datos (Menu_princial): #Herencia
	def __init__(self):
		Menu_princial.__init__(self)
		self.__texto = '    Ingresa vector separado por comas => ' #Abstraccion: Encapsulamiento

	def pedir_datos(self):
		self.pedir_opcion()
		if self.opcion == '1' or self.opcion =='2' or self.opcion =='4' or self.opcion =='5':
			try:
				self.vector1 = Vector(input(self.__texto))
				self.vector2 = Vector(input(self.__texto))
			except:
				print('    Los vectores unicamente se componen de números')
				return 0
			else:
				self.imprimir() #Polimorfismo

		elif self.opcion =='3':
			try:
				self.vector1 = Vector(input(self.__texto))
			except:
				print('    Los vectores unicamente se componen de números')
				return 0

			else:
				self.escalar = input('    Ingresa escalar =>')
				self.imprimir() #Polimorfismo

	def imprimir(self):
		if self.opcion == '1':
			print('\n    Resultado:',self.vector1.sumar(self.vector2))
		elif self.opcion == '2':
			print('\n    Resultado:',self.vector1.restar(self.vector2))
		elif self.opcion == '3':
			print('\n    Resultado:',self.vector1.multiplicar(self.escalar))
		elif self.opcion == '4':
			print('\n    Resultado:',self.vector1.resultante(self.vector2))
		elif self.opcion == '5':
			print('\n    Resultado:',self.vector1.angulo(self.vector2))
