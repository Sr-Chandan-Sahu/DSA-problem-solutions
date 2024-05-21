def checkPerfectNumber(num):
    sum1=0
    for i in range(1,num):
        if num%i == 0:
            sum1+=i
    if num==sum1:
        return True
    else:
        return False

print(checkPerfectNumber(28))