# Ejemplo de utilizacion del modulo logging para creación de archivos log's
# con la definicion/configuracion incluida en el código

# Importar el módulo: 
import logging

#Crear un logger:
logger = logging.getLogger(__name__)

#Configurar el handler (opcional):
handler = logging.FileHandler('archivo_registro.log')

#Configurar el formatter (opcional):
#ejemplo 1
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#ejemplo 2
formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s', "%Y-%m-%d %H:%M:%S")
handler.setFormatter(formatter)

#Añadir el handler al logger: 
logger.addHandler(handler)

#Establecer el nivel de registro:
logger.setLevel(logging.DEBUG)

#Registrar mensajes:
logger.debug('Este es un mensaje de depuración')
logger.info('Este es un mensaje informativo')
logger.warning('Este es un mensaje de advertencia')
logger.error('Este es un mensaje de error')
logger.critical('Este es un mensaje crítico')

#
#
