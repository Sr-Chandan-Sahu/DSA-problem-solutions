def checkPalindrome(n):
    temp=str(n)[::-1]
    return int(temp) ==n
print(checkPalindrome(1221))

#Approach 2
def checkPalindrome2(n):
    temp=n
    rev=0
    while n:
        dig=n%10
        rev=rev*10+dig
        n//=10
    return temp==rev
print(checkPalindrome2(1361))

