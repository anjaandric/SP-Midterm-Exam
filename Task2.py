def rekurzija(x, stepen):

    if stepen < 0:

        if x > 0:
            rec(x-1, stepen)
        else:
            rec(x+1, stepen)
    else:
        if x < n:
            rec(x + n, stepen)
        else:
            return

X1 = int(input("N: "))

X2 = int(input("M: "))
rekurzija(N,M)

