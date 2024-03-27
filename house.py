class House:
    def __init__(self,numberOfFloors):
        self.num = numberOfFloors

    def floor(self):
        while self.num <= 10:
            print('Текущий этаж равен', self.num)
            self.num = self.num + 1
dom = House(numberOfFloors = 1)
dom.floor()




