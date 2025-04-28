data = [5,3,8,4,9,1,6,2,7]

def selection_sort(A):
    for i in range(len(A)):
        for j in range(i+1,len(A)):
            if A[i]>A[j]:
                A[i],A[j] = A[j],A[i]
selection_sort(data)
