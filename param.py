def print_params(a=1,b='Строка',c=True):
    print(a,b,c)
print_params()
print_params(5)
print_params(5,6)
print_params(b=25)
print_params(c=[1,2,3])

values_list=[1,'Строка',True]
values_dict={'a':2,'b':'столбец','c':True}
res=print_params(*values_list)

res=print_params(**values_dict)

values_list_2=[3,'буква']
res=print_params(*values_list_2,42)
