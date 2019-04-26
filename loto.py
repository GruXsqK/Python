
__author__ = 'Белинский Андрей Петрович'

"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87      
      16 49    55 77    88    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html

"""

import random
import re


class Ticket:
    width_ticket = 26

    def __init__(self):
        self.__num_ticket = set()
        self.line1 = self.__generate_line()
        self.line2 = self.__generate_line()
        self.line3 = self.__generate_line()

    def __str__(self):
        return f'{self.line1}\n{self.line2}\n{self.line3}\n'

    def __generate_nums(self):
        tmp_lst = []
        while len(tmp_lst) < 5:
            elm = random.randint(1, 90)

            if elm not in self.__num_ticket:
                tmp_lst.append(elm)
                self.__num_ticket.add(elm)
        return tmp_lst

    def __generate_line(self):
        line = ''
        num_lst = self.__generate_nums()[:]
        blank = list('x' * 5 + ' ' * 10)
        random.shuffle(blank)

        for itm in blank:

            if itm == 'x':
                line += str(min(num_lst)) + ' '
                num_lst.remove(min(num_lst))
            else:
                line += ' '
        # для поиска по патерну
        line = ' ' + line + ' '
        return line.ljust(Ticket.width_ticket)

    def remove_number(self, numb_keg):

        if self.__remove_number_line(numb_keg, self.line1)[1]:
            self.line1 = self.__remove_number_line(numb_keg, self.line1)[0]
            return True
        elif self.__remove_number_line(numb_keg, self.line2)[1]:
            self.line2 = self.__remove_number_line(numb_keg, self.line2)[0]
            return True
        elif self.__remove_number_line(numb_keg, self.line3)[1]:
            self.line3 = self.__remove_number_line(numb_keg, self.line3)[0]
            return True
        else:
            return False

    @staticmethod
    def __remove_number_line(numb_sch, line):
        patern = re.compile('\D(' + str(numb_sch) + ')\D')
        s_char = patern.search(line)

        if s_char:

            if len(str(numb_sch)) == 1:
                patern2 = ' - '
            else:
                patern2 = ' -- '

            line = patern.sub(patern2, line)
            line.ljust(Ticket.width_ticket)
            return line, True
        else:
            return line, False

    def check_ticket(self):
        full_line = self.line1 + self.line2 + self.line3
        res = re.findall(r'\d', full_line)

        if any(res):
            return True
        else:
            return False


user = Ticket()
comp = Ticket()
keg_set = [_ for _ in range(1, 91)]

while any(keg_set):
    keg = random.choice(keg_set)
    keg_set.remove(keg)
    user_str = ' Ваша карточка '
    comp_str = ' Карточка компьютера '
    print(f'Новый бочонок: {keg} (осталось {len(keg_set)})\n')
    print(user_str.center(Ticket.width_ticket, '-') + '\n', user, '-' * Ticket.width_ticket)
    print(comp_str.center(Ticket.width_ticket, '-') + '\n', comp, '-' * Ticket.width_ticket)
    ans = input('Зачеркнуть цифру? (y/n)\n')
    key = user.remove_number(keg)

    if ans.lower() == 'y':
        if not key:
            print('Вы проиграли, {} нет в билете'.format(keg))
            break
    else:
        if key:
            print('Вы проиграли, {} есть в билете'.format(keg))
            break

    if not user.check_ticket():
        print('Поздравляем, Вы выиграли!')
        break

    comp.remove_number(keg)

    if not comp.check_ticket():
        print('Вы проиграли, Ваш соперник закрыл все числа')
        break

    print('#' * 30 + '\n')
