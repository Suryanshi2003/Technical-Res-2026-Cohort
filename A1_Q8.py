n=str(input())
k=int(input())
if k>0:
    m=n[-1:-(k+1):-1]
    p=m[-1:-(k+1):-1]
    n2=n.replace(p,'')
    r=p+n2
    print(r)
else:
    m=n[0:k]
    n2=n.replace(m,'')
    r=n2+m
    print(r)
