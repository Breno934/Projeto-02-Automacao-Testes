from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_login_sucesso(navegador):
    login = LoginPage(navegador)

    login.acessar()
    login.preencher_usuario("standard_user")
    login.preencher_senha("secret_sauce")
    login.clicar_login()

    assert "inventory" in navegador.current_url


def test_login_senha_incorreta(navegador):
    login = LoginPage(navegador)

    login.acessar()
    login.preencher_usuario("standard_user")
    login.preencher_senha("senha_errada")
    login.clicar_login()

    assert login.mensagem_erro_visivel()


def test_login_usuario_invalido(navegador):
    login = LoginPage(navegador)

    login.acessar()
    login.preencher_usuario("usuario_inexistente")
    login.preencher_senha("secret_sauce")
    login.clicar_login()

    assert login.mensagem_erro_visivel()


def test_logout(navegador):
    login = LoginPage(navegador)

    login.acessar()
    login.preencher_usuario("standard_user")
    login.preencher_senha("secret_sauce")
    login.clicar_login()

    assert "inventory" in navegador.current_url

    login.abrir_menu()
    login.clicar_logout()

    assert "saucedemo.com" in navegador.current_url


def test_adicionar_produto_ao_carrinho(navegador):
    login = LoginPage(navegador)
    inventario = InventoryPage(navegador)

    login.acessar()
    login.preencher_usuario("standard_user")
    login.preencher_senha("secret_sauce")
    login.clicar_login()

    assert "inventory" in navegador.current_url

    inventario.adicionar_produto()
    inventario.abrir_carrinho()

    assert inventario.produto_esta_no_carrinho()