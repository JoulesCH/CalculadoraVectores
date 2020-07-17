#UTF-8
import math
from ModuloVectores import Vector #Modulacion			

		
class Menu_princial:
	def __init__(self,opcion='0'):
		self.opcion = opcion

	def imprimir(slef):
		print('-----------------*-------------')
		print('     Calculadora de vectores')
		print('\n \n        [1]Sumar vectores')
		print('        [2]Restar vectores')
		print('        [3]Multiplicar vector por escalar')
		print('        [4]Calcular resultante entre vectores')
		print('        [5]Calcular angulo entre dos vectores')

		self.opcion = input('\n            => ')

class Maestro (Menu_princial): #Herencia
	def __init__(self):
		Menu_princial.__init__()

	def pedir_datos(self):
		if self.opcion == '1' or self.opcion =='2' or self.opcion =='4' or or self.opcion =='5':
			try:
				self.vector1 = Vector(input(texto))
				self.vector2 = Vector(input(texto)) 
			except:
				print('    Los vectores unicamente se componen de números')	
				return 0
			else:	
				return 1
		
		elif self.opcion =='3':
			try:
				self.vector1 = Vector(input(texto))
			except:
				print('    Los vectores unicamente se componen de números')	
				return 0
			
			else:
				self.escalar = input('    Ingresa escalar =>')
				return 1

			
if __name__ == '__main__':

	texto = '    Ingresa vector separado por comas => '

	while True:
		menu = Menu_princial()
		opcion = menu.imprimir()
		if opcion == '1': # Suma
			print('\n\n-----------------*------------------')
			print('     [1]Sumar vectores\n')
			try:
				vector1 = Vector(input(texto))
				vector2 = Vector(input(texto)) 
			except:
				print('    Los vectores unicamente se componen de números')	
			else:	
				print('\n    Resultado:',vector1.sumar(vector2)) 

			salir = input('    SALIR? [1/0] =>')
			if salir == '1':
				break	

		elif opcion == '2':# Resta
			print('\n\n-----------------*------------------')
			print('     [2]Restar vectores\n')

			try:
				vector1 = Vector(input(texto))
				vector2 = Vector(input(texto)) 
			except:
				print('    Los vectores unicamente se componen de números')	
			else: 

				print('\n    Resultado:',vector1.restar(vector2)) 

			salir = input('    SALIR? [1/0] =>')
			if salir == '1':
				break

		elif opcion == '3':# Multi. por escalar
			print('\n\n-----------------*------------------')
			print('     [3]Multiplicar vector por escalar\n')
			try:
				vector1 = Vector(input(texto))
			except:
				print('    Los vectores unicamente se componen de números')	
			
			else:
				escalar = input('    Ingresa escalar =>')
				print('\n    Resultado:',vector1.multiplicar(escalar)) 

			salir = input('    SALIR? [1/0] =>')
			if salir == '1':
				break

		elif opcion == '4':# Resultante
			print('\n\n-----------------*------------------')
			print('     [4]Calcular resultante entre vectores\n')

			try:
				vector1 = Vector(input(texto))
				vector2 = Vector(input(texto)) 
			except:
				print('    Los vectores unicamente se componen de números')	
			else:

				print('\n    Resultado:',vector1.resultante(vector2))  

			salir = input('    SALIR? [1/0] =>')
			if salir == '1':
				break

		elif opcion == '5':# Angulo
			print('\n\n-----------------*------------------')
			print('     [5]Calcular angulo entre dos vectores\n')

			try:
				vector1 = Vector(input(texto))
				vector2 = Vector(input(texto)) 
			except:
				print('    Los vectores unicamente se componen de números')	
			else:
				print('\n    Resultado:',vector1.angulo(vector2)) 

			salir = input('    SALIR? [1/0] =>')
			if salir == '1':
				break

		else:
			print('\n    Opcion iválida')
			print('        Selccione otra opcion: ')
			