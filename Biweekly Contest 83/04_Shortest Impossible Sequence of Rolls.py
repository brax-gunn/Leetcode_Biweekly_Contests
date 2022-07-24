class Solution:
    def shortestSequence(self, rolls: List[int], k: int) -> int:
        
        N = len(rolls)
        
        mySet = set()
        
        ans = 0
        for i in range(N):
            if rolls[i] not in mySet:
                mySet.add( rolls[i] )
                if len(mySet) == k:
                    ans += 1
                    mySet = set()
        
        return ans+1
                
                