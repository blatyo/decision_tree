# Decision Tree

## Running
You can run this program by doing:

    python decision_tree.py <dataset>

For example:

    python decision_tree.py data/car.csv

Or:

    python decision_tree.py data/tic-tac-toe.csv

## Problem Description
Implement the decision tree induction algorithm described in the course textbook (Section 18.3, pp. 697-707). Then produce a plot similar to the one in Figure 18.7 (page 703). Compute 10 different random orders for your training set. Then, compute the accuracy rate (correct recognition percentage) of the induced decision tree on the test set when the learning algorithm is run for 1 sample, 5 samples, 10 samples, .., up to N samples (where N is the number of training samples), for each of the 10 orderings of your training set. The values plotted in the graph should be the average of the accuracy rates observed for k-samples (k=1,5,10,...,n) over the 10 different orderings.
Then produce a second plot, which shows the average number of nodes in the decision tree for each value of k in the accuracy graph.

In your write-up, briefly summarize your implementation, and then discuss your results. Do you think that your decision tree has overfit the data? Why or why not?

For plotting, available tools include Matlab, Gnuplot, or the Python matplotlib library (this may be the most convenient option).

(Optional bonus, max. +20%) Using the tic-tac-toe data, repeat the experiment, this time pruning nodes after a tree has been constructed using the	chi-squared criterion described on p. 706. Then comment on the results in your write-up, comparing them to the performance of the regular decision tree.