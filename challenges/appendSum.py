# Write a function named append_sum that has one parameter named lst.

# The function should add the last two elements of lst together and append the result to lst. 
# It should do this process three times and then return lst.

# For example, if lst started as [1, 1, 2], the final result should be [1, 1, 2, 3, 5, 8].

def append_sum(lst):
    count = 0
    while(count<3):
        sumOflastTwoElements = lst[-2]+lst[-1]
        lst.append(sumOflastTwoElements)
        count = count+1
    return(lst)

print(append_sum([1,2,3]))