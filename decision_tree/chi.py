import math

class Chi:
	def __init__(self):
		"""values from http://www.uwsp.edu/psych/stat/x2.htm"""
		self.values = {
			1:		3.84,
			2:		5.99,
			3:		7.82,
			4:		9.49,
			5:		11.07,
			6:		12.59,
			7:		14.07,
			8:		15.51,
			9:		16.92,
			10:		18.31,
			11:		19.68,
			12:		21.03,
			13:		22.36,
			14:		23.69,
			15:		25.00,
			16:		26.30,
			17:		27.59,
			18:		28.87,
			19:		30.14,
			20:		31.41,
			21:		32.67,
			22:		33.92,
			23:		35.17,
			24:		26.42,
			25:		37.65,
			26:		38.89,
			27:		40.11,
			28:		41.34,
			29:		42.56,
			30:		43.77,
			35:		49.80,
			40:		55.76,
			45:		61.66,
			50:		67.51,
			60:		79.08,
			70:		90.53,
			80:		101.88,
			90:		113.15,
			100:	124.34
		}
	
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
		return D >= self.value(df)
		
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
	
	def value(self, df):
		"""return the chi squared distribution for the degrees of freedom, approximate if necessary"""
		if self.values.get(df):
			return self.values[df]
		
		new_df = 1
		for key in sorted(self.values.keys()):
			if key < df:
				new_df = key
		
		return self.values[new_df]