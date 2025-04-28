List=[8,4,2,3,7,6,5,1]

#def insert_sort(A):
#    for i in range(len(A)):
#        j = i-1
#        key = A[i]
#        while j>=0 and A[j]>key:
#            A[j],A[j+1] = A[j+1],A[j]
#            print(A)
#            j -= 1
# return A

#def insert_sort_cycle(A,i=None):
#    if i == None:
#        i = 0
#   n = len(A)
#    i+=1
#   j=i-1
#    if i<n:
#        key = A[i]
#       while j>=0 and A[j]>key:
#            A[j],A[j+1] = A[j+1],A[j]
#           j -= 1
#        insert_sort_cycle(A,i)
#   elif i==n : print(A)

def insert_sort(A, i=1, j=None):
    print(A)
    if i == len(A):
        return A
    if j == None:
        j = i
    if j > 0 and A[j] < A[j - 1]:
        A[j], A[j - 1] = A[j - 1], A[j]
        return insert_sort(A, i, j - 1)
    else:
        return insert_sort(A, i + 1)



#def insert_sort2(A,n):
#    for i in range(n-1):
#        j=i-1
#        while j>=0 and A[j]>A[j+1] :
#            A[j],A[j+1] = A[j+1],A[j]
#            j -= 1
#    return A


print(insert_sort(List))
            
