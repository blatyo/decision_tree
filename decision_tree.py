#!/usr/bin/evn python

import sys
import decision_tree.analyze as analyze
		
def main():
	"""Starts program"""
	analyzer = analyze.Analyzer(sys.argv[1])
	analyzer.analyze()

if __name__ == '__main__':
	main()