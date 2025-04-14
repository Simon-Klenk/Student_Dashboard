from datetime import date

class Modul:
    """
    Repräsentiert ein Modul mit Name, Credits, Note und Datum.
    """
    def __init__(self, modul_name: str, modul_credits: int, modul_note: float, modul_datum: date):
        """
        Initialisiert ein Modul mit Name, Credits, Note und Datum.
        :param modul_name: Name des Moduls
        :param modul_credits: Anzahl der Credits des Moduls
        :param modul_note: Note des Moduls
        :param datum: Datum des Moduls
        """
        self.__modul_name = modul_name
        self.__modul_credits = modul_credits
        self.__modul_note = modul_note
        self.__modul_datum = modul_datum

    def set_modul_name(self, modul_name: str):
        self.__modul_name = modul_name

    def get_modul_name(self) -> str:
        return self.__modul_name

    def set_modul_credits(self, modul_credits: int):
        self.__modul_credits = modul_credits

    def get_modul_credits(self) -> int:
        return self.__modul_credits

    def set_modul_note(self, modul_note: float):
        self.__modul_note = modul_note

    def get_modul_note(self) -> float:
        return self.__modul_note

    def set_modul_datum(self, datum: date):
        self.__modul_datum = datum

    def get_modul_datum(self) -> date:
        return self.__modul_datum
