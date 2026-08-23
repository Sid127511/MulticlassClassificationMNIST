from random import uniform

class Classifier:
    #if its taking forever to train, change second argument line 32 in run.py to something smaller like 25

    def __init__(self, classes, inputs):
        #number of classes (10)
        self.classes = classes
        #should have 10 arrays of 784(one for each pixel per number)
        self.weights = []
        self.inputs = inputs

    def classify(self, data):
        #find which set of weights(one for each number) score the highest
        max = 0
        max_index = 0
        for i in range(self.classes):
            sum = 0
            for j in range(self.inputs):
                sum += data[j]/255 * self.weights[i][j]
            if (sum > max):
                max = sum
                max_index = i
        return max_index

    def randomize(self):
        #randomize all the weights
        for i in range(self.classes):
            weight = []
            for j in range(self.inputs):
                weight.append(uniform(-1.00, 1.00))
            self.weights.append(weight)

    def train(self, train_data, epochs):
        self.randomize()
        accuracy = 0

        for n in range(epochs):
            correct_counter = 0
            for j in range(self.inputs):
                guessed = self.classify(train_data[j])
                if (guessed == train_data[j][-1]):
                     correct_counter += 1
                else:
                    for i in range(self.inputs):
                        #adjust weights
                        self.weights[guessed][i] -= train_data[j][i]/255
                        #if error convert to int with int()
                        self.weights[int(train_data[j][-1])][i] += train_data[j][i]/255
            accuracy = correct_counter/len(train_data)*100
            #print the accuracy
            print(f"Epoch: #{n+1}: {accuracy}")

        #return for display
        return accuracy