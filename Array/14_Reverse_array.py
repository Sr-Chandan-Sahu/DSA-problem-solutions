def reverseArray(arr):
    return arr[::-1]

print(reverseArray([3,5,2,1]))

#Approach 2
def reverseArray2(arr):
    arr1=[]
    for i in range(len(arr)-1,-1,-1):
        arr1.append(arr[i])
    return arr1
print(reverseArray2([2,4,5,3,9]))
