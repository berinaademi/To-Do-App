from services.task_manager import TaskManager


def zeige_menü():
    """
    Gibt das Hauptmenü der To-Do-App in der Konsole aus.
    """
    print("\n=== TO-DO-APP MENÜ ===")
    print("1. Aufgabe hinzufügen")
    print("2. Aufgaben anzeigen")
    print("3. Aufgabe als erledigt markieren")
    print("4. Aufgabe löschen")
    print("5. Statistiken anzeigen")
    print("6. Nur offene Aufgaben anzeigen")
    print("7. Beenden")


def hauptprogramm():
    """
    Startet die Hauptlogik der To-Do-App. Führt eine Schleife aus, in der Benutzer
    verschiedene Aktionen wie Hinzufügen, Löschen oder Abschließen von Aufgaben wählen können.
    """
    manager = TaskManager()
    # Erstelle eine neue Instanz des TaskManagers

    while True:
        zeige_menü()
        wahl = input("Wähle eine Option (1-7): ")

        # Neue Aufgabe hinzufügen
        if wahl == "1":
            name = input("Aufgabenname: ")
            priority = input("Priorität (Hoch/Mittel/Niedrig): ").capitalize()
            if priority in ["Hoch", "Mittel", "Niedrig"]:
                manager.add_task(name, priority)
            else:
                print("Ungültige Priorität.")

        # Alle Aufgaben anzeigen
        elif wahl == "2":
            manager.list_tasks()

        # Aufgabe als erledigt markieren
        elif wahl == "3":
            try:
                index = int(input("Welche Aufgabe erledigen (Index): "))
                manager.complete_task(index)
            except ValueError:
                print("Bitte eine gültige Zahl eingeben.")

        # Aufgabe löschen
        elif wahl == "4":
            try:
                index = int(input("Welche Aufgabe löschen (Index): "))
                manager.delete_task(index)
            except ValueError:
                print("Bitte eine gültige Zahl eingeben.")

        # Statistiken anzeigen
        elif wahl == "5":
            manager.get_statistics()

        # Nur offene Aufgaben anzeigen
        elif wahl == "6":
            manager.list_tasks(show_all=False)

        # Programm beenden
        elif wahl == "7":
            print("Auf Wiedersehen!")
            break

        # Ungültige Eingabe abfangen
        else:
            print("Ungültige Eingabe.")


# Starte das Programm nur, wenn diese Datei direkt ausgeführt wird
if __name__ == "__main__":
    hauptprogramm()
