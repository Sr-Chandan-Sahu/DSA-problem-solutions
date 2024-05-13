def SelectionSort(arr,n):
    for i in range(len(arr)):
            minval = arr[i]
            minindex = i
            
            for red in range(i+1,len(arr)): 
                if arr[red] < minval:
                    minval = arr[red]
                    minindex = red
            arr[i],arr[minindex] = arr[minindex],arr[i]
    return arr

result=SelectionSort([3,4,52,16,13,31],6)
print(result)