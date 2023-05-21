import random

# RULES: You can add or remove any framework or database you want.
# Just make sure to follow the format of the lists below.
# If you want to add a new framework, add it to the appropriate list.
# If you want to remove a framework, remove it from the appropriate list.
# Make sure to keep the lists in alphabetical order.


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

if is_ready == "y":
    # shuffle the lists
    random.shuffle(front_end_framework)
    random.shuffle(backend_end_framework)

    front_end_framework = random.choice(front_end_framework)
    backend_end_framework = random.choice(backend_end_framework)
    databases = random.choice(databases)

    print("\n")
    if backend_end_framework == "Firebase" or backend_end_framework == "Supabase":
        print(f"Your front end framework is: {front_end_framework}")
        print(f"Your backend framework is: {backend_end_framework}")
    else:
        print(f"Your front end framework is: {front_end_framework}")
        print(f"Your backend framework is: {backend_end_framework}")
        print(f"Your database is: {databases}")

if is_ready == "n":
    print("Okay. Goodbye!")
