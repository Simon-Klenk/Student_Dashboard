class Student:
    """
    Repräsentiert einen Studenten mit Name und ID.
    """
    def __init__(self, name: str, id: int):
        """
        Initialisiert einen Studenten mit Name und ID.
        :param name: Name des Studenten
        :param id: ID des Studenten
        """
        self.__name = name
        self.__id = id

    def set_name(self, name: str):
        """Setzt den Namen des Studenten."""
        self.__name = name

    def get_name(self) -> str:
        """Gibt den Namen des Studenten zurück."""
        return self.__name

    def get_id(self) -> int:
        """Gibt die ID des Studenten zurück."""
        return self.__id
