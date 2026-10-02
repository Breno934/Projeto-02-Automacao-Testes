class InventoryPage:

    def __init__(self, navegador):
        self.navegador = navegador

    def adicionar_produto(self):
        botao_produto = self.navegador.find_element(
            "id",
            "add-to-cart-sauce-labs-backpack"
        )

        botao_produto.click()

    def abrir_carrinho(self):
        carrinho = self.navegador.find_element(
            "class name",
            "shopping_cart_link"
        )

        carrinho.click()

    def produto_esta_no_carrinho(self):
        produto = self.navegador.find_element(
            "class name",
            "inventory_item_name"
        )

        return produto.is_displayed()