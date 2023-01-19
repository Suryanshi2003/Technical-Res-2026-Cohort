n=int(input())
if 2<=n<10**9:
    num=2
    while num<=n:
        if n%num==0:
            print(num)
            num=num
            n=n/num
        else :
            num=num+1
