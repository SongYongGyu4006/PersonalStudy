def quick_sort(A, left, right):
    if left < right:
        mid = partition(A, left, right)
        print(A)
        quick_sort(A, left, mid - 1)
        quick_sort(A, mid + 1, right)

def partition(A, left, right):
    low = left + 1				
    high = right				
    pivot = A[left] 				
    
    while low <= high:			 
        while low <= right and A[low] < pivot:
            low += 1
        while high >= left and A[high] > pivot:
            high -= 1

        if low < high:			
            A[low], A[high] = A[high], A[low]
    
    A[left], A[high] = A[high], A[left]
    return high					

data = [71, 49, 92, 55, 38, 82, 72, 53]
print("Initial list:", data)
quick_sort(data, 0, len(data) - 1)
print("Sorted list:", data)
