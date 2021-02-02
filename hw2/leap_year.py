"""
    Вводится год.
    Программа выводит количество дней в году, учитывая високосный год.

    * високосный год кратный 4, но не кратный 100 или кратный 400
"""

# Solutions

# 1 вариант (оптимальный)
year = int(input("year: "))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(366)
else:
    print(365)

# 2 вариант (последовательная проверка всех вариантов)
year = int(input("year: "))

if year % 4 != 0:
    print("365")
elif year % 100 != 0:
    print("366")
elif year % 400 != 0:
    print("365")
else:
    print("366")

# 3 вариант с обработкой возможных ошибок

year = input("year: ")
try:
    year = int(year)
except ValueError:
    print(year, "is not a valid year")
else:
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print(366)
    else:
        print(365)
