# Name: Alan Gewerc
# ID: 29961246
# Start Date: 05/05/2019
# Last Modified Date: 23/05/2019
# Module of Data pre-processing:
# This script gets one input - a XML file - and returns two outputs - txt documents
# It is meant to clean a file that has many forum conversations and separate questions from answers on the txt files
# The script has two functions: preprocessLine and splitFile

# Regular Expressions is the only library used in this script
import re

def preprocessLine(inputLine):
	# pre process the data in each line

	# Creating patterns to clean the content of the line - extracting the body
	clean_left = re.compile('<row(.*?)Body="')
	clean_right = re.compile('" />')
	inputLine = re.sub(clean_left, '', inputLine)  # eliminate the left side of the body
	inputLine = re.sub(clean_right, '', inputLine)  # eliminate the right side of the body

	# while any of the seven patterns is found in inputLine the work must continue
	while inputLine.count("&amp;") > 0 or inputLine.count("&quot;") > 0 or inputLine.count("&apos;") > 0 or\
			inputLine.count("&gt;") > 0 or inputLine.count("&lt;") > 0 or inputLine.count("&#xA;") > 0 or\
			inputLine.count("&#xD;") > 0:

			inputLine = inputLine.replace("&amp;", "&")  # each of this characters will be replaced by the proper one
			inputLine = inputLine.replace("&quot;", '"')
			inputLine = inputLine.replace("&apos;", "'")
			inputLine = inputLine.replace("&gt;", ">")
			inputLine = inputLine.replace("&#xA;", " ")
			inputLine = inputLine.replace("&lt;", "<")
			inputLine = inputLine.replace("&#xD;", " ")

	clean_tag = re.compile('<.*?>')  # this pattern is used to identify all html tags that will be cleaned
	inputLine = re.sub(clean_tag, '', inputLine)  # this function will eliminate any html tag using the pattern 'clean_tag'
	inputLine = inputLine.strip(" ")

	return inputLine  # the line is returned after the preprocessing


def splitFile(inputFile, outputFile_question, outputFile_answer):
	# preprocess the original file, and split them into two files.
	# please call preprocessLine() function within this function
	# write you code here

	xml_file = open(inputFile, 'r', encoding='utf-8')  # open the file in read mode
	outputFile_question = open(outputFile_question, 'a', encoding='utf-8')  # open the files in append mode
	outputFile_answer = open(outputFile_answer, 'a', encoding='utf-8')

	data_list = []  # we will use a list to store all the lines from the file

	for line in xml_file:
		data_list.append(line)  # all the data from the file is now in this list, which will be used to the processing

	# This patterns are used to identify it as a question or answer
	question = re.compile('PostTypeId="1"')
	answer = re.compile('PostTypeId="2"')

	for item in data_list:
		if re.search(question, item):   # if the question pattern is found....
			item = preprocessLine(item)  # do the data processing asked by using the function above
			outputFile_question.write(item)  # and write it in the proper file
		elif re.search(answer, item):  # the same process occurs if the answer pattern is found
			item = preprocessLine(item)
			outputFile_answer.write(item)


	# closing all files, this function has no return
	xml_file.close()
	outputFile_question.close()
	outputFile_answer.close()

if __name__ == "__main__":

	f_data = "data\\data.xml"
	f_question = "output\\question.txt"
	f_answer = "output\\answer.txt"

	splitFile(f_data, f_question, f_answer)
