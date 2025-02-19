# my_set = set()
# # print(type(my_set))
# my_set.add(1)
# my_set.add(1)
# my_set.add(2)
# my_set.clear()
# print(my_set)

# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}

# ans = x.difference(y)
# print(x)
# print(ans)

# x.difference_update(y)
# print(x)
# x.discard("banana")
# print(x)

# ans = x.intersection(y)
# print(ans)

# x.intersection_update(y)
# print(x)

# ans = x.isdisjoint(y)
# print(ans)

# x = {"a", "b", "c"}
# y = {"f", "e", "d", "c", "b", "a"}

# ans = x.issubset(y)
# print(ans)

# ans = y.issuperset(x)
# print(ans)

# x.pop()
# print(x)

# x.remove("a")
# print(x)

# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
# ans = x.symmetric_difference(y)
# print(ans)

# y.symmetric_difference_update(x)
# print(y)

# ans = x.union(y)
# print(ans)

# x.update({"Kundan","Uday"})
# print(x)


# arr = [1,1,2,3,4,4,3]
# print(list(set(arr)))

# num1 = 36
# num2 = 60
# ans = 1
# for i in range(2,min(num1,num2)+1):
#     if(num1%i ==0 and num2%i==0):
#         ans = i
# print(ans)


radius = 25
ans = 3.14*(radius**2)
print(ans)