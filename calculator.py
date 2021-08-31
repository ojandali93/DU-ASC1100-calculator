val_1 = input("Val 1: ")
val_2 = input("Val 2: ")
val_3 = input("+ / - / * / %: ")

def add_numbers(num1, num2):
    new_number = num1 + num2
    return new_number

def subtract_numbers(num1, num2):
    new_number = num1 - num2
    return new_number

def multiple_numbers(num1, num2):
    new_number = num1 * num2
    return new_number

def divide_numbers(num1, num2):
    divided_number = (num1 / num2)
    return divided_number

if val_3 == "+":
    total = add_numbers(int(val_1), int(val_2))
    print(total)
elif val_3 == "-":
    total = subtract_numbers(int(val_1), int(val_2))
    print(total)
elif val_3 == "*":
    total = multiple_numbers(int(val_1), int(val_2))
    print(total)
elif val_3 == "%":
    total = divide_numbers(int(val_1), int(val_2))
    print(total)