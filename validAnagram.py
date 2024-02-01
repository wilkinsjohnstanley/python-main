'''
Valid Anagram
An anagram is a word that uses the same letters as another word.

Given two strings 's' and 't'
return truue if 't' is an anagram of 's'
and false otherwise

Example 1:

Input: s="anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Constraints:
1 <=s.length, te.length <=5*10**4
s and t consist of lowercase English letters
'''

print("Welcome to the Valid Anagram checking program:")
s=input("Enter a word \n")
t=input("Enter a second word\n")


# for char in s:
#    for char in t:
#         if char not in t:
#             print("Not a valid anagram!")
#             break
#         else:   
#             print("Valid anagram")

def isAnagram(self, s:str, t:str)-> bool:
     if len(s)!=len(t):
         return False
     
     countS, countT = {}, {}

     for i in range(len(s)):
        countS[s[i]]=1+countS.get(s[i], 0)
        countT[t[i]]=1+countT.get(t[i], 0)
     for c in countS:
         if countS[c]!=countT.get(c, 0):
            return False
         
         
print(isAnagram(isAnagram, s, t))