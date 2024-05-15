def checkPalindrome(str):
    return str == str[::-1]
print(checkPalindrome("CSC"))

#Approach 2
def checkPalindrome2(str):
    s=""
    for i in range(len(str)-1, -1,-1):
        s+=str[i]
    return s==str
print(checkPalindrome2("CSCS"))