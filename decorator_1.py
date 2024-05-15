def is_prime(func):
    def wrapper(*args):
        res = func(*args)
        if res == 0:
            print('Это просто Ноль')
        elif res == 1:
            print('Это же Единица')
        elif res % 2 == 0 and res != 2:
            print('Составное')
        elif res % 3 == 0 and res != 3:
            print('Составное')
        elif res % 5 == 0 and res != 5:
            print('Составное')
        else:
            print('Простое')
        return res

    return wrapper


@is_prime
def sum_three(x, y, z):
    return x + y + z


result = sum_three(2, 3, 6)
print(result)
