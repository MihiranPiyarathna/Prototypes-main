"""
Have the function BracketMatcher(str) take the str parameter being passed and return 1 if the brackets are correctly matched and each one is accounted for. Otherwise return 0. For example: if str is "(hello (world))", then the output should be 1, but if str is "((hello (world))" the the output should be 0 because the brackets do not correctly match up. Only "(" and ")" will be used as brackets. If str contains no brackets return 1.
Examples
Input: "(coder)(byte))"
Output: 0
Input: "(c(oder)) b(yte)"
Output: 1
Tags
searchingstackrecursionfreevideologic
"""
strParam = "(coder)(byte))"
strParam = "(c(oder)) b(yte)"
strParam = "the color re(d))()(()"

def BracketMatcher(strParam):
  op=0
  cl=0
  # code goes here
  for i in strParam:
    if i=="(":
      op += 1
    if i== ")":
      cl += 1
      if cl>op:
        return 0
  if op==cl:
    return 1
  else:
    return 0

# keep this function call here 
print(BracketMatcher(strParam))