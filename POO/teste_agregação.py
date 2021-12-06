from agregação import CarrinhoDeCompras, Produto

carrinho = CarrinhoDeCompras()

p1 = Produto('camiseta', 24)
p2 = Produto('calça', 54)
p3 = Produto('tenis', 29)

carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p3)

carrinho.lista_produto()