prices = [500, 2400, 1200, 3100, 1800]
filter_prices = list(filter(lambda p:  p > 2000 ,prices))
print(filter_prices)