# task 1
day = input("enter day of the week in three-letter format\n")
if(day == "Sat" or day == "sat") or (day == "Sun" or day == "sun"):
    print("Hooray-it\'s the weekend!")
# task 2
else:
    print("Bad luck - back to studies")


#task 3

def rebook():
    while(True):
        ans = input("Would you like to book a retake?\n")
        if ans == "Y":
            print("Retake booked for tomorrow at 2pm")
            return
        elif ans == "N":
            print("You will need to book later")
            return
        else:
            print("Please enter \"Y\" or \"N\"")



def printScore(score):
    if score >= 80:
        print("Grade: A\nExcelent result")
    elif score>=70:  # no need to write the upper bound for the score.
        print("Grade: B\nVery good")
    elif score >= 60:
        print("Grade: C\nGood effort")
    elif score>= 50:
        print("Grade: D\nYou achieved a Pass")
    else:
        print("Grade: U")
        rebook()


score = int(input("Enter your score to the nearest whole mark:\n"))
printScore(score)
