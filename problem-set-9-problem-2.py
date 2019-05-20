# Module 6 - Problem Set No. 9 - Problem 2

"""
READ ALL INFORMATION CAREFULLY AND THEN READ IT AGAIN

IMPORTANT - PROVIDE AN IPO (Inputs, Processes, and Output) AT THE TOP OF 
EACH PROGRAM USING COMMENTS.

Write a program that accepts a sentence as input and converts each word 
to "Pig Latin." To convert a word to Pig Latin you remove the first letter
and place it at the end of the word. Then add "ay to the end of the word.

YOU MUST ASK FOR A SINGLE SENTENCE AS INPUT.

Here is an example:

English: I SLEPT MOST OF THE NIGHT

Pig Latin: IAY LEPTSAY OSTMAY FOAY HETAY IGHTNAY

HINTS
========================
- Split the sentence into a list
- Iterate through each word using a loop
- Get the last character of each word and assign it to a variable
- Use string slicing to get the last character of each word
- Remove the first character from the word
- Append it to the end of the current word
- Use the accumulator pattern to build a string

IPO
==========
INPUTS: user input phrase to be translated
PROCESSES: turn phrase to list, translate to pig latin
OUTPUTS: print pig latin

"""

def main():
    # your code goes here
    Orig=input("Enter a phrase to be converted to pig latin: ")
    Orig=str(Orig)
    list1=Orig.split()
    for i in list1:
        print(i[1:] + i[0] + "ay", end = " ")
main()