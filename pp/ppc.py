name = input("What is your name? ")
age = input("What is your age? ")

currentDate = int(2019)

TimeFuture = int(int(currentDate) - (int(age)))
Future = int(int(TimeFuture) + 100)

print("hello ", name, " you will be ", Future, " in 100 years!")
