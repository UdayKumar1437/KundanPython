# Readline()
# f = open("kundan.txt","r")
# while True:
#     line = f.readline()
#     if not line:
#         print(line,type(line))
#         break
#     print(line)


# f = open("kundan.txt","w")
# lines = ["line1\n","line2\n","line3\n"]
# f.writelines(lines)
# f.close()

# with open("kundan.txt","r") as f:
#     # Move to the 5th byte in the line
#     f.seek(5)
#     # Read the next 5 bytes
#     data = f.read(5)
#     print(data)

with open("kundan.txt","r") as f:
    # data = f.read(5)
    f.seek(10)
    current_position = f.tell()
    print(current_position)
    # Read the next 5 bytes
    # data = f.read(5)
    # print(data)


# with open("kundan.txt","w") as f:   
#     f.write("Kundanika Madireddy Is a good girl")
#     f.truncate(5)


# Lambda Function
# def double(x):
#     return x*2
def appply(func,value):
    return 6+func(value)
double = lambda x : x*2
cube = lambda x : x*x*x
avg = lambda x,y,z : (x+y+z)/3

# print(avg(1,2,3))
print(appply(lambda x : x*2,2))
