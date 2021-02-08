"""
    Рекурсия.

    Вызов функции из нее же самой называется рекурсией.

    Одним из примеров практического применения рекурсии -
        алгоритм вычисления факториала.

"""

# факториал числа 5 -> !5 = 1 * 2 * 3 * 4 * 5 = 120

n = int(input('n: '))


def fact(n):
    if n == 0:
        return 1  # если n == 0 - возвращаем 1, так как факториал числа !0 = 1
    return n * fact(n - 1)  # умножаем число n на вызов функции с числом n - 1


result = fact(n)
print(result)

# пример вычисления !5
# сначала идет рекурсивный вызов функции,
# затем начиная с последнего вызова идет возвращение значения - return

# 5 * fact(4)
#     4 * fact(3)
#         3 * fact(2)
#             2 * fact(1)
#                 1 * fact(0)
#                 1
#             2
#         6
#     24
# 120
