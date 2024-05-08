def ff_pp(oper):
    if oper == "division":
        def division(x,y):
            return x/y
        return division
    elif oper == "multiplication":
        def multiplication(x,y):
            return x*y
        return multiplication
f_div = ff_pp(oper="division")
print(f_div(9,3))
f_mult = ff_pp(oper="multiplication")
print(f_mult(4,6))

my_f = lambda x,y:x**y
print(my_f(2,3))
def my_ff(x,y):
    return x**y
print(my_ff(2,3))

class Square:
    def __init__(self,a,b):
        self.a = a
        self.b = b
        print('Стороны:',a,b)
    def __call__(self):
        return self.a*self.b

ss_f = Square(4,5)
print('Площадь:',ss_f())





