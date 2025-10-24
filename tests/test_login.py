import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.helpers import login

def test_elementos_login_visibles(driver):
    """Verifica que los campos de login y el botón estén visibles"""
    driver.get("https://www.saucedemo.com/")

    username = driver.find_element(By.ID, "user-name")
    password = driver.find_element(By.ID, "password")
    boton_login = driver.find_element(By.ID, "login-button")

    assert username.is_displayed(), "Campo de usuario no visible"
    assert password.is_displayed(), "Campo de contraseña no visible"
    assert boton_login.is_displayed(), "Botón de login no visible"


def test_login_exitoso(login_driver):
    """Valida que el login sea exitoso y redirija a la página de inventario"""
    driver = login_driver  # Usa el fixture ya logueado

    WebDriverWait(driver, 10).until(EC.url_contains("/inventory.html"))
    assert "/inventory.html" in driver.current_url, "No se redirigió a /inventory.html"

    titulo = driver.find_element(By.CLASS_NAME, "title").text
    assert "Products" in titulo, "El título 'Products' no está presente tras el login"

    logo_texto = driver.find_element(By.CLASS_NAME, "app_logo").text
    assert "Swag Labs" in logo_texto, "El logo no contiene 'Swag Labs'"
