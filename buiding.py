class Building:
    total = 0
    def __init__(self):
        Building.total +=1
kvartal = []
kvartal_size = 40
while len(kvartal) < kvartal_size:
    new_building = Building()
    kvartal.append(new_building)
    print(new_building,Building.total)

print(Building.total)
