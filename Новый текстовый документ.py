class gruz:
    def maxPetrolWaste(self):
        maxPlaceName = ""
        maxWaste = 0
        for key in self._placesTo:
            if maxWaste < self._placesTo[key][1] / self._placesTo[key][3]:
                maxPlaceName = key
                maxWaste = self. _placesTo[key][1] / self._placesTo[key][3]
        print(maxPlaceName, maxWaste)

    def pf(self):
        print("Всего населенных пунктов, из которых что-то отправляли ", len(self._placesFrom), ":")

        for key in self._placesFrom:
            print("     ", key, ", оттуда отправлено ", self._placesFrom[key][0], "кг. грузов;")
        print()

    def po(self):
        print("Всего населенных пунктов, в которые что либо отправляли", len(self._placesTo), ":")

        for key in self._placesTo:
            print("     ", key, ", туда отправлено ",  self._placesTo[key][0], "кг. грузов;")
        print()

    def searchMaxGruzesDay(self):
        maxKey = ""
        maxValue = 0
        for key in self.totalGruzesMasInEachDay:
            if maxValue < self.totalGruzesMasInEachDay[key]:
                maxKey = key
                maxValue = self.totalGruzesMasInEachDay[key]
        print("Больше всего грузов было ",maxKey, ". Тогда было перевезено ", maxValue, " кг груза.")

    _placesTo = dict()
    _placesFrom = dict()
    totalGruzesMasInEachDay = dict()

    def __init__(self, day, placeFrom, placeTo, distance, petrolWaste, mass):
        self.day = day

        if not(day in self.totalGruzesMasInEachDay):
            self.totalGruzesMasInEachDay[day] = 0
        self.totalGruzesMasInEachDay[day] += int(mass)
        self.placeFrom = placeFrom

        if not(placeFrom in self._placesFrom):
            self._placesFrom[placeFrom] = [0 for i in range(4)]
        self._placesFrom[placeFrom][0] += int(distance)
        self._placesFrom[placeFrom][1] += int(petrolWaste)
        self._placesFrom[placeFrom][2] += int(mass)
        self._placesFrom[placeFrom][3] += 1

        self.placeTo = placeTo

        if not(placeTo in self._placesTo):
            self._placesTo[placeTo] = [0 for i in range(4)]
        self._placesTo[placeTo][0] += int(distance)
        self._placesTo[placeTo][1] += int(petrolWaste)
        self._placesTo[placeTo][2] += int(distance)
        self._placesTo[placeTo][3] += 1

        self.distance = int(distance)
        self.petrolWaste = int(petrolWaste)
        self.weight = int(mass)


file = open("travels.txt")
dataBase = list()
for line in file:
    mas = line.split()
    dataBase.append( gruz(mas[0]+" "+mas[1], mas[2], mas[3], mas[4], mas[5], mas[6]) )
totalGruzes = list()
gruz.searchMaxGruzesDay(gruz)

totalMas = 0
for i in range( len(dataBase) ):
    if dataBase[i].placeFrom == "Липки":
        totalMas += dataBase[i].weight
print(totalMas)

index = 0
totalDistance = 0

while(dataBase[index].day == "1 октября"):
    totalDistance += dataBase[index].distance
    index+=1
print(totalDistance)

gruz.pf(gruz)
gruz.po(gruz)
gruz.maxPetrolWaste(gruz)
