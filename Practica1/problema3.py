for _ in range(int(input())):
    proteina=0
    contador=1
    n,k = map(int,input().split())
    A = map(int,input().split())
    for i in A:
        proteina=proteina+i-k
        if(proteina<0):
            print("NO "+str(contador))
            break
        contador=contador+1
    if(proteina>=0):
        print("YES")