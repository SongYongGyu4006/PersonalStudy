def quick_selection(A, left, right, k):
    if left <= right:
        pos = partition(A, left, right)
        print(A)
        if pos == k - 1:
            return A[pos]
        elif pos > k - 1:
            return quick_selection(A, left, pos - 1, k)
        else:
            return quick_selection(A, pos + 1, right, k)

def partition(A, left, right):
    low = left + 1
    high = right
    pivot = A[left]
    
    while low <= high:
        while low <= right and A[low] <= pivot:
            low += 1
        while high >= left and A[high] > pivot:
            high -= 1
        
        if low < high:
            A[low], A[high] = A[high], A[low]
    
    A[left], A[high] = A[high], A[left]
    return high

array = [12, 3, 5, 7, 4, 19, 26, 23, 15]
print(quick_selection(array, 0, len(array) - 1, 7))
