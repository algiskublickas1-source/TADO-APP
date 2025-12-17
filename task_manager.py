import json
from task import Task

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.ikelti_json()  # automatiškai įkelia užduotis paleidimo metu

    # -----------------------------
    #   PRIDĖTI UŽDUOTĮ
    # -----------------------------
    def prideti_task(self, task):
        self.tasks.append(task)
        self.issaugoti_json()

    # -----------------------------
    #   RODYTI UŽDUOTIS
    # -----------------------------
    def rodyti_tasks(self):
        if len(self.tasks) == 0:
            print("Nėra užduočių.")
        else:
            for i, task in enumerate(self.tasks):
                print(f"{i}. ", end="")
                task.info()

    # -----------------------------
    #   PAŽYMĖTI ATLIKTĄ
    # -----------------------------
    def pazymeti_atlikta(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].atlikta = True
            print("Užduotis pažymėta kaip atlikta.")
            self.issaugoti_json()
        else:
            print("Tokio indekso nėra.")

    # -----------------------------
    #   IŠTRINTI UŽDUOTĮ
    # -----------------------------
    def istrinti_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
            print("Užduotis ištrinta.")
            self.issaugoti_json()
        else:
            print("Tokio indekso nėra.")

    # -----------------------------
    #   IŠSAUGOTI Į JSON
    # -----------------------------
    def issaugoti_json(self):
        with open("tasks.json", "w") as f:
            json.dump([task.to_dict() for task in self.tasks], f, indent=4)

    # -----------------------------
    #   ĮKELTI IŠ JSON
    # -----------------------------
    def ikelti_json(self):
        try:
            with open("tasks.json", "r") as f:
                duomenys = json.load(f)
                self.tasks = [Task.from_dict(item) for item in duomenys]
        except FileNotFoundError:
            self.tasks = []

