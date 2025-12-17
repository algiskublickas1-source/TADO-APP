class Task:
    def __init__(self, pavadinimas, aprasymas):
        self.pavadinimas = pavadinimas
        self.aprasymas = aprasymas
        self.atlikta = False

    def info(self):
        statusas = "✓ atlikta" if self.atlikta else "✗ neatlikta"
        print(f"{self.pavadinimas} - {self.aprasymas} | {statusas}")

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
