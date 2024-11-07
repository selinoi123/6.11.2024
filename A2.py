#START A5

number: int = int(input("Enter a number with four digits :"))

num2:int = number % 10

print(num2)


#END

#START A6

number: int = int(input("Enter a number with four digits :"))

num2:int = ( number % 100 ) // 10

print(num2)


#END

#START A7

number: int = int(input("Enter a number with two digits :"))

first_digit:int = number // 10
second_digit: int = number % 10

sum_digit: int = first_digit + second_digit

print(sum_digit)

#END

#START A8

number: int = int(input("Enter a number with two digits :"))

first_digit:int = number // 10
second_digit: int = number % 10 * 10
sum_digit: int = second_digit + first_digit

print(sum_digit)

#END

#START A9

number: int = int(input("Enter a number :"))

if number % 2 == 0:
    print("even")
else:
    print("odd")

#END

#START A10

salary: int = int(input("Enter your salary :"))

if salary < 6000:
    print("You don't have to pay tax")
elif 6000 <= salary < 12000:
    tax: int = salary * 10 // 100
    print(f"Your salary is : {salary}. You have to pay a tax of {tax}")
elif 12000 <= salary < 18000:
    tax: int = salary * 20 // 100
    print(f"Your salary is : {salary}. You have to pay a tax of {tax}")
elif 18000 <= salary < 25000:
    tax: int = salary * 30 // 100
    print(f"Your salary is : {salary}. You have to pay a tax of {tax}")
elif 25000 <= salary < 35000:
    tax: int = salary * 40 // 100
    print(f"Your salary is : {salary}. You have to pay a tax of {tax}")
elif 35000 <= salary < 50000:
    tax: int = salary * 45 // 100
    print(f"Your salary is : {salary}. You have to pay a tax of {tax}")
else:
    tax: int = salary * 51 // 100
    print(f"Your salary is : {salary}. You have to pay a tax of {tax}")

#END

#START A11

age: int = int(input("Enter your age :"))
height: int = int(input("Enter your height in centimeters :"))

if 8 <= age <= 18 and height > 115 or 18 < age and height > 100:
    print("You can get on the roller coaster")
else:
    print("You can't get on a roller coaster")

#END

#START B3

n: int = int(input("Enter a positive integer : "))

if n % 2 != 0:
    n = n -1

for i in range(0, n + 1, 2):
    print(i)

#END

#START B4

max_num: int = int(input("Enter a positive integer number one : "))
den: int = int(input("Enter a positive integer number two : "))

if max_num % den != 0:
    rest = max_num % den
    max_num = max_num - rest


for i in range(0, max_num + 1, den):
    print(i)

#END

#START C4

num1: int = int(input("Enter a first number : "))
num2: int = int(input("Enter a second number: "))

count = 0
for i in range(num1):
    count = count + num2

print(count)

#END

#START C5

num1: int = int(input("Enter a first number : "))
num2: int = int(input("Enter a second number: "))

count = 1
for i in range(num2):
    count = count * num1

print(count)

#END

#START C6

number: int = int(input("Enter a number: "))
digit: int = int(input("Enter a digit: "))

digit_in_number = False

while number != 0:
    current_digit = number % 10
    if current_digit == digit:
        digit_in_number = True
        break
    number = number // 10

if digit_in_number:
    print("True")
else:
    print("False")

#END

#START C7

num1: int = int(input("Enter a first number : "))
num2: int = int(input("Enter a second number: "))

if num1 > num2:
    divisor = num2
else:
    divisor = num1

while divisor > 0:
    if num1 % divisor == 0 and num2 % divisor == 0:
        break
    else:
       divisor -= 1

print(f"The greatest divisor of {num1} and {num2} is {divisor}.")

#END

#START C8

number: int = int(input("Enter a number : "))

is_prime = True
for num in range(2, 10):
    if number % num == 0 and number > num:
        is_prime = False
        break
if is_prime:
    print(f"The number {number} is prime")
else:
    print(f"The number {number} is not prime")

#END

#START D2

print("Voting subject - The establishment of the State of Israel for the Jews")
print("1 - favor, 2 - against, 3 - abstained, 4 - veto")

count_1 = 0
count_2 = 0
count_3 = 0

favor_countries = []
against_countries = []
abstained_countries = []

for i in range(1, 44 + 1):
    try:
        country: int = int(input(f"Country vote number {i}: "))

        if country != 1 and  country != 2 and  country != 3 and country != 4:
            continue

        if country == 4:
            print(f"Country number {i}.")
            break

        elif country == 1:
            favor_countries.append(i)
            count_1 += 1
        elif country == 2:
            against_countries.append(i)
            count_2 += 1
        elif country == 3:
            abstained_countries.append(i)
            count_3 += 1

    except ValueError:
        print("Only numbers are allowed. Please try again.")


if country != 4:
    print(f"The number of votes in favor: {count_1}.")
    print(f"The number of votes against: {count_2}.")
    print(f"The number of abstained votes: {count_3}.")

    if count_1 > 0:
        print(f"Serial number of the first country that voted in favor is : {favor_countries[0]}.")
    if count_2 > 0:
        print(f"Serial number of the last country that voted against is : {against_countries[-1]}. ")

#END