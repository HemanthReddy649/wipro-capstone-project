import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InvoicePage:

    INVOICE_BUTTON = (
        By.XPATH,
        "//div[@class='btn light w-full flex items-center justify-start gap-2 cursor-pointer']"
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    def download_invoice(self):

        print("Downloading invoice...")

        invoice_button = self.wait.until(
            EC.element_to_be_clickable(self.INVOICE_BUTTON)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            invoice_button
        )

        self.driver.execute_script(
            "arguments[0].click();",
            invoice_button
        )

        print("Invoice button clicked")

        time.sleep(10)