class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]

        This method takes an array of integers and a target number.
        It will return the indices of the two array elements whose
        sum equals the target.

        Examples
        -----------
        >>>nums = [2, 7, 11, 15]
        >>>target = 9
        >>>twoSum(nums, target)
        [0, 1]

        >>>nums = [1, 2, 3, 4, 5, 6]
        >>>target = 11
        >>>twoSum(nums, target)
        [4, 5]
        import pdb; pdb.set_trace()


        MY FIRST ATTEMPT:
        while len(nums) > 1:
            y=nums.pop()
            for x in nums:
                sumxy = x + y
                if sumxy == target:
                    index1 = nums.index(x)
                    index2 = len(nums)
                    return [index1, index2]
        msg = "There is no solution given this list of numbers"
        raise ValueError(msg)


        MY SECOND ATTEMPT
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        msg = "There is no solution given this list of numbers"
        raise ValueError(msg)
        """
        hashmap={}
        for i in range(0, len(nums)):
            hashmap[nums[i]] = i
        for i in range(0, len(nums)):
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]]

        msg = "There is no solution given this list of numbers"
        raise ValueError(msg)




sol = Solution()
print(sol.twoSum([2,7,11,15], 9))
print(sol.twoSum([1,2,3,4,5,6], 11))
