class Building:
    def __init__(self, numberOfFloors, buildingType):
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType
    def __eq__(self, other):
       return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType

dom1 =Building(numberOfFloors=5,buildingType='brick')
dom2 =Building(numberOfFloors=5,buildingType='brick')
print(dom1==dom2)





