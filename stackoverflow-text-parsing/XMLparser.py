# Name: Alan Gewerc
# ID: 29961246
# Start Date: 09/05/2019
# Last Modified Date: 23/05/2019
# This script creates a class called Parser - that the main use is to extract relevant data from the main file
# There are two imports in this script: The regex library and the function preprocessLine imported from the first script

import re
from preprocessData import preprocessLine

class Parser:

	# This class is used to extract the data in the XML file. Many methods were created in order to obtain sensible
	# data from the forum questions, answers and others. The body (main content), the date, the type of post and the
	# number of words in each post.
	def __init__(self, inputString):
		self.inputString = inputString  # the inputstring is the main content - the line that will be analysed
		self.ID = self.getID()  # the other instance variables are obtained from methods of the class like get the ID
		self.type = self.getPostType()  # gets the post type (question, answer, others)
		self.dateQuarter = self.getDateQuarter()  # get the year and the quarter of the post
		self.cleanBody = self.getCleanedBody()  # get the main content of the post
		self.vocab = self.getVocabularySize()  # get the number of words

	def __str__(self):
		#print ID, Question/Answer/Others, creation date, the main content
		#Every information is printed in a new line
		return "ID: " + str(self.ID) + "\n" \
		"Type: " + str(self.type) + "\n" \
		"Creation Date: " + str(self.dateQuarter) + "\n" \
		"Size Vocab:" + str(self.vocab) + "\n" \
		"Main Content:" + str(self.cleanBody)

	def getID(self):
		# use of regular expressions to find the ID of the post
		id_search = re.search('Id="(\d+)"', self.inputString)
		return id_search.group(1)

	def getPostType(self):
		# use of regular expressions to find the post and return it as question or answer
		type_search = re.search('PostTypeId="(\d+)"', self.inputString)
		if type_search.group(1) == "1":
			return "Question"
		elif type_search.group(1) == "2":
			return "Answer"
		elif type_search.group(1) == "3" or type_search.group(1) == "4" or type_search.group(1) == "5" or \
				type_search.group(1) == "6" or type_search.group(1) == "7" or type_search.group(1) == "8" or \
				type_search.group(1) == "9":
			return "Other"
		else:
			return "Not Recognized"

	def getDateQuarter(self):
		# use of regular expressions to determine the year and quarter and return it as asked
		year_search = re.search('CreationDate="(\d+)-', self.inputString)
		month_search = re.search('CreationDate="\d+-(\d+)', self.inputString)
		if int(month_search.group(1)) > 0 and int(month_search.group(1)) < 4:
			return year_search.group(1) + "Q1"
		elif int(month_search.group(1)) > 3 and int(month_search.group(1)) < 7:
			return year_search.group(1) + "Q2"
		if int(month_search.group(1)) > 6 and int(month_search.group(1)) < 10:
			return year_search.group(1) + "Q3"
		if int(month_search.group(1)) > 9 and int(month_search.group(1)) < 13:
			return year_search.group(1) + "Q4"

	def getCleanedBody(self):
		# using the function created on the previous script
		return preprocessLine(self.inputString)

	def getVocabularySize(self):
		#write your code here
		clean_others = re.compile('[!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~]')  # all characters that must be removed
		clean_string = re.sub(clean_others, '', self.cleanBody)
		clean_string = clean_string.lower()  # eliminating upper characters
		clean_list = clean_string.split()
		clean_set = set(clean_list)  # a set has no duplicates, identifies all unique words
		return len(clean_set)   # returns the size of set with unique words
