from anwendungslogik import Anwendungslogik

class CLI:
    """
    Klasse für die Kommandozeilenoberfläche (CLI).
    Steuert die Interaktion mit dem Benutzer.
    """
    def __init__(self):
        self.anwendungslogik = Anwendungslogik()

    def zeige_hauptmenu(self):
        """
        Zeigt das Hauptmenü der Anwendung und ermöglicht die Auswahl von Optionen.
        """
        print("\nStudien-Dashboard - Leistungsanalyse")
        print("=====================================")
        print("1. Dashboard anzeigen")
        print("2. Beenden")
        print("=====================================")

    def starte(self):
        """
        Startet die CLI und ermöglicht dem Benutzer, mit der Anwendung zu interagieren.
        """
        while True:
            self.zeige_hauptmenu()
            auswahl = input("Bitte wählen Sie eine Option (1-2): ")

            if auswahl == "1":
                # Dashboard anzeigen
                print("\nDashboard:")
                self.anwendungslogik.zeige_leistungstrend()

            elif auswahl == "2":
                # Beenden
                print("\nProgramm wird beendet. Auf Wiedersehen!")
                break

            else:
                print("\nUngültige Eingabe! Bitte wählen Sie eine Option zwischen 1 und 2.")
