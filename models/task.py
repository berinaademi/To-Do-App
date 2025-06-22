from datetime import datetime
import json


class Task:
    def __init__(self, name, priority, completed=False, created_at=None):
        self.name = name
        self.priority = priority  # "Hoch", "Mittel", "Niedrig"
        self.completed = completed
        self.created_at = created_at or datetime.now()

    def complete(self):
        self.completed = True

    def to_dict(self):
        return {
            "name": self.name,
            "priority": self.priority,
            "completed": self.completed,
            "created_at": self.created_at.isoformat()
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data["name"],
            priority=data["priority"],
            completed=data.get("completed", False),
            created_at=datetime.fromisoformat(data["created_at"])
        )

    def __str__(self):
        status = "Erledigt" if self.completed else "Offen"
        return f"{self.name} ({self.priority}) – {status} – erstellt am {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}"
