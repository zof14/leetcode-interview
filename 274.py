class Solution:
    def hIndex(self, citations: List[int]) -> int:
        counts = [sum(1 for x in citations if x >= v) for v in citations]
        max_num=0
    
        for i in range(len(citations)):
            h = min(citations[i], counts[i])
            max_num = max(max_num, h)

        return max_num