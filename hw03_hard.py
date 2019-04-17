
__author__ = 'Белинский Андрей Петрович'

# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3

def fractions_calc(fr_string):

    def improper_fraction(frac):
        frac_tuple1 = frac.partition('/')

        if not frac_tuple1[1]:
            denominator = 1
            imp_numerator = int(frac_tuple1[0])
        else:
            denominator = int(frac_tuple1[2])
            frac_tuple2 = frac_tuple1[0].rpartition(' ')

            if frac_tuple2[0]:
                number = int(frac_tuple2[0])
            else:
                number = 0

            if number < 0:
                num_sig = -1
            else:
                num_sig = 1

            numerator = int(frac_tuple2[2])
            imp_numerator = (numerator + abs(number) * denominator) * num_sig

        return imp_numerator, denominator


    def summ_diff_fraction(frac_1, frac_2, sigil):

        gen_den = min(frac_1[1], frac_2[1])
        while True:
            if not gen_den % frac_1[1] and not gen_den % frac_2[1]:
                break
            gen_den += 1

        numer_res1 = int(gen_den / frac_1[1] * frac_1[0])
        numer_res2 = int(gen_den / frac_2[1] * frac_2[0])

        if sigil == '+':
            frac_res = numer_res1 + numer_res2, gen_den,
        else:
            frac_res = numer_res1 - numer_res2, gen_den,

        return frac_res


    frac_list = fr_string.partition(' + ')
    if frac_list[1]:
        sigil = '+'
    else:
        frac_list = fr_string.partition(' - ')
        sigil = '-'

    frac_1 = improper_fraction(frac_list[0])
    frac_2 = improper_fraction(frac_list[2])
    res_imp_frac = summ_diff_fraction(frac_1, frac_2, sigil)
    res_denominator = res_imp_frac[1]

    if res_imp_frac[0] < 0:
        sig_frac = -1
    else:
        sig_frac = 1

    res_fraction = divmod(abs(res_imp_frac[0]), res_denominator)
    res_number = res_fraction[0] * sig_frac
    res_numerator = res_fraction[1]

    com_factor = res_denominator
    while com_factor > 0:
        if not res_numerator % com_factor and not res_denominator % com_factor:
            res_denominator = int(res_denominator / com_factor)
            res_numerator = int(res_numerator / com_factor)
            break
        com_factor -= 1

    if not res_number and not res_numerator:
        return '{} = 0'.format(fr_string)
    elif not res_number:
        res_numerator *= sig_frac
        return '{} = {}/{}'.format(fr_string, res_numerator, res_denominator)
    elif not res_numerator:
        return '{} = {}'.format(fr_string, res_number)
    else:
        return '{} = {} {}/{}'.format(fr_string, res_number, res_numerator, res_denominator)
    
print(fractions_calc('-2 4/14 + 1 3/4'))
print()

# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

import os

path_workers = os.path.join('data', 'workers')
path_hours = os.path.join('data', 'hours_of')
path_payroll = os.path.join('data', 'payroll')
workers_list = []
hours_list = []
payroll_list = [['Имя', 'Фамилия', 'Зарплата', 'Отработано_часов']]

with open(path_workers, 'r', encoding='UTF-8') as file_workers:
    for line in file_workers:
        worker = list(filter(None, line.split(' ')))
        workers_list.append(worker)

with open(path_hours, 'r', encoding='UTF-8') as file_hours:
    for line in file_hours:
        hours = list(filter(None, line.split(' ')))
        hours_list.append(hours)

for ind_w in range(1, len(workers_list)):
    for ind_h in range(1, len(hours_list)):

        if workers_list[ind_w][:2] == hours_list[ind_h][:2]:
            norm = int(workers_list[ind_w][4])
            w_hours = int(hours_list[ind_h][2])
            salary = int(workers_list[ind_w][2])

            if norm == w_hours:
                pay = round(salary)
            elif norm < w_hours:
                pay = round(salary + (salary / norm) * (w_hours - norm) * 2)
            else:
                pay = round(salary - (salary / norm) * (norm - w_hours))

            hours_str = hours_list[ind_h][2]
            worker_payroll = [workers_list[ind_w][0], workers_list[ind_w][1], str(pay), hours_str[0:3]]
            payroll_list.append(worker_payroll)

with open(path_payroll, 'w', encoding='UTF-8') as file_payroll:
    for line in range(len(payroll_list)):
        for idx in range(len(payroll_list[line])):
            value = payroll_list[line][idx].ljust(9)
            file_payroll.write(value)
        file_payroll.write('\n')

# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))
