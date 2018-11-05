class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # original solution two for loop will exceed time limition because calculate sum every loop, so use remain
        # 5000ms
        '''
        for i in range(0,len(nums)-1):
            remain = target - nums[i]
            for j in range(i+1,len(nums)):
                if nums[j]==remain:
                    return [i,j]
        '''

        # use dict to save remainValue-index pair and quick find
        # 40ms
        d = {}
        for i in range(0, len(nums)):
            remain = target - nums[i]
            if remain in d:
                return [d[remain], i]
            else:
                d[nums[i]] = i
        return []

        # cost more time because it needs time to calculate when creating new index
        # 80ms
        '''
        d={}
        for i in range(len(nums)):
            if nums[i] in d:
                return [d[nums[i]],i]
            else:
                d[target-nums[i]] = i
        return []
        '''