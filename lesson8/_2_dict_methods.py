"""
    Методы словарей.

    clear() – очистить
    copy() – сделать копию
    get() – получить значение по ключу
    setdefault() – возвращает значение ключа или создает его
    pop(key) – удаляет ключ key и возвращает его значение
    popitem() – удаляет последнюю пару и возвращает кортеж (ключ, значение)
    update({'key': 'value'}) – обновить словарь

    items() – получить пары ключ-значений и виде списка кортежей
    keys() – получить список ключей
    values() – получить список зачений
"""

a = {'short': 'dict', 'long': 'dictionary'}

# Копия словаря
b = a.copy()
b = dict(a)

b['short'] = 'new'

print(a)
print(b)

# Получение значения по ключу
print(a.get('word'))

# Получение значения по ключу и создание, если его нет
print(a.setdefault('three', 'red'))
print(a.setdefault('two', 'red'))

# Удаление элементов из словаря
var1 = b.pop('short')
var2 = a.popitem()

print(var1, var2)

# Обновление словарей
b = {'new_key': 'value'}
c = {'long': 'some long string'}

a.update(b)
a.update(c)

print(a)

# в python3.9+ доступно объединение словарей с помощью оператора |

a = a | b  # a |= b == a.update(b)
a |= b | c  # объединяет все словари в a

# Обход словарей циклом

for item in a.values():
    print(item)

for key in a:
    print(key)

for key, value in a.items():
    print(key, value)
