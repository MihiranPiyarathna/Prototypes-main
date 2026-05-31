"""
Have the function OtherProducts(arr) take the array of numbers stored in arr and return a new list of the products of all the other numbers in the array for each element. For example: if arr is [1, 2, 3, 4, 5] then the new array, where each location in the new array is the product of all other elements, is [120, 60, 40, 30, 24]. The following calculations were performed to get this answer: [(2*3*4*5), (1*3*4*5), (1*2*4*5), (1*2*3*5), (1*2*3*4)]. You should generate this new array and then return the numbers as a string joined by a hyphen: 120-60-40-30-24. The array will contain at most 10 elements and at least 1 element of only positive integers.
"""
def OtherProducts(arr):

  # code goes here
  product =1
  for i in arr:
    product *=i
  new = [product/i for i in arr]
  new = '-'.join(str(int(e)) for e in new)
#   new = new[:-1]

  return new

# keep this function call here 
arr = [1,2,3,4,5]
print(OtherProducts(arr))