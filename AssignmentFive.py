# Task1


animals = ["cows", "sheep", "pigs", "horses", "chickens", "goats",
           "ducks"]


# Task 2

def get_animal(index):  # for usual str list
    if index > len(animals):
        return "none"
    else:
        return animals[index]


# Task 3


length = len(animals)


# Task 4


def getIndex(name, list):  # returns an index by animal's name
    for index in range(len(list)):
        if name == list[index]:
            return index
    return len(list)


print(animals.pop(getIndex("horses", animals)))  # animals.pop(3)

animals.append("donkeys")  # in the task wasn't mentioned where to append the animal so I will append the to the end

for i in range(length):
    print(get_animal(i))

    # Alternate solution


#  For alternative solution I've created special class that holds the necessary data
class Animal:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

    def get_name(self):
        return self.name

    def __eq__(self, string):
        return self.name == string

    def __str__(self):
        return str(self.name + " : " + str(self.capacity) + " heads")


classed_animals = []
animal_names = ["cows", "sheep", "pigs", "horses", "chickens", "goats",
                "ducks"]
for i in range(len(animals)):
    classed_animals.append(
        Animal(animal_names[i], int((i * 10 + (1 / (10 / (i + 1)))))))  # adding required animals with random values


# TASK 2
def get_classed_animal(index):
    if index > len(classed_animals):
        return Animal("none", 0)
    else:
        return classed_animals[index]


# TASK 3
classed_length = len(classed_animals)
# TASK 4
classed_animals.pop(getIndex("horses", classed_animals))  # or simply classed_animals.pop(3)
classed_animals.append(
    Animal("donkeys", 6))
for i in range(classed_length):
    print(get_classed_animal(i))
