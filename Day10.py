num = 12345
sum = 0
while num !=0:
    lastDigit = num%10
    sum+=lastDigit
    num = num//10
    print(num)
print(sum)