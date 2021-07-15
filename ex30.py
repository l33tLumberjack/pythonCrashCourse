people = 30
cars = 40
trucks = 15

if cars > people:
    print("We should take the cars")
elif cars < people:
    print("We should not take cars")
else:
    print("We cant decide")

if trucks > cars:
    print("Thats too many trucks")
elif trucks < cars:
    print("Maybe we should take the trucks")
else:
    print("We still cant decide")

if people > trucks:
    print("Alright lets just take the trucks")
else:
    print("Fine lets just stay home then.")
