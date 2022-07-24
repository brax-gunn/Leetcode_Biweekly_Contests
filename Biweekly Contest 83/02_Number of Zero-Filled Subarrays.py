from collections import defaultdict

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        
        N = len(nums)
        memoZero = defaultdict(int)
        
        i = 0
        while i < N:
            if nums[i] == 0:
                currentCount = 0
                j = i
                while j < N and nums[j] == 0:
                    currentCount += 1
                    j += 1
                memoZero[currentCount] += 1
                while i < N and nums[i] == 0:
                    i += 1
                continue
            i += 1
        
        calcTotal = 0
        for elem in memoZero:
            calcTotal += ( ((elem * (elem+1)) // 2)*memoZero[elem] )
        return calcTotal