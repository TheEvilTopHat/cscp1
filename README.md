# P1P1
This file is the radix sort file.
It uses one function that takes an unsorted array
then returns a sorted array.

To do this it uses a while loop that checks if the unsorted array still has
unsorted numbers, when that array is empty it breaks and returns.

Inside the while loop is a for loop that starting in the ones spot sorts 
each number by the least significant digit. These sorted numbers are 
stored in a separate array,

Then it loops through the new sorted array and if it has no more digits,
then it pops and places it into the return array.

The first array then becomes the second array and the process repeats.

# P1P2
This file is the postfix notation file.

It has two functions. Convert is the function that takes a 
string of data ("((5+2) ∗ (8−3))/4") then converts it into postfix notation
("52+83− ∗ 4/”).

The secound function postfix2, takes this formated text and then does the math for it
getting the answer for the question.
