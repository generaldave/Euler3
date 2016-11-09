#######################################################################
#                                                                     #
# David Fuller                                                        #
#                                                                     #
# Project Euler: Problem 2.                                           #
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

TITLE    = "Project Euler: Problem 2"   # GUI Title.
GEOMETRY = "300x222"                    # GUI screen size.
MAX      = 4000000                      # Max fibo number to find even
                                        #    values of.

#######################################################################
#                                                                     #
#                             EULER CLASS                             #
#                                                                     #
#######################################################################

class Euler:
    # Method decides whether a number is even or not
    def isEven(self, num):
        # If num is divisible by 2, return true
        if (num % 2 == 0):
            return True

        # Otherwise return false
        return False
    
    # Method finds solution to Project Euler: Problem 2
    def findSolution(self):
        # Declare variables
        fibo = 0
        sum = 2
        previous = 2
        beforePrevious = 1

        # Loop through fibonacci numbers until max is reached
        while (fibo < MAX):
            # Store fibonacci number and previous 2
            fibo = previous + beforePrevious
            beforePrevious = previous
            previous = fibo

            # If fibo is even, add to sum
            if (self.isEven(fibo)):
                sum += fibo

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
    description = "Each new term in the Fibonacci sequence is " + \
                  "generated by adding the previous two terms. " + \
                  "By starting with 1 and 2, the first 10 terms " + \
                  "will be:\n\n" + \
                  "1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...\n\n" + \
                  "By considering the terms in the Fibonacci " + \
                  "sequence whose values do not exceed four " + \
                  "million, find the sum of the even-valued terms."
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
