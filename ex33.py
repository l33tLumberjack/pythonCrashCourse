from sys import argv
script, arg1, arg2 = argv

numbers = []

def while_loop(input, skipper):
    i = 0
    numbers = []
    while i < input:
        print(f"At the top i is {i}")
        numbers.append(i)
        i += skipper
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")
    return numbers

def for_loop(input, skipper):
    i = 0
    numbers = []
    for i in range(0,input,skipper):
        print(f"At the top i is {i}")
        numbers.append(i)
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")
    return numbers

numbers = for_loop(int(arg1), int(arg2))

print("The numbers: ")

for num in numbers:
    print(num)
