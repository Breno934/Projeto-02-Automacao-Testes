import pytest
from selenium import webdriver


@pytest.fixture
def navegador():
    navegador = webdriver.Chrome()

    yield navegador

    navegador.quit()