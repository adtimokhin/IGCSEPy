import random

print(0 % 50)


def create_ID(car_make, car_model):
    first_letter = car_make[0]
    second_letter = car_model[0]
    number = random.randint(100, 999)
    check_digit = number % 10
    id_number = first_letter + second_letter + str(number) + str(check_digit)
    return id_number


# print(create_ID("Ford" , "Focus"))

makes = ["Ford", "Vauxhall", "Vauxhall", "Hyundai", "Daewoo", "Renault", "Citroen", "Ford", "Kia", "Toyota"]
models = ["Focus", "Corsa", "Nova", "I10", "Matiz", "Megane", "Xsara", "Focus", "Picante", "Yaris"]
years = [2007, 2009, 2016, 2015, 2012, 2008, 2015, 2014, 2013, 2012]
ids = []
number_of_hires = []
days_hired = []
availability = []
due_for_service = []
for i in range(len(models)):
    ids.append(create_ID(makes[i], models[i]))
    number_of_hires.append(0)
    days_hired.append(0)
    availability.append(True)
    due_for_service.append(False)

mileages = []
for i in range(len(makes)):
    print("Enter a mileage for a car with an id {0}".format(ids[i]))
    # milage = int(input())  # This line will allow the owner to enter a mileage by his own
    mileage = (2019 - years[i]) * 100 + 2019  # formula for an automatic appendage of mileages
    mileages.append(mileage)

for i in range(len(models)):
    print("Car details:")
    print("Id: {0}\nMaker: {1}\nModel: {2}\nYear when was made: {3}\nAvailability :{4}".format(ids[i], makes[i],
                                                                                               models[i], years[i],
                                                                                               ("Available" if
                                                                                                availability[
                                                                                                    i] else "Unavailable")))

# Interaction with a user
command = "hire"


def get_car_number():  # current function will loop itself until the existing id would be entered
    car_id = input("Enter car\'s id:\n")
    for i in range(len(ids)):
        if ids[i] == car_id:
            return i

    print("No such car was found.")
    return get_car_number()


def hire():
    car_number = get_car_number()
    available = availability[car_number]
    if available:
        hire_days = int(input("Enter number of days you would hire the car for?\n"))
        print("Car number {0} was successfully hired for {1} days".format(ids[car_number], hire_days))
        number_of_hires[car_number] += 1
        days_hired[car_number] += hire_days
        availability[car_number] = False
    else:
        print("A car with an id {0} is not currently available.".format(ids[car_number]))


def return_car():
    car_number = get_car_number()
    available = availability[car_number]
    out_of_service = due_for_service[car_number]
    if not available and not out_of_service:
        damaged = 'N'
        while type(damaged) is not bool:
            damaged = input("Was the car {0} damaged? Enter Y or N\n".format(ids[car_number]))
            if damaged == 'Y':
                damaged = True
            elif damaged == 'N':
                damaged = False
            else:
                print("Cannot resolve the input. Please, try again")

        if damaged:
            due_for_service[car_number] = True
        else:
            availability[car_number] = True

        print("The car was successfully returned")
        return car_number
    else:
        print("Current car is not hired")
        return -1


def check_hire_info(car_number):
    if number_of_hires[car_number] % 50 == 0 and number_of_hires[car_number] >= 50:
        availability[car_number] = False
        due_for_service[car_number] = True
    elif days_hired[car_number] % 300 == 0 and days_hired[car_number] >= 300:
        availability[car_number] = False
        due_for_service[car_number] = True


while command != "quit":
    command = input("What action you want to accomplish?\n")
    if command == "hire":
        hire()
    elif command == "return":
        returned_val = return_car()
        if returned_val != -1:
            check_hire_info(returned_val)
    elif command != "quit":
        print("Cannot resolve the input")

for i in range(len(models)):
    if due_for_service[i]:
        print("Car {0} is due for service".format(ids[i]))
