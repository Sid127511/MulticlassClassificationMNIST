from random import uniform

class Classifier:

    def __init__(self, classes):
        self.classes = classes
        self.weights = None

    def classify(self, data):
        return 0

    def randomize(self):
        pass

    def train(self, train_data, epochs):
        self.randomize()
        accuracy = 0

        return accuracy