import math
a=int(input("a값을 입력하세요. :"))
b=int(input("b값을 입력하세요. :"))
c=int(input("c값을 입력하세요. :"))

def findx(a,b,c):
    Discriminant = b*b-(4*a*c)
    if Discriminant > 0 :
        SqrtDiscriminant = math.sqrt(Discriminant)
        RESULT = (-b+SqrtDiscriminant)/(2*a)
        result = (-b-SqrtDiscriminant)/(2*a)
        print("x는",RESULT,"와",result,"입니다.")
    elif Discriminant < 0 :
        print("x는 존재하지 않습니다.")
    else :
        SqrtDiscriminant = math.sqrt(Discriminant)
        RESULT = (-b+SqrtDiscriminant)/(2*a)
        print("x는",RESULT,"입니다.")

print(a,"(x^2) +",b,"x +",c,"= 0")
findx(a,b,c)
