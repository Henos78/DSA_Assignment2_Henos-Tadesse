 # Question-Two:  Design and implement an algorithm that takes: a list containing n distinct natural numbers and a number k ≤ n and
# calculates the sum of the k largest numbers in the array. For example, if the list is {3, 7, 5, 12, 6} and k = 3, then
# the algorithm should return 25= (12+7+6).


# ....................................SOLUTION.........................................................


# We will define the function to the counting of the elements in the list
def largestNumber(n, k):
    # We will create a variable to store the list after removing duplicates by using the set
    DistinctList = list(set(n))
    # if the k passed is the less than the number of elements in the distinct list
    if k <= len(DistinctList):
        # the list is displayed
        print(f"\nThe distinct list: {DistinctList}")
        # It will be sorted in descending order do that we can perform operations easily on the largest element (first elements)
        newList = sorted(DistinctList, reverse=True)
        return f"The sum of {k} largest number is: {sum(newList[:k])}"

# Prints the values
print(largestNumber([10, 12, 11, 10, 20, 15, 8, 17], 4))

# ......................................THANK YOU....................................................................