def countBits(n):
    ans=[0]*(n+1)
    baseP=1
    for i in range(1,n+1):
        if(2*baseP==i):
            baseP=i
        ans[i]=ans[i-baseP]+1
    return ans
#numero=71
#print(countBits(numero)[:])