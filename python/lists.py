## Lists

# Comma separated values within square brackets.
# Items may not necessarily be of the same type.

list1 = ['apple', 'banana', 'orange']
list2 = [1, 2, 3, 4, 5]
list3 = ['boston', 'chicago', 10, 26]


print "first item in list1:", list1[0]	        	# accessing list elements
print "first 3 items in list2:", list2[0:2] 

list3[2] = 20								                      # updating lists
print list3

del list3[3]								                      # deleting elements
print list3

print len(list3)						                    	# length 
print list1 + list2					                   		# concatenation
print list1 * 2						                    		# repitition
print 'apple' in list1						                # membership
for x in list1: print x,					                # iteration
  
# List Functions:

print cmp(list1, list2)						                # compares elements of both tuples
print len(list1)							                    # gives length of tuple 
print max(list2)							                    # returns max value item
print min(list2)						                    	# returns min value item
list(seq)									                        # converts list into a tuple

# List Methods

list1.append('strawberry')					              # append new object to list
list1.count('apple')						                  # returns count of object in list
list1.extend(seq)							                    # appends contents of seq ro list		
list1.index('apple')						                  # returns lowest index at which 'apple' appears
list1.insert(0, 'mango')					                # insert object mango into list at offset index
list1.pop(obj=list1[-1])					                # removes and returns last object or obj from list
list1.remove('apple')						                  # removes object from list
list1.reverse()								                    # reverses objects in list
list1.sort()								                      # sorts objects of list, use compare func if given 
