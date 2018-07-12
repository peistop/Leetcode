"""
819. Most Common Word
https://leetcode.com/problems/most-common-word

Easy:
Testcase: "Bob hit a ball, the hit BALL flew far after it was hit."\n["hit"]

Given a paragraph and a list of banned words, return the most frequent word 
that is not in the list of banned words. It is guaranteed there is at least 
one word that isn't banned, and that the answer is unique.

Words in the list of banned words are given in lowercase, and free of 
punctuation.  Words in the paragraph are not case sensitive.  The answer 
is in lowercase.
"""
class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        
        symbols = ["!", "?", ",", ";", ".", "'"]
        for symbol in symbols:
            paragraph = paragraph.replace(symbol, "")
        words = [w.lower() for w in paragraph.split() if w.lower() not in banned ]
        record = list(set(words))
        count = [1] * len(record)
        for word in words:
            count[record.index(word)] += 1
        return(record[count.index(max(count))])

if __name__ == "__main__":
    solition = Solution()
    input1 = "Bob hit a ball, the hit BALL flew far after it was hit."
    input2 = ["hit"]
    print(solition.mostCommonWord(input1, input2))