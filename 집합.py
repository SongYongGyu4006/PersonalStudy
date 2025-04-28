def Union(a,b): #합집합 함수
    set_a = set(a)
    set_b = set(b)
    c = set_a.union(set_b)
    return list(c)

def Difference(a,b): #차집합 함수
    set_a = set(a)
    set_b = set(b)
    c = set_a - set_b
    return list(c)

def intersection(a, b): #교집합 함수
    return list(set(a) & set(b))


A = input("쉼표를 사용하여 집합A 요소들을 추가해주세요.").split(",")
B = input("쉼표를 사용하여 집합B 요소들을 추가해주세요.").split(",")
print("집합 A :",A)
print("집합 B :",B)
print("A와 B의 합집합 :",Union(A,B))
print("A와 B의 교집합 :",intersection(A,B))
print("A와 B의 차집합 :",Difference(A,B))
