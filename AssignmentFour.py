# Task One

for i in range(0, 11,2):  # we use 11 as a destination point because if we've used 10 then the range fuction would exclude number 10
    print(i)  # 11 can be replaced with 10 but then number 10 won't appear as an output


# Task Two


def checkInt(value):
    try:
        if type(eval(value)) is int:
            return True
        return False
    except:
        return False


ticket = input("enter number of tickets:\n")
while not checkInt(ticket):
    ticket = input("please enter an integer")

ticket = int(ticket)

for i in range(ticket):
    print("Ticket number " + str((i + 1)) + " booked")


# Task 3


for i in range(1,11): # using for loop
    div = 11-i
    print("24/"+str(div)+" : "+str(float(24/div)))


divisor = 10  # using while loop
while divisor >0:
    print("24/"+str(divisor)+" : "+str(float(24/divisor)))
    divisor -=1
