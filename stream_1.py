import time
from threading import Thread


def f_numb(i):
    for i in range(1, i):
        print(i)
        time.sleep(1)


def f_chr(i):
    for i in range(1, i):
        print(chr(i + 96))
        time.sleep(1)


th1 = Thread(target=f_numb, args=(11,))
th1.start()
th2 = Thread(target=f_chr, args=(11,))
th2.start()
th1.join()
th2.join()
