class Params:
	def __init__(self):
		## NEURAL NET PARAMETERS ##
		## Note: these currently contain random numbers for testing purposes!
		self.P_inputNum = 6
		self.P_numOutputs = 1
		self.P_numHiddenLayers = 3
		self.P_neuronsPerLayer = 3
		self.P_activationResponse = 5.7
		self.P_biasValue = 4.9

if __name__ == '__main__':
	params = Params()
	print(params.P_inputNum)
	print('Working!')