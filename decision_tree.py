#!/usr/bin/evn python

import sys
import decision_tree.analyze as analyze
		
def main():
	"""Starts program"""
	prune = False
	if len(sys.argv) == 3:
		prune = (not not sys.argv[2])
	analyzer = analyze.Analyzer(sys.argv[1], prune)
	analyzer.analyze()

if __name__ == '__main__':
	main()