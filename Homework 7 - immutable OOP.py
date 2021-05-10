class Person:

    def __init__(self, name, last_name):
        self.__name = name
        self.__last_name = last_name


    def __str__(self):
        return str(self.__name + ' ' + self.__last_name)


student = Person('John', 'Travolta')
print(student)
print(id(student))
print(hash(student))

student = Person('Will', 'Jason')
print(student)
print(id(student))
print(hash(student))
