class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1Arr = s1.strip().lower().split(" ")
        s2Arr = s2.strip().lower().split(" ")
        s1Arr.extend(s2Arr)

        uncommonWords = [w for w in s1Arr if s1Arr.count(w) == 1] 
            
        return uncommonWords

        