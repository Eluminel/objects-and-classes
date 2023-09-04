class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def lecturer_rate(self, lecturer, course, mark):
        if isinstance(lecturer, Lecturer) and (course in self.courses_in_progress or course in self.finished_courses):
            if course in lecturer.marks and 0 < mark <= 10:
                lecturer.marks[course] += [mark]
            else:
                lecturer.marks[course] = [mark]
        else:
            return 'Ошибка'
    def __str__(self):
        return f'Имя:{self.name}'.format(self=self)
        return f'Фамилия:{self.surname}'.format(self=self)
        return f'Средняя оценка за домашние задания:{self.grades}'.format(self=self)
        return f'Курсы в процессе изучения:{self.courses_in_progress}'.format(self=self)
        return f'Завершенные курсы:{self.finished_courses}'.format(self=self)

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self):
        self.marks = {}

    def __str__(self):
        return f'Имя:{self.name}'.format(self=self)
        return f'Фамилия:{self.surname}'.format(self=self)
        return f'Средняя оценка за лекции:{self.marks}'.format(self=self)


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя:{self.name}'.format(self=self)
        return f'Фамилия:{self.surname}'.format(self=self)


# best_student = Student('Ruoy', 'Eman', 'your_gender')
# best_student.courses_in_progress += ['Python']
#
# cool_mentor = Mentor('Some', 'Buddy')
# cool_mentor.courses_attached += ['Python']
#
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
#
# print(best_student.grades)