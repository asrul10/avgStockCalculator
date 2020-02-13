lot = int(input('Lot: '))
avgPrice = int(input('Avg Price: '))
totalStock = avgPrice * lot
print('Total stock: ' + str(totalStock * 100))
lotBuy = int(input('Buy Lot: '))
priceBuy = int(input('Buy Price: '))
totalStockBuy = priceBuy * lotBuy
print('Total stock want to buy: ' + str(totalStockBuy * 100))
avgTotal = (totalStock + totalStockBuy) / (lot + lotBuy)
print('Avg Price Become: ' + str(int(avgTotal)))