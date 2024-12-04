from typing import List



def removeDuplicates(nums: List[int]) -> int:
    i = 1
    counter = 0
    while i < len(nums):
        if nums[counter] != nums[i]:
            counter += 1
            nums[counter] = nums[i]
        i += 1
    return counter + 1

def test(input, expectedResCount, expectedList):
    assert removeDuplicates(input) == expectedResCount
    assert input[:expectedResCount] == expectedList

if __name__ == "__main__":
    test([1, 1, 2], 2, [1, 2])
    print("All test cases passed")
