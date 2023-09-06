class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, mark):
        if isinstance(lecturer, Lecturer) and (course in self.courses_in_progress or course in self.finished_courses):
            if 0 < mark <= 10:
                lecturer.marks[course] = mark
        else:
            return 'Ошибка'

    def average_student_grate(self):
        summa = 0
        for grade in self.grades.values():
            summa += grade
        return summa/len(self.grades.items())



    def __str__(self):
        return (f'Имя: {self.name} \nФамилия: {self.surname} '
                f'\nСредняя оценка за домашние задания: {self.average_student_grate()} '
                f'\nКурсы в процессе изучения: {"".join(self.courses_in_progress)} '
                f'\nЗавершенные курсы: {"".join(self.finished_courses)}').format(self=self)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.marks = {}

    def __str__(self):
        return (f'Имя:{self.name} '
                f'\nФамилия: {self.surname} '
                f'\nСредняя оценка за лекции: {self.average_lecturer_grate()}').format(self=self)

    def average_lecturer_grate(self):
        summa = 0
        for mark in self.marks.values():
            summa += mark
        return summa / len(self.marks.items())


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_student(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached:
            if course in student.courses_in_progress:
                student.grades[course] = grade

        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя:{self.name} \nФамилия:{self.surname}'.format(self=self)

def average_rating(student_list, course_name):
    grades_sum = 0
    counter = 0
    for student in student_list:
        if course_name in student.grades.keys():
            grades_sum += student.grades[course_name]
            counter += 1
    return grades_sum/counter

def average_rating_lecturer(lecturer_list, course_name):
    marks_sum = 0
    counter = 0
    for lecturer in lecturer_list:
        if course_name in lecturer.marks.keys():
            marks_sum += lecturer.marks[course_name]
            counter += 1
    return marks_sum/counter




best_student = Student('Ruoy', 'Eman', 'male')
best_student.courses_in_progress += ["Python"]
best_student.finished_courses.append('Java')

reviewer_1 = Reviewer('Lauri', 'Korhonen')
reviewer_1.courses_attached += ["Python"]
reviewer_1.rate_student(best_student, "Python", 10)

lecturer_1 = Lecturer('Ville', 'Lautanen')
lecturer_1.courses_attached.append('Python')

best_student.rate_lecturer(lecturer_1,'Python', 9)

worst_student = Student('Laura', 'Virtanen', 'female')
worst_student.courses_in_progress.append('Python')
worst_student.finished_courses.append('JS')

reviewer_2 = Reviewer('Marja', 'Vanamo')
reviewer_2.courses_attached.append('Python')
reviewer_2.rate_student(worst_student, 'Python', 2)

lecturer_2 = Lecturer('Noel', 'Tuominen')
lecturer_2.courses_attached.append('Python')

worst_student.rate_lecturer(lecturer_2,'Python', 7)

average_rating([best_student, worst_student], 'Python')
average_rating_lecturer([lecturer_1, lecturer_2], 'Python')



