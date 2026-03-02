# Validate Subsequence
#
# Given two non-empty arrays of integers, write a function that determines
# whether the second array is a subsequence of the first one.
#
# A subsequence of an array is a set of numbers that aren't necessarily
# adjacent in the array but that are in the same order as they appear
# in the array. For instance, the numbers [1, 3, 4] form a subsequence
# of the array [1, 2, 3, 4], and so do the numbers [2, 4].
# Note that a single number in an array and the array itself are both
# valid subsequences of the array.
#
# Sample Input:
# array = [5, 1, 22, 25, 6, -1, 8, 10]
# sequence = [1, 6, -1, 10]
#
# Sample Output:
# true


def isValidSubsequence_sol1(array: list, sequence: list) -> bool:
    start = 0
    for item in sequence:
        try:
            index = array.index(item, start)
            start = index + 1
        except ValueError:
            return False
    return True


def isValidSubsequence_sol2(array: list, sequence: list) -> bool:
    it = iter(array)
    return all(any(x == item for x in it) for item in sequence)


def isValidSubsequence_sol3(array: list, sequence: list) -> bool:
    seq_idx = 0
    arr_idx = 0
    while arr_idx < len(array) and seq_idx < len(sequence):
        if array[arr_idx] == sequence[seq_idx]:
            seq_idx += 1
        arr_idx += 1
    return seq_idx == len(sequence)


if __name__ == "__main__":
    array = [5, 1, 22, 25, 6, -1, 8, 10]
    sequence = [1, 6, -1, 10]
    print(isValidSubsequence_sol1(array, sequence))  # Expected: True
