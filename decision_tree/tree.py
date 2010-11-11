import math

class Builder:
	def __init__(self, examples):
		self.examples = examples
		
	def build(self):
		i, attributes = 0, []
		for col in self.examples[0][0:-1]:
			attributes.append(i)
			i += 1
		return self.learn(self.examples, attributes, self.examples)
	
	def learn(self, examples, attributes, parent_examples):
		if len(examples) == 0:
			return Leaf(self.plurality(parent_examples))
		elif self.same_classification(examples):
			return Leaf(examples[0][-1])
		elif len(attributes) == 0:
			return Leaf(self.plurality(examples))
		else:
			best = self.best_attribute(attributes, examples)
			sub_attributes = attributes[:]
			sub_attributes.remove(best)
			tree = Node(best)
			partitions = self.partition(examples, best)
			for key, sub_examples in partitions.iteritems():
				tree.add_child(key, self.learn(sub_examples, sub_attributes, examples))
			return tree
	
	def partition(self, examples, best):
		partitions = {}
		for example in examples:
			key = example[best]
			if partitions.get(key):
				partitions.get(key).append(example)
			else:
				partitions[key] = [example]
		return partitions
			
	def same_classification(self, examples):
		classification = None
		for row in examples:
			if not classification:
				classification = row[-1]
			elif classification != row[-1]:
				return False
		return True
	
	def plurality(self, examples):
		high = examples[0][-1]
		counts = {high: 0}
		for row in examples:
			label = row[-1]
			if counts.get(label):
				counts[label] += 1
				if counts[label] > counts[high]:
					high = label
			else:
				counts[label] = 0
		return high
	
	def best_attribute(self, attributes, examples):
		print attributes
		best = attributes[0]
		best_change = self.entropy_change(examples, 0)
		for attr in attributes[1:]:
			change = self.entropy_change(examples, attr)
			if change > best_change:
				best = attr
				best_change = change
		return best
	
	def entropy_change(self, examples, attribute):
		return self.non_split_entropy(examples) - self.split_entropy(examples, attribute)
	
	def non_split_entropy(self, examples):
		label_counts = {}
		for example in examples:
			if label_counts.get(example[-1]):
				label_counts[example[-1]] += 1
			else:
				label_counts[example[-1]] = 1
		return self.entropy(label_counts, len(examples))
	
	def split_entropy(self, examples, attribute):
		partitions = self.partition(examples, attribute)
		entropy = 0
		for k, ex in partitions.iteritems():
			en = self.non_split_entropy(ex)
			entropy += (len(ex) / float(len(examples))) * en
		return entropy
	
	def entropy(self, label_counts, total):
		entropy = 0
		for label, count in label_counts.iteritems():
			frac = count / float(total)
			part = 0
			if frac != 0:
				part = frac * math.log(frac, 2)
			entropy += part
		return part * -1

class Node:
	def __init__(self, attribute):
		self.attribute = attribute
		self.children = {}
		
	def add_child(self, value, node):
		self.children[value] = node
		
	def choose(self, example):
		return self.select_child(example).choose(example)
	
	def select_child(self, example):
		return self.children[example[self.attribute]]
		
	def number_of_nodes(self):
		num = 1
		for k, v in self.children.iteritems():
			num += v.number_of_nodes()
		return num
	
	def to_s(self, depth=1):
		s = "%i\n" % (self.attribute)
		for k, v in self.children.iteritems():
			s = "%s%s%s: %s" % (s, "  " * depth, k, v.to_s(depth + 1))
		return s

class Leaf:
	def __init__(self, choice):
		self.choice = choice
	
	def choose(self, example=None):
		return self.choice
	
	def number_of_nodes(self):
		return 1
	
	def to_s(self, depth):
		return "%s\n" % (self.choice)