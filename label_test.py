import numpy as np

test_data = np.genfromtxt('test.tsv', dtype=(str, str),delimiter='\t', skip_header=1)
print(test_data)