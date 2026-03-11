from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class FlightSearchPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    def open_flights_page(self):

        self.driver.get("https://phptravels.net/flights")
        self.driver.maximize_window()

        # wait for loader to disappear
        self.wait.until(
            EC.invisibility_of_element_located((By.ID, "page-loader"))
        )

    # -------------------------
    # Departure City
    # -------------------------
    def enter_departure(self, city):

        departure = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//input[@placeholder='Departure City or Airport']")
            )
        )

        departure.click()
        departure.clear()
        departure.send_keys(city)

        # select dropdown option (your locator)
        option = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "/html/body/section/div[2]/div/div/form/div/div/div/div[2]/div[2]/div/div[2]/div")
            )
        )
        time.sleep(5)

        self.driver.execute_script("arguments[0].click();", option)

    # -------------------------
    # Arrival City
    # -------------------------
    def enter_arrival(self, city):

        arrival = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//input[@placeholder='Arrival City or Airport']")
            )
        )

        arrival.click()
        arrival.clear()
        arrival.send_keys(city)

        option = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//span[normalize-space()='Indira Gandhi Intl']")
            )
        )
        time.sleep(5)

        self.driver.execute_script("arguments[0].click();", option)

    # -------------------------
    # Search Flights
    # -------------------------
    def search_flights(self):

        search = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(.,'Search Flights')]")
            )
        )

        self.driver.execute_script("arguments[0].click();", search)