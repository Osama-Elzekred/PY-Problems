
def quick_sort(arr,left,right):
  if right > left :
    pivot_index=partioning(arr,left,right) # find the next pivot index
    quick_sort(arr,left,pivot_index-1)
    quick_sort(arr,pivot_index+1,right)

def partioning(arr,left,right):
  pivot = arr[right]  # taking the far right item as the pivot 
  i = left
  j= right -1    
  while i < j:
    while i < right and arr[i] <= pivot:  # i tracks the item greater than pivot (left of povit items)
      i += 1
    while j > left and arr[j] >= pivot:  # j tracks the item lower than pivot (right of povit items)
      j-=1
    if i < j :
      arr[i],arr[j] = arr[j],arr[i]

  if arr[i] > pivot:
    arr[i],arr[right] = arr[right],arr[i] # swaping the pivot with arr[i]

  return i 

  # hints :                                                   i  -->                   
  # all the items in the left of i is less than pivot         ⬇                    (p)
  # all the items in the right of j is greater than pivot    [33,22,55,44,77,11,66,88]
  #                                                                              ⬆    
  #                                                                         <--  j    

arr= [33,22,55,44,77,11,66,88]
right= len(arr)-1
quick_sort(arr,0,right)
print(arr)

                                    