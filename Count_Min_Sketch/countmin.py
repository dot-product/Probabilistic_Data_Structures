import numpy as np
import math

class CountMin:

	# --------------------------------------------------------------------------------------
	''' 1. epsilon  represent the error fraction. i.e how much deviation can be allowed from the actual count'''
	'''	2. delta is the probablity of case 1. '''
	# ---------------------------------------------------------------------------------------

	def __init__(self, input_data, epsilon, delta):	

		self.input_data = input_data
		self.epsilon = epsilon
		self.delta = delta
		self.l = int( math.ceil(math.log(float(1)/delta) ) )
		self.bins = int( math.ceil(math.e/epsilon) )
		self.cms = np.zeros((self.l, self.bins))

		print 'number of bins ', self.bins
		print 'number of hash functions: ', self.l

		self.a = np.random.randint(1, 100000, self.l)
		self.b = np.random.randint(1, 100000, self.l)

# ------------------------------------------------------------------------------------------
	''' 1. This function builds the count_min sketch data structure 
	    2. cms variable is a two dimensional array that stores the count_min data structure'''
# ------------------------------------------------------------------------------------------
	def count(self):

		for element in self.input_data:

			for i in range(self.l):
				hash = ( self.a[i]*element +self.b[i] )%self.bins
				self.cms[i][hash] += 1

# -----------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------
	def get_count(self, element):

		minimum = float('inf')

		for i in range(self.l):

			hash = ( self.a[i]*element +self.b[i] )%self.bins
			if self.cms[i][hash] < minimum:
				minimum = self.cms[i][hash]

		print 'count of the element :', minimum






	
