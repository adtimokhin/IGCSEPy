# Task 3


country_name = input("enter country\'s name")
sport_counter = int(input("enter number of sports for which you want to enter data"))
golden_medals =0
for i in range(sport_counter):
    sport_name = input("enter sport\'s name")
    print("how many golden medals had {0} won in {1}".format(country_name, sport_name))
    medals = int(input())
    golden_medals += medals

print("{0} had won {1} golden medals".format(country_name,golden_medals))