# descriptive_statistics
based on sheldon ross text book chapter 2 descriptive statistics 
# this works for the datasets whose intervals are integers but not ranges
below is a working example (input)

![question](https://user-images.githubusercontent.com/59249456/71644019-9fe6ec00-2ce7-11ea-9d49-2032d5832a19.png)

# The outputs that can be produced on above example are:
1.central tendency measures (mean,median,mode)

2.variance and standard deviation

3.corelation constant value and its conclusion

4.chebyshevs inequality result statement

5.graphical representation (pie plot,bar plot,scatter plot)

# The actual outputs that i got on above example are:
# MODE 
![mode](https://user-images.githubusercontent.com/59249456/71644238-16d1b400-2ceb-11ea-82c6-82fbf3a25968.png)

# MEAN
![MEAN](https://user-images.githubusercontent.com/59249456/71644254-66b07b00-2ceb-11ea-8fef-866e5af5f1ce.png)

# MEDIAN
![median](https://user-images.githubusercontent.com/59249456/71644267-a37c7200-2ceb-11ea-80dd-8c1b9447578b.png)

# TEST FOR NORMAL DATASET
difference between mean and median will give us a useful result 
i.e, if mod(mean-median) is around 0 to 1 the given data set is said to be NORMAL DATASET

![normal](https://user-images.githubusercontent.com/59249456/71644332-d410db80-2cec-11ea-9bfd-0c6eeec21d35.png)

# VARIANCE
variance of the data is nothing but the sum of the deviations of each value from mean whole  divided by n-1

where n is no.of observations

![variance](https://user-images.githubusercontent.com/59249456/71644444-77162500-2cee-11ea-8841-8bb406219f87.png)

# STANDARD DEVIATION
It is nothing but the +ve square root value of the variance

![deviation](https://user-images.githubusercontent.com/59249456/71644470-dbd17f80-2cee-11ea-964c-afd4e2861896.png)

# CORELATION CONSTANT(r)

It gives an idea how x values are related to y values(frequencies)

    -1<r<1
 
 When r > 0 we say that the sample data pairs are positively correlated, and when r < 0 we
say that they are negatively correlated.

![coreate](https://user-images.githubusercontent.com/59249456/71644542-112a9d00-2cf0-11ea-9c6d-0aaf67c982d4.png)

# CHEBYSHEV'S RESULT

It gives the interval [a,b] in which some p percentile of data is actually present 

![chebshev](https://user-images.githubusercontent.com/59249456/71644584-cc533600-2cf0-11ea-9a3d-73b376feeeb3.png)

# PIE PLOT 

labels which are outside the pieplot indicates the values and its corresponding sector shows its frequency

![pie](https://user-images.githubusercontent.com/59249456/71644626-94002780-2cf1-11ea-89a3-cce10cc87a52.png)

# BAR PLOT

height of a bar gives its frequency

![barplot](https://user-images.githubusercontent.com/59249456/71644649-daee1d00-2cf1-11ea-9f04-df86c2fe9a23.png)

# SCATTER PLOT

scatter plot gives best result when there are vast no.of observations it shows how the points are scattered 

![Screenshot from 2020-01-01 23-53-03](https://user-images.githubusercontent.com/59249456/71644659-2b657a80-2cf2-11ea-819a-e23d7b4d8089.png)

The code i atttched contains some functions to convert given set of integers into stem leaf representation and vice versa

# STEM LEAF REPRESENTATION

the two data values 62 and 67 can be represented as

Stem    Leaf
 6      2, 7

stem leaf input syntax :[[6,[2,7]] 

its output will be :[62,67]

For simpler representation manny interger values are given in stem leaf representaion then,the procedure from_stemleaf_to_interval(a):
can be used to convert into list of integers so that aove operations can be performed and viceversa (check the code)

# Now final combined output for above example is :

![final](https://user-images.githubusercontent.com/59249456/71644812-b0519380-2cf4-11ea-8efe-b6c16031af29.png)
