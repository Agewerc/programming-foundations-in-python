#Author: Alan Gewerc
#Start Date: 28/03/2019
#End Date: 09/04/2019
#StudentID: 29961246


# This is a Nerd Rate calculator - user will input a list with Nerd Score and will get a list with Nerd Rates
# A if else structure was built to classify the Nerd Scores
# a For Loop is responsible to guarantee every one of the Scores was classified


def countStudentClass(studentScore_list):
    if len(studentScore_list) < 1:
        print("Please add at least 1 item into the list")
        return 0

    nerdCount_list = [0] * 7  # intialize the output list

    # Please write your own program here

    #    nerdOptions = ['Nerdlite','Nerdling','Nerdlinger','Nerd','Nerdington','Nerdrometa','Nerd Supreme']

    for nerdPerson in studentScore_list:  # checking every one of the nerds in the list

        if nerdPerson < 0:  # special scenario, no classification for negative numbers
            print(nerdPerson, " is a negative number, will not considered!")

        if nerdPerson >= 0 and nerdPerson < 1:
            nerdCount_list[0] += 1

        elif nerdPerson >= 1 and nerdPerson < 10:
            nerdCount_list[1] += 1

        elif nerdPerson >= 10 and nerdPerson < 100:
            nerdCount_list[2] += 1

        elif nerdPerson >= 100 and nerdPerson < 500:
            nerdCount_list[3] += 1

        elif nerdPerson >= 500 and nerdPerson < 1000:
            nerdCount_list[4] += 1

        elif nerdPerson >= 1000 and nerdPerson < 2000:
            nerdCount_list[5] += 1

        elif nerdPerson >= 2000:
            nerdCount_list[6] += 1

    return nerdCount_list

if __name__ == '__main__':
    # test cases
    # studentScore_list = []  #
    studentScore_list = [23, 76, 1300, 600]  # output should be [0, 0, 2, 0, 1, 1, 0]

    print(countStudentClass(studentScore_list))
