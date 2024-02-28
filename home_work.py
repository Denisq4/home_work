class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'ошибка'

    def get_average_grade_st(self):
        avg_grade = sum(self.grades.values()) / len(self.grades.values())
        return avg_grade

    def __str__(self):
        return f'имя: {self.name}\nфамилия: {self.surname}' \
               f'\nсредняя оценка за домашнее задание: {self.get_average_grade_st}\n' \
               f'курсы в прцоессе изучения: {", ".join(self.courses_in_progress)}' \
               f'\nзавершенные курсы: {self.finished_courses}'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f'имя: {self.name}\nфамилия: {self.surname}'


class Lecturer(Mentor):
    grades = {}
    def get_average_grade_lc(self):
        avg_grade = sum(self.grades.values()) / len(self.grades.values())
        return avg_grade

    def __str__(self):
        return f'имя: {self.name}\nфамилия: {self.surname}\nсредняя оценка за лекции: {self.get_average_grade_lc}'


class Reviewer(Mentor):
    def rate_homework(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            return 'ошибка'

    def __str__(self):
        return f'имя: {self.name}\nфамилия: {self.surname}'


class Comparisonn:
    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        return self.value < other.value


# экземпляр класса Reviewer №1
reviewer_1 = Reviewer('Дмитрий', 'Петров')
reviewer_1.courses_attached = 'Python'
# экземпляр класса Reviewer №2
reviewer_2 = Reviewer('Алексей', 'Дымченко')
reviewer_2.courses_attached = 'Java'
# экземпляр класса Lecturer №1
lecturer_1 = Lecturer('Басов', 'Александр')
lecturer_1.courses_attached = 'Python', 'Java'
# экземпляр класса Lecturer №2
lecturer_2 = Lecturer('Андрей', 'Селезнев')
lecturer_2.courses_attached = 'Java'
# экземпляр класса Student №1
student_1 = Student('Денис', 'Мокрецов', 'М')
student_1.courses_in_progress = 'Python', 'Java'
student_1.finished_courses = 'OOP Python'
# экземпляр класса Student №2
student_2 = Student('Юлия', 'Владиславовна', 'Ж')
student_2.courses_in_progress = 'Java', 'Python'
student_2.finished_courses = 'Java+'
# экземпляр класса Mentor №1
mentor_1 = Mentor('Евгений', 'Кожеватов')
mentor_1.courses_attached = 'Python'
# экземпляр класса Mentor №2
mentor_2 = Mentor('Михаил', 'Мартюшев')
mentor_2.courses_attached = 'Java'

reviewer_1.rate_homework(student_2, 'Java', '9')
reviewer_1.rate_homework(student_1, 'Python', '10')
student_1.rate_lecture(lecturer_1, 'Python', '8')
student_2.rate_lecture(lecturer_1, 'Java', '9')
print('Студенты')
print(student_1)
print(student_2)
print('--------------------------')
print('Лекторы')
print(lecturer_1)
print(lecturer_2)
print('--------------------------')
print('Ревьюверы')
print(reviewer_1)
print(reviewer_2)
print('-------------------------')
print('Менторы')
print(mentor_1)
print(mentor_2)

list_studentov = [student_1, student_2]
list_lecturer = [lecturer_1, lecturer_2]
list_course = ['Python', 'Java']
dict_grades = {'Python': [8, 9, 10, 5],
               'Java': [6, 4, 3, 10]}
def comparison(name_course, grades):
    avg = sum(grades[name_course]) / len(grades[name_course])
    return avg

b = comparison(list_course[1], dict_grades)
print(b)