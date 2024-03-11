def test(a,b,c,*args,**kwargs):
    print(a,b,c,args,kwargs)
test(3,45,7,89,98,cat='мяу')



def factorial(n):
    if n==1:
        return 1
    factorial_minus_1=factorial(n=n-1)
    return n*factorial_minus_1
print(factorial(7))
