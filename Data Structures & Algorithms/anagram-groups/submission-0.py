class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}

        for s in strs:
            complement = ''.join(sorted(s))

            if complement in seen:
                seen[complement].append(s)
                continue
            
            seen[complement] = [s]
        
        final = []

        for group in seen.values():
            final.append(group)

        return final 