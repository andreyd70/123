class Building:
    def __init__(self, numberOfFloors, buildingType):
        self.num = numberOfFloors
        self.bui = buildingType
    def __eq__(self, other):
       return self.bui == other.bui



dom1 =Building(numberOfFloors=20,buildingType='brick')
dom2 =Building(numberOfFloors=5,buildingType='brick')
print(dom1==dom2)





