# Código modificado y tomado de ejemplo del curso gratuito "UskoKruM2010_Python"
# Se respeta la autoría original, nombrando al autor, y su canal,
# como asi tambien se invita a visualizar el mismo.
# Se agradece su aporte y colaboracíon que brinda con sus curso gratuitos en su pagina web y su canal.
#
# Autor original: Oscar Alejandro Flavio García Fuentes (Oscar García Fuentes, UskoKruM)
# LinkEdin: https://pe.linkedin.com/in/uskokrum2010 , WebSite: https://uskokrum2010.com/
# Curso de Python en el canal de youtube [UskoKruM2010](https://youtube.com/UskoKruM2010)
# Curso de Python desde 0, creado en YouTube. en el canal.
# Todos los videos del curso:(https://www.youtube.com/playlist?list=PL_wRgp7nihybbJ2vZaVGI5TDdPaK_dFuC)


import logging
import os
import traceback


class Logger():

    def __set_logger(self):
        log_directory = './logs'
        # log_directory = '.' # utiliza la carpeta actual
        log_filename = 'app.log'

        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)

        log_path = os.path.join(log_directory, log_filename)
        file_handler = logging.FileHandler(log_path, encoding='utf-8')
        file_handler.setLevel(logging.DEBUG)

        formatter = logging.Formatter(
            '%(asctime)s | %(levelname)s | %(message)s', "%Y-%m-%d %H:%M:%S")
        file_handler.setFormatter(formatter)

        if (logger.hasHandlers()):
            logger.handlers.clear()

        logger.addHandler(file_handler)

        return logger

    @classmethod
    def add_to_log(cls, level, message):
        try:
            logger = cls.__set_logger(cls)

            if (level == "critical"):
                logger.critical(message)
            elif (level == "debug"):
                logger.debug(message)
            elif (level == "error"):
                logger.error(message)
            elif (level == "info"):
                logger.info(message)
            elif (level == "warn"):
                logger.warn(message)
        except Exception as ex:
            print(traceback.format_exc())
            print(ex)
