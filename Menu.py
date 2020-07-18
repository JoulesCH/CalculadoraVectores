class Menu_princial:
	def __init__(self,opcion='0'):
		self.opcion = opcion
		self.opciones = {'1':'[1] Suma','2':'[2] Resta','3':'[3] Multiplicacion','4':'[4] Resultante','5':'[5] Angulo'}

	def imprimir(self):
		print('-----------------*-------------')
		print('     Calculadora de vectores')
		print('\n \n        [1]Sumar vectores')
		print('        [2]Restar vectores')
		print('        [3]Multiplicar vector por escalar')
		print('        [4]Calcular resultante entre vectores')
		print('        [5]Calcular angulo entre dos vectores')

	def pedir_opcion(self):
		self.opcion = input('\n            => ')
		self.verificar_opcion()
		#return input('\n            => ')

	def verificar_opcion(self):
		if self.opcion == '1' or self.opcion =='2' or self.opcion=='3' or  self.opcion =='4' or  self.opcion =='5':
			print('\n\n-----------------*------------------')
			print('         ',self.opciones[self.opcion],'\n')
		else:
			print('\n    Opcion inválida')
			print('      Selccione otra opcion: ')
			self.pedir_opcion()
