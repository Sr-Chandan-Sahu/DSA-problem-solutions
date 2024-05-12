def kthSmallest(arr, l, r, k):
        '''
        arr : given array
        l : starting index of the array i.e 0
        r : ending index of the array i.e size-1
        k : find kth smallest element and return using this function
        '''
        temp=[]
        for i in arr:
            temp.append(i)
        temp.sort()
        return temp[k-1]
result=kthSmallest([12,3,43,54,23,45],0,5,3)
print(result)