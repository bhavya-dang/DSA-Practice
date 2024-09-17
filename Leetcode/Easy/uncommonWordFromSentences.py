def uncommonFromSentences(s1: str, s2: str) -> list[str]:
        # removing the leading and trailing spaces
        # ensuring that they are in lowercase
        # splitting them by the space to check for each word
        s1Arr = s1.strip().lower().split(" ")
        s2Arr = s2.strip().lower().split(" ")

        # creating a singular list to do the frequency check
        s1Arr.extend(s2Arr)

        uncommonWords = [w for w in s1Arr if s1Arr.count(w) == 1]

        # custom function to find count
        # def count(arr, word) :
        #     res = 0
        #     for i in range(len(arr)) :
        #         if (arr[i] == word):
        #             res = res + 1
        #     return res
        
        # for w in s1Arr:
        #     if count(s1Arr, w) == 1:
        #         uncommonWords.append(w)
            
        return uncommonWords
            
str1 = "this apple is sweet"
str2 = "this apple is sour"
print(uncommonFromSentences(str1, str2)) 