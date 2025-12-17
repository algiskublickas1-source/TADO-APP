class Task:
    def __init__(self, pavadinimas, aprasymas):
        self.pavadinimas = pavadinimas
        self.aprasymas = aprasymas
        self.atlikta = False

    def info(self):
        status = "✓" if self.atlikta else "✗"
        print(f"{self.pavadinimas} – {self.aprasymas} | Atlikta: {status}")

    def to_dict(self):
        return {
            "pavadinimas": self.pavadinimas,
            "aprasymas": self.aprasymas,
            "atlikta": self.atlikta
        }

    @staticmethod
    def from_dict(data):
        task = Task(data["pavadinimas"], data["aprasymas"])
        task.atlikta = data["atlikta"]
        return task

