# cook your dish here
N = int(input())

for i in range (0,N):
    x = input()
    x = list(x)
    first, last = int(x[0]),int(x[len(x)-1])
    
    print(first + last)
    
    