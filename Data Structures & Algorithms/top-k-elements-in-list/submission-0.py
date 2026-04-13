class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for num in nums:
            if num in seen:
                seen[num] += 1
                continue
            seen[num] = 1
        
        pairs = []
        for key, value in seen.items():
            pairs.append((key, value))
        
        pairs.sort(key=lambda x: x[1], reverse=True)

        result = []
        for num, freq in pairs[:k]:
            result.append(num)

        return result
