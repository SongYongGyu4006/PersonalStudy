List = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0]
def sort(A):
    n = len(A)
    for i in range(n):
        swapped = False 
        for j in range(n - 1 - i):
            if A[j] == 1 and A[j + 1] == 0:
                A[j], A[j + 1] = A[j + 1], A[j]
                swapped = True
        if not swapped: 
            break
    print(A)
sort(List)
