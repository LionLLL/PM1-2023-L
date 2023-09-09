from math import fabs
from math import sqrt
for _ in range(int(input())):
    a,b=map(int,input().split())
    divisores=0
    numero=fabs(a-b)
    for i in range(1,(int)(sqrt(numero))+1):
        if(numero%i==0):
            if(numero/i==i):
                divisores+=1
            else:
                divisores+=2
    print(divisores)