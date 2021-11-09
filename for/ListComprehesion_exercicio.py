carrinho = []
carrinho.append(('roupa 1', 25.50))
carrinho.append(('roupa 1', 35))
carrinho.append(('roupa 1', 45))

total = sum([float(y) for x, y in carrinho])
print(total)