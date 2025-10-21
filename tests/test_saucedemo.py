
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.helpers import login

# -------------------------------
# FIXTURE DE DRIVER
# -------------------------------
@pytest.fixture
def driver():
    """Crea y cierra el driver de Chrome para cada test"""
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


# -------------------------------
# TEST 1 - LOGIN EXITOSO
# -------------------------------
def test_login_exitoso(driver):
    """Valida que el login sea exitoso y redirija a la página de inventario, verificando Products y Swag Labs"""
    login(driver)

    # Espera explícita a que la URL contenga /inventory.html
    WebDriverWait(driver, 10).until(EC.url_contains("/inventory.html"))
    assert "/inventory.html" in driver.current_url, "No se redirigió a /inventory.html"

    # Verificación del título "Products"
    titulo = driver.find_element(By.CLASS_NAME, "title").text
    assert "Products" in titulo, "El título 'Products' no está presente tras el login"

    # Verificación del logo "Swag Labs"
    logo_texto = driver.find_element(By.CLASS_NAME, "app_logo").text
    assert "Swag Labs" in logo_texto, "El logo no contiene 'Swag Labs'"


# -------------------------------
# TEST 2 - ELEMENTOS DE LOGIN
# -------------------------------
def test_elementos_login_visibles(driver):
    """Verifica que los campos de login y el botón estén visibles"""
    driver.get("https://www.saucedemo.com/")
    username = driver.find_element(By.ID, "user-name")
    password = driver.find_element(By.ID, "password")
    boton_login = driver.find_element(By.ID, "login-button")

    assert username.is_displayed(), "Campo de usuario no visible"
    assert password.is_displayed(), "Campo de contraseña no visible"
    assert boton_login.is_displayed(), "Botón de login no visible"


# -------------------------------
# TEST 3 - CATÁLOGO DE PRODUCTOS
# -------------------------------
def test_catalogo_visible(driver):
    """Valida que la página de inventario muestre productos visibles"""
    login(driver)
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item"))
    )
    productos = driver.find_elements(By.CLASS_NAME, "inventory_item")
    assert len(productos) > 0, "No se encontraron productos visibles"


# -------------------------------
# TEST 4 - PRIMER PRODUCTO
# -------------------------------
def test_datos_primer_producto(driver):
    """Verifica que el primer producto tenga nombre y precio"""
    login(driver)
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item"))
    )
    primer_producto = driver.find_elements(By.CLASS_NAME, "inventory_item")[0]
    nombre = primer_producto.find_element(By.CLASS_NAME, "inventory_item_name").text
    precio = primer_producto.find_element(By.CLASS_NAME, "inventory_item_price").text

    assert nombre != "", "El nombre del producto está vacío"
    assert precio != "", "El precio del producto está vacío"


# -------------------------------
# TEST 5 - CARRITO DE COMPRAS
# -------------------------------
def test_agregaryverificar_carrito(driver):
    """Agrega el primer producto al carrito y valida que esté presente"""
    login(driver)

    wait = WebDriverWait(driver, 10)
    productos = wait.until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item"))
    )
    primer_producto = productos[0]
    nombre_producto = primer_producto.find_element(By.CLASS_NAME, "inventory_item_name").text

    # Agregar producto
    boton_agregar = primer_producto.find_element(By.CLASS_NAME, "btn_inventory")
    boton_agregar.click()

    # Verificar contador del carrito
    contador = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "shopping_cart_badge")))
    assert contador.text == "1", "El contador del carrito no se actualizó"

    # Entrar al carrito y verificar producto
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    wait.until(EC.url_contains("/cart.html"))
    nombres_carrito = [e.text for e in driver.find_elements(By.CLASS_NAME, "inventory_item_name")]
    assert nombre_producto in nombres_carrito, "El producto no está en el carrito"