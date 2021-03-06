
# QUESTION-THREE:

# KNAPSACK ALGORITHM


# We will start by define a function that will be used to implement the knapsack algorithm.


def knapsack(list_of_values, list_of_weights, bag_capacity, num_of_pellets):

    k = [[0 for _ in range(bag_capacity + 1)] for _ in range(num_of_pellets + 1)]
    # A List that will store pellets that contributes to the highest value
    # pellets_to_include = []

    """I created nested for loop to iterate through the ranges of the pellets (rows) and the bag capacity (columns) and 
    insert the values of the pellets as the capacity continues to change (to increased) based on the different 
    conditions."""
    for i in range(num_of_pellets + 1):
        for w in range(bag_capacity + 1):
            if i == 0 or w == 0:
                """For this condition, we check if the pellet is zero (which means, we don't have a pellet) and if the 
                capacity of the bag is zero then, the value will also be zero."""
                k[i][w] = 0

            elif list_of_weights[i - 1] <= w:
                """Or if the weight of certain pellet at position i is less than or equal to the weight or capacity of 
                the bag then compute for the maximum value."""
                k[i][w] = max(k[i-1][w], k[i-1][w - list_of_weights[i-1]] + list_of_values[i-1])

            else:
                """Else the value of the pellet at the particular capacity of the bag will be the previous' pellet at 
                that capacity of the bag one on top on it, one at the same """
                k[i][w] = k[i-1][w]

    # Finding which pellets that contributed to the highest value and append the value and its weight
    # while number_of_pellets > 0 and bag_capacity > 0:
    #     if k[number_of_pellets][bag_capacity] == k[number_of_pellets - 1][bag_capacity]:
    #         continue
    #
    #     else:
    #         pellets_to_include.append(f'{list_of_weights[number_of_pellets]}kg - {list_of_values[number_of_pellets]}')
    #         number_of_pellets -= 1
    #         bag_capacity = bag_capacity - list_of_weights[number_of_pellets]

    return f'\nThe highest profit that Burglar can make is: ${k[num_of_pellets][bag_capacity]}'


values = [0, 1200, 1700, 2000, 2500, 3000, 4100, 7000, 7500]
weights = [0, 1, 3, 4, 5, 6, 8, 11, 12]
capacity_of_bag = 20
pellets = 8

# Prints the values
print(knapsack(values, weights, capacity_of_bag, pellets))