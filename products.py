products = []
while True:
	name = input('請輸入商品名稱： ')
	if name == 'q':
		break
	price = input('請輸入商品價格： ')	

	products.append([name, price])#簡易寫法二
print(products)

for p in products:
	print(p[0], '的價格是', p[1])
