# Break and Continue
# for i in range(1,11):
#     print(i)
#     if i == 5:
#         break

# for i in range(1,11):
#     if(i ==4 or i ==5):
#         continue
#     print(i)


# num = int(input("Enter a Number: "))
# for i in range(1,13):
#     print(f"{num} X {i} = {num*i}")

#Armstrong
# num = int(input("Enter a Number: ")) #371
# strNum = str(num) #"371"
# length = len(strNum) # 3
# sum = 0
# for i in strNum:
#     sum = sum+int(i)**length
# print(sum)
# if(sum == num):
#     print(f"{num} is an Armstrong Number")
# else:
#     print(f"{num} is not an Armstrong Number")

# Strong Number
# num = int(input("Enter a Number"))
# strNum = str(num)
# sum = 0
# for i in strNum:
#     factAns = 1
#     for j in range(1,int(i)+1):
#         factAns = factAns*j
#     sum = sum+factAns
# print(sum)
# if(sum == num):
#     print(f"{num} is an Strong Number")
# else:
#     print(f"{num} is not an Strong Number")

# Perfect Number
num = int(input("Enter a Number: "))
sum = 0
for i in range(1,num):
    if (num%i == 0):
        sum = sum+i
if(sum == num):
    print(f"{num} is an Perfect Number")
else:
    print(f"{num} is not an Perfect Number")