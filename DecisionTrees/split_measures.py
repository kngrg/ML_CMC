import numpy as np


def evaluate_measures(sample):
    """Calculate measure of split quality (each node separately).

    Please use natural logarithm (e.g. np.log) to evaluate value of entropy measure.

    Parameters
    ----------
    sample : a list of integers. The size of the sample equals to the number of objects in the current node. The integer
    values are equal to the class labels of the objects in the node.

    Returns
    -------
    measures - a dictionary which contains three values of the split quality.
    Example of output:

    {
        'gini': 0.1,
        'entropy': 1.0,
        'error': 0.6
    }

    """
    labels, counts = np.unique(sample, return_counts=True)
    total = len(sample)
    print(counts / total)

    gini = 1 - np.sum((counts/total) ** 2)
    entropy = -np.sum((counts/total) * np.log(counts/total))
    error = 1 - np.max(counts) / total

    measures = {'gini': gini, 'entropy': entropy, 'error': error}
    return measures
