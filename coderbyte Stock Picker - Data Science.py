"""

"""
arr = [10,12,4,5,9]

def StockPicker(arr):
    if len(arr)<2: return -1
    buy = arr[0]
    max_profit = -1
    for p in arr[1:]:
        if p<buy : 
            buy = p
        else:
            max_profit = max(p-buy, max_profit)
    return max_profit

StockPicker(arr)
# pass