def removeDuplicates(str):
        # code here
        l=[]
        for i in str:
            if i not in l:
                l.append(i)
        return "".join(l)
print(removeDuplicates("google"))