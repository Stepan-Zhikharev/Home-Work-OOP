class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __average_rating(self):
        count = 0
        total = 0
        for key, volue in self.grades.items():
            for grade in volue:
                count += 1
                total += grade
        if count <= 0 or total <= 0:
            return 0
        else:
            return round((total / count), 1)
    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {self.__average_rating()}\n'
                f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
                f'Завершенные курсы: {", ".join(self.finished_courses)}\n')
    def __lt__(self, other):
        return self.__average_rating() < other.__average_rating()
    def __le__(self, other):
        return self.__average_rating() <= other.__average_rating()
    def __eq__(self, other):
        return self.__average_rating() == other.__average_rating()
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
    def __average_rating(self):
        count = 0
        total = 0
        for key, volue in self.grades.items():
            for grade in volue:
                count += 1
                total += grade
        if count <= 0 or total <= 0:
            return 0
        else:
            return round((total / count), 1)
    def __lt__(self, other):
        return self.__average_rating() < other.__average_rating()
    def __le__(self, other):
        return self.__average_rating() <= other.__average_rating()
    def __eq__(self, other):
        return self.__average_rating() == other.__average_rating()
    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {self.__average_rating()}\n')
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
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n')


best_student = Student('Jon', 'Snow', 'your_gender')
best_student.courses_in_progress += ['Python', 'Git']
best_student.finished_courses += ['Основы языка программирования Python']
bad_student = Student('Ralf', 'Low', 'your_gender')
bad_student.courses_in_progress += ['Python', 'Git']
bad_student.finished_courses += ['Основы языка программирования Python']

cool_lecturer = Lecturer('Ban', 'Clon')
cool_lecturer.courses_attached += ['Python', 'Git']
good_lecturer = Lecturer('Severus', 'Snap')
good_lecturer.courses_attached = ['Python', 'Git']
good_reviewer = Reviewer('Jack', 'Teel')
good_reviewer.courses_attached += ['Python', 'Git']
cool_reviewer = Reviewer('Tom', 'Radl')
cool_reviewer.courses_attached += ['Python', 'Git']

best_student.rate_hw(cool_lecturer, 'Python', 9)
bad_student.rate_hw(cool_lecturer, 'Python', 7)
best_student.rate_hw(good_lecturer, 'Python', 8)
bad_student.rate_hw(good_lecturer, 'Python', 5)
good_reviewer.rate_hw(best_student, 'Python', 9)
good_reviewer.rate_hw(best_student, 'Git', 8)
good_reviewer.rate_hw(bad_student, 'Python', 3)
good_reviewer.rate_hw(bad_student, 'Git', 2)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Git', 10)
cool_reviewer.rate_hw(bad_student, 'Git', 4)
cool_reviewer.rate_hw(bad_student, 'Python', 5)
print(best_student)
print(bad_student)
print(cool_lecturer)
print(good_lecturer)
print(good_reviewer)
print(cool_reviewer)
print(best_student > bad_student)
print(cool_lecturer < good_lecturer)

list_students = [best_student, bad_student]
list_lecturer = [cool_lecturer, good_lecturer]

def average_student(students, course):
    total = []
    for student in students:
        total += student.grades[course]
    return round(sum(total) / len(total), 1)

def average_lecturer(lecturer, course):
    total = []
    for lector in lecturer:
        total += lector.grades[course]
    return round(sum(total) / len(total), 1)

print(average_student(list_students, 'Python'))
print(average_student(list_students, 'Git'))
print(average_lecturer(list_lecturer, 'Python'))