"""
Have the function MinWindowSubstring(strArr) take the array of strings stored in strArr, which will contain only two strings, the first parameter being the string N and the second parameter being a string K of some characters, and your goal is to determine the smallest substring of N that contains all the characters in K. For example: if strArr is ["aaabaaddae", "aed"] then the smallest substring of N that contains the characters a, e, and d is "dae" located at the end of the string. So for this example your program should return the string dae.

Another example: if strArr is ["aabdccdbcacd", "aad"] then the smallest substring of N that contains all of the characters in K is "aabd" which is located at the beginning of the string. Both parameters will be strings ranging in length from 1 to 50 characters and all of K's characters will exist somewhere in the string N. Both strings will only contains lowercase alphabetic characters.
Examples
Input: ["ahffaksfajeeubsne", "jefaa"]
Output: aksfaje
Input: ["aaffhkksemckelloe", "fhea"]
Output: affhkkse
Tags
string manipulationsearchinghash tableGoogleFacebookAmazonfreevideo
"""
strArr = ["ahffaksfajeeubsne", "jefaa"]
strArr = ["aaffsfsfasfasfasfasfasfacasfafe", "fafe"]
N = strArr[0]
K = strArr[1]

# N = "bacffa"
# K = "aff"

# Check if window is valid
Nlist= list(N)
Klist= list(K)

def isvalid(Nlist,Klist):
    Ndict={}
    Kdict={}
    Nunq=0
    Kunq=0

    for i in Klist:
        if i not in Kdict.keys():
            Kdict[i]= 1
            Kunq+=1
        else:
            Kdict[i] +=1

    for i in Nlist:
        if i not in Ndict.keys():
            Ndict[i]= 1
            Nunq+=1
        else:
            Ndict[i] +=1
    if Nunq< Kunq:
        return False
    else:
        pass
    for k,v in Kdict.items():
        if k not in Ndict.keys():
            return False
        elif v> Ndict[k]:
            return False
    return True
            
isvalid(Nlist,Klist)

###############
# sliding windows
###############

Nlen= len(Nlist)
Klen= len(Klist)
a=0
b= Klen
validwind={}
cnt=0

# init window
wnd= Nlist[a:b]
while b<=Nlen and cnt <100:
    if isvalid(wnd,Klist):
        print(wnd)
        validwind[''.join(wnd)] = len(wnd)
        # collapse window
        a +=1
    # expand window
    else:
        b +=1
    wnd = Nlist[a:b]

    cnt += 1
###############


# retn the min win
strArr = min(validwind, key= validwind.get)