import random
import os
import sys


def menu():
    print("1. Add a framework")
    print("2. Remove a framework")
    print("3. Update a framework")
    print("4. View all frameworks")
    print("5. Choose my next stack")
    print("6. Exit")

    choice = input("Enter your choice: ")
    return choice


def choose_stack(front_end_framework, backend_end_framework, databases):
    random.shuffle(front_end_framework)
    random.shuffle(backend_end_framework)

    # pick a random item from each list
    front_end_framework = random.choice(front_end_framework)
    backend_end_framework = random.choice(backend_end_framework)
    databases = random.choice(databases)

    print("\n")  # spacing

    # conditionally print the results
    if backend_end_framework == "Firebase" or backend_end_framework == "Supabase":
        clear_terminal()
        print(f"Your front end framework is: {front_end_framework}")
        print(f"Your backend framework is: {backend_end_framework}")
    else:
        clear_terminal()
        print(f"Your front end framework is: {front_end_framework}")
        print(f"Your backend framework is: {backend_end_framework}")
        print(f"Your database is: {databases}")

    user_agrees = input("Ready to build? (y/n): ")
    return user_agrees


def opening_message():
    print(
        """
***************************************
    Welcome to the Stack Generator!
***************************************    
    
This script will help you choose a framework for your next project
by randomly selecting a front end framework, a backend framework, and a database.
    
        """
    )


def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")


def print_frameworks():
    print("These are your current available front end frameworks:")

    print("------------------------------------------------------")
    for framework in front_end_framework:
        print(framework)

    print("\n")
    print("These are your current available backend frameworks:")
    print("-----------------------------------------------------")
    for framework in backend_end_framework:
        print(framework)

    print("\n")
    print("These are your current available databases:")
    print("--------------------------------------------")
    for db in databases:
        print(db)

    print("\n")


# All frameworks need to be in a stable 1.0 release
front_end_framework = [
    "NextJS",
    "Vue",
    "Nuxt",
    "SvelteKit",
    "Qwik",
    "QwikCity",
    "Solid",
]

# All frameworks need to be in a stable 1.0 release
backend_end_framework = [
    "Express",
    "Django REST Framework",
    "Firebase",
    "Supabase",
]

# All frameworks need to be in a stable 1.0 release
databases = [
    "PostgreSQL",
]


def main():
    opening_message()
    print_frameworks()

    menu_choice = menu()
    if menu_choice == "6":
        print("Okay. Goodbye!")
        sys.exit()

    elif menu_choice == "1":
        print("Adding a framework")
    elif menu_choice == "2":
        print("Removing a framework")
    elif menu_choice == "3":
        print("Updating a framework")
    elif menu_choice == "4":
        print("Viewing all frameworks")
    elif menu_choice == "5":
        # shuffle the lists
        user_option = choose_stack(
            front_end_framework, backend_end_framework, databases
        )
        if user_option == "y":
            print("Okay. Goodbye!")
            sys.exit()
        else:
            print("Sorry. Goodbye for now!")
            sys.exit()
            #
    else:
        print("Sorry. That's not a valid choice.")


if __name__ == "__main__":
    main()
