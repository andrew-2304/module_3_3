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
