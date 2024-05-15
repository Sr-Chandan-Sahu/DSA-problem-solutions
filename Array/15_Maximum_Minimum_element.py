#Approach 1
def MinAndMax(arr):
    arr.sort()
    return arr[0],arr[-1]

print("Min and Max:",MinAndMax([73,5,3,6,34,2]))

#Approach 2
def MinAndMax2(arr):
    return min(arr),max(arr)

print("Min and Max:",MinAndMax2([12,54,23,4]))

#Approach 3
def MinAndMax3(arr):
    min=arr[0]
    max=arr[-1]
    for i in arr:
        if i<min:
            min=i
        if i>max:
            max=i
    return min,max
print("Min and Max:",MinAndMax3([2,3,52,34]))