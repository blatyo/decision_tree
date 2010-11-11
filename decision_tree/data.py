import csv
import random

class Samples:
	def __init__(self, file_name):
		"""reads in the sample data"""
		self.data = []
		for row in csv.reader(open(file_name, 'rb')):
			self.data.append(row)
	
	def random_split(self):
		"""creates random splits of the data"""
		random.shuffle(self.data)
		middle = len(self.data) / 2
		return (self.data[0:middle], self.data[middle:])