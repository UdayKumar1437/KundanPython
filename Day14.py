# list1 = [1,2,3,2,3,2,2,1]
# list2 = ["Red","yellow","green","yellow","green","yellow","green"]
# list3 = [1,2,1,4.3,True,[1,2,[1,2]],False]

# print(type(list3))


# a = [1,2,3]
# a.append(4)
# print(a)
# a.clear()
# print(a)

# a = [1,2,3,4]
# b = a.copy()
# a.append(1)
# print(b)

# a = [1,2,1,2,3,1,2,1,1,1]
# ans = a.count(1)
# print(ans)

# a = [1,2]
# a.append(3)
# a.append(4)
# a.append(5)
# a.extend([3,4,5])
# print(a)

# a = [1,2,1,2,3,1,2,1,1,1]
# ans = a.index(3)
# print(ans)

# a = [1,2,4]
# a.insert(2,3)
# print(a)

# a=[2,1,2,3,4,5]
# a.pop(0)
# a.pop(0)
# print(a)

# a = [2,1,2,3,4,5]
# a.remove(2)
# print(a)

# a = [2,1,2,3,4,5]
# a.sort() #[1,2,2,3,4,5]
# a.reverse() #[5,4,3,2,2,1]
# print(a)


# a = [1,2,3,4,5,5,66,5,5,5,55,5,5,55,5,5,55,5,55,5]
# ans = sum(a)
# ans = max(a)
# ans = min(a)
# print(ans)


a = [1,22,541,3,6]
maxi = a[0]
for i in a:
    if(i>maxi):
        maxi = i
print(maxi)