class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lec(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def avg_grades_hm(self, grades):
        return map(lambda grade: sum(grade) / len(grade), grades)

    def __str__(self):
        return f'Имя:{self.name}, Фамилия:{self.surname}, Средняя оценка за домашнее задание:{self.avg_grades_hm}' \
               f', Курсы в прцоессе изучения:{self.courses_in_progress}, {self.finished_courses}'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f'Имя:{self.name}, фамилия:{self.surname}'

class Lecturer(Mentor):
    grades = {}
    def avg_grades_lec(self, grades):
        return map(lambda grade: sum(grade) / len(grade), grades)



    def __str__(self):
        return f'Имя:{self.name}, Фамилия:{self.surname}, Средняя оценка за лекции:{self.avg_grades_lec}'


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)

print(best_student.grades)