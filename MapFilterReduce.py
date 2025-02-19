# numbers = [1,2,3,4,5,6]

# def square(num):
#     return num*num
# ans = map(square,numbers)
# print(list(ans))

# name = input()
# print(name.split())

# nums = list(map(int,input().split()))
# print(nums)


# Filter

# nuumbers = [1,2,3,4,5,6,7,8]
# ans = []
# for i in nuumbers:
#     if i%2 ==0:
#         ans.append(i)

# def isEven(num):
#     return num%2==0

# evens = filter(isEven,nuumbers)
# evens = filter(lambda x : x%2==0,nuumbers)
# print(list(evens))

from functools import reduce
# Reduce
nums = [1,2,3,4,5,6,7,8]
# ans = 0
# for i in nums:
#     ans +=i
# print(ans)

ans = reduce(lambda x,y : x+y,nums)
print(ans)




