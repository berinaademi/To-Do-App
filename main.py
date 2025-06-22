from services.task_manager import TaskManager


def zeige_menü():
    print("\n=== TO-DO-APP MENÜ ===")
    print("1. Aufgabe hinzufügen")
    print("2. Aufgaben anzeigen")
    print("3. Aufgabe als erledigt markieren")
    print("4. Aufgabe löschen")
    print("5. Statistiken anzeigen")
    print("6. Nur offene Aufgaben anzeigen")
    print("7. Beenden")


def hauptprogramm():
    manager = TaskManager()

    while True:
        zeige_menü()
        wahl = input("Wähle eine Option (1-7): ")

        if wahl == "1":
            name = input("Aufgabenname: ")
            priority = input("Priorität (Hoch/Mittel/Niedrig): ").capitalize()
            if priority in ["Hoch", "Mittel", "Niedrig"]:
                manager.add_task(name, priority)
            else:
                print("❌ Ungültige Priorität.")
        elif wahl == "2":
            manager.list_tasks()
        elif wahl == "3":
            try:
                index = int(input("Welche Aufgabe erledigen (Index): "))
                manager.complete_task(index)
            except ValueError:
                print("❌ Bitte eine gültige Zahl eingeben.")
        elif wahl == "4":
            try:
                index = int(input("Welche Aufgabe löschen (Index): "))
                manager.delete_task(index)
            except ValueError:
                print("❌ Bitte eine gültige Zahl eingeben.")
        elif wahl == "5":
            manager.get_statistics()
        elif wahl == "6":
            manager.list_tasks(show_all=False)
        elif wahl == "7":
            print("👋 Auf Wiedersehen!")
            break
        else:
            print("❌ Ungültige Eingabe.")


if __name__ == "__main__":
    hauptprogramm()
