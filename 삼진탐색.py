List = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]

def ternary_search(A,low,high,key):
    print(high)
    if high==1 :
        if A[0] == key:
            return 0
        else : return -1
    if high>1 :
        if A[high//3] == key :
            return high/3
        elif A[high//3] > key :
            return ternary_search(A,0,high//3-1,key)
        else :
            return ternary_search(A,high//3+1,2*(high//3)-1,key)

print(ternary_search(List,0,14,8))
