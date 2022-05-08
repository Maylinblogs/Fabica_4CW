class Person:

    # initialization or constructor method of
    def __init__(self):
        # class Student
        self.name = input('enter student name:')
        self.surname = input('enter student surname:')
        self.patronymic = input('enter patr:')
        self.number = input('enter number')

    def get_name(self):
        return self.name

    def get_surname(self):
        return self.surname

    def get_patronymic(self):
        return self.patronymic

    def get_number(self):
        return self.number

