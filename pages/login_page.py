from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    def __init__(self, navegador):
        self.navegador = navegador
        self.espera = WebDriverWait(navegador, 10)

    def acessar(self):
        self.navegador.get("https://www.saucedemo.com/")

    def preencher_usuario(self, usuario):
        campo_usuario = self.espera.until(
            EC.visibility_of_element_located(
                (By.ID, "user-name")
            )
        )

        campo_usuario.send_keys(usuario)

    def preencher_senha(self, senha):
        campo_senha = self.espera.until(
            EC.visibility_of_element_located(
                (By.ID, "password")
            )
        )

        campo_senha.send_keys(senha)

    def clicar_login(self):
        botao_login = self.espera.until(
            EC.element_to_be_clickable(
                (By.ID, "login-button")
            )
        )

        botao_login.click()

    def mensagem_erro_visivel(self):
        mensagem = self.espera.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "[data-test='error']")
            )
        )

        return mensagem.is_displayed()

    def abrir_menu(self):
        botao_menu = self.espera.until(
            EC.element_to_be_clickable(
                (By.ID, "react-burger-menu-btn")
            )
        )

        botao_menu.click()

    def clicar_logout(self):
        def encontrar_logout(driver):
            elementos = driver.find_elements(
                By.ID,
                "logout_sidebar_link"
            )

            for elemento in elementos:
                if elemento.is_displayed():
                    return elemento

            return False

        botao_logout = self.espera.until(encontrar_logout)

        self.navegador.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            botao_logout
        )

        self.navegador.execute_script(
            "arguments[0].click();",
            botao_logout
        )