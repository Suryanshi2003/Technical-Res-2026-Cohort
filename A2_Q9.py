n=int(input())
for i in range(1,n+1):
    for j in range(i,i+1):
        if i<3:
            print('\t'*(i-1)+'*'+'\t'*int(4/i)+'*')
        elif i==3:
            print('\t'*2+'*'+'\t'*2)
        else:
            print('\t'*(n-i)+'*'+'\t'*int((i*2)-6)+'*')
