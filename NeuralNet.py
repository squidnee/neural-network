import random
import params
from ctypes import *
from math import exp

## TODO:
# activation = 0
# for i in input:
#	 activation += x[i] * w[i]

## NEURON, NEURON LAYER, AND NEURAL NETWORK CLASSES ##

## NOTE: The primary logic for this code can be found at (http://www.ai-junkie.com/ann/evolved/nnt6.html).
## I do not own the logic for this code. I simply converted the code into Python from C++.
## My goal is to eventually reconstruct the network as I see fit, using this as a temporary 'blueprint'.

# Initializes a neuron based on number of inputs.
class Neuron:
	def __init__(self, inputNum):
		self.inputNum = inputNum + 1
		self.weights = list(random.random() for i in range(inputNum+1))

# Creates a layer of neurons by initializing a Neuron for the required number of times.
class NeuronLayer:
	def __init__(self, neuronNum, inputsPerNeuron):
		self.neuronNum = neuronNum
		self.neurons = list(Neuron(inputsPerNeuron) for i in range(neuronNum))

class NeuralNet:
	# Initializes the neural net based on the default values in params.py.
	def __init__(self):
		init = params.Params()
		self.numInputs = init.P_inputNum
		self.numOutputs = init.P_numOutputs
		self.numHiddenLayers = init.P_numHiddenLayers
		self.neuronsPerLayer = init.P_neuronsPerLayer
		self.layers = []

		self.createNet()

	# Creates the neuron layers based upon the initialized values.
	def createNet(self):
		if self.numHiddenLayers > 0:
			self.layers.append(NeuronLayer(self.neuronsPerLayer, self.numInputs))
			for i in range(self.numHiddenLayers-1):
				self.layers.append(NeuronLayer(self.neuronsPerLayer, self.neuronsPerLayer))
			self.layers.append(NeuronLayer(self.numOutputs, self.neuronsPerLayer))
		else:
			self.layers.append(NeuronLayer(self.numOutputs, self.numInputs))

	# Returns a list containing the weights.
	def getWeights(self):
		weightValues = []
		for layer in range(self.numHiddenLayers+1):
			for neuron in range(self.layers[layer].neuronNum):
				for weight in range(self.layers[layer].neurons[neuron].inputNum):
					weightValues.append(self.layers[layer].neurons[neuron].weights[weight])
		return weightValues

	# Replaces the weights in the neural network with the new values returned by getWeights().
	def setWeights(self, weights):
		weights = self.getWeights()
		i = 0
		for layer in range(self.numHiddenLayers+1):
			for neuron in range(self.layers[layer].neuronNum):
				for weight in range(self.layers[layer].neurons[neuron].inputNum):
					self.layers[layer].neurons[neuron].weights[weight] = weights[i]
					i = i + 1

	# Returns total number of weights needed for the net.
	def getNumberOfWeights(self):
		weights = 0
		for layer in range(self.numHiddenLayers+1):
			for neuron in range(self.layers[layer].neuronNum):
				for weight in range(self.layers[layer].neurons[neuron].inputNum):
					weights = weights + 1
		return weights

	# Calculates the output vector when given an input vector.
	def update(self,inputs=list(i for i in range(params.Params().P_numOutputs))):
		init = params.Params()
		outputs = list()
		weightVal = 0
		if len(inputs) is not init.P_numOutputs:
			return outputs
		else:
			for layer in range(self.numHiddenLayers+1):
				if layer > 0:
					inputs = outputs
				outputs = []
				weightVal = 0
				for neuron in range(self.layers[layer].neuronNum):
					netInput = 0
					thisInputNum = self.layers[layer].neurons[neuron].inputNum
					for weight in range(thisInputNum-1):
						netInput += self.layers[layer].neurons[neuron].weights[weight] * inputs[weightVal]
					weightVal = weightVal + 1
					netInput += self.layers[layer].neurons[neuron].weights[thisInputNum-1] * init.P_biasValue
					outputs.append(self.sigmoid(netInput, init.P_activationResponse))
					weightVal = 0
			return outputs

	# Creates the sigmoid function.
	def sigmoid(self, netInput, response):
		return ( 1 / ( 1 + exp((netInput * -1) / response)))

## FOR TESTING PURPOSES ##
if __name__ == '__main__':
	neuron = Neuron(3)
	print('Neuron is working!')
	
	neuronLayer = NeuronLayer(3, 6)
	print ('NeuronLayer is working!')

	net = NeuralNet()
	weights = net.getWeights()
	net.setWeights(weights)
	weightNum = net.getNumberOfWeights()
	outputs = net.update()
	print(outputs)
	print('Neural Network is working!!')