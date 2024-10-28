def multiplication_table(integer):
    for i in range(11):
        table = integer * i
        print(f"{integer} x {i} = {table}")

integer = int(input("Input an integer"))
multiplication_table(integer)