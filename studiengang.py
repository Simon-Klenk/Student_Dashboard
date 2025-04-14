from typing import List
from semester import Semester
from student import Student

class Studiengang:
    """
    Repräsentiert einen Studiengang mit Name, Semestern und Studenten.
    """
    def __init__(self, studiengang_name: str):
        """
        Initialisiert einen Studiengang mit Name und leeren Listen für Semester und Studenten.
        :param studiengang_name: Name des Studiengangs
        """
        self.__studiengang_name = studiengang_name
        self.__semester: List[Semester] = []
        self.__studenten: List[Student] = []

    def set_studiengang_name(self, studiengang_name: str):
        """Setzt den Namen des Studiengangs."""
        self.__studiengang_name = studiengang_name

    def get_studiengang_name(self) -> str:
        """Gibt den Namen des Studiengangs zurück."""
        return self.__studiengang_name

    def add_semester(self, semester_nummer: int):
        """
        Erstellt ein neues Semester und fügt es zum Studiengang hinzu.
        :param semester_nummer: Nummer des Semesters
        """
        neues_semester = Semester(semester_nummer)
        self.__semester.append(neues_semester)

    def get_semester(self) -> List[Semester]:
        """Gibt die Liste der Semester zurück."""
        return self.__semester

    def add_student(self, name: str, id: int):
        """
        Erstellt einen neuen Studenten und fügt ihn zum Studiengang hinzu.
        :param name: Name des Studenten
        :param id: ID des Studenten
        """
        neuer_student = Student(name, id)
        self.__studenten.append(neuer_student)

    def get_studenten(self) -> List[Student]:
        """Gibt die Liste der Studenten zurück."""
        return self.__studenten

    def remove_semester(self, semester: Semester):
        """Entfernt ein Semester aus dem Studiengang."""
        if semester in self.__semester:
            self.__semester.remove(semester)

    def remove_student(self, student: Student):
        """Entfernt einen Studenten aus dem Studiengang."""
        if student in self.__studenten:
            self.__studenten.remove(student)
