Text = "BRUTEFORCE"

def String_Search(A,key):
    for i in range(len(A)):
        if A[i] == key[0]:
            for j in range(1,len(key)):
                if A[i+j] != key[j] :break
                else : return i
    return -1
print(String_Search(Text,"BR"))
