# Complete the code to correctly use the count() method to find the number of duplicates of 2 in the following tuple.

tup = 1, 2, 3, 2, 4, 5, 6, 2, 7, 2, 8, 9
duplicates = ()

for num in range(len(tup)):
    double = tup.count(num)
    if double > num:
        duplicates += (double,)

 
print(duplicates) # outputs: 4