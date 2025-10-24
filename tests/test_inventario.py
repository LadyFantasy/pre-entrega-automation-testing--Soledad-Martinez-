from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_catalogo_visible(login_driver):
    """Valida que la página de inventario muestre productos visibles"""
    driver = login_driver

    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item"))
    )
    productos = driver.find_elements(By.CLASS_NAME, "inventory_item")

    assert len(productos) > 0, "No se encontraron productos visibles"


def test_datos_primer_producto(login_driver):
    """Verifica que el primer producto tenga nombre y precio"""
    driver = login_driver

    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item"))
    )

    primer_producto = driver.find_elements(By.CLASS_NAME, "inventory_item")[0]
    nombre = primer_producto.find_element(By.CLASS_NAME, "inventory_item_name").text
    precio = primer_producto.find_element(By.CLASS_NAME, "inventory_item_price").text

    assert nombre != "", "El nombre del producto está vacío"
    assert precio != "", "El precio del producto está vacío"
