def reverseString(str):
    return str[::-1]
print(reverseString("RAM"))

#Approach 2
def reverseString2(str):
    s=""
    for i in range(len(str)-1, -1,-1):
        s+=str[i]
    return s
print(reverseString2("KARMA"))