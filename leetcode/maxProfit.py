def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    min = float("inf")
    max = 0
    for i in range(len(prices)):
        if prices[i] < min:
            min = prices[i]
        elif max < prices[i] - min:
            max = prices[i] - min
    return max


print(maxProfit([1, 6, 4, 3, 1]))
