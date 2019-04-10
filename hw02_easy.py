
__author__ = 'Белинский Андрей Петрович'

# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

fruts = ['яблоко', 'банан', 'киви', 'арбуз', 'груша', 'апельсин', 'ананас']

max_string = []
i = 0

while i < len(fruts):
    if len(max_string) < len(fruts[i]):
        max_string = fruts[i]
    i += 1

for idx, value in enumerate(fruts, start=1):
    item_string = '{}{:>}'.format(' '*(len(max_string) - len(value)), value)
    print('{}. {}'.format(idx, item_string))

print()

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

random_list1 = [1, 2, 'a', 'b', 3, 'c'] * 4
random_list2 = ['a', 'c', 2] * 4

for itm in random_list2:
    while itm in random_list1:
        random_list1.remove(itm)

print(random_list1)
print()

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

int_list = [1, 5, 6, 8, 9, 15, 3, 10, 7, 11, 14]
new_list = []

for value in int_list:
    if value % 2:
        new_list.append(value * 2)
    else:
        new_list.append(value / 4)

print(new_list)