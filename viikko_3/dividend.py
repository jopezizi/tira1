def find_profits(prices):
    profits = []
    profits.append(0)

    cheapest = prices[0] + 0

    for i in range(1,len(prices)):
        profit = (prices[i]+i) - cheapest
        profits.append(max(profit,0))

        today = prices[i] + i
        if today < cheapest:
            cheapest = today
    
 
    return profits
if __name__ == "__main__":
    print(find_profits([9, 6, 10, 10, 3, 6, 7, 6, 5, 7])) # [0, 0, 5, 6, 0, 4, 6, 6, 6, 9]
    print(find_profits([5,4,9,2,9,10,10,1,2,7])) # [0, 0, 6, 0, 8, 10, 11, 3, 5, 11]
    print(find_profits([1, 2, 3, 4])) # [0, 2, 4, 6]
    print(find_profits([4, 3, 2, 1])) # [0, 0, 0, 0]
    print(find_profits([1, 1, 1, 1])) # [0, 1, 2, 3]
    print(find_profits([2, 4, 1, 3])) # [0, 3, 1, 4]
    print(find_profits([1, 1, 5, 1])) # [0, 1, 6, 3]
    print(find_profits([3, 2, 3, 5, 1, 4])) # [0, 0, 2, 5, 2, 6]
 
    prices = list(range(1, 10**5+1))
    print(find_profits(prices)[:5]) # [0, 2, 4, 6, 8]