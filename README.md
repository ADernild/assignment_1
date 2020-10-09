# Assignment_1

My solutions to the first assignment in DS800: Introduction to Data Processing

## Assignment 1: Programming

1) **Pythagorean theorem:** Write a program that solves the Pythagorean theorem.
The user is asked to input two out of three side lengths a, b and c (for the unknown
one, the user might enter "?"), and the program should calculate and print the
length of the unknown side.

2) **Median value:** Write a function median(L) that takes a list of numbers L and returns
its median value. Sorting the list first helps to solve this task.

3) **Unique list items:** Write a function unique(L) that takes a list of objects L and
returns a sub-list that contains those items that occur only once in L.

4) **Character count:** Write a function characters(textfile) that calculates the fre-
quencies of characters in textfile. Use a dictionary to count how often each char-
acter occurs. Finally, print the entire dictionary sorted alphabetically by keys.
Test your function with the file raven.txt that should count, e.g., 109 occurrences
of , (comma) and 17 occurrences of N. 

5) **Word frequency:** The file genesis.zip contains text files for the 50 chapters of the
Bible book Genesis. Write a function count(term) that analyzes the frequencies of
term as follows:

	1. initialize the variable frequencies
	2. loop through the 50 chapters, for each chapter do the following:
		i. open the corresponding TXT file
		ii. load the text using the read function
		iii. split text into words
		iv. loop words and count how often a word equals term
		v. add the result to frequencies
	3. visualize frequencies with a line chart using matplotlib

