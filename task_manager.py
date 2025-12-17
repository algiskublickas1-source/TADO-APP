import json
from task import Task

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.ikelti_json()

    def prideti_task(self, task: Task):
        self.tasks.append(task)
        self.issaugoti_json()

    def rodyti_tasks(self):
        if not self.tasks:
            print("Nėra užduočių.")
            return
        for i, task in enumerate(self.tasks):
            print(f"{i}. ", end="")
            task.info()

    def pazymeti_atlikta(self, index):
        self.tasks[index].atlikta = True
        self.issaugoti_json()

    def istrinti_task(self, index):
        self.tasks.pop(index)
        self.issaugoti_json()

    def redaguoti_task(self, index, naujas_pavadinimas, naujas_aprasymas):
        self.tasks[index].pavadinimas = naujas_pavadinimas
        self.tasks[index].aprasymas = naujas_aprasymas
        self.issaugoti_json()

    def rodyti_atliktas(self):
        for i, task in enumerate(self.tasks):
            if task.atlikta:
                print(f"{i}. ", end="")
                task.info()

    def rodyti_neatliktas(self):
        for i, task in enumerate(self.tasks):
            if not task.atlikta:
                print(f"{i}. ", end="")
                task.info()

    def issaugoti_json(self):
        with open("tasks.json", "w", encoding="utf-8") as f:
            json.dump([task.to_dict() for task in self.tasks], f, ensure_ascii=False, indent=4)

    def ikelti_json(self):
        try:
            with open("tasks.json", "r", encoding="utf-8") as f:
                data = json.load(f)
                self.tasks = [Task.from_dict(item) for item in data]
        except FileNotFoundError:
            self.tasks = []
