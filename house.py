class House:
    def __init__(self,numberOfFloors):
        self.numberOfFloors = numberOfFloors

    def floor(self):
        while self.numberOfFloors <= 10:
            print('Текущий этаж равен', self.numberOfFloors)
            self.numberOfFloors = self.numberOfFloors + 1
dom = House(numberOfFloors = 1)
dom.floor()




