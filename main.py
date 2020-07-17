#UTF-8
from Pedir_Datos_O_Imprimirlos import Datos #Modulacion
from Menu import Menu_princial #Modulacion

if __name__ == '__main__':


	while True:
		menu = Menu_princial()
		menu.imprimir()

		master = Datos()
		master.pedir_datos()

		salir = input('    SALIR? [1/0] =>')
		if salir == '1':
			break
