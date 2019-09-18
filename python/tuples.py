2. Tuples
# A finite, ordered list (sequence) of elements that cannot be changed(immutable)

	bag = ('notebook','pen','bottle')				    # define a tuple by the name bag
	print 'Number of items in bag:', len(bag)		    # tuple operation: length
	wardrobe = ('trousers', 'shirts', bag) 				# lets define another tuple by the name wardrobe
	print bag[0]									    # indexing to retrieve first element in a bag
	print wardrobe[2][2]

# Note that tuple within a tuple does not lose its identity 	

	print 'bottle' in bag 								# Membership - returns true
	print (1,2,3) + (4,5,6)								# Conca+enation
	print ('Hello',)* 5									# Repititi*n
	for x in (1, 2, 3): print x,						# Iteration
	
# Note: To construct a tuple with a single element, the first item needs to be specified followed by a comma

	singleton = (2,)

# Tuple Functions:

	print cmp(wardrobe, bag)							# compares elements of both tuples
	print len(wardrobe)									# gives length of tuple 
	print max(1,2,3)									# returns max value item
	print min(1,2,3)									# returns min value item
	tuple(list)											# converts list into a tuple
