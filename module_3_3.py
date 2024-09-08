# def print_params(a, b, c): # *args (для списков, кортежей), **kwargs (для словарей)
#     print(a, b, c)

# def print_params(*params):  #запаковка
#     print(params)
# print_params(1, 2, 3, 4, 5, 6, 7)

# def print_params(*params):  #распаковка
#     print(*params)
# print_params(1, 2, 3, 4, 5, 6, 7)


# def print_params(*params):  #если более 7 параметров, то обчно исп *args
#     print(params)
# print_params()



# def print_params(a, b, c):
#     print(a, b, c)
#
#
# list_ = [1, 2, 3]
# print_params(list_, 2, 3)


# def print_params(a, b, c):
#     print(a, b, c)
#
#
# list_ = [1, 2, 3]
# print_params(*list_)


# def print_params(a, b, c):
#     print(a, b, c)
#
#
# list_ = [1, 2] #ошибка, нужно передать 3 параметра, а не 2
# print_params(*list_)


# def print_params(a, b, c):
#     print(a, b, c)
#
#
# list_ = [1, 2]
# print_params(1, *list_)



# def print_params(a, b, c):
#     print(a, b, c)
#     print(c)
#
#
# list_ = [1, 2]
# print_params(*list_, 4)


# def print_params(a, b, c):
#     print(a, b, c)
#
#
# dict_ = {'a': 1, 'b': 2, 'c': 3} # имена ключей - имена параметров
# print_params(**dict_)


# def print_params(**kwargs):
#     print(kwargs)
#
#
# dict_ = {'a': 1, 'b': 2, 'c': 3}
# print_params(**dict_)


# def print_params(**kwargs):
#     for key in kwargs:
#         print(key)
#
#
# dict_ = {'a': 1, 'b': 2, 'c': 3}
# print_params(**dict_)

# def print_params(**kwargs):
#     for key, value in kwargs.items():
#         print(key, value)
#
#
# dict_ = {'a': 1, 'b': 2, 'c': 3}
# print_params(**dict_)



# def print_params(a, b, c):
#     print(a, b, c)
#
#
# list_ = [1, 2]
# dict_ = {'c': 3}
# print_params(*list_, **dict_)

# Задача "Распаковка":
# 1.Функция с параметрами по умолчанию:
# Создайте функцию print_params(a = 1, b = 'строка', c = True), которая принимает три параметра со значениями по умолчанию (например сейчас это: 1, 'строка', True).
# Функция должна выводить эти параметры.
# Вызовите функцию print_params с разным количеством аргументов, включая вызов без аргументов.
# Проверьте, работают ли вызовы print_params(b = 25) print_params(c = [1,2,3])
# 2.Распаковка параметров:
# Создайте список values_list с тремя элементами разных типов.
# Создайте словарь values_dict с тремя ключами, соответствующими параметрам функции print_params, и значениями разных типов.
# Передайте values_list и values_dict в функцию print_params, используя распаковку параметров (* для списка и ** для словаря).
# 3.Распаковка + отдельные параметры:
# Создайте список values_list_2 с двумя элементами разных типов
# Проверьте, работает ли print_params(*values_list_2, 42)
# Пример результата выполнения программы:
# Исходный код:
# values_list_2 = [54.32, 'Строка' ]
# print_params(*values_list_2, 42)
# Вывод на консоль:
# 54.32 'Строка' 42


def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params(2, 'str')
print_params()
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [1, 'str', False]
values_dict = {'a': 2, 'b': 'dict', 'c': False}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [1, 'str']
print_params(*values_list_2, 42)