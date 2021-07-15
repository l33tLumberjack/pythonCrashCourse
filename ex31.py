print("""YOu enter a dark room with two doors.
Do you go through door #1 or door #2""")

door = input("> ")

if door == "1":
    print("You see Shai LeBouf with a crazy look in his eye")
    print("What do you do?")
    print("1. Run")
    print("2. Sneak away")

    shai = input("> ")
    if shai == "1":
        print("ARGH! YOUR LEG ITS STUCK IN A BEAR TRAP!")
    elif shai == "2":
        print("You snuck away from Shai LeBouf")
    else:
        print(f"Well, doing {shai} is probably better.")
        print("Shai LeBouf receeds into the shadows")
elif door == "2":
    print("You sneak up on Shai LeBouf with a crazy look in your eye")
    print("What do you do?")
    print("1. BUT I CAN DO JU-JITSU!")
    print("2. Sneak away")

    shai = input("> ")
    if shai == "1":
        print("You are once again safe from Shai LeBouf")
    elif shai == "2":
        print("ACTUAL CANNABAL SHAI LEBOUF")
    else:
        print(f"Well, doing {shai} is probably better.")
        print("Shai LeBouf receeds into the shadows")
else:
    print("Thats all she wrote folks")
