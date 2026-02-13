#functions with no inputs

def greet():
    for i in range(3):
        print(f"Statement {i + 1}")

greet()

#function with inputs
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")

name = input("What is your name?")
greet_with_name(name)

def life_in_weeks(age):
    
    remaining_weeks = (52 * 90) - (age * 52)
    
    print(f"You have {remaining_weeks} weeks left.\n")
    
life_in_weeks(20)