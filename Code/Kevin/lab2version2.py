import random
antonym = input("Give me an antonym for 'data':  ")
adjective = input("Tell me a list of adjectives to use:  ")
adjective_list = adjective.split(',')
buzzword = input("Give me a sciency buzzword:  ")
animals = input("A type of animal (plural):  ")
science = input("Some Sciency thing:  ")
science2 = input("Another Sciency thing:  ")
s_adjective = input("A science adjective:  ")

print("Nonmaterial Scientist Job Description:")
print(f"Seeking a {random.choice(adjective_list)} engineer, able to work on {buzzword} projects with a team of {animals}.")
print(f"Key Responsibilities: \n- Extract patterns from non-material")
print(f"- Optimize {science}\n- Transform {science2} into {s_adjective}.")
