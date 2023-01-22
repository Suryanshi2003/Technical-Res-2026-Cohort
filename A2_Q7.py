n=int(input())
for i in range(1,n+1):
    for j in range(i,i+1):
        print('\t'*(i-1)+'*'+'\t'*(n-i))
