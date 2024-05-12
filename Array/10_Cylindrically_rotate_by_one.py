def rotate( arr, n):
    last=arr[n-1]
    for i in range(len(arr)):
        temp=arr[i]
        arr[i]=last
        last=temp
    return arr

print(rotate([1,2,3,4,5],5))