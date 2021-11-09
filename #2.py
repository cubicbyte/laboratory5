class StudentJournal:
    labs = []
    creatives = []

    def __init__(self, name, params):
        self.name = name
        self.maxCreativeScore = params['max-creative-score']
        self.maxLabScore = params['max-laboratory-score']
        self.labCount = params['lab-works-count']
        self.passScore = params['pass-score']

        self.Laboratory.Config(self.maxLabScore)
        self.Creative.Config(self.maxCreativeScore)
    
    def addLaboratory(self, work):
        self.labs.append(work)

    def addCreative(self, work):
        self.creatives.append(work)
    
    def getResult(self):
        sum = self.scoreSum
        return sum, sum >= self.passScore
    
    @property
    def scoreSum(self):
        sum = 0
        for i in self.labs:
            sum += i.lastAttemp
        for i in self.creatives:
            sum += i.lastAttemp
        return sum

    class Work:
        @classmethod
        def Config(self, maxScore):
            self.maxScore = maxScore

        def __init__(self, attemps = 0, lastAttemp = 0):
            if (lastAttemp > self.maxScore):
                print('Ошибка: балл за выполнение этой работы не моет превышать', self.maxScore)
                self.attemps = 0
                self.lastAttemp = 0
            else:
                self.attemps = attemps
                self.lastAttemp = lastAttemp
        
        def addAttemp(self, score):
            if (score > self.maxScore):
                print('Ошибка: балл за выполнение этой работы не моет превышать', self.maxScore)
                return False

            self.attemps += 1
            self.lastAttemp = score

    class Laboratory(Work):pass
    class Creative(Work):pass

def main():
    params = {
        'max-creative-score': 16,
        'max-laboratory-score': 8,
        'lab-works-count': 10,
        'pass-score': 80
    }

    journal = StudentJournal('Головач Олена Василівна', params)

    journal.addLaboratory(journal.Laboratory(2, 8))
    journal.addLaboratory(journal.Laboratory(3, 8))
    journal.addLaboratory(journal.Laboratory(1, 7))
    journal.addLaboratory(journal.Laboratory(2, 7))

    journal.addCreative(journal.Creative(1, 14))
    journal.addCreative(journal.Creative(1, 12))
    journal.addCreative(journal.Creative(3, 15))
    journal.addCreative(journal.Creative(2, 15))

    print(journal.getResult())
    
if __name__ == '__main__':
    main()