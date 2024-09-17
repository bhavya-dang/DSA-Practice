def countForEachElementInArray(strArr: list[str]) -> dict:
            word_count = {}
            for w in strArr:
                if w in word_count:
                    word_count[w] += 1
                else:
                    word_count[w] = 1
            return word_count