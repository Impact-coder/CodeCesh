# cook your dish herefrom
import math

T = int(input())

for i in range(0,T):
    x = int(input())
    count = x*10 
    for j in range(10):
        n = count + j
        Sum =0
        for a in list(str(n)):
            Sum = Sum + int(a)
        
        if(Sum%10 == 0):
            print(n)
            
        
            
            
    