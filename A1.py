#START A1

num1: float = float(input("Enter a first decimal number:"))
num2: float = float(input("Enter a second decimal number :"))

if num1 < num2 :
    print(num1)
    print(num1)
    print(num1)
else:
    print(num2)
    print(num2)
    print(num2)

#END

#START A2

num1: int = int(input("Enter a first number :"))
num2: int = int(input("Enter a second number :"))

average = (num1 + num2) / 2

print(f"The average of two numbers is {average}.")

#END

#START A3

num1: int = int(input("Enter number one :"))
num2: int = int(input("Enter number two :"))
num3: int = int(input("Enter number three :"))

if num1 > num2 and num1 > num3:
    print(num1)
elif num2 > num1 and num2 > num3 :
    print(num2)
else:
    print(num3)

#END

#START A4

num: int = int(input("Enter the length of the movie in minutes : "))

hours = num //60
minutes = num % 60

print(f"The length of the movie is {hours} hours and {minutes} minutes.")

#END

#START B1

top: int = int(input("Enter a positive integer : "))

for i in range(1, top + 1):
    print(i)

#END

#START B2

num1: int = int(input("Enter a first number :"))
num2: int = int(input("Enter a second number :"))

if num1 > num2:
    for i in range(num2, num1 + 1):
        print(i)
else:
    for i in range(num1, num2 + 1):
        print(i)

#END

#START C1

array_num = []
number: int = int(input("Enter a number:"))

if number == -99:
    print("None")
else:
    while number != -99:
        array_num.append(number)
        number: int = int(input("Enter a number:"))
    print(f"The sum is the numbers is {sum(array_num)}.")


#END

#START C2

array_num = []
number: int = int(input("Enter a number:"))

if number == -99:
    print("None")
else:
    while number > 0 or number != 0:
        array_num.append(number)
        number: int = int(input("Enter a number:"))

    print(f"Max: {max(array_num)}.")
    print(f"Min: {min(array_num)}.")
#END

#START C3

array_num = []
temp = None
max_index = 0

for i in range(1, 5 + 1):
    number: int = int(input("Enter a number: "))
    array_num.append(number)
    if temp is None :
        temp = number
    if number > temp:
        max_index = array_num.index(number)
        temp = number

print(f"The ordinal number of the largest number is {max_index + 1}")

#END

#START D1

while True:
    try:
        array_temp = []
        temperature = True
        for i in range(1, 12 + 1):
            temperature: float = float(input(f"Enter the temperature in Tel Aviv number {i}: "))
            if len(array_temp) >= 1 and array_temp[-1] == 0 and temperature == 0:
                print("Two consecutive zeros detected, please enter the temperature.")
                i -= 2
                continue
            array_temp.append(temperature)
            if temperature > 40 or temperature < -5:
                temperature = False
                break

        if temperature:
            print("Correct")
            average = sum(array_temp) / 12
            print(f"The average temperature is {average}.")
            print(f"The highest temperature is {max(array_temp)}.")
            print(f"The lowest temperature is {min(array_temp)}.")
            break
        else:
            print("Wrong data")
            break
    except ValueError:
        print("Only numbers are allowed. Please try again.")

#END