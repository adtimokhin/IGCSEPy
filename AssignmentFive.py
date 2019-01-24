# Task1


animals = ["cows", "sheep", "pigs", "horses", "chickens", "goats",
           "ducks"]  # not quite sure how to hold capacity of the animals


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
        return self.name


classed_animals = []
for i in range(len(animals)):
    classed_animals.append(Animal(animals[i], (i * 10 + (1 / 10))))  # adding required animals with random values


# Task 2

def get_animal(index):  # for usual str list
    if index > len(animals):
        return "none"
    else:
        return animals[index]


def get_classed_animal(index):
    if index > len(classed_animals):
        return Animal("none", 0)
    else:
        return classed_animals[index]


# Task 3


length = len(animals)
classed_length = len(classed_animals)


# Task 4


def getIndex(name, list):  # returns an index by animal's name
    for index in range(len(list)):
        if name == list[index]:
            return index


print(classed_animals.pop(getIndex("horses", classed_animals)))  # or simply classed_animals.pop(3)
print(animals.pop(getIndex("horses", animals)))  # animals.pop(3)


classed_animals.append(
    Animal("donkeys", 6))  # in the task wasn't mentioned where to append the animal so I will append the to the end
animals.append("donkeys")

for i in range(length):  # not 'classed' animals
    print(get_animal(i))

for i in range(classed_length):
    print(get_classed_animal(i))
