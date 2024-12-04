from typing import List


def removeDuplicates(nums: List[int]) -> int:
    i = 0
    j = 0
    ans = 0
    n = len(nums)
    while j < n:
        curr_value = nums[j]
        t = j
        while j + 1 < n and nums[j] == nums[j + 1]:
            j += 1
        j += 1
        k = 0
        while k < 2 and k < j - t:
            nums[i] = curr_value
            i += 1
            k += 1
            ans += 1
    return ans

if __name__ == "__main__":
    testCase1 = [1,1,1,2,2,3]
    removeDuplicates(testCase1)
    print(testCase1)