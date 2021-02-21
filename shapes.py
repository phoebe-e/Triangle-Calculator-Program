print("\nTriangle Calculator Program")

#Main menu function definition
def mainMenuLoader():
    """
    Print main menu options to screen

    Parameters:
        None
    Returns:
        Nothing
    """

    print("\n*************"
          "\n* Main Menu *"
          "\n*************"
          "\n1. Find the missing angle of a triangle"
          "\n2. Find the hypotenuse of a right-angle triangle"
          "\n3. Find the area of a triangle"
          "\nq. Exit program")
    return

#Call previously defined function and prompt user
mainMenuLoader()
menuItem = input("\nMake a selection and press [ENTER] ")

#Menu items: nested if-statment within while loop to avoid carrying out unnecessary calculations
while(menuItem != "q"):
    #Menu item 1: find the missing angle given 2 angles
    if(menuItem == "1"):
        print("\n1. Find the missing angle of a triangle")
        angle1InDegrees = float(input("Enter the 1st known angle of the triangle (in degrees) and press [ENTER] "))
        angle2InDegrees = float(input("Enter the 2nd known angle of the triangle (in degrees) and press [ENTER] "))
        #Condition to ensure that all 3 angles are positive and will add up to 180 degrees
        if(0 < angle1InDegrees and 0 < angle2InDegrees and 0 < angle1InDegrees + angle2InDegrees < 180):
            #Angles must sum to 180 degrees
            unknownAngleInDegrees = 180.00 - angle1InDegrees - angle2InDegrees
            print("\n*SOLUTION*")
            print("First angle: " + str(angle1InDegrees) + "°")
            print("Second angle: " + str(angle2InDegrees) + "°")
            print("Unknown angle: " + str(unknownAngleInDegrees) + "°")
            print("\nReturning to Main Menu...")
        else:
            print("\nThat doesn't seem to be a triangle! Please try again.")
            print("Returning to Main Menu...")

    #Menu item 2: find the hypotenuse given the opposite and adjacent
    elif(menuItem == "2"):
        print("\n2. Find the hypotenuse of a right-angle triangle")
        lengthOppInCm = float(input("Enter the length of the opposite (in cm) and press [ENTER] "))
        lengthAdjInCm = float(input("Enter the length of the adjacent (in cm) and press [ENTER] "))
        #Condition to ensure that the given lengths are positive
        if(0 < lengthOppInCm and 0 < lengthAdjInCm):
            #Pythagoras' theorem
            lengthHypInCm = (lengthOppInCm**2 + lengthAdjInCm**2)**0.5
            print("\n*SOLUTION*")
            print("Opposite: " + str(lengthOppInCm) + " cm")
            print("Adjacent: " + str(lengthAdjInCm) + " cm")
            print("Hypotenuse: " + str(lengthHypInCm) + " cm")
            print("\nReturning to Main Menu...")
        else:
            print("\nThat doesn't seem to be a triangle! Please try again.")
            print("Returning to Main Menu...")

    #Menu item 3: find the area given the side lengths
    elif(menuItem == "3"):
        print("\n3. Find the area of a triangle")
        lengthSide1InCm = float(input("Enter the length of the first side of the triangle (in cm) and press [ENTER] "))
        lengthSide2InCm = float(input("Enter the length of the second side of the triangle (in cm) and press [ENTER] "))
        lengthSide3InCm = float(input("Enter the length of the third side of the triangle (in cm) and press [ENTER] "))
        #Condition derived from triangle inequality theorem 
        if(lengthSide1InCm + lengthSide2InCm > lengthSide3InCm and lengthSide1InCm + lengthSide3InCm > lengthSide2InCm and lengthSide2InCm + lengthSide3InCm > lengthSide1InCm):
            #Calucation steps of Area = (p(p-a)(p-b)(p-c))**0.5
            #Where p is the perimeter of the triangle halved and a, b and c are the sides of the triangle
            halfPerimeterInCm = (lengthSide1InCm + lengthSide2InCm + lengthSide3InCm)/2
            areaOfTriangleInCmSq = (halfPerimeterInCm*(halfPerimeterInCm - lengthSide1InCm)*(halfPerimeterInCm - lengthSide2InCm)*(halfPerimeterInCm - lengthSide3InCm))**0.5
            print("\n*SOLUTION*")
            print("Side 1: " + str(lengthSide1InCm) + "cm")
            print("Side 2: " + str(lengthSide2InCm) + "cm")
            print("Side 3: " + str(lengthSide3InCm) + "cm")
            print("Area: " + str(areaOfTriangleInCmSq) + "cm^2")
            print("\nReturning to Main Menu...")
        else:
            print("\nThat doesn't seem to be a triangle! Please try again.")
            print("Returning to Main Menu...")

    #Error message: if neither 1, 2 or 3 is selected
    else:
        print("\nError!")
        print("Please try again...")

    mainMenuLoader()
    menuItem = input("\nMake a selection and press [ENTER] ")

#If q is selected:
print("Exiting programme...")
exit()