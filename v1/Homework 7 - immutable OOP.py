class Person:

    def __init__(self, name, last_name):
        self.__name = name
        self.__last_name = last_name

    # output to string
    def __str__(self):
        return str(self.__name + ' ' + self.__last_name)

    # method for updating object data
    def update(self, name, last_name):
        self.__name = name
        self.__last_name = last_name
        return self.__name, self.__last_name


student = Person('John', 'Travolta')  # create object
print(student)
print(id(student))
print(hash(student))

student.update('James', 'Bond')  # updating object data
print(student)
print(id(student))
print(hash(student))

student = Person('Otto', 'Bismark')  # new object
print(student)
print(id(student))
print(hash(student))
