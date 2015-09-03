# A basic genome class.

class Genome:
	def __init__(self, weights=list(), fitness=0.0):
		self.weights = weights
		self.fitness = fitness

if __name__ == '__main__':
	genome = Genome(weights=[5,8,9],fitness=7)
	print(genome.weights)
	print(genome.fitness)
	print('Genome is working!')