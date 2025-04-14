from typing import List
from modul import Modul

class Semester:
    """
    Repräsentiert ein Semester mit Nummer, Credits und einer Liste von Modulen.
    """
    def __init__(self, semester_nummer: int):
        """
        Initialisiert ein Semester mit Nummer und leerer Modul-Liste.
        :param semester_nummer: Nummer des Semesters
        """
        self.__semester_nummer = semester_nummer
        self.__semester_credits = 0
        self.__module: List[Modul] = []

    def set_semester_nummer(self, semester_nummer: int):
        self.__semester_nummer = semester_nummer

    def get_semester_nummer(self) -> int:
        return self.__semester_nummer

    def add_modul(self, modul: Modul):
        self.__module.append(modul)
        self.__semester_credits += modul.get_modul_credits()

    def get_module(self) -> List[Modul]:
        return self.__module

    def berechne_durchschnitt(self) -> float:
        """
        Berechnet den Notendurchschnitt aller Module im Semester.
        :return: Durchschnittsnote oder 0.0 falls keine Module vorhanden sind.
        """
        if not self.__module:
            return 0.0
        return sum(modul.get_modul_note() for modul in self.__module) / len(self.__module)

    def get_semester_credits(self) -> int:
        return self.__semester_credits
