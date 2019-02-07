# Task 13

response = 'K'
# response variable has to be initialised before the entering the loop. Otherwise a mistake will occur.
while response != 'N' and response != 'Y':
    response = input("Do you have an account?")
    if response == 'Y':
        login = input("Enter login")
        password = input("Entere password")
    elif response == 'N':
        print("Go to a registration page")
    else:
        print("Invalid input. Try again")


# Task 19

Dogs = []

for i in range(5):
    breed = input("enter a new breed of dogs")
    Dogs.append(breed)

print(Dogs)


