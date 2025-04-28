import queue
L = int(input("스택의 길이를 정수로 입력해주세요."))
S = queue.LifoQueue(maxsize=L)
for i in range(0,L) :
    S.put(input("문자열을 입력하세요."))
for i in range(0,L) :
    val = S.get()
    print(val,end = ' ')
