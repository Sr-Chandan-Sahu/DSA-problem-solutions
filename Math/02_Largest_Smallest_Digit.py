def findLargestSmallest(n):
    a=str(n)
    print(max(a),min(a))

findLargestSmallest(783)


#Approach 2(Long method)
def findLargestSmallest2(n):
    large=0
    small=9
    while n:
        res=n%10
        large=max(res,large)
        small=min(small,res)
        n//=10
    print(large,small)

findLargestSmallest2(435)