def findFact(n):
    ans=n
    i=n-1
    while i>0:
        sum=0
        for j in range(i):
            sum+=ans
        ans=sum
        i-=1
    return ans

print(findFact(5))




