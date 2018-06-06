import numpy as np
import math

class Bloom():

	def __init__(self, input, p):

		self.input = input
		self.p = p
		n = input.shape[0]

	# link for the formulae :https://en.wikipedia.org/wiki/Bloom_filter
		
		self.m = -int( math.ceil( float( n* math.log(p,math.e ) ) / math.pow(math.log(2, math.e),2) ) )
		self.k = int( math.ceil( ( float(self.m)/n )*math.log(2, math.e) ) )
		self.filter = np.zeros( self.m,dtype= bool )

# ------------------------------------------------------------------------------------------------------------------------
			'''This function generates k hash functions in two lists a,b'''
# ------------------------------------------------------------------------------------------------------------------------

	def hashfunctions(self,low,high):

		a = np.random.randint(low,high,self.k)
		b = np.random.randint(low,high,self.k)

		return a,b


# -----------------------------------------------------------------------------------------------------------------------------------------------------------
			'''This function simulates bloom filter working. a, b store hash functions we use hash functions of the format  (a*element+b)mod m'''
# ------------------------------------------------------------------------------------------------------------------------------------------------------------

	def train_bloom(self):

		self.a,self.b = self.hashfunctions(1,100000)

		
		for element in self.input:

			for i in range(self.k):

				hash = ( self.a[i]*element + self.b[0] ) % self.m
				self.filter[hash] = True 


# -------------------------------------------------------------------------------------------------------------------------------
	''' This function test the performance of the bloom filter by checking set containment for each element in test'''
# ------------------------------------------------------------------------------------------------------------------------------

	def test_bloom(self, test):

		falsepositives = 0

		for element in test:

			count = 0

			for i in range(self.k):

				hash = (self.a[i]*element + self.b[i] ) % self.m
				if self.filter[hash] == True:
					count = count +1

				if count == self.k and element not in self.input:
					falsepositives = falsepositives+1

		print 'number of false positives', falsepositives





