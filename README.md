# magic-square
A magic square is a matrix in which the sum of the numbers on each row, column, and diagonal is the same and all the numbers are unique positive whole numbers.
This algorithm aims to efficiently generate 3x3 magic squares of any sum. To explain the algorithm lets look at how we
would solve a magic square:

# Solving a magic square
Lets say that we have a solvable matrix where the first row and first column is filled

![alt text](https://github.com/EmptyDot/magic-square/blob/master/images/ms1.jpg?raw=true)

Since we know the target sum and only one number across the diagonal is missing, we can fill the remaining number.

![alt text](https://github.com/EmptyDot/magic-square/blob/master/images/ms2.jpg?raw=true)

Now the other diagonal is only missing one number, so we can fill the remaining number.

![alt text](https://github.com/EmptyDot/magic-square/blob/master/images/ms3.jpg?raw=true)

For the two remaining numbers we can fill in any of them, but we need to make sure that the sum is the same in both
the corresponding row and column and agrees with the target sum. 

![alt text](https://github.com/EmptyDot/magic-square/blob/master/images/ms5.jpg?raw=true)

All of these steps can be represented as a system of equations:

    (1) a[0, 0] = n - a[0, 1] - a[0, 2] 
    (2) a[1, 1] = n - a[0, 2] - a[2, 0]
    (3) a[2, 2] = n - a[0, 0] - a[1, 1]
    (4) a[1, 2] = n - a[0, 2] - a[2, 2] = n - a[1, 0] - a[1, 1]
    (5) a[2, 1] = n - a[2, 0] - a[2, 2] = n - a[0, 1] - a[1, 1]

Substituting the values of the missing numbers into the system of equations we get:

    (1) a[0, 0] = n - a[0, 1] - a[0, 2] 
    (2) a[1, 1] = n - a[0, 2] - a[2, 0] 
    (3) a[2, 2] = n - a[0, 0] - (2)
    (4) a[1, 2] = n - a[0, 2] - (3) = n - a[1, 0] - (2) 
    (5) a[2, 1] = n - a[2, 0] - (3) = n - a[0, 1] - (2) 

When we simplify equations (4) and (5) we get:

    (4) a[0, 2] + a[2, 0] - a[1, 0] = n - 2 * a[0, 2] + a[0, 0] - a[2, 0]
    (5) a[2, 0] + a[0, 2] - a[0, 1] = n - 2 * a[2, 0] + a[0, 0] - b[0, 2]

If these are true, and they are both greater than 0, then the square can be filled. 


# The algorithm
The algorithm is as follows:  
### First array
Generate a pair of unique numbers from 1 to n.  
Get the missing number by subtracting the sum of the pair from n.  
This is the array we will put in the first row.  

### Second array
Generate one number from 1 to n.  
Since the first row and column share the number at a[0, 0],  
We can use this to get the missing number in the first column by subtracting the sum of a[0, 0] and our generated number from n.  
This is the array we will put in the first column.
    
If along any of these steps, any of the generated numbers break the rules of the magic square then we go to the next number in the sequence.

### Checking if the square is valid
Finally, when we have two valid arrays that are filled with numbers,  
we can check equations (4) and (5) and if they evaluate to True, then we have a valid magic square.






    