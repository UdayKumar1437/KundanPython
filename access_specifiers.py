#Public Access Modifier

# class Student:
#     def __init__(self,age,name):
#         self.age = age
#         self.name = name

# obj = Student("kundan",18)
# print(obj.age)
# print(obj.name)


# Private Access Modifier
# class Student:
#     def __init__(self,name,age):
#         self.__age = age
    
#     def getAge(self):
#         print(self.__age)
#     def __function(self):
#         self.y = 25
#         print(self.y)

# class Subject(Student):
#     pass

# obj = Student("kundan",18)
# obj1 = Subject("Uday",24)

# obj.getAge()


# class Student:
#     def __init__(self,name,age):
#         self._age = age

# class Subject(Student):
#     pass

# obj = Subject("kundan",18)
# print(obj._age)