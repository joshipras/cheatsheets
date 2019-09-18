# Strings

# Sequence of characters enclosed in quotes (single and double quotes are treated the same)
# Strings are immutable

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
print "Today is the first %s of %s." %("monday", "january") # string format operator %

# %c: character       			 %s: string conversion via str
# %i, %u: signed integer  		 %u: unsigned decimal integer
# %o: octal integer				 %x, %X: hexadecimal integer  
# %e, %E: exponential notation	 %g: the shorter of %f and %e  
# %f: floating point real number %G: the shorter of %f and %E  

# String Methods:

str1 = "hi! \t How are you doing today?"
str2 = "Where are you going?"

print str1.capitalize() 					     # only first character capitalized
print str1.center(18[,aaaa])	    		     # center string and paste fill char before and after 
print str1.count("oi", start=0, end=len(str1))   # count occurence of substring in sub
print str1.encode('base64','strict')			 # return string encoded to specified encoding		 
print str1.startswith("hi")						 # true if string starts with the specified prefix
print str1.endswith("ay?",0,len(str1)) 		 	 # true if string ends with specified suffix
print str1.expandtabs(16)			         	 # return copy of string where all tab characters expanded
print str2.find("are", 0, len(str1))			 # returns lowest index in string where sub is found
print str2.index("are", 0, len(str))		     # like find(), but raise ValueError when the substring is not found
print str2.isalnum()						     # true if all characters alphanumeric, at least one character
print str1.isalpha()							 # true if all characters alphabetic, at least one character
print str2.isdigit()						     # true if all characters digits, at least one character
print str1.lower()
print str2.islower()						     # true if all cased characters are lowercase and there's at least one cased character	
print str1.isspace()							 # true if there are only whitespace characters 
print str1.istitle()							 # true if the string is a titlecased string
print str1.isupper()							 # true if all upper case
print str1.upper()								 # convert to upper case

s = "-";
seq = ("a", "b", "c"); 							 # This is sequence of strings.
print s.join( seq )							     # return a string which is the concatenation of the strings in the sequence seq. The separator between elements is the string providing this method.

print str1.ljust(50,0)							 # return string left justified in a string of length width. 
print str1.lstrip()								 # remove whitespace
print str1.lstrip('')
print str1.lstrip('hi')
print str1.replace("How", "What", 1)			 # return a copy of the string with all occurrences of substring old replaced by new. 											 
												 # if the optional argument count is given, only the first count occurrences are replaced.
print str1.rfind("are", 0, len(str1))			 # return the highest index in the string where substring sub is found, 
												 # such that sub is contained within s[start,end]. Optional arguments start and end are interpreted as in slice notation. 
print str1.rindex("are", 0, len(str1))			 # like rfind() but raises ValueError when the substring sub is not found.
print str1.rjust(50,0)							 # return the string right justified in a string of length width. Padding is done using the specified fillchar (default is a space). 
print ' a b c '.rsplit(None, 1)					 # return a list of the words in the string, using sep as the delimiter string. 
												 # if maxsplit is given, at most maxsplit splits are done, the rightmost ones. 
												 # if sep is not specified or None, any whitespace string is a separator. 
												 # except for splitting from the right, rsplit() behaves like split().
print '   spacious   '.rstrip()					 # return a copy of the string with trailing characters removed.    
print ‘blue,red,green’.split(",")				 # return a list of the words in the string, using sep as the delimiter string. 
												 # if sep is not specified or is None, a different splitting algorithm is applied. 
												 # first, whitespace characters (spaces, tabs, newlines, returns, and formfeeds) are stripped from both ends. 
												 # then, words are separated by arbitrary length strings of whitespace characters. 
												 # consecutive whitespace delimiters are treated as a single delimiter ("'1 2 3'.split()" returns "['1', '2', '3']"). 
												 # splitting an empty string or a string consisting of just whitespace returns an empty list.

print str1.splitlines(True)					 	 # return a list of the lines in the string, breaking at line boundaries(\n). 
												 # line breaks are not included in the resulting list unless keepends is given and true.

print str1.swapcase()							 # uppercase characters converted to lowercase and vice versa.
print str1.title()								 # first letter of each word capitalized
print str1.zfill(width)							 # return the numeric string left filled with zeros in a string of length width. The original string is returned if width is less than len(s).

intab = "aeiou"									 # return a copy of the string where all characters occurring in the optional argument deletechars are removed, and the remaining characters have been mapped through the given translation table, which must be a string of length 256.
outtab = "12345"								 # for Unicode objects, the translate() method does not accept the optional deletechars argument. 
												 # Instead, it returns a copy of the s where all characters have been mapped through the given translation table which must be a mapping of Unicode ordinals to Unicode ordinals, Unicode strings or None. Unmapped characters are left untouched. 	
trantab = maketrans(intab, outtab)		
str = "this is string example....wow!!!";
print str.translate(trantab)