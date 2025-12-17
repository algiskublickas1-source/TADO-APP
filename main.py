from task import Task
from task_manager import TaskManager

manager = TaskManager()

while True:
    print("\n====== T A D O - A P P ======")
    print("1. Pridėti užduotį")
    print("2. Rodyti užduotis")
    print("3. Pažymėti atliktą")
    print("4. Ištrinti užduotį")
    print("5. Išeiti")

    pasirinkimas = input("Pasirinkite: ")

    if pasirinkimas == "1":
        print("\n--- Nauja užduotis ---")
        pavadinimas = input("Pavadinimas: ")
        aprasymas = input("Aprašymas: ")
        task = Task(pavadinimas, aprasymas)
        manager.prideti_task(task)
        print("Užduotis pridėta!")

    elif pasirinkimas == "2":
        print("\n--- Visos užduotys ---")
        manager.rodyti_tasks()

    elif pasirinkimas == "3":
        manager.rodyti_tasks()
        index = int(input("Kuri užduotis atlikta? (numeris): "))
        manager.pazymeti_atlikta(index)

    elif pasirinkimas == "4":
        manager.rodyti_tasks()
        index = int(input("Kurią užduotį ištrinti? (numeris): "))
        manager.istrinti_task(index)

    elif pasirinkimas == "5":
        print("Viso gero!")
        break

    else:
        print("Neteisingas pasirinkimas!")
