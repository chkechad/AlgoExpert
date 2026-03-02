# Sorted Squared Array
#
# Write a function that takes in a non-empty array of integers
# that are sorted in ascending order and returns a new array
# of the same length with the squares of the original integers
# also sorted in ascending order.
#
# Sample Input:
# array = [1, 2, 3, 5, 6, 8, 9]
#
# Sample Output:
# [1, 4, 9, 25, 36, 64, 81]


def sortedSquaredArray(array: list) -> list:
    # memory allocation
    result = [0] * len(array)
    # two pointer and index
    length_list = len(array) - 1
    left, right, index = 0, length_list, length_list

    while left <= right:
        if abs(array[left]) > abs(array[right]):
            result[index] = array[left] ** 2
            left += 1
        else:
            result[index] = array[right] ** 2
            right -= 1
        index -= 1
    return result


if __name__ == "__main__":
    array = [-2, -1]
    assert sortedSquaredArray(array) == [1, 4]
    array = [1, 2, 3, 5, 6, 8, 9]
    assert sortedSquaredArray(array) == [1, 4, 9, 25, 36, 64, 81]
