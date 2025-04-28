List = [1,2,3,4,5,6,7,8,9]

def tri_sort(A,left=0,right=None,key=None):
    if len(A) == 1 :
        return 0
    if right == None:
        right = len(A)
    point1 = left+((right-left)//3)
    point2 = left+(2*(right-left)//3)
    if A[point1] == key:
        return point1
    if A[point2] == key:
        return point2
    if A[point1]>key:
        return tri_sort(A,left,point1-1,key)
    elif A[point2]<key:
        return tri_sort(A,point2+1,right,key)
    else :
        return tri_sort(A,point1+1,point2-1,key)


print(tri_sort(List,key = 8))
