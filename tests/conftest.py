import pytest
from selenium import webdriver
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from utils.helpers import login

# Carpeta donde se guardarán las capturas
SCREENSHOT_DIR = os.path.join(os.getcwd(), "reports", "screenshots")
os.makedirs(SCREENSHOT_DIR, exist_ok=True)

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Guarda screenshot si el test falla"""
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver")
        if driver:
            screenshot_path = os.path.join(SCREENSHOT_DIR, f"{item.name}.png")
            driver.save_screenshot(screenshot_path)
            print(f"\nScreenshot guardado en: {screenshot_path}")

@pytest.fixture
def driver():
    """Crea y cierra el navegador"""
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.fixture
def login_driver(driver):
    """Realiza login automáticamente antes del test"""
    login(driver)
    return driver
