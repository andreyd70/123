import multiprocessing
from multiprocessing import Process, Queue


class WarehouseManager(Process):
    def __init__(self, data_queue, requests, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data_queue = data_queue
        self.requests = requests

    def process_request(self, request):
        product, action, quantity = request
        data = self.data_queue.get()

        if action == "receipt":
            if product in data:
                data[product] += quantity
            else:
                data[product] = quantity
        elif action == "shipment":
            if product in data and data[product] > 0:
                data[product] = max(0, data[product] - quantity)

        self.data_queue.put(data)

    def run(self):
        for request in self.requests:
            self.process_request(request)


if __name__ == "__main__":
    data = {}
    data_queue = Queue()
    data_queue.put(data)

    requests = [
        ("product1", "receipt", 100),
        ("product2", "receipt", 150),
        ("product1", "shipment", 30),
        ("product3", "receipt", 200),
        ("product2", "shipment", 50)
    ]

    manager = WarehouseManager(data_queue, requests)
    manager.start()
    manager.join()

    result_data = data_queue.get()
    print(result_data)