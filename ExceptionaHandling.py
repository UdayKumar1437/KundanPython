# try:
#     a = int(input("Enter a Number: "))
#     b = int(input("Enter a Number: "))
#     print(a+b)
# except:
#     print("There is an error in code.")
# else:
#     print("I am going to execute if there is no errors in the code.")
# finally:
#     print("I'm Sittayyaaa")

# try:
#     # a = 10
#     # print(a/0)
#     a = [1,2,4]
#     print(a[10])
# except ZeroDivisionError:
#     print("Error")
# except SyntaxError:
#     print("Syntax Error")
# except IndexError:
#     print("IndexError")
# except:
#     print("I catch everything!!!.")


# salary = int(input("Enter your salary: "))
# if salary<5000:
#     raise ZeroDivisionError("Kundan wants more than 5000")
# else:
#     print("will execute without an error")

# def isPrime(num):
#     try:
#         count = 0
#         for i in range(2,num):
#             if(num%i ==0):
#                 count+=1
#         return count ==0
#     except NameError:
#         return "Error Occured"
# print(isPrime(4))

# try:
#     a = [1,2,34,1,2,3,4,"jgkfjs"]
#     sum =0
#     for i in a:
#         if(type(i) == int):
#             sum+=i
#     print(sum)
# except:
#     print("Error Occured!")

num = 376
square_of_num = num*num
l = len(str(num))
if(int(str(square_of_num)[len(str(square_of_num))-len(str(num)):])==num):
    print("AutoMorphic Number")
else:
    print("Not an Automorphic Number")

