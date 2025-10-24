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

pre-entrega-automation-testing-maria-soledad-martinez
│
├── tests/
│ ├── conftest.py
│ ├── test_login.py
│ ├── test_inventario.py
│ ├── test_carrito.py
│
├── utils/
│ └── helpers.py
│
├── reports/
│ ├── screenshots/ # Capturas automáticas en caso de fallos
│ └── reporte.html # Reporte HTML generado por pytest-html
│
├── requirements.txt
└── README.md

## Instalación y Configuración

1. **Clonar el repositorio:**

   git clone https://github.com/LadyFantasy/pre-entrega-automation-testing--Soledad-Martinez-
   cd pre-entrega-automation-testing-maria-soledad-martinez

2. ## Instalar dependencias:

pip install -r requirements.txt
Verificar que tengas ChromeDriver instalado y accesible en tu PATH.

3. ## Ejecución de las Pruebas
   Para ejecutar todos los tests con salida detallada:

pytest -v

4. ## Para generar un reporte en HTML:

pytest -v --html=reports/reporte.html

# Casos de Prueba Implementados

🔹 test_login.py
Objetivo: Validar el flujo de inicio de sesión.
Validaciones:
Redirección a /inventory.html.
Presencia de los textos “Products” y “Swag Labs” tras el login.
Campos y botón de login visibles.

🔹 test_inventario.py
Objetivo: Verificar el catálogo de productos tras el login.
Validaciones:
Existencia de productos visibles.
Nombre y precio del primer producto no vacíos.

🔹 test_carrito.py
Objetivo: Probar la interacción con el carrito.
Validaciones:
Agregar el primer producto.
Contador del carrito actualizado.
El producto aparece correctamente en la página del carrito.

## Evidencias y Reportes

Las capturas de pantalla automáticas se guardan en reports/screenshots/ cuando ocurre un fallo.

El reporte HTML se genera en reports/reporte.html con los resultados de las pruebas.
