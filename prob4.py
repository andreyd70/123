class NameException(Exception):
    def __init__(self,name,age):
        self.name=name
    def __str__(self):
        return f' {self.name} не наш ! '
class AgeExseption(Exception):
    def __init__(self,name,age):
        self.age = age
    def __str__(self):
        return f' не того возраста:{self.age}'

class Human:
    def __init__(self, name, age):
        if name !='Tim':
            self.name = name
        else:
            raise NameException(name,age)
        if age != 20:
             self.age = age
        else:
            raise AgeExseption(name,age)
    def info(self):
        print(f'имя: {self.name},возрaст: {self.age}')
try:
    sam = Human('Tom',20)
    sam.info()

except NameException as e:
    print('Ошибка:', e)
    raise NameException('Tim', 20)
except AgeExseption as e:
    print('Упс!!!', e)
    raise AgeExseption('Tim', 20)

finally:
    print('Уpa')
