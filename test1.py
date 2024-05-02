import warnings

def funwar():
    a=10
    b=2
    for i in range(100):
        if b < 0.01:
            warnings.warn('близко ноль ',UserWarning)
#            warnings.simplefilter('always', UserWarning)
#            print('Помогите')

#            warnings.simplefilter('error', UserWarning)
#            print('Ошибка')

            warnings.simplefilter('ignore', UserWarning)
            print('Не важно')
        a = a/b
        b = b/10
        print(a,b)
funwar()


