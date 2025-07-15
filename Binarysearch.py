def binarySearch(arr,i,j,x):
    mid = i+(j-i)//2
    if(arr[mid] == x):
        return mid
    elif arr[mid]<x:
        return binarySearch(arr,mid+1,j,x)
    else:
        return binarySearch(arr,i,mid-1,x)


arr=[2,4,6,8,9,11]
i = 0
j = len(arr)-1
x = 8
result = binarySearch(arr,i,j,x)
print(result)