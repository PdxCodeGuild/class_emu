# Version 1
#
# The goal is to calculate how many years it will take for two jackalopes to create a population of 1000.
#
#     Jackalopes are reproductive from ages 4-8 and die at age 10.
#     Gestation is instantaneous. Each gestation produces three offspring.
#     Jackalopes are hermaphrodites, it takes a pair to reproduce, but any pair will do
#
# With these conditions in mind, we can represent our population as a list of ints.

jackalopes = [0, 0]
jackalope_cemetery = 0
n_offspring = 1
years = 0
while len(jackalopes) < 1000:
    years += 1
#age the jackalopes
    for i in range(len(jackalopes)):
        jackalopes[i] += 1
    #breed them between ages 4 and 8 (once per couple per year)
    breeding_jackalope_counter = 0
    for jackalope in jackalopes:
        if jackalope >=4 and jackalope <= 8:
            breeding_jackalope_counter += 1
    breeding_jackalope_couples = breeding_jackalope_counter // 2
    for i in range(breeding_jackalope_couples * n_offspring):
        jackalopes.append(0)
    #kill them all (at age 10)
    temp_jackalopes = []
    for i in range(len(jackalopes)):
        if jackalopes[i] < 10:
            temp_jackalopes.append(jackalopes[i])
        else:
            jackalope_cemetery += 1
    jackalopes = temp_jackalopes


print(jackalopes)
print(years)
print(jackalope_cemetery)
