from collections import defaultdict

class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        memoRank = defaultdict(int)
        memoSuit = defaultdict(int)
        
        for i in range(5):
            memoRank[ ranks[i] ] += 1
            memoSuit[ suits[i] ] += 1
            
        # find Flush
        if len(memoSuit) == 1:
            return "Flush"
        # find Three of a Kind
        for elem in memoRank:
            if memoRank[elem] >= 3:
                return "Three of a Kind"
        # find Pair
        for elem in memoRank:
            if memoRank[elem] >= 2:
                return "Pair"
        
        return "High Card"