#######################################################################
#                                                                     #
# David Fuller                                                        #
#                                                                     #
# Project Euler: Problem 3.                                           #
#                                                                     #
# 11/11/2016                                                           #
#                                                                     #
#######################################################################

#######################################################################
#                                                                     #
#                          IMPORT STATEMENTS                          #
#                                                                     #
#######################################################################

from tkinter import *   # For GUI
import time             # For keeping track of elapsed time
import math             # For square root

#######################################################################
#                                                                     #
#                              CONSTANTS                              #
#                                                                     #
#######################################################################

TITLE    = "Project Euler: Problem 3"   # GUI Title.
GEOMETRY = "300x133"                    # GUI screen size.
NUMBER   = 600851475143                 # Find prime factors of this

#######################################################################
#                                                                     #
#                             EULER CLASS                             #
#                                                                     #
#######################################################################

class Euler:
    # Method finds solution to Project Euler: Problem 3
    def findSolution(self):
        # Declare factor variable
        number = NUMBER

        # Find highest prime factor
        counter = 2
        while (counter * counter <= number):
            if (number % counter == 0):
                number = number / counter
                factor = number
            counter = counter + 1

        # Return factor
        return int(factor)

#######################################################################
#                                                                     #
#                              GUI CLASS                              #
#                                                                     #
#######################################################################

class EulerForm:
    def __init__(self, parent, msg):
        # Set up GUI
        self.parent = parent
        self.parent.title(TITLE)
        self.parent.geometry(GEOMETRY)

        # Create solution StringVar
        self.solution = StringVar()
        self.solution.set("")

        # Create GUI Widgets
        self.descriptionMessage = Message(parent, \
                                          text = msg, \
                                          width = 280)
        self.solutionButton = Button(parent, \
                                     text = "Find Solution", \
                                     command = self.findSolution)
        self.solutionLabel = Label(parent, \
                                   textvariable = self.solution)

        # Place GUI Widgets
        self.descriptionMessage.pack()
        self.solutionButton.pack()
        self.solutionLabel.pack()

    # Method finds and displays solution and elapsed time
    def findSolution(self):
        # Store start time
        start = time.time()

        # Project Euler object
        euler = Euler()
        solution = euler.findSolution()

        # Calculate elapsed time, rounded to 2 decimals
        elapsed = ("%.2f" % (time.time() - start))

        # Display the sum, as well as elapsed time
        solution = str(solution) + \
                   " found in " + \
                   str(elapsed) + \
                   " seconds."
        self.solution.set(solution)

#######################################################################
#                                                                     #
#                                DRIVER                               #
#                                                                     #
#######################################################################

# Method sets up Problem description
def createDescription():
    description = "The prime factors of 13195 are 5, 7, 13, and  " + \
                  "29.\n\n " + \
                  "What is the largest prime factor of the number " + \
                  "600851475143?"
    return description

# Define main - app driver
def main():
    # Initialize GUI
    root = Tk()

    # Call function to set up Problem description
    description = createDescription()

    # Set up EulerForm
    euler = EulerForm(root, description)

    # Keep app running
    root.mainloop()

# Begin app
main()
