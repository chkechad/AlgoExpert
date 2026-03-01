# Two Number Sum
# Difficulty: Easy | Category: Arrays

# Write a function that takes in a non-empty arrays of distinct integers
# and an integer representing a target sum.
# If any two numbers in the input arrays sum up to the target sum,
# the function should return them in an arrays, in any order.
# If no two numbers sum up to the target sum, the function should return an empty arrays.

# Note: the target sum has to be obtained by summing two DIFFERENT integers in the arrays.
# You can't add a single integer to itself to obtain the target sum.
# You can assume there will be at most one pair of numbers summing up to the target sum.

# Sample Input:
# arrays = [3, 5, -4, 8, 11, 1, -1, 6]
# targetSum = 10

# Sample Output:
# [-1, 11]  # the numbers could be in reverse order

def two_number_sum_solution1(array: list, target_sum: int) -> list:
    for i in range(0, len(array) - 1):
        for j in range(1, len(array)):
            if i != j and array[i] + array[j] == target_sum:
                return [array[i], array[j]]
    return []


def two_number_sum_solution2(array: list, target_sum: int) -> list:
    seen = set()
    for num in array:
        delta = target_sum - num
        if delta in seen:
            return [delta, num]
        seen.add(num)
    return []


def two_number_sum_solution3(array: list, target_sum: int) -> list:
    array.sort()
    left = 0
    right = len(array) - 1
    while left < right:
        current_sum = array[left] + array[right]
        if current_sum == target_sum:
            return [array[left], array[right]]
        elif current_sum < target_sum:
            left += 1
        else:
            right -= 1
    return []

if __name__ == "__main__":
    array = [3, 5, -4, 8, 11, 1, -1, 6]
    target_sum = 10
    print(two_number_sum_solution3(array, target_sum))  # Expected: [-1, 11]
