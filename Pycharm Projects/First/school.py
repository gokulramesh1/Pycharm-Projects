class Person:

    def __init__(self, first, last):
        self.firstName = first
        self.lastName = last

    def say_hi(self):
        print(f"Hello {self.firstName} {self.lastName}!")

    def __repr__(self):
        return f"{self.firstName} {self.lastName}"


class Student(Person):

    def __init__(self, first, last, school, std, section):
        super().__init__(first, last)
        super().say_hi()
        self.school = school
        self.std = std
        self.section = section
        self.school.classes[self.std - 1][ord(self.section) - 65].students.append(self)
        self.marks = {}

    subjects = ['Math', 'Physics', 'Biology', 'Chemistry', 'Social Science', 'Computers']

    def get_marks(self):
        print("Enter your marks:")
        for subject in self.subjects:
            self.marks[subject] = input(f"{subject}: ")


class Class:

    def __init__(self, std, section):
        self.std = std
        self.section = section
        self.students = []

    def __repr__(self):
        return f"{self.std}{self.section}"


class School:
    standards = list(range(1, 13))
    sections = ['A', 'B', 'C']

    def __init__(self):
        self.teachers = []
        self.classes = []

        for standard in self.standards:
            classes = []
            for section in self.sections:
                classes.append(Class(standard, section))
            self.classes.append(classes)

    def show_classes(self):
        print([s.classes[x][y].students for x in range(len(self.classes)) for y in range(len(self.classes[x]))])


class Teacher(Person):

    def __init__(self, first, last, school, *subjects):
        super().__init__(first, last)
        super().say_hi()
        self.school = school
        self.subjects = [subject for subject in subjects]
        self.classes = {}

    def get_classes(self):
        for subject in self.subjects:
            self.classes[subject] = []
            print(f"Which classes do you teach {subject} for?")
            while True:
                c = input()
                if c:
                    self.classes[subject].append(c)
                else:
                    break


s = School()
print(s.classes)
bob = Student('Bob', 'Hope', s, 4, 'B')
s.show_classes()
mary = Teacher('Mary', 'Adams', s, 'Math', 'Physics')
mary.get_classes()
print(mary.classes)
