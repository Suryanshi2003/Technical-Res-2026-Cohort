num1=int(input())
num2=int(input())
if num1%num2==0:
    print(num2)
elif num2%num1==0:
    print(num1)
else:
    gcd=1
    if num1<num2:
        for i in range(2,num1+1):
            if num1%i==0 and num2%i==0:
                gcd=i
        print(gcd)
    else:
        for i in range(2,num2+1):
            if num1%i==0 and num2%i==0:
                gcd=i
        print(gcd)
lcm=(num1*num2)//gcd
print(lcm)
    
