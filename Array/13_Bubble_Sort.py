def bubbleSort(arr, n):
        for i in range(len(arr)):
            for red in range(len(arr)-1, i, -1):
                if arr[red] < arr[red-1]:
                    arr[red],arr[red-1] = arr[red-1],arr[red]
        return arr

print(bubbleSort([3,2,5,74,21],5))