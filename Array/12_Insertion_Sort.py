def insertionSort( arr, n):
        for i in range(0,len(arr)):
            temp = arr[i]
            red = i-1
            
            while ((temp < arr[red]) and (red >= 0)):
                arr[red+1] = arr[red]
                red -= 1
            arr[red+1] = temp
        return arr

print(insertionSort([4,2,45,23,6,5,1],7))