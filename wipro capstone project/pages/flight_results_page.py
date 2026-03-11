from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FlightResultsPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 40)

    def select_first_flight(self):

        print("Waiting for flights to load...")

        # YOUR ORIGINAL BOOK NOW LOCATOR
        book_now_locator = (
            By.XPATH,
            "//div[@class='grid grid-cols-12 gap-4']//div[1]//div[1]//div[1]//div[2]//div[1]//div[3]//button[1]//span[2]"
        )

        # Wait for element
        book_button = self.wait.until(
            EC.element_to_be_clickable(book_now_locator)
        )

        # Scroll to button
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            book_button
        )

        # Click with JS (most reliable)
        self.driver.execute_script(
            "arguments[0].click();",
            book_button
        )

        print("Clicked Book Now")