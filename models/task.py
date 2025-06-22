from datetime import datetime
import json


class Task:
    """
    Repräsentiert eine einzelne Aufgabe mit Name, Priorität, Status und Erstellungszeitpunkt.
    """

    def __init__(self, name, priority, completed=False, created_at=None):
        """
        Konstruktor für eine neue Task-Instanz.

        name: Name der Aufgabe
        priority: Priorität der Aufgabe ('Hoch', 'Mittel', 'Niedrig')
        completed: Gibt an, ob die Aufgabe bereits erledigt ist (Standard: False)
        created_at: Zeitpunkt der Erstellung; wird automatisch gesetzt, wenn nicht übergeben
        """
        self.name = name
        self.priority = priority
        self.completed = completed
        self.created_at = created_at or datetime.now()

    def complete(self):
        self.completed = True
        # Markiert die Aufgabe als erledigt.

    def to_dict(self):
        """
        Konvertiert die Aufgabe in ein Dictionary zur Speicherung in JSON.

        :return: Dictionary mit den Aufgabendaten
        """
        return {
            "name": self.name,
            "priority": self.priority,
            "completed": self.completed,
            "created_at": self.created_at.isoformat()
        }

    @classmethod
    def from_dict(cls, data):
        """
        Erstellt eine Task-Instanz aus einem Dictionary (z.B. beim Laden aus einer JSON-Datei).

        data: Dictionary mit Aufgabendaten
        return: Task-Objekt
        """
        return cls(
            name=data["name"],
            priority=data["priority"],
            completed=data.get("completed", False),
            created_at=datetime.fromisoformat(data["created_at"])
        )

    def __str__(self):
        """
        Gibt eine lesbare Darstellung der Aufgabe zurück

        return: Formatierter String mit Aufgabendetails
        """
        status = "Erledigt" if self.completed else "Offen"
        return f"{self.name} ({self.priority}) – {status} – erstellt am {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}"

    class RewardedTask(Task):
        def get_reward(self):
            return "Belohnung: Du hast die Aufgabe erledigt!"
