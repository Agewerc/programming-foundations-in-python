# Name: Alan Gewerc
# ID: 29961246
# Start Date: 06/05/2019
# Last Modified Date: 23/05/2019
# Module of Data Visualization
# Creates a function to visualise words distribution from posts and one to see the quantity of posts across quarters

from parser_29961246 import Parser
import matplotlib.pyplot as plt
import numpy as np

def visualizeWordDistribution(inputFile, outputImage):
	# creating supporting lists that will be used for data manipulation
	data_list = []
	vocab_size_list = []  # all the valid data will be inserted in this list
	objects_list = ['0-10', '10-20', '20-30', '30-40', '40-50', '50-60', '60-70', '70-80', '80-90', '90 -100','others']
	vocab_dist= [0]*11  # this list will become the y axis in the chart

	xml_file = open(inputFile, 'r', encoding='utf-8')

	for line in xml_file:
		data_list.append(line)  # appending the data in the list

	for item in data_list:
		if item.count("<row Id") > 0:   # this is to filter invalid rows with no relevant information
			parser_item = Parser(item)
			vocab_size_list.append(int(parser_item.getVocabularySize()))  # creating a list with the "date" of each post

	# this for-loop will generate a list that has the exact amount of posts of each quarter
	for item in vocab_size_list:
		if item >= 0 and item < 10:  # every post with 0 to 9 words will be counted in the first item of the vocab_dist
			vocab_dist[0] += 1  # the same logic will operate on the following lines (10-19, 20-29, etc...)
		elif item >= 10 and item < 20:
			vocab_dist[1] +=1
		elif item >= 20 and item < 30:
			vocab_dist[2] +=1
		elif item >= 30 and item < 40:
			vocab_dist[3] += 1
		elif item >= 40 and item < 50:
			vocab_dist[4] +=1
		elif item >= 50 and item < 60:
			vocab_dist[5] +=1
		elif item >= 60 and item < 70:
			vocab_dist[6] +=1
		elif item >= 70 and item < 80:
			vocab_dist[7] +=1
		elif item >= 80 and item < 90:
			vocab_dist[8] +=1
		elif item >= 90 and item < 100:
			vocab_dist[9] += 1
		elif item >= 100:
			vocab_dist[10] += 1

	# we will use the data to generate a plot that counts the number each quarter/year by range
	index = np.arange(len(objects_list))
	plt.bar(index, vocab_dist)  # determinate the data from the y axis
	plt.xlabel('Range of Words', fontsize=7)
	plt.ylabel('Number of Words', fontsize=7)
	plt.xticks(index, objects_list, fontsize=10, rotation = 30)  # formating the chart
	plt.title('Distribution of Words from Posts', fontsize=15)
	plt.savefig(outputImage)
	plt.close()


# visualizePostNumberTrend(inputFile, outputImag):
# This function displays the trend of the post number in the Q&A site. Given the input
# file “data.xml”, you should first get the number of questions and answers in each quarter.
# Then following the time order, you should draw a line chart to annotate the number
# of posts in each quarter. Note that you should draw two lines for question number
# and answer number respectively, and add a legend in the figure to tell which line is for
# which type of posts. You should save your visualization figure into a png file named as
# “postNumberTrend.png”.

def visualizePostNumberTrend(inputFile, outputImage):
	# write your code here

	# creating supporting lists that will be used for data manipulation
	# many lists were used - for many different purposes
	support_list = []  # all the data from posts will be inserted here first

	question_date_list = []  # all the questions quarters will be be inserted here
	unique_question_date_list = []  # this will become a list with all the quartes/years but no duplicates
	count_question_date_list = []  # this will become a list with the questions of posts of each quarter

	answer_date_list = []  # all the answers quarters will be be inserted here
	unique_answer_date_list = []  # this will become a list with all the quartes/years but no duplicates
	count_answer_date_list = []  # this will become a list with the answers of posts of each quarter

	xml_file = open(inputFile, 'r', encoding='utf-8')

	for line in xml_file:
		support_list.append(line)

	for item in support_list:
		if item.count("<row Id") > 0:   # this is to filter invalid rows with no relevant information
			parser_item = Parser(item)
			if parser_item.getPostType() == 'Question':
				question_date_list.append(parser_item.getDateQuarter())  # getting the quarter from questions
			elif parser_item.getPostType() == 'Answer':
				answer_date_list.append(parser_item.getDateQuarter())  # getting the quarter from answers

	unique_question_date_list = list(set(question_date_list))  # eliminating duplicates using sets
	unique_question_date_list.sort()  # organizing the quarters from the oldest to the youngest
	unique_answer_date_list = list(set(answer_date_list))  # same logic repeats for answers
	unique_answer_date_list.sort()

	for item in unique_question_date_list:
		count_question_date_list.append(question_date_list.count(item))  # creating a list with the number of questions each quarter

	for item in unique_answer_date_list:
		count_answer_date_list.append(answer_date_list.count(item))

	# creating the plot - two lines - with legends, a title and good format
	plt.plot(unique_answer_date_list, count_answer_date_list, color='g', label = "Answers")  # answer line
	plt.plot(unique_question_date_list, count_question_date_list, color='orange', label = "Questions")  # question line
	plt.ylabel('#Number of Items', fontsize=7)
	plt.xticks(fontsize=9, rotation = 30)  # formating the chart in the x level
	plt.legend()
	plt.title('Questions and Answers by Quarter', fontsize=15)
	plt.savefig(outputImage)
	plt.close()

if __name__ == "__main__":

	f_data = "data.xml"
	f_wordDistribution = "wordNumberDistribution.png"
	f_postTrend = "postNumberTrend.png"
	
	visualizeWordDistribution(f_data, f_wordDistribution)
	visualizePostNumberTrend(f_data, f_postTrend)
