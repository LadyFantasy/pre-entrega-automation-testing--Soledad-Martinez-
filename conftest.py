import pytest
from selenium.webdriver.common.by import By
import os

# Carpeta donde se guardarán las capturas
SCREENSHOT_DIR = os.path.join(os.getcwd(), "reports", "screenshots")
os.makedirs(SCREENSHOT_DIR, exist_ok=True)

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
   
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver")
        if driver:
            # Nombre del test + timestamp
            test_name = item.name
            screenshot_path = os.path.join(SCREENSHOT_DIR, f"{test_name}.png")
            driver.save_screenshot(screenshot_path)
            print(f"\nScreenshot guardado en: {screenshot_path}")
