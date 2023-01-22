n=int(input())
for i in range(1,(n*2)+1):
    if i%2!=0 and i<=n*2:
        for j in range(i,i+1):
            if i<=n:
                m=int((n-j)/2)
                print('\t'*m+'*\t'*j+'\t'*m)
            else:
                m=int((j-n)/2)
                k=i-((j-n)*2)
                print('\t'*m+'*\t'*k+'\t'*m)
