import sys
sys.path.append('data')
from DataProcessor import DataProcessor
from SimpleNeuralNet import SimpleNeuralNet

dataProcessor = DataProcessor()
features, labels = dataProcessor.getData()

net = SimpleNeuralNet()
net.trainModel(features, labels)