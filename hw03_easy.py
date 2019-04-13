
__author__ = 'Белинский Андрей Петрович'

# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    x = round(number, ndigits)
    return x

print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    ticket = str(ticket_number)
    if len(ticket) == 6:
        if sum(map(int, ticket[:3])) == sum(map(int, ticket[3:])):
            message = 'Билет № {} счастливый'.format(ticket_number)
        else:
            message = 'Билет № {} не счастливый'.format(ticket_number)
    else:
        message = 'Номер билета неверный'
    return message

print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
