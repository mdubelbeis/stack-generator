import random

front_end_framework = [
    "React",
    "NextJS",
    "Vue",
    "Nuxt",
    "SvelteKit",
    "Qwik",
    "QwikCity",
    "Solid",
    "SolidStart",
]
# meta_framework = ['NextJS', 'Nuxt', 'SvelteKit', 'QwikCity', 'SolidStart']
backend_end_framework = [
    "Express",
    "Django REST Framework",
]
databases = [
    "MongoDB",
    "PostgreSQL",
    "MySQL",
]

full_stack_framework = front_end_framework + backend_end_framework

print("\n")
print("Welcome to the Full Stack Framework Generator!")
print("This script will help you choose a framework for your next project.")
print("*** NOTE: Front End Frameworks and Meta Frameworks have been combined. *** ")

is_ready = input("Are you ready [y/n]?: ")

if is_ready == "y":
    print(front_end_framework)
    random.shuffle(front_end_framework)
    random.shuffle(backend_end_framework)
    print(front_end_framework)

    print("Great! Let's get started.")
    print("\n")
    print("These are the available front end frameworks:")
    for framework in front_end_framework:
        print(framework)

    print("\n")
    print("These are the available backend frameworks:")
    for framework in backend_end_framework:
        print(framework)

    print("\n")
    try:
        print("Your front end framework is: " + front_end_framework[-1])
    except Exception as e:
        print("Error in frontend framework. Please try again.")
        print(e)

    try:
        print("Your backend framework is: " + backend_end_framework[-1])
    except Exception as e:
        print("Error in backend framework: Please try again.")
        print(e)

if is_ready == "n":
    print("Okay. Goodbye!")
