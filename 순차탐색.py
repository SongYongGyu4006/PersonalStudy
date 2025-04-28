data = [5,3,8,4,2,7]

def Key_Search(A,key):
    for i in range(len(A)):
        if key == A[i]:
            return i
    return -1

print(Key_Search(data,2))
print(Key_Search(data,9))
