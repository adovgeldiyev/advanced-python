# Advanced-python<br>
## Problem 1: Stem and Leaf<br>
Find on the D2L three “StemAndLeaf” datafiles. Write code that….<br>
### a) 
Greets the user.<br>
### b) 
Asks the user to input a 1, 2 or 3.<br>
### c) 
Given the input, reads in the appropriate datafile and displays a stem and leaf plot. (Note: This will require you to make several design decisions.)<br>
### d) 
Loops until the user wishes to exit.<br>
<br>
## Problem 2: Avocados<br>
### a) 
Define a function that takes a variable name in the form of a string (e.g. “Total Volume”), reads into memory the values for that variable (but just that variable) and computes the mean using the statistics module.<br>
mean_SM = readAndComputeMean_SM(“Total Volume”)<br>
### b) 
Define a function that takes a variable name in the form of a string (e.g. “Total Volume”), reads into memory the values for that variable (but just that variable) and computes the standard deviation using the statistics module.<br>
sd_SM = readAndComputeSD_SM(“Total Volume”)<br>
### c) 
Define a function that takes a variable name in the form of a string (e.g. “Total Volume”), reads into memory the values for that variable (but just that variable) and computes the median using the statistics module.<br>
median_SM = readAndComputeMedian_SM(“Total Volume”)<br>
### d) 
Repeat a-c, but instead of using the statistics module write your own “homegrown” code to compute the mean, standard deviation and median.<br>
mean_HG = readAndComputeMean_HG(“Total Volume”) sd_HG = readAndComputeSD_HG(“Total Volume”) median_HG = readAndComputeMedian_HG(“Total Volume”)<br>
### e) 
Repeat a-c, but your functions must be memoryless – you can hold in memory only a single value from the file at any given time.<br>
mean_MML = readAndComputeMean_MML(“Total Volume”) sd_MML = readAndComputeSD_MML(“Total Volume”) median_MML = readAndComputeMedian_MML(“Total Volume”)<br>
### f) 
Write test code to demonstrate that the means, standard deviations and medians are the same across all three techniques.<br>
<br>
## Problem 3: 7s and 12s<br>
Consider this game. The user begins with an account value of $100. She may place a bet of an amount of her choosing, but not more than her current balance. She then rolls two six-sided dice. Her score is the sum of the faces of the dice. If she rolls a 7 or a 12 she wins and doubles her bet. If she does not roll a 7 or 12, she has the option to double her bet and roll a third die. If all three dice sum to 7 or 12 she wins three times the total value of her bet.
Implement this game. Consider all the ways the user might interact with the system. Use exception handling when appropriate. Your program should be robust to all possible user inputs.
