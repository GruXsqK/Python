
__author__ = 'Белинский Андрей Петрович'

# Задание-1: Решите задачу (дублированную ниже):

# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки они получают
# удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

# С использованием классов.
# Реализуйте классы сотрудников так, чтобы на вход функции-конструктора
# каждый работник получал строку из файла


import os


class Workers:
    def __init__(self, line_data):
        self.line_data = line_data.split()
        self.name = self.line_data[0]
        self.surname = self.line_data[1]
        self.salary = int(self.line_data[2])
        self.position = self.line_data[3]
        self.norm = int(self.line_data[4])
        self.hours = int(self.line_data[5])

    def payroll(self):
        if self.norm == self.hours:
            payroll = self.salary
        elif self.norm > self.hours:
            payroll = round(self.salary - (self.salary / self.norm) * (self.norm - self.hours))
        else:
            payroll = round(self.salary + (self.salary / self.norm) * (self.hours - self.norm) * 2)

        return payroll


def worker_data(name, surname):
    with open(os.path.join('data', 'workers'), 'r', encoding='UTF-8') as file_workers:
        for line in file_workers:
            tmp = line.split()
            if name == tmp[0] and surname == tmp[1]:
                worker_data = line

    with open(os.path.join('data', 'hours_of'), 'r', encoding='UTF-8') as file_hours:
        for line in file_hours:
            tmp = line.split()
            if name == tmp[0] and surname == tmp[1]:
                worker_full_data = worker_data + ' ' + tmp[2]
    return worker_full_data


worker1 = Workers(worker_data('Петр', 'Дурин'))
print('Заработная плата:', worker1.payroll())
