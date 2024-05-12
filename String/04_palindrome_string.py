def isPalindrome( S):
        # code here
        if S==S[::-1]:
            return 1
        return 0
print(isPalindrome("iti"))