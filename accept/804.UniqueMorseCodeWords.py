"""
804. Unique Morse Code Words


Easy: 59.76%
Testcase Example: ["gin", "zen", "gig", "msg"]

Given a list of words, each word can be written as a 
concatenation of the Morse code of each letter. 
For example, "cab" can be written as "-.-.-....-", 
(which is the concatenation "-.-." + "-..." + ".-"). 
We'll call such a concatenation, the transformation of a word.

Return the number of different transformations among all words 
we have.

Example:

Input: words = ["gin", "zen", "gig", "msg"]
Output: 2
Explanation: 
The transformation of each word is:
"gin" -> "--...-."
"zen" -> "--...-."
"gig" -> "--...--."
"msg" -> "--...--."

There are 2 different transformations, "--...-." and "--...--.".

"""

class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        represent = []
        for word in words:
            r = ""
            for c in word:
                r += morse[ord(c) - ord('a')]
            represent.append(r)
        return(len(set(represent)))

if __name__ == "__main__":
    solution = Solution()
    input = ["gin", "zen", "gig", "msg"]
    print(solution.uniqueMorseRepresentations(input))
