from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:

    def __init__(self, navegador):
        self.navegador = navegador
        self.espera = WebDriverWait(navegador, 10)

    def adicionar_produto(self):
        botao_produto = self.espera.until(
            EC.element_to_be_clickable(
                (By.ID, "add-to-cart-sauce-labs-backpack")
            )
        )

        botao_produto.click()

    def abrir_carrinho(self):
        carrinho = self.espera.until(
            EC.element_to_be_clickable(
                (By.CLASS_NAME, "shopping_cart_link")
            )
        )

        carrinho.click()

    def produto_esta_no_carrinho(self):
        produto = self.espera.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "inventory_item_name")
            )
        )

        return produto.is_displayed()