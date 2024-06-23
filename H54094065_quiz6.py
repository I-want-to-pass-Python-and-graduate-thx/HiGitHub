#_____part 1: GUESS_____

#use the random module
import random

#make a list with 1 to 26

#randomly pick one and see it as an index for the alphabets

#make a list for 26 alphabets

#use index to pick the alphabet

#make the alphabet 
#let user input the lowercase alphabets they guess
Guess = str(input("Guess the lowercase alphabet: "))

#variables for printing the results
lower = print("The alphabet you are looking for is alphabetically lower.")
higher = print("The alphabet you are looking for is alphabetically higher.")

#make variable i to turn what users guess into the index of the alphabet
 

#create a loop for:
#(1)see if the index aligns with the random generated number of the alphabet
#if lower, prints lower
#if higher, prints higher
#(2)make a variable n to +1 after every loop before it breaks.
#initialize n 
n = 0


#_____part 2: Users get the answer_____

right_answer = print("Congratulations! You guessed the alphabet ", Guess, " in", n, "tries.")
#when the users guess right, print right_answer



#_____part3: the guess histogram_____

#Make the range of the alphabet through index

#and make a, b, c, d, e, f, g as the number of tries of the classified range
#initialize them
a=[]
b=[]
c=[]
d=[]
e=[]
f=[]
g=[]
#make them insert one* per users guess in the range since they are mutable