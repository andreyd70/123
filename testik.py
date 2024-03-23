def test_funchion():
    def inner_funchion():
        def func():
            print('Я в области видимости функции test_funchion')
        func()
    inner_funchion()
test_funchion()
