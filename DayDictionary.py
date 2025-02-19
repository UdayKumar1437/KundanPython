my_data = {
    "name":"Kundanika",
    "age" : 18,
    "Graduated":False,
    "key":"value"
}

# print(type(my_data))
# my_data["age"] = 20
# my_second = my_data.copy()
# print(my_data.get("name","NA"))
# print(my_data.items())
# print(my_data.keys())
# print(my_data.values())

# rest_info = {
#     "lastName" : "Madireddy",
#     "middleName":""
# }
# my_data.update(rest_info)
# my_data.pop("Graduated")
# my_data.popitem()
# print(my_data)


# arr = "kundanika"
# ans ={}
# for i in arr:
#     if i not in ans.keys():
#         ans[i] = 1
#     else:
#         ans[i] = ans.get(i)+1
# print(ans)

# num = 1202010
# strNum = str(num)

# print(strNum.replace("0","1"))

# ans =""
# for i in strNum:
#     if i != "0":
#         ans+=i
#     else:
#         ans+="1"
# print(int(ans))

# name = "Kundanika madireddy"
# ans = ""
# for i in name:
#     if i != " ":
#         ans+=i
# print(ans)

# a = [1,1,2,3,3]
# ans = []
# for i in a:
#     if i not in ans:
#         ans.append(i)
# print(len(ans))

# def factors(num):
#     # return [i for i in range(1,num+1) if num%i ==0]
#     ans = []
#     for i in range(1,num+1):
#         if(num%i ==0):
#             ans.append(i)
#     return ans
# arr = [10,12,16,110,100]
# new_arr = list(set(arr))
# ans = {}
# for i in arr:
#     ans[i] = factors(i)
# print(ans)

