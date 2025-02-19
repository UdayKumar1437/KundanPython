# def myName():
#     print("Kundan")

# for i in range(1,1001):
#     myName()


# def myName(name):
#     print(f"Hi, {name}")

# myName("Kundan")
# myName("Uday")

# Armstrong Numbers between 1-1000

# def isArmstrongNumber(num):
#     strNum = str(num)
#     length = len(strNum)
#     sum = 0
#     for i in strNum:
#         sum = sum+int(i)**length
#     if(sum == num ):
#         print(f"{num} is an Armstrong Number")
# for i in range(1,1001):
#     isArmstrongNumber(i)

#Prime numbers between 1 - 2000


#Friendy Pair
# num1 = 6
# num2 = 28

# def Factors(num):
#     sum = 0
#     for i in range(1,num):
#         if(num%i == 0):
#             sum +=i
#     return num/sum

# if(Factors(num1) == Factors(num2)):
#     print(f"{num1} and {num2} are Friendly Pairs")
# else:
#     print(f"{num1} and {num2} are not friendly Pairs")

# def add(num1,num2=3):
#     # print(num1+num2)
#     return num1+num2
# print(add(1,5))


for i in range(1,4):
    print(i*"*")