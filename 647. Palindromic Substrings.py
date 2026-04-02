"""
Medium
Topics
premium lock icon
Companies
Hint
Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

 

Example 1:

Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
Example 2:

Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
 

Constraints:

1 <= s.length <= 1000
s consists of lowercase English letters.
"""
# sliding window question

s = "abc" # 3
s = "aaa" # 6


def countSubstrings(s):#
    
        def ispalin(s):
            if len(s)<1:
                return False
            for i in range (len(s)//2):
                if s[i] == s[-1-i]:
                    pass
                else:
                    return False
            return True
        
        # print(ispalin(s))
        s_len = len(s)
        cnt=0
        palincnt=0
        a=0
        b=1
        """
        below usual rubber band sliding window not exhaustive
        have to resort to o(n**2) 

        while b<= s_len:
            if ispalin(s[a:b]):
                print(s[a:b], " ",a, " ",b)
                palincnt +=1
                if b-a <=1:
                    b +=1
                else:
                    a +=1
                
            else:
                b +=1
        """
        for i in range(len(s)):
            inum = s[i]
            # print(inum)
            for j in range(i,s_len):
                if ispalin(s[i:j+1]):
                    # print(s[i:j+1])
                    palincnt +=1
        return palincnt

countSubstrings(s)
# turns out above is o(n**3)


# trying out Leet niits solution

s= list(s)
s_len = len(s)
palincnt=0
for i in range (s_len):
    oddL = s[i]
    oddR = s[i]
    palincnt +=1
    print( oddL, oddR)

    evenL = s[i]
    evenR = s[i+1]
    if evenL == evenR:
        palincnt +=1
        print( evenL, evenR)

    for j in range (1,s_len-i+1):
        oddL = s[i-j]
        oddR = s[i+j]
        if oddL == oddR:
            palincnt +=1
            print( oddL, oddR)
        evenL = s[i-j]
        evenR = s[i+1+j]
        if evenL == evenR:
            palincnt +=1
            print( evenL, evenR)

print(palincnt)
# multiple out of bounds errors

# paraphrasing niits code from memory

s_len = len(s)
def countpalin(s, l, r):
    palincnt = 0
    while l>=0 and r<s_len and s[l]==s[r]:
        print( s[l], s[r])
        palincnt +=1
        l -=1
        r +=1
    return palincnt
palintot = 0
for i in range(len(s)):
    palintot += countpalin(s,i,i)
    palintot += countpalin(s,i,i+1)
print(palintot)