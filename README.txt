Installationsanleitung für Windows 11

1. Installation von Python und git:
    1.1. Python: https://www.python.org/downloads/
    1.2. Git: https://git-scm.com/downloads/win

2. Projekt von GitHub herunterladen
    2.1. Kommandozeile öffnen
    2.2. Zum gewünschten Ordner navigieren: cd Pfad/zum/Ordner
    2.3. Repository von GitHub klonen: git clone https://github.com/Simon-Klenk/Student_Dashboard.git

3. Pfad von Python und pip suchen
    3.1. Standardpfad der Python Installation ist:
    C:\Users\<Benutzer>\AppData\Local\Programs\Python\Python313
    3.2. Standardpfad der pip Installation ist:
    C:\Users\<Benutzer>\AppData\Local\Programs\Python\Python313\Scripts

4. Umgebungsvariablen hinzufügen
    4.1. In der Windows Suche nach Systemumgebungsvariablen bearbeiten suchen
    4.2. Umgebungsvariablen anklicken
    4.3. Unter Systemvariablen die Variable Pfad anklicken und auf Bearbeiten gehen
    4.4. Auf Neu klicken und den vorher gesuchten Pfad von Python hinzufügen
    4.5. Dasselbe mit dem Pfad von pip machen

5. Abhängigkeiten installieren In der Kommandozeile eingeben:
    5.1. pip install pandas
    5.2. pip install matplotlib

6. Dashboard starten
    6.1. Kommandozeile öffnen und in den vorher von GitHub geladenen Ordner „Student_Dashboard“ wechseln
    6.2. Programm starten über die Kommandozeile: python main.py
    6.3 Anweisungen im Kommandozeileninterface (CLI) folgen, um die Diagramme zu erstellen
