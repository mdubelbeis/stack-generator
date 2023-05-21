import random


def menu():
    print("1. Add a framework")
    print("2. Remove a framework")
    print("3. Update a framework")
    print("4. View all frameworks")
    print("5. Choose my next stack")
    print("5. Exit")

    choice = input("Enter your choice: ")
    return choice


front_end_framework = [
    "React",
    "NextJS",
    "Vue",
    "Nuxt",
    "SvelteKit",
    "Qwik",
    "QwikCity",
    "Solid",
]
# meta_framework = ['NextJS', 'Nuxt', 'SvelteKit', 'QwikCity', 'SolidStart']
backend_end_framework = [
    "Express",
    "Django REST Framework",
    "Firebase",
    "Supabase",
]

# backend_as_a_service = [
#     "Firebase",
#     "Supabase",
# ]

databases = [
    "MongoDB",
    "PostgreSQL",
]


print(
    """
***************************************
    Welcome to the Stack Generator!
***************************************    
    
This script will help you choose a framework for your next project
by randomly selecting a front end framework, a backend framework, and a database.
    
"""
)

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
is_ready = input("Are you ready [y/n]?: ")

menu_choice = menu()


if is_ready == "y":
    # shuffle the lists
    random.shuffle(front_end_framework)
    random.shuffle(backend_end_framework)

    # pick a random item from each list
    front_end_framework = random.choice(front_end_framework)
    backend_end_framework = random.choice(backend_end_framework)
    databases = random.choice(databases)

    print("\n")  # spacing

    # conditionally print the results
    if backend_end_framework == "Firebase" or backend_end_framework == "Supabase":
        print(f"Your front end framework is: {front_end_framework}")
        print(f"Your backend framework is: {backend_end_framework}")
    else:
        print(f"Your front end framework is: {front_end_framework}")
        print(f"Your backend framework is: {backend_end_framework}")
        print(f"Your database is: {databases}")

if is_ready == "n":
    print("Okay. Goodbye!")
