import random
import json
import os
from datetime import datetime
from models.task import Task


class TaskManager:
    def __init__(self, data_file="data/tasks.json"):
        self.data_file = data_file
        self.tasks = []
        self.total_points = 0
        self.completed_count = 0
        self.load_data()

    def add_task(self, name, priority):
        task = Task(name=name, priority=priority)
        self.tasks.append(task)
        self.save_data()

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            self.save_data()

    def complete_task(self, index):
        if 0 <= index < len(self.tasks) and not self.tasks[index].completed:
            task = self.tasks[index]
            task.complete()
            points = self.calculate_points(task.priority)
            self.total_points += points
            self.completed_count += 1
            print(
                f"✔ Aufgabe abgeschlossen! Du hast {points} Punkte erhalten.")
            self.check_reward()
            self.save_data()
        else:
            print("⚠ Aufgabe nicht gefunden oder bereits erledigt.")

    def calculate_points(self, priority):
        if priority == "Hoch":
            return 10
        elif priority == "Mittel":
            return 5
        else:
            return 2

    def check_reward(self):
        if self.total_points >= 10:
            print("🎉 Belohnung freigeschaltet!")
            print(self.random_reward())
            self.total_points -= 10  # Punkte zurücksetzen

    def random_reward(self):
        rewards = [
            "Du bist großartig!",
            "Mach eine Pause ☕",
            "Super gemacht!",
            "Keep going!",
            "Du rockst das 💪"
        ]
        return random.choice(rewards)

    def list_tasks(self, show_all=True):
        for i, task in enumerate(self.tasks):
            if show_all or not task.completed:
                print(f"{i}: {task}")

    def get_statistics(self):
        total = len(self.tasks)
        done = sum(1 for t in self.tasks if t.completed)
        print(f"📊 Aufgaben insgesamt: {total}")
        print(f"✅ Erledigt: {done}")
        print(f"🕓 Offen: {total - done}")

    def save_data(self):
        os.makedirs(os.path.dirname(self.data_file), exist_ok=True)
        data = {
            "tasks": [task.to_dict() for task in self.tasks],
            "total_points": self.total_points,
            "completed_count": self.completed_count
        }
        with open(self.data_file, "w") as f:
            json.dump(data, f, indent=2)

    def load_data(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, "r") as f:
                data = json.load(f)
                self.tasks = [Task.from_dict(t) for t in data.get("tasks", [])]
                self.total_points = data.get("total_points", 0)
                self.completed_count = data.get("completed_count", 0)
