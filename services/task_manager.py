import random
import json
import os
from datetime import datetime
from models.task import RewardedTask


class TaskManager:
    """
    Diese Klasse verwaltet Aufgaben: Aufgaben können hinzugefügt, gelöscht, abgeschlossen und gespeichert werden.
    Es gibt ein Belohnungssystem basierend auf den gesammelten Punkten.
    """

    def __init__(self, data_file="data/tasks.json"):
        """
        Initialisiert den TaskManager.

        :param data_file: Pfad zur JSON-Datei, in der die Aufgaben gespeichert werden.
        """
        self.data_file = data_file
        self.tasks = []
        # Liste aller Aufgaben (Task-Objekte)
        self.total_points = 0
        # Gesamtpunkte für abgeschlossene Aufgaben
        self.completed_count = 0
        # Anzahl erledigter Aufgaben
        self.load_data()
        # Lade vorhandene Daten aus der Datei

    def add_task(self, name, priority):
        """
        Fügt eine neue Aufgabe zur Liste hinzu.

        name: Name der Aufgabe
        priority: Priorität der Aufgabe (z.B. 'Hoch', 'Mittel', 'Niedrig')
        """
        task = RewardedTask(name=name, priority=priority)
        self.tasks.append(task)
        self.save_data()

    def delete_task(self, index):
        """
        Löscht eine Aufgabe anhand ihres Indexes in der Liste.

        index: Index der zu löschenden Aufgabe
        """
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            self.save_data()

    def complete_task(self, index):
        """
        Markiert eine Aufgabe als erledigt, vergibt Punkte und prüft auf Belohnungen.

        index: Index der zu erledigenden Aufgabe
        """
        if 0 <= index < len(self.tasks) and not self.tasks[index].completed:
            task = self.tasks[index]
            task.complete()
            # Markiere Aufgabe als erledigt
            points = self.calculate_points(task.priority)
            self.total_points += points
            self.completed_count += 1
            print(
                f"Aufgabe abgeschlossen! Du hast {points} Punkte erhalten.")
            self.check_reward()
            self.save_data()
        else:
            print("!! Aufgabe nicht gefunden oder bereits erledigt.")

    def calculate_points(self, priority):
        """
        Berechnet Punkte basierend auf der Priorität der Aufgabe.

        priority: Priorität der Aufgabe
        return: Vergebene Punktzahl
        """
        if priority == "Hoch":
            return 10
        elif priority == "Mittel":
            return 5
        else:
            return 2

    def check_reward(self):
        """
        Prüft, ob genügend Punkte für eine Belohnung gesammelt wurden.
        Wenn ja, wird eine zufällige Belohnung angezeigt und Punkte werden reduziert.
        """
        if self.total_points >= 10:
            print("Belohnung freigeschaltet!")
            print(self.random_reward())
            self.total_points -= 10
            # 10 Punkte abziehen nach Belohnung

    def random_reward(self):
        """
        Gibt eine zufällige Belohnungsnachricht zurück.

        return: String mit Belohnungstext
        """
        rewards = [
            "Du bist großartig!",
            "Mach eine Pause und genieße eine Schokolade",
            "Super gemacht!",
            "Keep going!",
            "Du rockst dassss",
            "Staaark gemacht!",
            "Du bist ein Held!",
        ]
        return random.choice(rewards)

    def list_tasks(self, show_all=True):
        """
        Gibt die Aufgabenliste aus. Optional können nur unerledigte Aufgaben angezeigt werden.

        show_all: True zeigt alle Aufgaben, False nur unerledigte
        """
        for i, task in enumerate(self.tasks):
            if show_all or not task.completed:
                print(f"{i}: {task}")

    def get_statistics(self):
        """
        Gibt Statistiken zur Gesamtanzahl, erledigten und offenen Aufgaben aus.
        """
        total = len(self.tasks)
        done = sum(1 for t in self.tasks if t.completed)
        print(f"Aufgaben insgesamt: {total}")
        print(f"Erledigt: {done}")
        print(f"Offen: {total - done}")

    def save_data(self):
        """
        Speichert alle Aufgaben und den Punktestand in der JSON-Datei.
        """
        os.makedirs(os.path.dirname(self.data_file), exist_ok=True)
        data = {
            "tasks": [task.to_dict() for task in self.tasks],
            "total_points": self.total_points,
            "completed_count": self.completed_count
        }
        with open(self.data_file, "w") as f:
            json.dump(data, f, indent=2)

    def load_data(self):
        """
        Lädt Aufgaben und Punktestand aus der JSON-Datei, falls vorhanden.
        """
        if os.path.exists(self.data_file):
            with open(self.data_file, "r") as f:
                data = json.load(f)
                self.tasks = [RewardedTask.from_dict(
                    t) for t in data.get("tasks", [])]
                self.total_points = data.get("total_points", 0)
                self.completed_count = data.get("completed_count", 0)
