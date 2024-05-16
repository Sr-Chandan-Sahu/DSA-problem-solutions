def findAllPalindromes(N):
    for i in range(1,N+1):
        temp =i
        i=str(i)[::-1]
        if temp ==int(i):
            print(i,end=" ")
findAllPalindromes(50)

print("\n")
#Approach 2

def findAllPalindromes2(N):
    for i in range(1,N+1):
        temp =i
        rev=0
        while temp:
            dig=temp%10
            rev=rev*10+dig
            temp//=10
        if rev==i:
            print(i,end=" ")
findAllPalindromes2(40)