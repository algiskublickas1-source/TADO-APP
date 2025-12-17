from task_manager import TaskManager
from task import Task

class Colors:
    GREEN = "\033[92m"
    CYAN = "\033[96m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    RESET = "\033[0m"

manager = TaskManager()

while True:
    print(Colors.CYAN + "\n======  T A D O – A P P  ======" + Colors.RESET)
    print(Colors.GREEN + "1. Pridėti užduotį")
    print("2. Rodyti visas užduotis")
    print("3. Rodyti atliktas")
    print("4. Rodyti neatliktas")
    print("5. Pažymėti atliktą")
    print("6. Redaguoti užduotį")
    print("7. Ištrinti")
    print("8. Išeiti" + Colors.RESET)

    pasirinkimas = input("Pasirinkite: ")

    if pasirinkimas == "1":
        p = input("Pavadinimas: ")
        a = input("Aprašymas: ")
        manager.prideti_task(Task(p, a))
        print("Užduotis pridėta!")

    elif pasirinkimas == "2":
        manager.rodyti_tasks()

    elif pasirinkimas == "3":
        manager.rodyti_atliktas()

    elif pasirinkimas == "4":
        manager.rodyti_neatliktas()

    elif pasirinkimas == "5":
        manager.rodyti_tasks()
        i = int(input("Kuria užduotį pažymėti atlikta? "))
        manager.pazymeti_atlikta(i)
        print("Pažymėta kaip atlikta!")

    elif pasirinkimas == "6":
        manager.rodyti_tasks()
        i = int(input("Kurią užduotį redaguoti? "))
        p = input("Naujas pavadinimas: ")
        a = input("Naujas aprašymas: ")
        manager.redaguoti_task(i, p, a)
        print("Užduotis redaguota!")

    elif pasirinkimas == "7":
        manager.rodyti_tasks()
        i = int(input("Kurią užduotį ištrinti? "))
        manager.istrinti_task(i)
        print("Ištrinta!")

    elif pasirinkimas == "8":
        print("Viso gero!")
        break

    else:
        print(Colors.RED + "Neteisingas pasirinkimas!" + Colors.RESET)
