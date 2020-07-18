#Author: Alan Gewerc
#Start Date: 28/03/2019
#End Date: 09/04/2019
#StudentID: 29961246

# The present program calculates a nerd score for the user
# A Menu is offered to the user that can choose each step he will run
# To obtain the nerd score the user must input 3 variables: fandomScore, hobbieScore, sportsItemsNumber
# Each input has to be an integer and has different specifications
# Every input is checked and returns an error message if there is any inputation error
# A nerd rate can also be calculated after nerd score is calculated


# STARTING POINT

# important variables declaration
# These are the inputs from the user to calculate nerd score and the result variable
fandomScore = "empty"
hobbieScore = "empty"
sportsItemsNumber = "empty"
nerdScore = "empty"

# These are supporting variables that the user will input through the process to support the menu structure
inputQuestion1 = "a"
inputQuestion2 = "b"
inputQuestion3 = "c"
MenuQuestion = "menu"

# A try-except structure is used in this work
# These are customized exceptions that will be used for variable input checking
# Built-in python Exceptions are also used in this code


class NonMultipleOfFourError(Exception):
    pass


class NonNegativeError(Exception):
    pass


# The user will always come back to the menu after answering every question.
# The system will only stop running when the user decides to quit
while MenuQuestion != "q":  # the user will need to input "q" on the menuquestion for this while to "break"

    # This is the menu question
    MenuQuestion = input("Select Option: \n a - Input Scores \n b - Calculate Nerd Score \n \
c - Calculate Nerd Rating \n q - quit \n: ")

    # MenuQuestion = "a"
    #  Input or change any of the scores (fandomScore, hobbieScore, sportsItemNumber)

    if MenuQuestion == "a":  # "a" is for inputing the scores (fandomScore, hobbieScore and sportsItemsNumber

        # Input fandomScore

        while True:  # while the user does not input a valid answer for inputQuestion1(y or n) - keep asking

            # The may skip every variable input. For instance, if he wants to change only one of the variables
            inputQuestion1 = input("Would you like to input(or change) your Fandom Score? Type y for yes, type n for no: ")

            if inputQuestion1 == "y":

                while True:  # this will enforce the user to input a valid fandom score (positive integer)
                    try:
                        fandomScore = int(input("Enter the number of things that you are fan off: "))
                        if fandomScore <= 0:
                            raise NonNegativeError
                        break  # the while loop will only find the break with a valid input
                    except NonNegativeError:
                        print("Error: This number should be a higher than zero, please try again!")
                    except ValueError:
                        print("Error: This should be a positive integer, please try again!")

                break  # breaks the while loop that checks inputQuestion1 (not fandomScore)

            if inputQuestion1 == "n":  # in case the user wants to skip the fandomScore
                break

            else:  # in case inputQuestion1 is different than y or n - not accepted, the while will not break
                print("invalid input, please type y for yes and n for no!")

        print("lets move on!")

        # A very similar structure is repeated for the next variables (hobbieScore and sportsItemsNumber)

        # Input hobbieScore
        while True:  # This will is related to the inputQuestion2 variable. The user must give a valid answer(y/n)

            inputQuestion2 = input("Do you want to input(or change) your Hobbie Score? (y/n): ")

            if inputQuestion2 == "y":
                while True:  # This will is related to the hobbieScore input
                    try:
                        hobbieScore = int(input("Enter the number of your monthly hobbie activities: "))
                        if hobbieScore <= 0:
                            raise NonNegativeError
                        elif hobbieScore %4 != 0:  # If hobbieScore isn`t multiple of 4 the user will get error message
                            raise NonMultipleOfFourError
                        break  # the while will go on until it find`s this break, otherwise, error message
                    except NonNegativeError:
                        print("Error: This number should be non-negative, try again!")
                    except NonMultipleOfFourError:
                        print("Error: This number should be multiple of four, try again!")
                    except ValueError:
                        print("Error: This should be a valid number, try again!")

                break  # breaks the while loop that checks inputQuestion1 (not hobbieScore)

            if inputQuestion2 == "n":  # in case the user wants to skip the hobbieScore
                break

            else:
                print("invalid input, please type y for yes and n for no!")

        print("lets move on!")

        # A very similar structure is repeated for the next sportsItemsNumber

        # Input sportsItemsNumber
        while True:

            inputQuestion3 = input("Do you want to input(or change) your Sports Score? (y/n): ")

            if inputQuestion3 == "y":

                while True:
                    try:
                        sportsItemsNumber = int(input("Enter the number of sports itens you own: "))
                        if sportsItemsNumber <= 0:
                            raise NonNegativeError
                        break
                    except NonNegativeError:
                        print("Error: This number should be non-negative, try again!")
                    except ValueError:
                        print("Error: This should be a valid number, try again!")

                break

            if inputQuestion3 == "n":
                break

            else:
                print("Invalid input, please type y for yes and n for no!")

        print("lets go back to the menu!")

    # To calculate the nerdScore, user must input b
    # Nevertheless, user must have valid inputs for fandomScore, hobbieScore and SportsItemNumber or will find error

    elif MenuQuestion == "b":

        if fandomScore == "empty" and hobbieScore == "empty" and sportsItemsNumber == "empty":  # no input scenario
            print("Fandom Score, Hobbie Score and Sports Score are missing!")

        elif fandomScore == "empty" and hobbieScore == "empty":  # only sportsItemNumber was correctly inputed
            print("Fandom Score and Hobbie Score are missing!")

        elif fandomScore == "empty" and sportsItemsNumber == "empty":  # only hobbiescore was correctly inputed
            print("Fandom Score and Sports Score are missing!")

        elif hobbieScore == "empty" and sportsItemsNumber == "empty":  # only fandomScore was correctly inputed
            print("Hobbie Score and Sports Score are missing!")

        elif fandomScore == "empty":
            print("Fandom Score is missing!")

        elif hobbieScore == "empty":
            print("Hobbie Score is missing!")

        elif sportsItemsNumber == "empty":
            print("Sports Score is missing!")

        else:
            nerdScore = fandomScore * (42 * hobbieScore ** 2 / (sportsItemsNumber + 1)) ** (1 / 2)
            print("Your nerd score is ", nerdScore)

    # To calculate the nerd rate, user must input c
    # Nevertheless, user must have the nerdScore or will find error message

    elif MenuQuestion == "c":

        if nerdScore == "empty":  # the user has not calculated the nerdScore
            print("First calculate your NerdScore!")

        elif nerdScore >= 0 and nerdScore < 1:
            print("you are a Nerdlite!")

        elif nerdScore >= 1 and nerdScore < 10:
            print("you are a Nerdling!")

        elif nerdScore >= 10 and nerdScore < 100:
            print("you are a Nerdlinger!")

        elif nerdScore >= 100 and nerdScore < 500:
            print("you are a Nerd!")

        elif nerdScore >= 500 and nerdScore < 1000:
            print("you are a Nerdington!")

        elif nerdScore >= 1000 and nerdScore < 2000:
            print("you are a Nerdrometa!")

        elif nerdScore >= 2000:
            print("you are a Nerd Supreme!")

    elif MenuQuestion != "a" and MenuQuestion != "b" and MenuQuestion != "c" and MenuQuestion != "q":  #
        print("invalid input!")  # invalid answer for menu question
