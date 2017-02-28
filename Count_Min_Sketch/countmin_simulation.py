import  numpy as np 
from countmin import CountMin 




def simulation():

	# train_set = [1,1,1,1,2,3,4,5,5,5,5,6,6,7,8,8,8,9,9,9,1,2,5,7,4,3,5]
	train_set = np.random.randint(1,50, size = 1000)
	epislon = 0.018
	delta	= 0.1

	c = CountMin( train_set, epislon, delta )

	c.count()

	c.get_count(1)
	actual_count = 0

	for element in train_set:
		if element == 1:
			actual_count +=1

	print 'Actual count of the element is : ', actual_count

simulation()