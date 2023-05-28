import random
import os
import sys
import subprocess
import time
from colorama import Fore, Back, Style
from scaffold_framework import scaffold
from classes import Project

project = Project("My Project")

front_end_frameworks = [
    "react",
    "vue",
    "svelte",
    "qwik",
    "solid",
    "astro",
    "solid",
]

meta_frameworks = [
    "next",
    "nuxt",
    "svelte_kit",
    "qwik_city",
    "solid_start",
]

# Randomize to get the combined_framework tuple, then randomize the tuple to get the framework or meta_framework
CLI_commands = {
    "react": f"npm create vite@latest -- --template react-ts",
    "vue": f"npm create vite@latest -- --template vue-ts",
    "svelte": f"npm create vite@latest -- --template svelte-ts",
    "next": "npx create-next-app@latest",
    "qwik": "npm create qwik@latest",
    "qwik_city": "npm create qwik@latest",
    "solid_start": "npm init solid@latest",
    "nuxt": "npx nuxi@latest init ",
    "svelte_kit": "npm create svelte@latest ",
    "solid": "npx degit solidjs/templates/ts ",
    "astro": "npm create astro@latest",
}


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
        return choice
    else:
        print("Goodbye!")
        sys.exit()


def main_menu():
    print(f"\n{Fore.GREEN}Which menu would you like to see?: ")
    print(f"{Fore.BLUE}~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~{Style.RESET_ALL}")
    print(f"{Fore.GREEN}[1]{Style.RESET_ALL} - Stack Generator Menu")
    print(f"{Fore.GREEN}[2]{Style.RESET_ALL} - Scaffold a Framework")
    # print(f"{Fore.GREEN}[2]{Style.RESET_ALL} - Operations Menu")
    print(f"{Fore.GREEN}[q]{Style.RESET_ALL} - Quit")

    menu_choice = input("Enter your choice: ")

    if menu_choice == "1" or menu_choice == "2":
        return menu_choice
    else:
        print("Goodbye!")
        sys.exit()


def choose_stack():
    # shuffle the lists (so the order is different each time)
    random.shuffle(front_end_frameworks)
    random.shuffle(meta_frameworks)
    random.shuffle(backend_end_frameworks)
    random.shuffle(databases)

    # Filter FE framework and meta framework
    front_end_framework_options = [random.choice(front_end_frameworks)]
    front_end_framework_options.append(random.choice(meta_frameworks))

    front_end_framework_selected = random.choice(
        meta_frameworks
    )  # My use case right now (meta frameworks)
    backend_end_framework_selected = random.choice(backend_end_frameworks)
    database_selected = random.choice(databases)

    print("\n")  # spacing

    # conditionally print the results
    if (
        backend_end_framework_selected == "firebase"
        or backend_end_framework_selected == "supabase"
    ):
        database_selected = None

    return {
        "front_end_framework": front_end_framework_selected,
        "backend_end_framework": backend_end_framework_selected,
        "databases": database_selected if database_selected else database_selected,
    }


def opening_message():
    clear_terminal()
    print(f"{Fore.BLUE}#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~{Style.RESET_ALL}")
    print(
        f"{Fore.BLUE}#{Style.RESET_ALL} {Fore.GREEN} Welcome to the Stack Generator! {Fore.BLUE}#{Style.RESET_ALL}"
    )
    print(f"{Fore.BLUE}#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~{Style.RESET_ALL}")

    print("\n")
    print(
        "This script will help you choose a framework for your next project by randomly selecting one for you then upon approval, will generate a stack for you."
    )


def print_stack(stack):
    if stack["databases"] == None:
        print(
            f"""Your frontend framework is: {Fore.BLUE}{stack['front_end_framework'].title().replace('_', ' ')}{Style.RESET_ALL}"""
        )
        print(
            f"""Your backend framework is: {Fore.BLUE}{stack['backend_end_framework'].title()}{Style.RESET_ALL}"""
        )
    else:
        print(
            f"""Your frontend framework is: {Fore.BLUE}{stack['front_end_framework'].title().replace('_', ' ')}{Style.RESET_ALL}"""
        )
        print(
            f"""Your backend framework is: {Fore.BLUE}{stack['backend_end_framework'].title()}{Style.RESET_ALL}"""
        )
        print(
            f"""Your database is: {Fore.BLUE}{stack['databases'].title()}{Style.RESET_ALL}"""
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
    menu_choice = main_menu()

    if menu_choice == "1":
        random_generator = stack_generator_menu()
        if random_generator == "1":
            stack = choose_stack()
            print_stack(stack)

            # if user is satisfied, then install the chosen frontend framework via terminal command
            satisfied = input(
                f"{Fore.GREEN}[y/n]{Style.RESET_ALL} - Are you satisfied with this stack?: "
            )
            if satisfied == "y":
                scaffold(stack, CLI_commands, project)

            else:
                # fetch a new stack for the user
                print(f"\n{Fore.BLUE}Fetching a new stack...{Style.RESET_ALL}")
                stack = choose_stack()
                print_stack(stack)

                satisfied = input(
                    f"{Fore.GREEN}[y/n]{Style.RESET_ALL} - Ready to install?: "
                )

                if satisfied == "y":
                    return_val = None
                    if (
                        stack["front_end_framework"] == "svelte_kit"
                        or stack["front_end_framework"] == "nuxt"
                        or stack["front_end_framework"] == "solid"
                    ):
                        new_project_name = input(
                            f"{Fore.GREEN}Name your project?: {Style.RESET_ALL}"
                        )

                        # OUTPUT TO USER ALL FANCY COLORED ABOUT THE PROCESS
                        print(f"New project name: {project.name}")

                        return_val = subprocess.call(
                            f"cd ~/Desktop && cd {new_project_name} && {CLI_commands[stack['front_end_framework']]} {new_project_name} .",
                            shell=True,
                        )
                    else:
                        return_val = subprocess.call(
                            f"cd ~/Desktop && {CLI_commands[stack['front_end_framework']]}",
                            shell=True,
                        )
                else:
                    print("Goodbye!")
                    sys.exit()

                    # user has no option but to accept the stack
                    print(f"{Fore.GREEN}Done!{Style.RESET_ALL}")

    elif menu_choice == "2":
        clear_terminal()
        print(
            f"{Fore.GREEN}Here are your current available frontend frameworks: {Style.RESET_ALL}"
        )
        print(
            f"{Fore.BLUE}-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~{Style.RESET_ALL}"
        )
        for key in CLI_commands.keys():
            print(f"{key}")
        print("\n")  # spacing
        print("\n")  # spacing
        user_framework_choice = input("Enter a framework: ")
        if user_framework_choice.lower() in CLI_commands:
            print(f"{user_framework_choice.title()}....Found!")

            # install the framework
            scaffold(user_framework_choice, CLI_commands, project)

            print(
                f"{Fore.GREEN}H{Style.RESET_ALL}{Fore.BLUE}a{Style.RESET_ALL}{Fore.GREEN}p{Style.RESET_ALL}{Fore.BLUE}p{Style.RESET_ALL}{Fore.GREEN}y{Style.RESET_ALL} {Fore.BLUE}C{Style.RESET_ALL}{Fore.GREEN}o{Style.RESET_ALL}{Fore.BLUE}d{Style.RESET_ALL}{Fore.GREEN}i{Style.RESET_ALL}{Fore.BLUE}n{Style.RESET_ALL}{Fore.GREEN}g{Style.RESET_ALL}{Fore.BLUE}!{Style.RESET_ALL}{Style.RESET_ALL}"
            )
        else:
            print(
                f"{Fore.RED}Invalid framework choice. Add today's newest framework or please try spelling again.{Style.RESET_ALL}"
            )
            main_menu()

    elif menu_choice == "q":
        print("Goodbye!")
        sys.exit()
    else:
        print("Invalid choice. Please try again.")
        main_menu()


if __name__ == "__main__":
    main()
