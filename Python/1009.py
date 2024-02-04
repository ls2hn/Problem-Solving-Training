def processor(a, b):
    if a==1 or a==5 or a==6 :
        result = a
    elif a==2 or a==3 or a==7 or a==8 :
        if b%4 == 0:
            result = a**4%10    # 거듭제곱(**)이 %보다 우선
        else :
            result = a**(b%4)%10
    elif a==4 or a==9 :
        if b%2 == 0:
            result = a**2%10
        else :
            result = a
    else :
        result = 10
    return result

for _ in range(int(input())) :
    a, b = map( int, input().split() )
    a= a%10
    print(processor(a,b))
