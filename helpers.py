import logging
import inspect
import os


def make_log(message: str = "", level: int = 1) -> None:
    """
    Enregistre un message dans le log avec le niveau spécifié.

    :param message: Le message à inscrire dans le log.
    :param level: Le niveau de sévérité du log.
        - 1 : DEBUG
        - 2 : INFO
        - 3 : WARNING
        - 4 : ERROR
        - 5 : CRITICAL
    """
    # Récupérer le fichier appelant
    frame = inspect.stack()[1]
    filename = os.path.basename(frame.filename)

    # Configuration du logger
    logging.basicConfig(
        filename="./app.log",
        format="{asctime} - {levelname} - {message}",
        style="{",
        datefmt="%Y-%m-%d %H:%M",
    )
    logger = logging.getLogger("CustomLogger")

    # Dictionnaire pour mapper les niveaux numériques aux niveaux de log
    log_levels = {
        1: logger.debug,
        2: logger.info,
        3: logger.warning,
        4: logger.error,
        5: logger.critical,
    }

    log_function = log_levels.get(level, logger.debug)
    log_message = f"[{filename}] {message}"
    log_function(log_message)
