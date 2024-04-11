class Solution(object):
    def mergeAlternately(self, word1, word2):      
        merged_string = ""

        #This line calculates the maximum length between word1 and word2. 
        #This length will determine the number of iterations needed in the loop to ensure 
        #all characters from both words are processed.
        max_length = max(len(word1), len(word2))

        for i in range(max_length):
            if i < len(word1):
                merged_string += word1[i]
            if i < len(word2):
                merged_string += word2[i]

        return merged_string
'''
Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
'''

