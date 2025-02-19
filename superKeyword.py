# class parent_class:
#     def parent_method(self):
#         print("This is the parent method")

# class child_class(parent_class):
#     def child_method(self):
#         print("This is the child method.")
#         super().parent_method()

# child_object = child_class()
# child_object.child_method()

class parent_class1:
    def parent_method(self):
        print("This is the parent1 method")
        

class parent_class2:
    def parent_method(self):
        print("This is the parent2 method")

class child_class(parent_class1,parent_class2):
    def child_method(self):
        print("This is the child method.")
        super().parent_method()

child_object = child_class()
child_object.child_method()