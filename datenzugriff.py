from studiengang import Studiengang
from modul import Modul
from datetime import date

class Datenzugriff:
    """
    Klasse für den Datenzugriff. Hier werden Testdaten erstellt und geladen.
    """
    def __init__(self):
        self.__studiengang = None

    def init_beispieldatensatz(self) -> bool:
        """
        Erstellt einen Testdatensatz mit einem einzigen Studenten und Beispielwerten.
        :return: True, wenn der Datensatz erfolgreich erstellt wurde.
        """
        # Beispielstudiengang erstellen
        self.__studiengang = Studiengang("Informatik")

        # Einen einzelnen Studenten hinzufügen
        self.__studiengang.add_student("Max Mustermann", 12345678)

        # Ein Semester hinzufügen und Module erstellen
        self.__studiengang.add_semester(1)
        semester1 = self.__studiengang.get_semester()[0]

        semester1.add_modul(Modul("Mathematik", 5, 2.3, date(2024, 1, 15)))
        semester1.add_modul(Modul("Programmierung", 5, 2.5, date(2024, 2, 20)))
        semester1.add_modul(Modul("Java", 5, 2.9, date(2024, 3, 10)))
        semester1.add_modul(Modul("Python", 5, 3.5, date(2024, 4, 25)))
        semester1.add_modul(Modul("c#", 5, 3.2, date(2024, 5, 10)))
        semester1.add_modul(Modul("Betriebssysteme_1", 5, 3.0, date(2024, 6, 25)))

        # Ein Semester hinzufügen und Module erstellen
        self.__studiengang.add_semester(2)
        semester2 = self.__studiengang.get_semester()[1]

        semester2.add_modul(Modul("Datenbanken_2", 5, 2.8, date(2024, 7, 10)))
        semester2.add_modul(Modul("Betriebssysteme", 5, 2.5, date(2024, 8, 25)))
        semester2.add_modul(Modul("Programmierung_2", 5, 2.7, date(2024, 9, 10)))
        semester2.add_modul(Modul("Betriebssysteme_Kernel", 5, 3.0, date(2024, 10, 25)))
        semester2.add_modul(Modul("Betriebssysteme_Kernel", 5, 2.6, date(2024, 11, 25)))
        semester2.add_modul(Modul("Betriebssysteme_Kernel", 5, 2.3, date(2024, 12, 25)))

        # Ein Semester hinzufügen und Module erstellen
        self.__studiengang.add_semester(3)
        semester3 = self.__studiengang.get_semester()[2]

        semester3.add_modul(Modul("Mathematik", 5, 2.0, date(2025, 1, 15)))
        semester3.add_modul(Modul("Programmierung", 5, 1.7, date(2025, 2, 20)))
        semester3.add_modul(Modul("Mathematik", 5, 1.4, date(2025, 3, 15)))
        semester3.add_modul(Modul("Programmierung", 5, 1.7, date(2025, 4, 20)))
        semester3.add_modul(Modul("Mathematik", 5, 1.3, date(2025, 5, 15)))
        semester3.add_modul(Modul("Programmierung", 5, 1.5, date(2025, 6, 20)))

        # Ein Semester hinzufügen und Module erstellen
        self.__studiengang.add_semester(4)
        semester4 = self.__studiengang.get_semester()[3]

        semester4.add_modul(Modul("Mathematik", 5, 1.7, date(2025, 7, 15)))
        semester4.add_modul(Modul("Programmierung", 5, 1.6, date(2025, 8, 20)))
        semester4.add_modul(Modul("Mathematik", 5, 2.3, date(2025, 9, 15)))
        semester4.add_modul(Modul("Programmierung", 5, 1.7, date(2025, 10, 20)))
        semester4.add_modul(Modul("Mathematik", 5, 1.5, date(2025, 11, 15)))
        semester4.add_modul(Modul("Programmierung", 5, 1.4, date(2025, 12, 20)))

        # Ein Semester hinzufügen und Module erstellen
        self.__studiengang.add_semester(5)
        semester5 = self.__studiengang.get_semester()[4]

        semester5.add_modul(Modul("Mathematik", 5, 1.5, date(2026, 1, 15)))
        semester5.add_modul(Modul("Programmierung", 5, 1.3, date(2026, 2, 20)))

        return True

    def lade_studiengang_daten(self) -> Studiengang:
        """
        Gibt den gesamten Studiengang zurück.
        :return: Das Studiengang-Objekt.
        """
        return self.__studiengang

    def get_studiengang(self) -> Studiengang:
        """Gibt den Studiengang zurück."""
        return self.__studiengang

    def set_studiengang(self, studiengang: Studiengang):
        """Setzt den Studiengang."""
        self.__studiengang = studiengang
