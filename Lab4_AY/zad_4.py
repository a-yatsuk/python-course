warsztat_python = set()
warsztat_ai = set()

while True:
    print("""
========== MENU ==========
1. Register for Python
2. Register for AI
3. Show participants
4. Participants of both workshops
5. All unique participants
0. Exit
==========================
""")

    option = input("Choose an option: ")

    if option == "1" or option == "2":
        name = input("First name: ")
        surname = input("Last name: ")

        participant = (name, surname)

        if option == "1":
            if participant in warsztat_python:
                print("Participant already registered.")
            else:
                warsztat_python.add(participant)
                print("Participant added.")

        else:
            if participant in warsztat_ai:
                print("Participant already registered.")
            else:
                warsztat_ai.add(participant)
                print("Participant added.")

    elif option == "3":
        print("Python workshop:")
        for name, surname in sorted(warsztat_python):
            print(name, surname)

        print("AI workshop:")
        for name, surname in sorted(warsztat_ai):
            print(name, surname)

    elif option == "4":
        common = warsztat_python & warsztat_ai

        print("Participants of both workshops:")
        for name, surname in sorted(common):
            print(name, surname)

    elif option == "5":
        everyone = warsztat_python | warsztat_ai

        print("All unique participants:")
        for name, surname in sorted(everyone):
            print(name, surname)

    elif option == "0":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Try again.")
