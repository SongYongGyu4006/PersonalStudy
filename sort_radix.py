from queue import Queue# 파이썬 queue모듈의 Queue 사용
def radix_sort(A) :
    queues = []						# 큐의 리스트
    for i in range(BUCKETS) :
        queues.append(Queue())		# BUCKETS개의 큐 사용
    print(queues)
    n = len(A)
    factor = 1						# 1의 자리부터 시작
    for d in range(DIGITS) :			# 모든 자리에 대해
        for i in range(n) :			# 자릿수에 따라 큐에 삽입
            queues[(A[i]//factor) % 10].put(A[i])	# 숫자를 삽입
        j = 0
        for b in range(BUCKETS) :		# 버킷에서 꺼내어 원래의 리스트로
            while not queues[b].empty() : # b번째 큐가 공백이 아닌 동안
                A[j] = queues[b].get()	# 원소를 꺼내 리스트에 저장
                j += 1
        factor *= 10			# 그 다음 자리수로 간다.
        print("step", d+1, A)			# 중간 과정 출력용 문장



BUCKETS = 10		#10진수 사용
DIGITS  = 3		#최대 자리수
data = [10,992,82,432,123,234,345,56,636,76,567,119]
radix_sort(data)						# 기수 정렬
print("Radix:", data)					# 결과 출력
