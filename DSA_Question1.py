#QUESTION-ONE: State the Big O-notation and implement the algorithm that perform the following operations:
# The algorithm takes as input a list of numbers which may contain duplicates. It returns true if
# all elements of the list occur an odd number of times. Otherwise it returns false. For example, on the
# list {1, 3, 2, 2, 5, 2} it returns true, but on the list {1, 3, 2, 2, 5, 2, 5} it returns false because
# 5 occurs an even number of times. [5]

# ............................................SOLUTION..................................................................


# Import timeit and matplotlib form the python lib
import timeit
from matplotlib import pyplot as plt

# We start by creating a function to count the elements in the list
def countingDict(list_):
    # We will Create a variable to store the time that is used to run the function
    runTime = timeit.timeit()

    # We will Create an empty dictionary that will be used to count
    count_dictionary = {}

    # We use a for loop to iterate through the list, by making elements of the list the key to dictionary
    # and values to be the counts
    for element in list_:
        if element in count_dictionary:
            count_dictionary[element] += 1
        else:
            count_dictionary[element] = 1

    # we will create a variable count to count values which are of odd values
    count = 0
    for key in count_dictionary:
        if count_dictionary[key] % 2 != 0:
            count += 1

    """ It returns true if the count is equal to the len of set of the list and false otherwise (a set because it doesn't
     allow duplicates, so we will see if all elements' values have been counted to be odd) """

    return f'\nOdd number of occurrence: {True}\nThe time taken to run is: {runTime} seconds' if count == len(set(list_))\
        else f'\nOdd number of occurrence: {False}\nThe time taken to run is: {runTime} seconds'


# We will Test the lists from the prompt
list1 = [1, 3, 2, 2, 5, 5, 2]
list2 = [1, 3, 2, 2, 5, 2]

# Analysing time complexity and stating the big O notation
L = []
for item in range(len(list2)):
    lst = [1] * item
    run_time = timeit.timeit()
    countingDict(lst)
    L.append(run_time)

plt.plot(list2, L, 'o-', label='change of time with length')
plt.xlabel('lengths of list')
plt.ylabel('Average time (ms)')
plt.show()

# PROMPT answers
print(countingDict(list2))
print("\nThe Big O notation of the algorithm is O(n) ")

# ...........................................THANK YOU!.......................................................