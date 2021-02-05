# AlgorithmsHW7


Suppose that you are given an array of letters and you are asked to find a subarray with maximum
length having the property that the subarray remains the same when read forward and backward. Design a
dynamic programming algorithm for this problem. Provide the recursive formula of your algorithm and ex-
plain the formula. Provide also the pseudocode of your algorithm together with its explanation. Analyze the
computational complexity of your algorithm as well. Implement your algorithm as a Python program. (20
points)



Q2. Let A = ( x 1 , x 2 ,
, x n ) be a list of n numbers, and let  a 1 , b 1  ,
,  a n , b n  be n intervals with
1  a i  b i  n , for all 1  i  n . Design a divide-and-conquer algorithm such that for every interval
 a i , b i  ,
all values m i = min  x j | a i  j  b i  are simultaneously computed with an overall complexity of
O ( n log( n )) . Express your algorithm as pseudocode and explain your pseudocode. Analyze your algorithm,
prove its correctness and its computational complexity. Implement your algorithm using Python. (20 points)


Q3. Suppose that you are on a road that is on a line and there are certain places where you can put adver-
tisements and earn money. The possible locations for the ads are x 1 , x 2 , ..., x n . The length of the road is M
kilometers. The money you earn for an ad at location x i is r i > 0. Your restriction is that you have to place
your ads within a distance more than 4 kilometers from each other. Design a dynamic programming algo-
rithm that makes the ad placement such that you maximize your total money earned. Provide the recursive
formula of your algorithm and explain the formula. Provide also the pseudocode of your algorithm together
with its explanation. Analyze the computational complexity of your algorithm as well. Implement your algo-
rithm as a Python program. (20 points)



Q4. A group of people and a group of jobs is given as input. Any person can be assigned any job and a
certain cost value is associated with this assignment, for instance depending on the duration of time that the
pertinent person finishes the pertinent job. This cost hinges upon the person-job assignment. Propose a poly-
nomial-time algorithm that assigns exactly one person to each job such that the maximum cost among the
assignments (not the total cost!) is minimized. Describe your algorithm using pseudocode and implement it
using Python. Analyze the best case, worst case, and average-case performance of the running time of your
algorithm. (20 points)



Q5. Unlike our definition of inversion in class, consider the case where an inversion is a pair i < j such
that x i > 2 x j in a given list of numbers x 1 , ..., x n . Design a divide and conquer algorithm with complexity
O(n log n) and finds the total number of inversions in this case. Express your algorithm as pseudocode and
explain your pseudocode. Analyze your algorithm, prove its correctness and its computational complexity.
Implement your algorithm using Python. (20 points)
