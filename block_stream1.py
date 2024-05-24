import threading
from threading import Thread

locker = threading.Lock()


class BankAccount(Thread):
    def __init__(self, account, amount, lock=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.account = account
        self.amount = amount
        self.locker = lock

    def deposit(self, amount):
        self.account += amount

    def withdraw(self, amount):
        self.account -= amount


def deposit_task(account, amount):
    for _ in range(5):
        with locker:
            account.deposit(amount)
            print(f'Deposited {amount}, new balance {account.account}')


def withdraw_task(account, amount):
    for _ in range(5):
        with locker:
            account.withdraw(amount)
            print(f'Withdrew {amount}, new balance is {account.account}')


account = BankAccount(account=1000, amount=0, lock=locker)

deposit_thread = threading.Thread(target=deposit_task, args=(account, 100))
withdraw_thread = threading.Thread(target=withdraw_task, args=(account, 150))
deposit_thread.start()
withdraw_thread.start()

deposit_thread.join()
withdraw_thread.join()
