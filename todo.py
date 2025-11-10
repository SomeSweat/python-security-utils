
tasks = [] # storing data
 
while True:
    print("\n--- To-Do list ---")
    print("1. View tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Quit")


    choice = input("Choose an option (1-4): ")

    if choice == "1":
        if not tasks:
            print("add a task fuckwit!", flush=True)
        else:
            print("\nYour tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
    
    elif choice == "2":
        new_task = input("Enter a new task: ")
        tasks.append(new_task)
        print(f"Task added: {new_task}")

    elif choice == "3":
        if not tasks:
            print("bro you ain't got no tasks debil")
        else:
            print("\nYour tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

            try:
                index = int(input("yo what index you trynna remove: ")) - 1
                if 0 <= index < len(tasks):
                    removed = tasks.pop(index)
                    print(f"Removed: {removed}")
                else:
                    print("yo you aint got no task there")

            except ValueError:
                print("a number that you have in your tasks dawg")


    elif choice == "4":
        print("Lock in twin the world isn't slowing down for you")
        break

    else:
        print("Invalid choice, try again.")








