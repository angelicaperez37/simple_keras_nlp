
class DataProcessor:

    def __init__(self):
        self.labels = list()
        self.sentences = list()
        self.features = list()
        self.readSentences('data/negativeSentences.txt', 0)
        self.readSentences('data/positiveSentences.txt', 1)
        self.getFeatures()

    def readSentences(self, dataFile, label):
        for line in open(dataFile):
            words = line.strip().split(' ')
            self.sentences.append(words)
            self.labels.append(label)

    def getFeatures(self):
        for words in self.sentences:
            featureVector = list()
            featureVector.append(self.containsPositiveWord(words))
            featureVector.append(self.containsNegativeWord(words))
            self.features.append(featureVector)

    def containsPositiveWord(self, words):
        positiveWords = ['awesome', 'positive', 'party']
        return self.containsWord(words, positiveWords)

    def containsNegativeWord(self, words):
        negativeWords = ['sad', 'no', 'negative']
        return self.containsWord(words, negativeWords)

    def containsWord(self, words, targetWords):
        for word in words:
            if word in targetWords:
                return 1.0
        return 0.0

    def getData(self):
        return self.features, self.labels


