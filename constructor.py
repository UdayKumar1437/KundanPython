# Contructor

'''
A constructor is a special method in a class used to create and initialze an object of a class. There are differennt ypes of constructor. Constructor is invoked automatically when an object of a class is created.

A constructor is a unique function that gets called automatically when an object is created of a class.The main purpose of a constructor is to initilize or assign values of the data members of that class. It cannot return any value other than None.

'''

# def __init__(self):
#     #Body

'''
Types of Constructors in Python
Parametrized Constructor
Default Constructor
'''


# class Details:

#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def __init__(self):
#         print("Hiiiiiiiiiiiii")
#     def get_info(self):
#         print(f"Hey I'm {self.name} and I'm {self.age} years old.")

# obj1 = Details("Uday Kumar",24)
# obj2 = Details("Kundanika",18)
# obj1.get_info()


class Person:
    def walk(self):
        print("I'm walking")
    def sleep(self):
        print("I'm sleeping")
kundan = Person()
kundan.sleep()
uday = Person()
uday.walk()