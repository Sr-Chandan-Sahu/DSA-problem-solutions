def intersectionSortedArray(arr1,arr2):
    arr1=set(arr1)
    arr2=set(arr2)
    return list(arr1.intersection(arr2))
print(intersectionSortedArray([1,3,4,5],[2,3,4,5,6]))

#Approach 2
def intersectionSortedArray2(arr1,arr2):
    #Remove duplicates from arr1
    map={}
    for i in range(len(arr1)):
        if arr1[i] in map:
            map[arr1[i]]+=1
        else:
            map[arr1[i]]=1
    
    #Remove duplicates from arr2
    for i in range(len(arr2)):
        if arr2[i] in map:
            map[arr2[i]]+=1
        else:
            map[arr2[i]]=1
    
    inter=[]
    for i in arr1:
        if i in arr2:
            inter.append(i)
    return inter
print(intersectionSortedArray2([1,2,4,6],[2,3,4,5]))