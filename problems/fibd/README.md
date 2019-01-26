## Mortal Fibonacci Rabbits

Recall the definition of the Fibonacci numbers, which followed the recurrence relation Fn=Fn−1+Fn−2 and assumed that each pair of rabbits reaches maturity in one month and produces a single pair of offspring (one male, one female) each subsequent month.

Our aim is to somehow modify this recurrence relation to achieve a dynamic programming solution in the case that all rabbits die out after a fixed number of months.

**Given**: Positive integers n≤100 and m≤20.

**Return**: The total number of pairs of rabbits that will remain after the n-th month if all rabbits live for m months.

[Link](http://rosalind.info/problems/fibd/)