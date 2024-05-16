#Move to end
def segregateElements(arr):
    p=[i for i in arr if i>=0]
    n=[i for i in arr if i<0]
    arr.clear()
    arr.extend(p+n)
    return arr
print(segregateElements([-2,4,-6,7,8,-1]))

#Move to Begin
def segregateElements2(arr):
    arr.sort()
    return arr
print(segregateElements2([3,5,-6,9,-4]))