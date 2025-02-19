# a=1
# b=2
# c=3
# d=4
# ans = a if(a>b and a>c and a>d) else b if(b>c and b>d) else c if(c>d) else d
# print(ans)


# name = "kundanika madireddy"
# ans = name.split("a")
# print(ans)


# a = ["kun","dan","ika"]
# ans = "".join(a)
# print(ans)


# a = "kundan is a very very good girl"
# arr = a.split(" ")
# ans = []
# for i in arr:
#     b =""
#     for j in range(len(i)):
#         if(j==0 or j==len(i)-1):
#             b+=i[j].upper()
#         else:
#             b+=i[j]
#     ans.append(b)
# print(" ".join(ans))


# name = "prepinsta"
# ans = name[0].upper()+name[1:len(name)-1]+name[-1].upper()
# print(ans)

st="prep insta"
ar=st.split(" ") # ["prep","insta"]
for i in range(len(ar)):
    ar[i]= ar[i].replace(ar[i][0],ar[i][0].upper())
    ar[i]=ar[i].replace(ar[i][-1],ar[i][-1].upper())

print(" ".join(ar))