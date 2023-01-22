n=int(input())
for i in range(1,n+1):
    if i<=3:
        for j in range(i,i+1):
            print('*\t'*(4-i)+'\t'*(i-1)*2+'\t*'*(4-i))
    else:
        for j in range(i,i+1):
            print('*\t'*(i-2)+'\t'*(n-i)*2+'\t*'*(i-2))
