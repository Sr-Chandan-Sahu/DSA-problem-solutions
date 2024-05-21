def checkArmstrongNumber(num):
    temp = num
    res=0
    length=len(str(num))
    while num:
        digit=num%10
        res+=digit**length
        num//=10
    if temp == res:
        return True
    else:
        return False

print(checkArmstrongNumber(152))