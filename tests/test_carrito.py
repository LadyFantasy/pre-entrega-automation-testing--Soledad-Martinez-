from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_agregar_y_verificar_carrito(login_driver):
    """Agrega el primer producto al carrito y valida que esté presente"""
    driver = login_driver
    wait = WebDriverWait(driver, 10)

    productos = wait.until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item"))
    )
    primer_producto = productos[0]
    nombre_producto = primer_producto.find_element(By.CLASS_NAME, "inventory_item_name").text

    # Agregar producto al carrito
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
