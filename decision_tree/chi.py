import math

class Chi:
	def __init__(self):
		self.compare = 5.99
	
	def significant(self, partitions, examples):
		"""Calculates the distribution and compares it against the chi squared distribution"""
		(p, n) = self.split(examples)
		
		D = 0
		for i in partitions.values():
			(pi, ni) = self.split(i)
			pi_hat = p * ((pi + ni) / float(p + n))
			ni_hat = n * ((pi + ni) / float(p + n))
			D += (math.pow(pi - pi_hat, 2) / pi_hat) + (math.pow(ni - ni_hat, 2) / ni_hat)
		
		df = len(examples) - 1
		return D >= self.compare
		
	def split(self, examples):
		"""counts positives and negatives"""
		p_label = examples[0][-1]
		p, n = 0, 0
		for example in examples:
			if example[-1] == p_label:
				p += 1
			else:
				n +=1
		return (p, n)