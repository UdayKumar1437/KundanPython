# arr = [1,2,3,4]
# # [ value to be stored for loop constional statement ]

# ans = [ i*2 for i in arr if i%2 ==0 ]
# print(ans)


# arr = ["dad","Mom","jajdgakhd","Kundan","levEl"]
# ans = [x for x in arr if x.lower() == x.lower()[::-1]]
# print(ans)


keys = ["uday","kundan"]
values = [23,56]
myDict = {
    key:value for (key,value) in zip(keys,values) if key =="uday"
}
print(myDict)