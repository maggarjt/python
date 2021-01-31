# using find() vs re.search

hand = open('mbox-short.txt')
for line in hand:	
	line = line.rstrip()
	# strip removes whitespace characters from R side of line
	#strip(). rstrip(), lstrip()
	if line.find('From:') >= 0;
	print(line)

# find()  returns 1 if string is there, 0 if it is not
# re.search('str', 'where')   returns Boolean value 


#using re.search()  , parameters (text or regex sequence, where to search)

hand = open('mbox-short.txt')
for line in hand:	
	line = line.rstrip()
	if re.search('From', line)
		print(line)

---------------------------------------------------------------------------------------------------------------------






# startswith vs re.search()

hand = open('mbox-short.txt')
for line in hand:	
	line = line.rstrip()
	if line.startswith('From'):
		print(line)


hand = open('mbox-short.txt')
for line in hand:
	line = line.rstrip()
	if re.search('^From', line)
	print(line)


---------------------------------------------------------------------------------------------------------------------
'''WHY?    We will run out of string methods built in to python as complexity increases, 
regex will  make complex searchjes easier as you iterate through lines'''


------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------


#Regex ^X.*:      (starts with X, any character 0 or more times, then ':')

#regex ^X-\S+:    (starts with 'X-', one or more non white space characters, ':')

# [0-9] +    any number 1 or more times


#re.search returns T, F
# re.findall() returns list of search items in nelwy formed [str,str,str]

----------------------------------------------------------------------------------------------------

import re
x = 'My 2 favorite numebrs are 19 and 42'
y = re.findall('[0-9]+', x) #creates str list
print(y)

#print a list of strings (regex default)

------------------------------------------------------------------------


import re

newlist = []
x = 'My 2 favorite numebrs are 19 and 42'
y = re.findall('[0-9]+', x) #creates str list
for i in y:
	newlist.append(int(i))

print(newlist)
 

#print a list of ints instead of normally regex default of  list of strings

---------------------------------------------------------------------------------------------------

import re
x = 'My 2 favorite numebrs are 19 and 42'
y = re.findall('[0-9]+', x) #creates str list
print(y)

y = re.findall('[AEIOU]+', x) # finds 1 or more vowels inside of x
print(y)
 #matches nothing, returns a blank list

 -----------------------------------------------------------

 #  regex ->   ^F.+:   (starts with F, 1 or more of any characters, ':')
 # greedy matching example
 import re
 x = 'From: Using the : character'
 y = re.findall('^F.+:', x)
 print(y)

# returns (From: Using the :)

---------------------------------------------
#non greedy

import re
 x = 'From: Using the : character'
 y = re.findall('^F.+?:', x)
 print(y)
#returns lst of ['From:']
-----------------------------------------------------


#Fine tuning
x = 'From stephen.marquardt@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('\S+@\S', x)
print(y)
#outputs [stephen.marquardt@uct.ac.za]
x = 'From stephen.marquardt@uct.ac.za Sat Jan  5 09:14:16 2008'

-----------------------------------------------------------------
# finding sequence, extracting subsequence using () in regex

y = re.findall('^From (\S+@\S+)', x)
print(y)
#outputs [stephen.marquardt@uct.ac.za]

-----------------------------------------------------------------
#APPLICATIONS FOR Regex

data = 'From stephen.marquardt@uct.ac.za Sat Jan  5 09:14:16 2008'
atposition = data.find('@')
print(atposition)  # output 21


space_position = data.find('', atposition) #second paramter is index to start searching
print(space_position)


host = data[atpos + 1 : space_position]

print(host) #outputs uct.ac.za
-----------------------------------------------------
DOUBLE SPLIT PATTERN  using split    and using regex

split example

words = line.split() # returns a list of words [str,str,str]
email = words[1]
pieces = email.split('@') # list of [str, str] ['stephen.marquardt', 'uct.ac.za']
print(pieces[1])  #outputs 'uct.ac.za'

------------------------------------------------------------------
regex example

import re
lin = 'From stephen.marquardt@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('@([^ ]*') # find 0 or more non blank characters after the '@'


#[^ ] = non blank character  (includes all letters, numbers and breakouts)   triggered by ''???

#\S = non white space character (all letters, numbers)  triggered by '' and  breakouts???

---------------------------------------------------------------------------------

import re
lin = 'From stephen.marquardt@uct.ac.za Sat Jan  5 09:14:16 2008'
y = findall('FROM .*@([^ ]*)', lin)
# FROM space , 0 or more of any character, '@', zero or more of any non blank character
print(y)

#outputs ['uct.ac.za']
-----------------------------------------------------
import re
hand = open('mbox-short.txt')
numlist = list() #instantiation of blank list using list method of python core
for line in hand:
	line = line.rstrip()
	stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
	if len(stuff) != 1 : continue
	num = float(stuff[0])
	numlist.append(num)
print('Maximum:' , max(numlist)

#outputs max of list of all x-dspam-confidence values in mbox-short.txt file

---------------------------------------------------------------
ESCAPE character

import re
x = "We just received $10.00 for cookies."
y = re.findall('\$[0-9.]+', x) #\$ due to $ being end of line search in regex
print(y) #outputs $10.00