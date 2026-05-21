"""
mediumDiscussion Solutions 
K Unique Characters

Have the function KUniqueCharacters(str) take the str parameter being passed and find the longest substring that contains k unique characters, where k will be the first character from the string. The substring will start from the second position in the string because the first character will be the integer k. For example: if str is "2aabbacbaa" there are several substrings that all contain 2 unique characters, namely: ["aabba", "ac", "cb", "ba"], but your program should return "aabba" because it is the longest substring. If there are multiple longest substrings, then return the first substring encountered with the longest length. k will range from 1 to 6.
Examples
Input: "3aabacbebebe"
Output: cbebebe
Input: "2aabbcbbbadef"
Output: bbcbbb
Tags
searchingGoogleFacebook
"""
strParam = "3aabacbebebe" # Output: cbebebe
strParam = "2aabbcbbbadef" # Output: bbcbbb
strParam = "3abcddoppqrs" # Output: ddopp

def KUniqueCharacters(strParam):
    # edgecases = less elem, nothing found
    dict0 = {}
    strParam, k = strParam[1:], int(strParam[0])
    if len(strParam)< k:
        return 'can''t find KUniqueCharacters'
    a= 0
    b= k+1
    def expand(a,b):
        n = len(set(strParam[a:b]))
        if n==k:
            dict0[strParam[a:b]] = len(strParam[a:b])
            return True
        elif n<k:
            return True
        else:
            return False
    
    while b<= len(strParam):
        if expand(a,b):
            b +=1
        else:
            a +=1

    return max(dict0, key=dict0.get)

KUniqueCharacters(strParam)
# pass