immutable_var = (1, 2, 3, 'мяч', True)
print(immutable_var)
# immutable_var[2] = 4
# immutable_var[2] = 'шайба' - операции изменения элементов невыполнимы, т.к. кортеж не поддерживает обращение
# по элементам. Неизменяемые типы, такие как числа или строки не могут быть модифицированы. Содержимое элементов
# изменяемого типа,таких как списки, может быть изменено с помощью такого обращения, но хранящаяся в структуре кортежа
# ссылка на модифицированный объект останется неизменной, содержимое кортежа сохраняется.
# print(immutable_var) - результат попытки исполнения - ошибка типа "'tuple' object does not support item assignment"

mutable_list = [1, 3, 5, 'тюлень', False]
mutable_list[2] = 7
mutable_list[3] = 'морж'
print(mutable_list)
