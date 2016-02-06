#--Fractured Code--

#Inpput & Output 
#print (raw_input('what is your name?'))

#x = raw_input('What is your name?')
#print ('your name is' + x)

#----------------------------------------------------

#[1,2,3]
#x = input('What are the first 10 perfect squares?')
#map(lambda x: x*x, range(10))

#x = None
#while not x:
#	try:
#		x = int(raw_input())
#	except ValueError:
#		print 'Invalid Number'

#----------------------------------------------------
# To run this module, a txt document would first have to be created - file name: test.txt
#f = open('test.txt', 'r')
#for line in f:
#	print line[0]
#f.close()

#with open("text.txt", "r") as txt:
#	for line  in txt:
#		print line

#for line in open ('test.txt', 'r'):
#	print line[0]

#c = f.read(1)
#while len (c) > 0:
#	if len(c.strip()) > 0: print c,
#	c = f.read(1)

#f.seek(0)

#----------------------------------------------------

#import sys
#for line in sys.stdin:
#	print line,

#----------------------------------------------------

#if True:
#	print "True"
#else:
#	print "False"

#if True:
#	print "Answer"
#	print "True"
#else: 
#	print "Answer"
#	print "False"

#----------------------------------------------------

#import sys

#try: 
#	file = open(file_name, "w")
#except IOError:
#	print "There was an error writing to", file_name 
#	sys.exit
#print "Enter '", film_finished,
#print "' When finished"
#while file_text != file_finish:
#	file_text = raw_input("Enter text: ")
#	if file_text == file_finish:
#		file.close
#		break
#	file.write(file_text)
#	file.write("\n")
#file.close()
#file_name = raw_input("Enter filename: ")
#if len(file_name) == 0:
#	print "Next time please enter something"
#	sys.exit()
#try:
#	file = open(file_name, "r")
#except IOError:
#	print "There was an error reading file"
#	sys.exit()
#file_text = file.read()
#file.close()
#print file_text

#----------------------------------------------------

#total = item_one + \
#		item_two + \
#		item_three

#days = [ 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday' ]

#----------------------------------------------------

#days = ['Moday,' 'Tuesday', 'Wednesday','Thursday', 'Friday']

#----------------------------------------------------

#raw_input("\n\nPress the enter key to exit.")

#----------------------------------------------------

#def fib(n):
#	a, b = 0, 1
#	while b < n:
#		print b, 
#		a, b = b, a+b

#def fib2(n):
#	result = []
#	a, b = 0, 1
#	while b < n:
#		result.append(b)
#		a, b = b, a+b
#	return result

#import fibo

#fibo.fib(1000)
#fibo.fib(100)
#fibo.__nam__

#----------------------------------------------------

#if __name__ == "__main__":
#	import sys
#	fib(int(sys.argv[1]))

#----------------------------------------------------
#Unittesting

#import unittest

#def IsOdd(n):
#	return n % 2 == 1

#class IsOddTests(unittest.TestCase):

#	def testOne(self):
#		self.fallUnless(IsOdd(1))

#	def testTwo(self):
#		self.failif(IsOdd(2))

#def main():
#	unittest.main()

#if __name__ == '__main__':
#	main()

#----------------------------------------------------
#Unittesting 

#30 Nov 2004: Dinner with the David
#April 10: Happy days
#Wednesday: Piano lessono
#Last Thursday: Goody night at book study. Yum. 
#-1: Pay the rent!

#import unittest
#class FooTests(unittest.TestCase):

#	def testFoo(self):
#		self.failUnless(False)

#def main():
#	unittest.main()

#if __name__ == '__main__':
#	main()

#def testMatches(self):
#	p = DatePattern(2004, 9, 28)
#	d = datetime.date(2004, 9, 28)
#	self.failUnless(p.matches(d))

#class DatePattern:

#	def __init__(self, year, month, day):
#		pass

#	def matches(self, date):
#		return True 

#def testMatchesFalse(self):
#	p = DatePattern(2004, 9, 28)
#	d = datetime.date(2004, 9, 29)
#	self.failIf(p.matches(d))

#class DatePattern:

#	def __init__(self, year, month, day):
#		self.date = datetime.date(year, month, day)

#	def matches(self, date):
#		return self.date == date

#def testMatchesYearAsWildCard(self):
#	p = DatePattern(0, 4, 10)
#	d = datetime.date(2005, 4, 10)
#	self.failUnless(p.matches(d))

#class DatePatter:
	
#	def __init__(self, year, month, day):
#		self.year = year
#		self.month = month
#		self.day = day

#	def matches(self, date):
#		return ((self.year and self.year == date.year or True) and self.month == date.month and self.day == date.day)

#def testMatchesYearAndMonthAsWildCards(self):
#	p = DatePattern(0, 0, 1)
#	d = datetime.date(2004, 10, 1)
#	self.failUnless(p.matches(d))

#def matches(self, date):
#	return ((self.year and self.year == date.year or True) and
#			(self.month and self.month == date.month or True) and
#			self.day == date.day)

#def testMatchesWeekday(self):
#	p = DatePattern(__init__)

#def testMatchesWeekday(self):
#	p = DatePattern(0, 0, 0, 2)
#	d = datetime.data(2004, 9, 29)
#	self.failUnless(p.matches(d))

#def __init__(self, yar, month, day, weekday=0):
#	self.year = year
#	self.month = month
#	self.day = day
#	self.weekday = weekday

#def matches(self, date):
#	return ((self.year and self.yar == date.year or True) and
#			(self.month and self.month == date.month or True) and
#			(self.day and self.day == date.day or True) and
#			(self.weekday and self.weekday == date.weekday() or True())

#def matches(self, date):
#	return (self.yearMatches(date) and
#			self.monthMatches(date) and
#			self.dayMatches(date) and
#			self.weedayMatches(date))

#def yearMatches(self, date):
#	if not self.year: return True
#	return self.month == date.month

#def dayMatches(self, date):
#	if not self.day: return True
#	return self.day == date.day

#def weekdayMatches(self, date):
#	if not self.weekday: return True
#	return self.weekday == date.weekday()

#def testMatchesLastWeekday(self):
#	p = DatePattern(0, 0, 0, 3)

#----------------------------------------------------
# While Loops

#a = 0
#while a < 5:
#	a += 1 # Same as a = a + 1
#	print (a)

#a = 1
#s = 0
#print ('Enter Numbers to add to the sum.')
#print ('Enter 0 to quit.')
#while a != 0:
#	print ('current sum:', s)
#	a = raw_input('Number? ')
#	a = float(a)
#	s += a
#print('Total Sum = ',s)

#----------------------------------------------------
# For Loops

#while 1 == 1:
#	print ("Help, Im stuck in a loop.")

#----------------------------------------------------
#Refacturing code 

#a = 0
#b = 1
#count = 0
#max_count = 20
#while count < max_count:
#	count = count + 1
	# We need to keep track of a since we change it
#	old_a = a
#	old_b = b
#	a = old_b
#	b = old_a + old_b
	# Notice that the , at the end of a print statement keeps it
	# from switching to a new line
#	print (old_a),

#----------------------------------------------------
#passwords

# Waits until a password has been entered. Use control-C to break out without the password.

#Note that this must not be the password so that the while loop runs at least once.
#password = "foobar"

#note that != means not equal
#while password != "unicorn":
#	password = raw_input("Password: ")
#print ("Welcome in")

#----------------------------------------------------
#Number Loops

#onetoten = range(1,11)
#for count in onetoten:
#	print (count)

#----------------------------------------------------

#for count in range(1,11):
#	print (count)

#----------------------------------------------------

#for a in range(10):
#	print (a)

# The above code acts exactly the same as:

#for a in range(0, 10):
#	print (a)

#for a in range(0, 10):
#	print (a)

#----------------------------------------------------
# Print item with word

#demolist = ['life', 42, 'the universe', 6, 'and', 7, 'everything']
#for item in demolist:
#	print ("The current item is: %s" % item)

#----------------------------------------------------
# Maths multiplication 

#list = [2, 4, 6, 8]
#sum = 0
#for num in list:
#	sum = sum + num
#print ("The sum is: %d" % sum)

# Or you could write a program to find out if there are any duplicates in a list like this program does:

#list = [4, 5, 7, 8, 9, 1, 0, 7, 10]
#list.sort()
#print ("1.sort()", "\t1:",1)
#prev = 1[0]
#print ("prev = 1[0]", "\tprev:", prev)
#prev = list [0]
#del 1[0]
#print ("del 1[0]", "\t1:", 1)
#for item in 1:
#	if prev == item:
#		print ("Duplicate of ", prev, " Found")
#	print("if prev == item:", "\tprev:",prev, "\titem:", item)
#	prev = item
#del list [0]
#for item in list:
#	if prev == item:
	#print ("Duplicate of ", prev, " Found")
#		prev = item 

#----------------------------------------------------
# For Loops

#a = 1
#b = 1
#for c in range(1, 10):
#	print(a)
#	n = a + b
#	a = b
#	b = n 
#print ("")

#----------------------------------------------------

#for i in xrange(0, 10000000):
#	print (i)
	# end for 

#----------------------------------------------------

#found = False # Initial assumption
#for value in values_to_check():
#	if is_what_im_looking_for(value):
#		found = True
#		break
	 #end if
	 #end for
	# ...found is True on success, False on failure

#----------------------------------------------------
# Loops

#Values = iter(values_to_check())
#while True:
#	value = next(values, None)
#	if value == None:
#		found = False
#		break
# End if
#	if is_what_im_looking_for(value):
#		found = True
#		break
		# End if
		# End while
		# ...found is True on success, False on failure

#----------------------------------------------------
#Reading Files

#from sys import argv
#script, filename = argv
#txt = open(filename)

#print "Here's your file %r:" % filename
#print txt.read()

#print "Type the filename again:"
#file_again = raw_input("> ")
#txt_again = open(file_again)
#print txt_again.read()

#----------------------------------------------------