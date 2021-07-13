def ATM(X,Y):
    if(X%5==0) and X+0.5<=Y:
        X=X+0.50
        Y=Y-X
        print("%.2f"%Y)
    else:
        print("%.2f"%Y)


X,Y = input().split()
X=int(X)
Y=float(Y)
ATM(X,Y)

