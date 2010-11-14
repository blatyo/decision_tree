import csv
import random

class Samples:
	def __init__(self, file_name):
		"""reads in the sample data"""
		self.data = []
		self.attrs = {}
		for row in csv.reader(open(file_name, 'rb')):
			self.data.append(row)
			for i in range(len(row) - 1):
				if self.attrs.get(i):
					if not row[i] in self.attrs[i]:
						self.attrs[i].append(row[i])
				else:
					self.attrs[i] = [row[i]]
				
	def attributes(self):
		"""attributes linked to their values"""
		return self.attrs
	
	def random_split(self):
		"""creates random splits of the data"""
		random.shuffle(self.data)
		middle = len(self.data) / 2
		return (self.data[0:middle], self.data[middle:])