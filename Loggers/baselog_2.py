# Ejemplo de utilizacion del modulo logging para creación de archivos log's
# con la definicion/configuracion incluida en un paquete utils e importada
# posteriormente en el código

# Importar los módulo: 
import traceback
# Logger
from utils.Logger import Logger

#Registrar mensajes en cualquier parte:
Logger.add_to_log("debug",'Este es un mensaje de depuración')
Logger.add_to_log("info",'Este es un mensaje informativo')
Logger.add_to_log("warning",'Este es un mensaje de advertencia')
Logger.add_to_log("error",'Este es un mensaje de error')
Logger.add_to_log("critical",'Este es un mensaje crítico')

# ejemplo de utilizacion cuando se genera una excepción 

number1 = 20
number2 = 0 # probar el ejemplo poniendo un 0 (cero) o un 1 (uno)


def main():
    try:
        result = number1 / number2
        # cuando no se produce la excepción, se puede controlar el codigo desde el log
        # en lugar de estar generado print a la terminal
        print(f"El resultado es: {result}")
        Logger.add_to_log("info", "El resultado es: {}".format(result))
    except Exception as ex:
        Logger.add_to_log("error", str(ex))
        Logger.add_to_log("error", traceback.format_exc())
        print("No se puede dividir entre 0...")


main()
