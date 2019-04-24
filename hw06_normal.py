# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.


class People:
    all_class = set()

    def __init__(self, surname, name, patronymic, class_room):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.class_room = class_room
        People.all_class.update(set(class_room.split()))

    def get_full_name(self):
        return self.surname + ' ' + self.name + ' ' + self.patronymic


class Student(People):
    def __init__(self, surname, name, patronymic, class_room,
                 f_name, f_patronymic,
                 m_name, m_patronymic):
        People.__init__(self, surname, name, patronymic, class_room)
        self.f_name = f_name
        self.f_patronymic = f_patronymic
        self.m_name = m_name
        self.m_patronymic = m_patronymic

    def get_parents_names(self):
        return self.surname + ' ' + self.f_name + ' ' + self.f_patronymic + ' и ' + \
               self.surname + ' ' + self.m_name + ' ' + self.m_patronymic


class Teacher(People):
    __all_subjects = set()

    def __init__(self, surname, name, patronymic, school_subject, class_room):
        People.__init__(self, surname, name, patronymic, class_room)

        if school_subject not in Teacher.__all_subjects:
            self.school_subject = school_subject
            Teacher.__all_subjects.add(school_subject)
        else:
            self.school_subject = None

        self.class_room = set([itm for itm in class_room.split()])

    def get_teacher_workload(self):
        return str(self.school_subject) + ' ' + str(self.class_room)

    def add_class_room(self, new_class_room):
        self.class_room.update(set([itm for itm in new_class_room.split()]))

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе


def get_students_in_class_room(class_room):
    students_list = []
    n = 10
    i = 1
    while i <= n:
        stud_num = 'stud' + str(i)
        if eval(stud_num).class_room == class_room:
            students_list.append(eval(stud_num).surname + ' ' + eval(stud_num).name[0]
                                 + '. ' + eval(stud_num).patronymic[0] + '. ')
        i += 1
    return students_list


def get_students_subject(stud_num):
    stud_name = stud_num.get_full_name()
    stud_class = stud_num.class_room
    students_subject = []
    n = 5
    i = 1
    while i <= n:
        teacher_num = 'teacher' + str(i)
        if stud_class in eval(teacher_num).class_room:
            students_subject.append(eval(teacher_num).school_subject)
        i += 1
    return f'Список предметов {stud_name}: {students_subject}'


def get_teachers_in_class_room(class_room):
    teachers_list = []
    n = 5
    i = 1
    while i <= n:
        teacher_num = 'teacher' + str(i)
        if class_room in eval(teacher_num).class_room:
            teachers_list.append(eval(teacher_num).surname + ' ' + eval(teacher_num).name[0]
                                 + '. ' + eval(teacher_num).patronymic[0] + '.')
        i += 1
    return f'В классе {class_room} преподают: {teachers_list}'


stud1 = Student('Курбатов', 'Филипп', 'Иванович', '6А', 'Иван', 'Фомевич', 'Розалия', 'Романовна')
stud2 = Student('Хомколова', 'Агния', 'Несторовна', '6Б', 'Нестор', 'Кириллович', 'Фаина', 'Михеевна')
stud3 = Student('Кузуб', 'Карл', 'Матвеевич', '7А', 'Матвей', 'Антонов', 'Ксения', 'Давидовна')
stud4 = Student('Китаева', 'Стела', 'Иларионовна', '6А', 'Иларион', 'Брониславович', 'Розалия', 'Ильевна')
stud5 = Student('Гавриленкова', 'Клара', 'Ильевна', '6Б', 'Илья', 'Михеев', 'Ефросиния', 'Якововна')
stud6 = Student('Шепкин', 'Фока', 'Мирославович', '7А', 'Мирослав', 'Саввевич', 'Светлана', 'Игоревна')
stud7 = Student('Паршина', 'Берта', 'Павеловна', '6Б', 'Павел', 'Измаилович', 'Галина', 'Станиславовна')
stud8 = Student('Михайличенко', 'Евгения', 'Филипповна', '7А', 'Филипп', 'Сидорович', 'Вера', 'Родионовна')
stud9 = Student('Лобза', 'Агафон', 'Глебович', '7Б', 'Глеб', 'Модестович', 'Василиса', 'Семеновна')
stud10 = Student('Комягина', 'Арина', 'Геннадиевна', '7Б', 'Геннадий', 'Сергеевич', 'Юнона', 'Романовна')

teacher1 = Teacher('Яковиченко', 'Василиса', 'Михеевна', 'русский язык', '6А 6Б 7А 7Б')
teacher2 = Teacher('Шаронова', 'Ариадна', 'Степановна', 'математика', '6А 6Б 7А 7Б')
teacher3 = Teacher('Тукай', 'Ефросинья', 'Тимуровна', 'физика', '6А 6Б')
teacher4 = Teacher('Летова', 'Берта', 'Филипповна', 'химия', '7А 7Б')
teacher5 = Teacher('Антиповский', 'Анатолий', 'Карлович', 'физкультура', '6А 6Б')

print('Список всех классов:', *People.all_class)
print('Список учеников в указанном классе:', *get_students_in_class_room('7А'))
print(get_students_subject(stud5))
print('Родители: ' + stud3.get_parents_names())
print(get_teachers_in_class_room('7Б'))
