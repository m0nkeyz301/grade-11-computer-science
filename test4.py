def joke_1():
    print("Che-mystery")

def joke_2():
    print("One pence")

def joke_3():
    print("Funny joke here")

joke_type = input("Which joke do you want to hear? (1/2/3)")
if joke_type == "1":
    joke_1()
elif joke_type == "2":
    joke_2()
elif joke_type == "3":
    joke_3()
else:
    print("Insert valid input")