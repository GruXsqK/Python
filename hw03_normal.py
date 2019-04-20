
__author__ = 'Белинский Андрей Петрович'

# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    if n < 1:
        return 'n должно быть больше 1'
    else:
        fib = [0, 1]
        for i in range(2, m + 1):
            fib.append(fib[i - 1] + fib[i - 2])
        fib_n_m = fib[n:m+1]
        return fib_n_m

print(fibonacci(1,10))
print()

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

def sort_to_max(origin_list):
    stop_list = len(origin_list) - 1
    while True:
        for i in range(stop_list):
            if origin_list[i + 1] < origin_list[i]:
                origin_list[i + 1], origin_list[i] = origin_list[i], origin_list[i + 1]
        if stop_list <= 0:
            break
        stop_list -= 1
    return origin_list

print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))
print()

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def my_filter(func, item):

    new_item = [elem for elem in item if func(elem)]
    if type(item) is tuple:
        new_item = tuple(new_item)
    if type(item) is set:
        new_item = set(new_item)
    if type(item) is str:
        new_item = ''.join(new_item)
    return new_item

print(my_filter(lambda x: x <= 0, [2, 10, -12, 2.5, 20, -11, 4, 4, 0] ))
print()

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

def pgram(a, b, c, d):

    def paral(a, b, c, d):
        ab = ((b[0] - a[0])**2 + (b[1] - a[1])**2)**0.5
        cb = ((b[0] - c[0])**2 + (b[1] - c[1])**2)**0.5
        cd = ((d[0] - c[0])**2 + (d[1] - c[1])**2)**0.5
        ad = ((d[0] - a[0])**2 + (d[1] - a[1])**2)**0.5

        if ab == cd and cb == ad:
            return True
        else:
            return False

    def diag(a, b, c, d):

        h_o1 = ((a[0] + c[0])/2, (a[1] + c[1])/2)
        h_o2 = ((b[0] + d[0])/2, (b[1] + d[1])/2)

        if h_o1 == h_o2:
            return True
        else:
            return False

    if paral(a, b, c, d) and diag(a, b, c, d):
        print('Вершины A1{}, A2{}, A3{}, A4{} являются параллелограммом'.format(a, b, c, d))
    else:
        print('Точки не являются вершинами параллелограмма')

pgram([-4, -2], [-3, 2], [7, -1], [6, -5])