"""
PowerOfTen
"""
# Provide your solution here
# to_pay = 0
# received = 0
#
while True:
    to_pay = int(input("To pay: "))
    if to_pay < 0:
        print("Negative payment is invalid.")
        continue
    while True:
        received = int(input("Received: "))
        if received < 0:
            print("Negative received amount is invalid.")
            break
        change = to_pay - received
        if change > 0:
            print("You did not pay enough.")
        else:
            print(f"Your change is: {change * -1}")
            break


"""
Cash Box
"""
# Provide your solution here

while True:
    number = input("Enter a max 3 digit number: ")
    if int(number) < 0:
        print("number cannot be negative")
        break
    if len(number) > 3:
        print("number has more than 3 digits")
        break
    else:
        continue
        first_digit = int(number)//10
        if first_digit <= 0:
            print(f"{number} = {number} * 1")
        else:
            continue
            second_digit = int(number) % 10
            if second_digit <= 0:
                print(f"{number} = 10 * {first_digit} + 1 * {second_digit}")
            else:
                continue
                third_digit = int(number) % 100
                if third_digit <= 0:
                    print(f"{number} = 100 * {first_digit} + 10 * {second_digit} + 1 * {third_digit}")