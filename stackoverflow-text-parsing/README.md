# Parsing Text from Stack Overflow

Implementation of a basic parser to investigate the natural-language posts from Q&A (Question and Answering) site. The parser is able to perform basic data extraction, statistical analysis on a number of linguistic features and also to present the analysis results using some form of visualization.


Python libraries required:
- RE
- Pandas


## Data and Files Overview

`data.xml:` An XML file with 10.700 questions and answers from Stack Overflow about hardware. 


`preprocessData.py:` Module of Data pre-processing: Defines one function of pre-processing and one function to read the data, pre-process it and save .txt files with the answers and questions from all posts in .xml file.

`parser.py:` The class Parser is used to easily parse and deal with given rows of the data representing posts in XML format. Some useful methods are defined and explained below, allowing the user to easily get the type, ID, date quarter, cleaned body and vocabulary size of the post. A string overloading method is also defined to allow proper printing of the object instances of this class.

`dataVisualization.py:` The dataVisualization module defines two functions, one to visualize the vocabulary size distribution and the other to visualize the post number trend.

## Output Files

`question.txt:` A file with all the questions from the data.xml parsed. 

`answer.txt:` A file with all the answers from the data.xml parsed. 


## Usage

To create an instance named my_parse of the class Parser, the user should just type:

`my_parse = Parser(post_line)`

Where **post_line** is a string representing one single post (question or answer).


### Visuals

Use the functions:

`visualizeVocabularySizeDistribution(inputFile, outputImage)`

Here, we define the inputFile as the XML with all posts and outputImage as the name of the image to be produced and saved in the present working directory. The plot will be a bar plot representing the vocabulary size distribution across all posts. Each bar represents the amount of posts that contain a certain range of distinct words in its body.

![viz1](https://github.com/Agewerc/programming-foundations-in-python/blob/master/stackoverflow-text-parsing/output/postNumberTrend.png)

`visualizePostNumberTrend(inputFile, outputImage)`

Again, we define the inputFile as the XML with all posts and outputImage as the name of the image to be produced and saved in the present working directory. The plot will be a line chart with two lines: a red one representing the name of questions posted in each quarter, and a blue on representing the number of answers posted in one quarter.


![viz1](https://github.com/Agewerc/programming-foundations-in-python/blob/master/stackoverflow-text-parsing/output/wordNumberDistribution.png)
