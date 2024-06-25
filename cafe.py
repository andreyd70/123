import queue
import threading
import time
from threading import Thread


class Table:
    def __init__(self, number):
        self.number = number
        self.is_busy = False


class Customer(Thread):
    def __init__(self, customer, table, cafe, queue, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.customer = customer
        self.table = table
        self.cafe = cafe
        self.queue = queue

    def run(self):
        time.sleep(5)
        print(f'Посетитель номер {self.customer} покушал и ушел.')
        self.table.is_busy = False
        if not self.queue.empty():
            next_customer = self.queue.get()
            self.cafe.serve_customer(next_customer)


class Cafe:
    def __init__(self, tables):
        self.customer_threads = []
        self.queue = queue.Queue()
        self.tables = tables
        self.lock = threading.Lock()

    def customer_arrival(self):
        for i in range(1, 21):
            print(f'Посетитель номер {i} прибыл.')
            self.serve_customer(i)
            time.sleep(1)

    def serve_customer(self, customer):
            free_table = False
            for table in self.tables:
                if not table.is_busy:
                    table.is_busy = True
                    print(f'Посетитель номер {customer} сел за стол {table.number}')
                    customer_thr = Customer(customer=customer, table=table, cafe=self, queue=self.queue)
                    customer_thr.start()
                    self.customer_threads.append(customer_thr)
                    return
            if not free_table:
                print(f'Посетитель номер {customer} ожидает свободный стол')
                self.queue.put(customer)


table1 = Table(1)
table2 = Table(2)
table3 = Table(3)
tables = [table1, table2, table3]

cafe = Cafe(tables)
customer_arrival_thread = threading.Thread(target=cafe.customer_arrival)
customer_arrival_thread.start()
customer_arrival_thread.join()

for i in cafe.customer_threads:
    i.join()
