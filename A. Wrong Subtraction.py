try:
    num,n = map(int,input().split())
    for _ in range(n):
        if num%10!=0:
            num=num-1
        else:
            num/=10
    print(int(num))

except:
    pass