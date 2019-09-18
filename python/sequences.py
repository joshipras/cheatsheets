# Sequences

- 
# Types of sequences:

# strings: sequence of characters enclosed in quotes (single and double quotes are treated the same)
# strings are immutable

string1 = "Hello Python!"

# To create a unicode string, use the \u prefix

string2 = 'Goodbye\u0020World !'      # escape sequence indicates the Unicode character with the ordinal value0x0020


# String special Operators:

print "Hello" + "Python!"			  # concatenation
print "Hello" * 2					  # repitition
print string2[1]					  # slice
print string[1:4]					  # range slice
print "o" in string1				  # membership
print "w" not in string1			
print r'\n'							  # raw character: supresses special characters
print R'\n'
print "Today is the first %s of %s."  # string format operator %

# %c: character       			 %s: string conversion via str
# %i, %u: signed integer  		 %u: unsigned decimal integer
# %o: octal integer				 %x, %X: hexadecimal integer  
# %e, %E: exponential notation	 %g: the shorter of %f and %e  
# %f: floating point real number %G: the shorter of %f and %E  

# String Methods:
str2 = "hi! \t How are you doing today?"
str2 = "Where are you going?"

print str.capitalize() 					     # only first character capitalized
print str.center(18[,aaaa])	    		     # center string and paste fill char before and after 
count("oi", start=0, end=len(str))		     # count occurence of substring in sub
decode([encoding[, errors]])		 		 #
encode([encoding[,errors]])					 #
print str.endswith("ay?",0,len(str)) 		 # return true if string ends with specified suffix
print str.expandtabs(16)			         # return copy of string where all tab characters expanded
print str2.find("are", 0, len(str))			 # returns lowest index in string where sub is found
print str2.index("are", 0, len(str))		 # like find(), but raise ValueError when the substring is not found
print str2.isalnum()						 # true if all characters alphanumeric, at least one character
print str2.isalpha()						 # true if all characters alphabetic, at least one character
print str2.isdigit()						 # true if all characters digits, at least one character
print str2.islower()						 # true if all cased characters are lowercase and there's at least one cased character	




print str.isspace()							 # true if there are only whitespace characters 
print str.istitle()							 # true if the string is a titlecased string
print str.isupper()							 # true if all upper case
join(seq)									 # return a string which is the concatenation of the strings in the sequence seq. The separator between elements is the string providing this method.

str.ljust(	width[, fillchar])			     # Return string left justified in a string of length width. 
lower( )                                     # Return an uppercase copy of the string.
upper(  )
lstrip(	[chars])                             # Return a copy of the string with leading characters removed. chars argument: set of characters to be removed. 
replace(	old, new[, count])               # Return a copy of the string with all occurrences of substring old replaced by new. If the optional argument count is given, only the first count occurrences are replaced.
rfind(	sub [,start [,end]])                 # Return the highest index in the string where substring sub is found, such that sub is contained within s[start,end]. Optional arguments start and end are interpreted as in slice notation. Return -1 on failure.
rindex(	sub[, start[, end]])                 # Like rfind() but raises ValueError when the substring sub is not found.
rjust(	width[, fillchar])                   # Return the string right justified in a string of length width. Padding is done using the specified fillchar (default is a space). The original string is returned if width is less than len(s). Changed in version 2.4: Support for the fillchar argument.
rsplit(	[sep [,maxsplit]])                   # Return a list of the words in the string, using sep as the delimiter string. If maxsplit is given, at most maxsplit splits are done, the rightmost ones. If sep is not specified or None, any whitespace string is a separator. Except for splitting from the right, rsplit() behaves like split() which is described in detail below. New in version 2.4.
rstrip(	[chars])                             # Return a copy of the string with trailing characters removed. The chars argument is a string specifying the set of characters to be removed. If omitted or None, the chars argument defaults to removing whitespace. The chars argument is not a suffix; rather, all combinations of its values are stripped:
split(	[sep [,maxsplit]])                   # Return a list of the words in the string, using sep as the delimiter string. 
                                             # If maxsplit is given, at most maxsplit splits are done. (thus, the list will have at most maxsplit+1 elements). If maxsplit is not specified, then there is no limit on the number of splits (all possible splits are made). 
                                             # Consecutive delimiters are not grouped together and are deemed to delimit empty strings (for example, "'1,,2'.split(',')"returns "['1', '', '2']"). 
                                             # The sep argument may consist of multiple characters (for example, "'1, 2, 3'.split(', ')" returns "['1', '2', '3']"). Splitting an empty string with a specified separator returns "['']".
splitlines(	[keepends])                      # Return a list of the lines in the string, breaking at line boundaries. Line breaks are not included in the resulting list unless keepends is given and true.
startswith(	prefix[, start[, end]])          # Return True if string starts with the prefix, otherwise return False. With optional start, test string beginning at that position. With optional end, stop comparing string at that position.
strip(	[chars])
swapcase(	)                                # uppercase characters converted to lowercase and vice versa.
title(	)                                    # Return a titlecased version of the string: words start with uppercase characters, all remaining cased characters are lowercase.
translate(	table[, deletechars])            # Return a copy of the string where all characters occurring in the optional argument deletechars are removed, 
                                             # and the remaining characters have been mapped through the given translation table, which must be a string of length 256.
zfill(	width)                               # Return numeric string left filled with zeros in a string of length width. 
                                             # Original string is returned if width is less than len(s).








