# Module 6 - Problem Set No. 9 - Problem 1

"""
READ ALL INFORMATION CAREFULLY AND THEN READ IT AGAIN

IMPORTANT - PROVIDE AN IPO (Inputs, Processes, and Output) AT THE TOP OF 
EACH PROGRAM USING COMMENTS.

Write a program that gets a string containing the person's first, middle and 
last names using input(), and then displays their first, middle and last 
initials. For example, the user enters "Bruce Lawrence Elgort", the program 
should display B.L.E. It must display exactly like this with the .'s after 
each letter with no spaces.

IPO
==========
INPUTS: user input first middle and last names
PROCESSES: take the first letters of each 
OUTPUTS: output initals

"""

def main():
    name = input("Enter your first middle and last names: ")
    initial = str()
    for word in name.split():
        initial = initial + word[0]+"."
    initial = initial.upper()
    print("The initials are", initial)
main()