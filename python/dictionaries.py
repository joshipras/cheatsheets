## Dictionaries

# key:value pairs seperated by commas

	dict1 = {'Name': 'Adam', 'Age': 7, 'Class': 'First'}
	dict2 = {'Name': 'Lily', 'Age': 10, 'Class': 'First'}

# keys need to be immutable objects(like strings). Values can be mutable

	print("Adam's Age is", dict1['Age']) 				# Access values using keys
	dict1['Age'] = 8 									# Update existing entry
	dict1['City'] = "Boston"							# Add a new entry 

# To remove elements of a dictionary:

	del dict1['Name']; 								    # remove entry with key 'Name'
	dict1.clear();    								    # remove all entries in dict
	del dict1 ;        								    # delete entire dictionary

# Dictionary Functions:

	dict1 = {'Name': 'Adam', 'Age': 7, 'Class': 'First'}

	print cmp(dict1, dict2)								# compares elements of 2 dicts
	print len(dict1)									# gives length of dictionary
	print str(dict)										# produces a printable string representation of dictionary

# Dictionary Methods:

	dict1.copy()										# Returns a shallow copy of dictionary dict
	dict1.fromkeys()									# Create a new dictionary with keys from seq and values set to value.
	dict1.get('Name', default = None)					# For key key, returns value or default if key not in dictionary
	dict1.has_key('Age')								# Returns true if key in dictionary dict, false otherwise
	dict1.items()										# Returns a list of dict's (key, value) tuple pairs
	dict1.keys()										# Returns a list of dict's keys
	dict1.setdefault(key, default = None)				# Similar to get(), but will set dict[key]=default if key is not already in dict
	dict1.update(dict2)									# Adds dictionary dict2's key-values pairs to dict
	dict1.values()										# Returns list of dictionary dict's values
	dict1.clear()										# Removes all elements
