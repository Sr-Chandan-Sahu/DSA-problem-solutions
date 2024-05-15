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

#Approach 3
def reverseArray3(A,start,end):
    while start < end:
        A[start], A[end] = A[end], A[start]
        start += 1
        end -= 1
    return A

print(reverseArray3([3,4,5,6],0,3))

#Approach 4
def reverseArray4(arr):
    return list(reversed(arr))
print(reverseArray4([1,2,3,4]))
