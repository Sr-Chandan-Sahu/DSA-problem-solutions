def findMissingNum(arr,n):
    sum1=int((n*(n+1))/2)
    sum_arr=sum(arr)
    mis_num=sum1-sum_arr
    print(mis_num)

findMissingNum([1,2,3,4,6,7,8,9,10],10)
