def unionSortedArray(arr1,arr2):
    arr1 = set(arr1)
    arr2 = set(arr2)
    return list(arr1.union(arr2))
print(unionSortedArray([1,2,3,4,5],[7,8,9,10]))

#Approach 2
def unionSortedArray2(arr1,arr2):
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
    uni=list(map.keys())
    return uni

print(unionSortedArray2([2,4,6,7],[1,2,3,4,5]))
