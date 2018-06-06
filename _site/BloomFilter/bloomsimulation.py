import numpy as np
from bloom import Bloom

def simulation():

	input = np.random.randint(1, 1000000, size = 10000)
	test = np.random.randint(1, 1000000, size = 1000)

	b = Bloom(input, 0.01)
	b.train_bloom()
	b.test_bloom(test)
	

simulation()
