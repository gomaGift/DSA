def buy_and_sell_stock(prices):
    profit = 0
    buy_price = prices[0]

    for price in prices:
        if price < buy_price:
            buy_price = price
        else:
            profit +=  price - buy_price
            buy_price = price
    return profit


print(buy_and_sell_stock([7,1,5,3,6,4]))
