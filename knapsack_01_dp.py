#def knapSack_dc(W, wt, val, n):
#    if n == 0 or W == 0 :       # 기반 상황
#        return 0
#  
#    if (wt[n-1] > W):							# 넣을 수 없음
#        return knapSack_dc(W, wt, val, n-1)	# 나머지 항목들로 처리
#    else: 
#        valWithout = knapSack_dc(W, wt, val, n-1)
#        valWith = val[n-1] + knapSack_dc(W-wt[n-1], wt, val, n-1)
#        return max(valWith, valWithout)	    	# 둘 중에서 더 큰 값


def knapSack_dp(W, wt, val, n): 
    A = [[0 for x in range(W + 1)] for x in range(n + 1)] 
  
    for i in range(1, n + 1): 
        for w in range(1, W + 1): 
            if wt[i-1] > w:			# i번째 물건이 배낭 용량 초과
                A[i][w] = A[i-1][w]
            else :					# i번째 물건이 배낭 용량 이하
                valWith = val[i-1] + A[i-1][w-wt[i-1]]  # 넣는 경우
                valWithout = A[i-1][w]                  # 빼는 경우
                A[i][w] = max(valWith, valWithout)      # 더 큰 값 선택
  
    return A[n][W]

val = [26, 20, 14, 40, 50] 
wt = [3, 2, 1, 4, 5] 
W = 6
n = len(val) 
#print("0-1배낭문제(분할 정복): ", knapSack_dc(W, wt, val, n)) 
print("0-1배낭문제(동적 계획): ", knapSack_dp(W, wt, val, n)) 
