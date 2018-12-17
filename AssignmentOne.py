#task 2
name = input("enter guest\'s name:\n") #data type - string
nights_number = int(input("enter number of nights "+ name+ " will stay in the hotel:\n")) # data type - integer (int)
is_evening_meal_required = bool(input("enter \'yes\' if "+ name + " needs an evening meal, otherwise: \'no\'") == "yes") # boolean

#task3
student_name = input("Enter student\'s name:\n")
age = int(input("enter student\'s age:\n"))
nationality = input("enter student\'s nationality:\n")
print("\nstudent:\n"+ student_name+"\nage:\n" + (str(age))+" years\nnationality:\n"+nationality+"\nwas successfully added to the database") # massage was too long

#task4
def getNumName(number):
    if number > 10 or number < 1:
        return "none"
    if number == 1: return "one" # switch-case alternative. We can leave the cycle as soon as we'll find value needed. Hence we can use if instead of elif
    if number == 2: return "two"
    if number == 3: return "three"
    if number == 4: return "four"
    if number == 5: return "five"
    if number == 6: return "six"
    if number == 7: return "seven"
    if number == 8: return "eight"
    if number == 9: return "nine"
    if number == 10: return "ten"


num_one = int(input("enter first number\n"))
num_two = int(input("enter second number\n"))
num_three = int(input("enter third number\n"))

num_one = getNumName(num_one)
num_two = getNumName(num_two)
num_three = getNumName(num_three)

print("numbers:\n"+ num_one+"\n"+num_two+"\n"+num_three)


