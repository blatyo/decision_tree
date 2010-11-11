import data
import tree
import csv

class Analyzer:
	def __init__(self, file_name):
		self.samples = data.Samples(file_name)
		self.builder = tree.Builder()
		self.file_name = file_name.split('/')[-1]
	
	def analyze(self):
		"""calculates averages for correctly classified and node count"""
		
		"""generate sample sets"""
		samples, length = [], 0
		for i in range(10):
			(tr, te) = self.samples.random_split()
			samples.append((tr, te))
			length = len(tr)
		
		step = self.step(length)
		
		"""calculate averages"""
		counts, node_counts, averages, average_nodes = {}, {}, {}, {}
		for i in step:
			print i
			for sample in samples:
				if not counts.get(i):
					counts[i] = 0
				if not node_counts.get(i):
					node_counts[i] = 0
				(tr, te) = sample
				tree = self.builder.build(tr[0:i])
				counts[i] += self.test(tree, te)
				node_counts[i] += tree.number_of_nodes()
			averages[i] = counts[i] / float(len(samples))
			average_nodes[i] = node_counts[i] / float(len(samples))
			
			self.write(averages, average_nodes)
	
	def write(self, ave, node_ave):
		"""outputs averages"""
		w = csv.writer(open("output/correct_averages_%s" % (self.file_name), 'wb'), dialect='excel')
		for k in sorted(ave.keys()):
			w.writerow([k, ave[k]])
		
		w = csv.writer(open("output/node_averages_%s" % (self.file_name), 'wb'), dialect='excel')
		for k in sorted(node_ave.keys()):
			w.writerow([k, node_ave[k]])
					
	def test(self, tree, tests):
		"""compares expected with actual values"""
		count = 0
		for test in tests:
			if test[-1] == tree.choose(test):
				count += 1
		return count
	
	def step(self, length):
		"""generates the steps to iterate over"""
		"""does every 5 starting at 5, 1, and n if its not a multiple of 5"""
		step = [i for i in range(5, length, 5)]
		step.insert(0, 1)
		if length % 5 != 0:
			step.append(length)
		return step
			