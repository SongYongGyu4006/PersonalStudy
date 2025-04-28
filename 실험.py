def bino_coef_mem(n,k):
    if C[n][k] == None :
        if k == 0 or k ==n :
            C[n][k] = 1
        else:
            print(C[n][k], C[n-1][k-1],C[n-1][k])
            C[n][k] = bino_coef_mem(n-1, k-1) + bino_coef_mem(n-1, k)
            
    return C[n][k]
n=6
k=3

C = [[None for _ in range(k+1)] for _ in range(n+1)]
print(bino_coef_mem(n,k))
