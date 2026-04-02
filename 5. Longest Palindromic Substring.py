"""
5. Longest Palindromic Substring
Medium
Topics
premium lock icon
Companies
Hint
Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
"""

s = "babad" # bab or aba
s = "cbbd" # bb

def longpalin_(s,l,r):
    palin = s[l:r]
    while l>=0 and r<len(s) and s[l]==s[r]: # and not(l==0 and r==len(s)-1):
        if len(s[l:r+1])> len(palin):
            palin = s[l:r+1]
        l -=1
        r +=1
    # print( palin)
    return palin

longpalin = s[0]
for i in range( len( s ) ):
    palin = max(longpalin_(s,i,i), longpalin_(s,i,i+1), key=len)
    longpalin = max(longpalin, palin, key=len)
# print( longpalin)

# pass beats 30%