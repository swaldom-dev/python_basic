"""
    1. Найти наибольшую цифру числа.
    2. Найти количество четных и нечетных цифр в числе.
"""

number = int(input("Введите число: "))
biggest = 0
even = 0
odd = 0

while number > 0:
    last_digit = number % 10

    if last_digit % 2 == 0:
        even += 1
    else:
        odd += 1

    if last_digit > biggest:
        biggest = last_digit

    number //= 10

print("biggest:", biggest)
print("even:", even)
print("odd:", odd)
