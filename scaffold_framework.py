import subprocess
import time
from colorama import Fore, Back, Style


def scaffold(stack: str or object, CLI_commands, project):
    return_val = None

    if type(stack) == str:
        return_val = None
        stack = stack.lower()
        if stack == "svelte_kit" or stack == "nuxt" or stack == "solid":
            new_project_name = input(
                f"{Fore.GREEN}Name your project?: {Style.RESET_ALL}"
            )

            project.name = new_project_name

            # On the desktop, create a new folder with the project name
            # and change directory to that folder then install frontend
            # framework via terminal command.

            # if stack == "nuxt":
            subprocess.call(
                f"cd ~/Desktop && {CLI_commands[stack]} {new_project_name}",
                shell=True,
            )
            # else:
            #     subprocess.call(
            #         f"cd ~/Desktop && mkdir {new_project_name} && cd {new_project_name} && {CLI_commands[stack]} {new_project_name}",
            #         shell=True,
            #     )

            # Change directory to the new project and install dependencies.
            subprocess.call(
                f"cd ~/Desktop/{new_project_name} && npm install",
                shell=True,
            )
        else:
            # new_project_name = input(
            #     f"{Fore.GREEN}Name your project?: {Style.RESET_ALL}"
            # )

            # project.name = new_project_name
            subprocess.call(
                f"cd ~/Desktop && {CLI_commands[stack]}",
                shell=True,
            )

    if type(stack) is object:
        if (
            stack["front_end_framework"] == "svelte_kit"
            or stack["front_end_framework"] == "nuxt"
        ):
            new_project_name = input(
                f"{Fore.GREEN}Name your project?: {Style.RESET_ALL}"
            )

            # OUTPUT TO USER ALL FANCY COLORED ABOUT THE PROCESS
            print(f"New project name: {project.name}")

            return_val = subprocess.call(
                f"cd ~/Desktop && mkdir {new_project_name} && cd {new_project_name} && {CLI_commands[stack['front_end_framework']]} {new_project_name}",
                shell=True,
            )
        elif (
            stack["front_end_framework"].lower() == "solid"
            and stack["backend_end_framework"] == "supabase"
        ):
            new_project_name = input(
                f"{Fore.GREEN}Name your project?: {Style.RESET_ALL}"
            )

            supabase_component_template = """
    import { createClient } from '@supabase/supabase-js'

    const supabaseUrl = import.meta.env.VITE_SUPABASE_URL
    const supabaseAnonKey = import.meta.env.VITE_SUPABASE_ANON_KEY

    export const supabase = createClient(supabaseUrl, supabaseAnonKey)
            """

            # Install frontend framework via terminal command
            subprocess.call(
                f"cd ~/Desktop && {CLI_commands[stack['front_end_framework']]} {new_project_name} && cd {new_project_name} && npm install @supabase/supabase-js && touch .env && echo 'testing' > .env",
                shell=True,
            )

            # create a .env file
            subprocess.call(
                f"cd ~/Desktop/{new_project_name} && echo 'VITE_SUPABASE_URL=YOUR_SUPABASE_URL\nVITE_SUPABASE_ANON_KEY=YOUR_SUPABASE_ANON_KEY' > .env",
                shell=True,
            )

            # create a src folder and a supabaseClient.tsx file
            subprocess.call(
                f"touch ~/Desktop/{new_project_name}/src/supabaseClient.tsx",
                shell=True,
            )

            # write boilerplate to the supabaseClient.tsx file
            # subprocess.call(
            #     f"google https://supabase.com/docs/guides/getting-started/tutorials/with-solidjs#initialize-a-solidjs-app",
            #     shell=True,
            # )
            subprocess.call(
                f"cd ~/Desktop/{new_project_name}/src && echo '{supabase_component_template.strip()}' > supabaseClient.tsx",
                shell=True,
            )
        else:
            return_val = subprocess.call(
                f"cd ~/Desktop && {CLI_commands[stack['front_end_framework']]}",
                shell=True,
            )

    print(f"Return value: {return_val}")
    print(f"{Fore.GREEN}Done!{Style.RESET_ALL}")
