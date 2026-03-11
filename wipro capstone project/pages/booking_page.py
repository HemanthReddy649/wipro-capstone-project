from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time


class BookingPage:

    # -------------------------
    # Locators
    # -------------------------

    EMAIL_FIELD = (By.XPATH, "//input[@x-model='primary_guest.email']")
    TITLE_DROPDOWN = (By.XPATH, "(//select)[1]")
    FIRSTNAME_FIELD = (By.XPATH, "//input[@placeholder='Enter First Name']")
    LASTNAME_FIELD = (By.XPATH, "//input[@placeholder='Enter Last Name']")
    PHONE_FIELD = (By.XPATH, "//input[@placeholder='Enter Phone Number']")
    NATIONALITY_DROPDOWN = (By.XPATH, "//div[@class='mb-4']//select[@class='select']")
    PASSPORT_FIELD = (By.XPATH, "//input[@placeholder='6 - 15 Numbers']")
    PAY_LATER = (By.XPATH, "//div[@class='font-semibold text-gray-900 text-base'][normalize-space()='Pay Later']")
    TERMS_CHECKBOX = (By.XPATH, "//div[@class='checkbox-item']//span[@class='material-symbols-outlined text-white text-xs checkbox-icon'][normalize-space()='check']")
    CONFIRM_BOOKING = (By.XPATH, "//button[contains(.,'Confirm Booking')]")
    INVOICE_BUTTON = (By.XPATH, "//div[@class='btn light w-full flex items-center justify-start gap-2 cursor-pointer']")

    # -------------------------
    # Constructor
    # -------------------------

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    # -------------------------
    # Fill Passenger Details
    # -------------------------

    def fill_guest_details(self, firstname, lastname, email, phone):

        print("Filling passenger details...")

        self.wait.until(
            EC.visibility_of_element_located(self.EMAIL_FIELD)
        )

        title = self.wait.until(
            EC.element_to_be_clickable(self.TITLE_DROPDOWN)
        )
        Select(title).select_by_index(1)

        self.driver.find_element(*self.FIRSTNAME_FIELD).send_keys(firstname)
        self.driver.find_element(*self.LASTNAME_FIELD).send_keys(lastname)
        self.driver.find_element(*self.EMAIL_FIELD).send_keys(email)
        self.driver.find_element(*self.PHONE_FIELD).send_keys(phone)

        print("Email and Phone entered")

        self.driver.execute_script("window.scrollBy(0,500)")
        time.sleep(2)

        nationality = self.wait.until(
            EC.element_to_be_clickable(self.NATIONALITY_DROPDOWN)
        )
        Select(nationality).select_by_visible_text("India")

        passport = self.driver.find_element(*self.PASSPORT_FIELD)
        passport.send_keys("A1234567")

        print("Nationality and passport entered")

        pay_later = self.wait.until(
            EC.element_to_be_clickable(self.PAY_LATER)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            pay_later
        )

        time.sleep(2)

        self.driver.execute_script(
            "arguments[0].click();",
            pay_later
        )

    # -------------------------
    # Confirm Booking
    # -------------------------

    def confirm_booking(self):

        print("Confirming booking...")

        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight)"
        )
        time.sleep(2)

        terms = self.wait.until(
            EC.presence_of_element_located(self.TERMS_CHECKBOX)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            terms
        )

        time.sleep(2)

        self.driver.execute_script(
            "arguments[0].click();",
            terms
        )

        print("Terms accepted")

        confirm_button = self.wait.until(
            EC.element_to_be_clickable(self.CONFIRM_BOOKING)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            confirm_button
        )

        time.sleep(2)

        self.driver.execute_script(
            "arguments[0].click();",
            confirm_button
        )

        print("Booking confirmed")

        time.sleep(10)

    # -------------------------
    # Download Invoice
    # -------------------------

    def download_invoice(self):

        print("Downloading invoice...")

        invoice_button = self.wait.until(
            EC.presence_of_element_located(self.INVOICE_BUTTON)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            invoice_button
        )

        time.sleep(2)

        self.driver.execute_script(
            "arguments[0].click();",
            invoice_button
        )

        print("Invoice download triggered")

        time.sleep(10)