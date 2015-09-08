import random
import math

# A super basic Genetic Algorithm, just for fun. Playing around with mutations, fitness functions, etc.
# TODO: implement one to complement the Neural Network.

class GenePool:
	def __init__(self, ):
		geneSize= 9
		self.sample = geneSize
		self.target = random.lognormvariate(random.random()*10, random.random()*10)
		self.gene = self.encodeChromosome()
		self.offspring = self.crossoverRate()
		self.fitness = self.fitnessFunction()
		if len(str(self.target)) < self.sample:
			self.shuffleTarget()

	def encodeChromosome(self):
		gene = ('').join(str(s) for s in random.sample(range(9), self.sample))
		return gene

	def decodeChromosome(self, gene=0):
		if gene is 0:
			gene = self.gene
		while int(self.fitnessFunction()) - self.sample > 0.001:
			gene = self.encodeChromosome()
		else:
			return gene

	def fitnessFunction(self, target=0):
		if target is 0:
			target = self.target
		dist = []
		for i in range(1000):
			gene = str(target)
			dist.append(len(gene))
		average = (sum(d for d in dist) / len(dist))
		return int(average - len(self.gene))

	def crossoverRate(self):
		rate = random.random() + random.random()
		if rate > 1.0:
			rate = 0.7
		gene = self.encodeChromosome()
		first = self.decodeChromosome(gene)
		second = self.gene
		index = int(rate * 10)

		offspring_1 = first[0:index] + second[index:self.sample+1]
		offspring_2 = second[0:index] + first[index:self.sample+1]

		return offspring_1 or offspring_2

	def mutationRate(self):
		rate = random.randrange(1, 100, 1)
		if rate < 5:
			self.offspring = self.offspring[0:self.sample]
		elif rate == 1:
			self.offspring = self.offspring[0:self.sample-1]

	def shuffleTarget(self):
		while len(str(self.target)) < self.sample:
			self.target = random.lognormvariate(random.random()*10, random.random()*10)


if __name__ == '__main__':
	gene = GenePool()
	