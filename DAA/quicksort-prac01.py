def quicksort(arr,left,right):
    if left<right:
        partition_pos=partition(arr,left,right)
        quicksort(arr,left,partition_pos-1)
        quicksort(arr,partition_pos+1,right)
    

def partition(arr,left,right):
    i=left
    j=right
    pivot=arr[right]
    while i<j:
        while i< right and arr[i]<pivot:
            i+=1
        while j > left and arr[j] >= pivot:
            j-=1

        if i < j:
            arr[i],arr[j]=arr[j],arr[i]
        
    if arr[i]>pivot:
        arr[i],arr[right]=arr[right],arr[i]
        
    return i

arr=[3,5,1,2,4,6,7,8,5,4,3,21]
quicksort(arr,0,len(arr)-1)
print(arr)