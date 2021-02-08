"""
    Для объявления функции используется ключевое слово def,
    после чего идет название функции, скобки и двоеточие.
    С новой строки с отступами начинается тело функции.
"""


def func():
    # тело функции
    print('Hello world!')


func()  # вызов объявленной функции


def summ(a, b):  # a и b - обязательные параметры функции
    summ = a + b
    print(summ)


# вызов функции сумм с передачей в нее разных аргументов
summ(5, 10)  # 5 и 10 - аргументы функции
summ(1, 19)
summ(33, 178)


# функция может возвращать значение с помощью ключевого слова return
def summ(a, b):
    return a + b


a = summ(5, 10)  # возращаемое значение функция можно присвоить переменной
print(a)


def usd_to_uah(currency, rate=28):  # rate - не обязательный параметр
    return currency * rate


uah = usd_to_uah(10)
print(uah)

uah = usd_to_uah(15, 28.9)
print(uah)


# функция может принимать 0 и более аргументов.
# Для этого используются операторы * (кортеж) и ** (словарь)
def func(*args, **kwargs):
    print(args)  # сюда попадают все не именованные аргументы
    print(kwargs)  # здесь - именованные


func(1, 2, 3, 4, 'python', [], 3.14, name='max', age=20)


def func(number, *args, **kwargs):  # number - обязательный параметр
    print(number)
    print(args)
    print(kwargs)


func(1, 2, 3, 4, 'python', [], 3.14, name='max', age=20)


def main():
    pass


if __name__ == '__main__':
    main()
