noten = []

note = input("How many grades would you like to add?")

while True:
    print("\n--- Calculator ---")
    print("1.View grades")
    print("2.Add grades")
    print("3.Calculate grade average")
    print("4. Remove grade")

    choice = input("Chose option (1-3):")

    if choice == "1":
        if not noten:
            print("There are no grades for you to view")
        else:
            print("\nYour grades")
            for i, note in enumerate(noten, start=1):
                print(f"{i}. {note}")
    
    elif choice == "2":
        new_grade = input("Enter a new grade: ")
        try:
            float(new_grade)
            noten.append(new_grade)
            print(f"Grade added:{new_grade}")
        except ValueError:
            print("Please enter a valid number!")


    elif choice == "4":
        if not noten:
            print("No grades for you to remove")
        else:
            print("\nYour grades")
            for i, note in enumerate(noten, start=1):
                print(f"{i}. {note}")

            try:
                index = int(input("Which index of grade would you like to remove: ")) - 1
                if 0 <= index < len(noten):
                    removed = noten.pop(index)
                    print(f"Removed: {removed}")

            except ValueError:
                print("No grade at that index")

    elif choice == "3":
        if not noten:
            print("No grades to calculate average off.")
        else:
            float_grades = [float(grade) for grade in noten]

            average = sum(float_grades) / len(float_grades)

            print(f"The average is: {average:.2f}")