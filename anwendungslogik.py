import pandas as pd
import matplotlib.pyplot as plt
from datenzugriff import Datenzugriff
from datetime import date
from matplotlib.font_manager import FontProperties

class Anwendungslogik:
    """
    Klasse für die Anwendungslogik. Enthält Funktionen zur Analyse der Daten.
    """
    def __init__(self):
        self.__datenzugriff = Datenzugriff()
        self.__datenzugriff.init_beispieldatensatz()

    def zeige_leistungstrend(self):
        """
        Visualisiert den Zeitverlauf der Leistung und die Durchschnittsnoten pro Semester,
        inklusive einer Tabelle mit den Durchschnittsnoten über dem Balkendiagramm.
        Fügt eine Überschrift hinzu.
        """
        studiengang = self.__datenzugriff.get_studiengang()
        student = studiengang.get_studenten()[0]

        # Daten für die Tabelle und das Balkendiagramm
        semester_nummern = [f"Semester {s.get_semester_nummer()}" for s in studiengang.get_semester()]
        durchschnittsnoten = [
            round(sum(m.get_modul_note() for m in s.get_module()) / len(s.get_module()), 2)
            if s.get_module() else 0
            for s in studiengang.get_semester()
        ]

        # Daten für das Liniendiagramm (Notenverlauf nach Datum)
        module_daten = []
        for semester in studiengang.get_semester():
            for modul in semester.get_module():
                module_daten.append({
                    "Modulname": modul.get_modul_name(),
                    "Note": modul.get_modul_note(),
                    "Datum": modul.get_modul_datum()
                })
        module_daten.sort(key=lambda x: x["Datum"])

        # Liniendiagrammdaten vorbereiten
        daten = [modul["Datum"] for modul in module_daten]
        noten = [modul["Note"] for modul in module_daten]

        # Diagramme erstellen
        fig, axs = plt.subplots(2, 2, figsize=(15, 10), gridspec_kw={'height_ratios': [1, 2]})
        fig.delaxes(axs[0, 1]) 

        # Überschrift hinzufügen
        fig.suptitle("Studien-Dashboard - Leistungsanalyse\nÜberblick über Noten und Fortschritt", fontsize=20, fontweight='bold')

        # Tabelle erstellen
        table_data = pd.DataFrame({
            "Semester": semester_nummern,
            "Durchschnittsnote": durchschnittsnoten
        })

        # Tabelle erstellen
        cell_text = table_data.values
        colLabels = table_data.columns
        
        table = axs[0, 0].table(cellText=cell_text, colLabels=colLabels, loc='center', cellLoc='center')
        
        # Anpassung der Schriftgröße und Zellengröße
        table.auto_set_font_size(False)
        table.set_fontsize(12)

        # Skalieren der Tabelle
        table.scale(1.2, 1.5)

        axs[0, 0].axis('tight')
        axs[0, 0].axis('off')

        # Header fett machen
        for key, cell in table.get_celld().items():
            if key[0] == 0:
                cell.set_text_props(fontproperties=FontProperties(weight='bold'))


        # Balkendiagramm (Durchschnittsnoten pro Semester)
        axs[1, 0].bar(semester_nummern, durchschnittsnoten, color='green')
        axs[1, 0].set_title("Durchschnittsnoten pro Semester")
        axs[1, 0].set_ylabel("Note")

        # Liniendiagramm (Notenverlauf nach Datum)
        axs[1, 1].plot(daten, noten, marker='o', color='green', label="Notenverlauf")
        
        axs[1, 1].set_title("Leistungsverlauf nach Datum")
        axs[1, 1].set_ylabel("Note")
        
        plt.tight_layout(rect=[0, 0.03, 1, 0.95])
        plt.show()
