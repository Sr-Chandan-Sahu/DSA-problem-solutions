def removeEmpty(arr):
    zero_arr=[]
    non_zero_arr=[]
    for i in arr:
        if i==0:
            zero_arr.append(i)
        else:
            non_zero_arr.append(i)
    return non_zero_arr+zero_arr

print(removeEmpty([1,2,0,4,0,6,0]))
