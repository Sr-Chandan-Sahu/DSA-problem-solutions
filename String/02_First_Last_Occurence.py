def firstLastOccurence(str,ch):
    f_index=str.find(ch)
    l_index=str.rfind(ch)
    return f_index,l_index
print(firstLastOccurence("Developer","e"))