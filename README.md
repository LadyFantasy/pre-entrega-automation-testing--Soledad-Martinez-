# Pre-Entrega Automatización QA - Saucedemo.com

**Descripción:**  
Suite de pruebas automatizadas para Saucedemo.com utilizando Selenium WebDriver y Pytest. Esta suite valida funcionalidades clave del sitio, incluyendo login, catálogo de productos y carrito de compras. El objetivo es demostrar la capacidad de automatizar flujos básicos de navegación web y verificar elementos e interacciones en la página.

La suite también incluye **capturas de pantalla automáticas** en caso de fallo de cualquier test, guardadas en `reports/screenshots/`.

---

## Tecnologías utilizadas

- **Python 3.13**
- **Selenium WebDriver**
- **Pytest**
- **Pytest-HTML** para generación de reportes
- **Git / GitHub** para control de versiones
- **ChromeDriver** para la automatización del navegador

---

## Estructura del proyecto

preentrega/
│
├─ tests/
│ └─ test_saucedemo.py # Contiene los 5 tests principales
│
├─ utils/
│ └─ helpers.py # Función de login reusable
│
├─ reports/ # Carpeta para reportes HTML y capturas automáticas
│ └─ screenshots/ # Capturas de pantalla de tests fallidos
│
├─ datos/ # (Opcional) Archivos externos como CSV o JSON
│
└─ README.md

yaml
Copiar código

---

## Descripción de los tests

La suite contiene **5 tests principales**:

1. **test_login_exitoso:** Valida que el login con credenciales correctas redirija a la página de inventario (`/inventory.html`) y verifica que el título y logo "Swag Labs" estén presentes.
2. **test_elementos_login_visibles:** Verifica que los campos de usuario, contraseña y botón de login estén visibles.
3. **test_catalogo_visible:** Comprueba que la página de inventario muestre productos visibles.
4. **test_datos_primer_producto:** Valida que el primer producto tenga nombre y precio.
5. **test_agregaryverificar_carrito:** Agrega el primer producto al carrito, valida el contador y verifica que el producto aparezca en el carrito.

---


## Instalar dependencias:
pip install -r requirements.txt

## Ejecución de tests
Desde la raíz del proyecto:
pytest -v tests/test_saucedemo.py

## Para generar un reporte HTML:
pytest -v tests/test_saucedemo.py --html=reports/reporte.html

Nota: Si un test falla, se guardará automáticamente una captura de pantalla en reports/screenshots/ con el nombre del test que falló.
