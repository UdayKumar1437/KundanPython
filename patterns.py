# n =5
# for i in range(n):
#     print("*"*n)

# n = 5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()

# n = 5
# for i in range(1,n+1):
#     print("*"*i)
# for i in range(n-1,0,-1):
#     print("*"*i)

# n=5
# for i in range(1,2*n):
#     if i<=n:
#         for j in range(i):
#             print("*",end="")
#         print()
#     else:
#         for j in range(2*n-i):
#             print("*",end="")
#         print()


# n = 5
# for i in range(1,n+1):
#     start = 1 if i%2==1 else 0
#     for j in range(i):
#         print(start,end="")
#         start=1-start
#     print()

# n = 5
# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()

# n = 5
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end="")
#     for j in range((2*n-1)-((n-i)*2)):
#         print("*",end="")
#     for j in range(n-i):
#         print(" ",end="")
#     print()
# for i in range(n,0,-1):
#     for j in range(n-i):
#         print(" ",end="")
#     for j in range((2*n-1)-((n-i)*2)):
#         print("*",end="")
#     for j in range(n-i):
#         print(" ",end="")
#     print()


n=4
start = 1
for i in range(1,n+1):
    for j in range(i):
        print(start,end="")
        start+=1
    print()