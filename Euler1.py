#######################################################################
#                                                                     #
# David Fuller                                                        #
#                                                                     #
# Project Euler: Problem 1.                                           #
#                                                                     #
# 11/9/2016                                                           #
#                                                                     #
#######################################################################

#######################################################################
#                                                                     #
#                          IMPORT STATEMENTS                          #
#                                                                     #
#######################################################################

from tkinter import *   # For GUI
import time             # For keeping track of elapsed time

#######################################################################
#                                                                     #
#                              CONSTANTS                              #
#                                                                     #
#######################################################################

# Define Constant for max number to fo find multiples
# of 3 and 5 up to
MAX = 1000

#######################################################################
#                                                                     #
#                             EULER CLASS                             #
#                                                                     #
#######################################################################

class Euler:
    # Method finds solution to Project Euler: Problem 1
    def findSolution(self):
        # Declare summation variable
        sum = 0

        # Loop through numbers 1-Max to find multiples of 3 and 5
        for i in range(3, MAX):
            if (i % 3 == 0 or i % 5 == 0):
                sum = sum + i

        # Return sum
        return sum
        

#######################################################################
#                                                                     #
#                              GUI CLASS                              #
#                                                                     #
#######################################################################

class EulerForm:
    def __init__(self, parent, msg):
        # Set up GUI
        self.parent = parent
        self.parent.title("Project Euler: Problem 1")
        self.parent.geometry("300x150")

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
    description = "If we list all the numbers below 10 that are " + \
                  "multiples of 3 or 5, we get 3, 5, 6, and 9. " + \
                  "The sum of these multiples is 23.\n\n" + \
                  "Find the sum of all the multiples of 3 or 5 " + \
                  "below 1000."
    return description

# Define main - app driver
def main():
    # Initialize GUI
    root = Tk()

    # Call function to set up Problem description
    description = createDescription()

    # Set up EulerForm
    euler1 = EulerForm(root, description)

    # Keep app running
    root.mainloop()

# Begin app
main()
