import random
import os
import sys
from colorama import Fore, Back, Style


PROJECT_NAME = "my-project"

# All frameworks need to be in a stable 1.0 release
front_end_frameworks = [
    "react",
    "vue",
    "svelte",
    "qwik",
    "solid",
    "astro",
]

meta_frameworks = [
    "next",
    "nuxt",
    "svelte_kit",
    "qwik_city",
    "solid_start",
]

# Randomize to get the combined_framework tuple, then randomize the tuple to get the framework or meta_framework
CLI_commands = [
    {"react": "npm create vite@latest"},
    {"vue", "npm create vite@latest"},
    {"svelte": "npm create vite@latest"},
    {"next": "npx create-next-app@latest"},
    {"qwik", "npm create qwik@latest"},
    {"qwik_city", "npm create qwik@latest"},
    {"solid_start", "npm init solid@latest"},
    {"nuxt": "npx create-nuxt-app " + PROJECT_NAME},
    {"svelte_kit", "npm create svelte@latest " + PROJECT_NAME},
    {"solid", "npx degit solidjs/templates/js " + PROJECT_NAME},
    {"astro", "npm create astro@latest"},
]

# All frameworks need to be in a stable 1.0 release
backend_end_frameworks = [
    "express",
    "djangorestframework",
    "firebase",
    "supabase",
]

# All frameworks need to be in a stable 1.0 release
databases = [
    "postgresql",
    "mongodb",
]


def operations_menu():
    print("OPERATIONS MENU")
    print("---------------")
    print("1. Add a frontend framework")
    print("2. Add a meta framework")
    print("3. Add a database")
    print("3. Group a frontend framework with a meta framework")
    print("5. Remove a frontend framework")
    print("6. Remove a meta framework")
    print("7. Remove a database")
    print("10. Print all frameworks and databases")
    print("11. View all databases")

    print("\n")
    print(f"Exit {Fore.GREEN}[q/Q]{Style.RESET_ALL}")

    operation = input("Enter your choice: ")

    if operation == "q" or operation == "Q":
        print("Goodbye!")
        sys.exit()
    return operation


def stack_generator_menu():
    print(
        f"""
{Fore.BLUE}#~#~#~#~#~#~#~#~#~#~#~#~{Style.RESET_ALL}
{Fore.BLUE}#{Style.RESET_ALL} {Fore.GREEN}Stack Generator Menu{Style.RESET_ALL} {Fore.BLUE}#{Style.RESET_ALL}
{Fore.BLUE}#~#~#~#~#~#~#~#~#~#~#~#~{Style.RESET_ALL}
        """
    )
    print(f"{Fore.GREEN}[1]{Style.RESET_ALL} - Randomize my next stack")
    print(f"{Fore.GREEN}[q]{Style.RESET_ALL} - Quit")

    print("\n")
    choice = input("Enter your choice: ")

    if choice == "1":
        stack = choose_stack()
        print(stack)

    print("Goodbye!")
    sys.exit()


def main_menu():
    print(f"\n{Fore.GREEN}Which menu would you like to see?: ")
    print(f"{Fore.BLUE}~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~{Style.RESET_ALL}")
    print(f"{Fore.GREEN}[1]{Style.RESET_ALL} - Operations Menu")
    print(f"{Fore.GREEN}[2]{Style.RESET_ALL} - Stack Generator Menu")
    print(f"{Fore.GREEN}[q]{Style.RESET_ALL} - Quit")

    menu_choice = input("Enter your choice: ")

    while True:
        if menu_choice == "1":
            operations_menu()
        elif menu_choice == "2":
            stack_generator_menu()
        elif menu_choice == "q":
            print("Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")
            main_menu()


def choose_stack():
    # shuffle the lists (so the order is different each time)
    random.shuffle(front_end_frameworks)
    random.shuffle(meta_frameworks)
    random.shuffle(backend_end_frameworks)
    random.shuffle(databases)

    # pick a random item from each list

    # Filter FE framework and meta framework
    front_end_framework_options = [random.choice(front_end_frameworks)]
    front_end_framework_options.append(random.choice(meta_frameworks))

    front_end_framework_selected = random.choice(
        meta_frameworks
    )  # My use case right now
    backend_end_framework_selected = random.choice(backend_end_frameworks)
    print(backend_end_framework_selected)
    database_selected = random.choice(databases)

    print("\n")  # spacing

    # conditionally print the results
    if (
        backend_end_framework_selected == "firebase"
        or backend_end_framework_selected == "supabase"
    ):
        database_selected = None
        print(
            f"Your front end framework is: {front_end_framework_selected.title().replace('_', ' ')}"
        )
        print(f"Your backend framework is: {backend_end_framework_selected.title()}")
    else:
        print(f"Your front end framework is: {front_end_framework_selected.title()}")
        print(f"Your backend framework is: {backend_end_framework_selected.title()}")
        print(f"Your database is: {database_selected.title()}")

    return {
        "front_end_framework": front_end_framework_selected.title().replace("_", " "),
        "backend_end_framework": backend_end_framework_selected.title(),
        "databases": database_selected.title(),
    }


def opening_message():
    print(f"{Fore.BLUE}#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~{Style.RESET_ALL}")
    print(
        f"{Fore.BLUE}#{Style.RESET_ALL} {Fore.GREEN} Welcome to the Stack Generator! {Fore.BLUE}#{Style.RESET_ALL}"
    )
    print(f"{Fore.BLUE}#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~{Style.RESET_ALL}")

    print("\n")
    print(
        "This script will help you choose a framework for your next project by randomly selecting one for you then upon approval, will generate a stack for you."
    )


def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")


def print_frameworks():
    print("\n")
    print(
        f"{Fore.GREEN}Here are your current available frontend frameworks: {Style.RESET_ALL}"
    )
    print(
        f"{Fore.BLUE}-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~{Style.RESET_ALL}"
    )

    for framework in front_end_frameworks:
        print(framework)

    print("\n")
    print(
        f"{Fore.GREEN}Here are your current available meta frameworks: {Style.RESET_ALL}"
    )
    print(
        f"{Fore.BLUE}-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~{Style.RESET_ALL}"
    )

    for framework in meta_frameworks:
        print(framework)

    print("\n")
    print(
        f"{Fore.GREEN}These are your current available backend frameworks: {Style.RESET_ALL}"
    )
    print(
        f"{Fore.BLUE}-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-{Style.RESET_ALL}"
    )

    for framework in backend_end_frameworks:
        print(framework)

    print("\n")
    print(f"{Fore.GREEN}These are your current available databases: {Style.RESET_ALL}")
    print(f"{Fore.BLUE}-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~{Style.RESET_ALL}")

    for db in databases:
        print(db)


def main():
    opening_message()
    print_frameworks()
    main_menu()


if __name__ == "__main__":
    main()
