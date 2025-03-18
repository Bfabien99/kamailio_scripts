# from helpers import make_log


class MissingDataError(Exception):
    """Exception de base pour les données manquantes."""

    def __init__(self, message="Données manquantes"):
        super().__init__(message)
        # make_log(message, 4)
        print(message)


class InvalidDataError(Exception):
    """Exception de base pour les données invalides."""

    def __init__(self, message="Données manquantes"):
        super().__init__(message)
        # make_log(message, 4)
        print(message)
