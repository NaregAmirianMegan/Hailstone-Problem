# Hailstone-Problem

## The Problem
The problem also known as the Collatz Conjecture is yet to be understood by mathematics. The problem:
Start at any positive integer n. If n is even n = n / 2. If n is odd n = 3n + 1. In all cases currently 0 through 2^60 if the rules are recursively applied, n will end up oscillating between 1 and some other integer. 
## Solution Test Algorithm
The interactive script allows you to enter numbers and see the process of calculation down to one. The all numbers script goes up from 2 and prints a new number every time that number takes a larger amount of iterations to reach one. A hash table (python dictionary) stores the values with key as the number and value as the steps to one so as to reduce computational cost. You can choose to save the dictionary you have created as a json file in data folder. (example_data.json in data folder)
