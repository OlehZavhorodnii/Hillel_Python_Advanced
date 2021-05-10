
class Person:

    def __init__(self, name, last_name):
        self.__name = name
        self.__last_name = last_name

    def __str__(self):
        return str(self.__name + ' ' + self.__last_name)


student = Person('John', 'Palmer')
print(student)
print(id(student))
print(hash(student))

student = Person('Will', 'Smith')
print(student)
print(id(student))
print(hash(student))
