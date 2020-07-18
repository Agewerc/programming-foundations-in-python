#Author: Alan Gewerc
#Start Date: 28/03/2019
#End Date: 09/04/2019
#StudentID: 29961246


# The program calculates the nerd score of a user
# The user inputs 3 variables: FandomScore, HobbiesScore and SportsNum
# The system will check if the inputs are valid and if not will send an error message describing the problem
# If there is no invalid input the system will return the nerd score

import math  # used to perform math calculation

# Functionality: calculate the skill score by the equation
# x, y, z are inputs


def calculateSkillEquation(FandomScore, HobbiesScore, SportsNum):

    skillScore = ""  # intialize the output list

# A try-except structure was used to check input
# A specific exception(error) is raised every time the user gives an invalid input
# Creating/customizing exceptions:

    class IntegerErrorF(Exception):
        pass

    class IntegerErrorH(Exception):
        pass

    class IntegerErrorS(Exception):
        pass

    class NonNegativeErrorF(Exception):
        pass
       
    class NonMultipleOfFourError(Exception):
        pass

    class NonNegativeErrorH(Exception):
        pass

    class NonNegativeErrorS(Exception):
        pass


#  before calculating nerdScore the system will check if they have the correct data type, are positive, multiple of 4...
#  if there is no problem the nerd score will be calculated

    try:

        if type(FandomScore) != int:
            raise IntegerErrorF

        if type(HobbiesScore) != int:
            raise IntegerErrorH

        if type(SportsNum) != int:
            raise IntegerErrorS

        if FandomScore <= 0:
            raise NonNegativeErrorF
 
        if HobbiesScore < 0:
            raise NonMultipleOfFourError

        if HobbiesScore %4 != 0:
            raise NonNegativeErrorH

        if SportsNum < 0:
            raise NonNegativeErrorS

        skillScore = FandomScore*math.sqrt(42*HobbiesScore**2/(SportsNum+1))

    except :  # one except its enough for all the exceptions
        print("Error, try again!")


# The folowing if structure is supposed to print for the user every input mistake he  he may have done

    if type(FandomScore) != int:
        print("FandomScore must be a integer")

    elif FandomScore <= 0:
        print("FandomScore must be higher than 0")

    if type(HobbiesScore) != int:
        print("HobbiesScore must be a integer")

    elif HobbiesScore < 0:
        print("HobbiesScore must be equal or higher than 0")

    elif HobbiesScore %4 != 0:
        print("HobbiesScore must be multiple of 4")

    if type(SportsNum) != int:
        print("SportsNum must be a integer")

    elif SportsNum < 0:
        print("SportsNum must be equal or higher than 0")
            
    return skillScore	

if __name__ == '__main__':

    FandomScore, HobbiesScore, SportsNum = 1,4,1 #the output should be 18.33030277982336

    print(calculateSkillEquation(FandomScore, HobbiesScore, SportsNum))
