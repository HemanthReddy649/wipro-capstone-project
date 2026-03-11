import pytest
from pages.flight_search_page import FlightSearchPage
from pages.flight_results_page import FlightResultsPage
from pages.booking_page import BookingPage
from pages.invoice_page import InvoicePage
from utilities.logger_util import get_logger
from utilities.excel_util import get_excel_data

logger = get_logger()

# Read Excel Data
test_data = get_excel_data("testdata/testdata.xlsx", "Sheet1")

# Use only first row
data = test_data[0]


# Test Case 1 - Flight Search Page
def test_flight_search_page(driver):

    logger.info("===== Test Case 1: Flight Search Page =====")

    search = FlightSearchPage(driver)

    logger.info("Opening flights page")
    search.open_flights_page()

    logger.info(f"Entering departure city: {data['departure']}")
    search.enter_departure(data["departure"])

    logger.info(f"Entering arrival city: {data['arrival']}")
    search.enter_arrival(data["arrival"])

    logger.info("Clicking search button")
    search.search_flights()

    logger.info("Flight search completed successfully")


# Test Case 2 - Flight Results Page
def test_flight_results_page(driver):

    logger.info("===== Test Case 2: Flight Results Page =====")

    search = FlightSearchPage(driver)
    results = FlightResultsPage(driver)

    search.open_flights_page()
    search.enter_departure(data["departure"])
    search.enter_arrival(data["arrival"])
    search.search_flights()

    logger.info("Selecting first flight from results")
    results.select_first_flight()

    logger.info("Flight selected successfully")


# Test Case 3 - Booking Page
def test_booking_page(driver):

    logger.info("===== Test Case 3: Booking Page =====")

    search = FlightSearchPage(driver)
    results = FlightResultsPage(driver)
    booking = BookingPage(driver)

    search.open_flights_page()
    search.enter_departure(data["departure"])
    search.enter_arrival(data["arrival"])
    search.search_flights()

    results.select_first_flight()

    logger.info("Filling guest details")

    booking.fill_guest_details(
        data["firstname"],
        data["lastname"],
        data["email"],
        data["phone"]
    )

    logger.info("Confirming booking")
    booking.confirm_booking()

    logger.info("Booking successful")


# Test Case 4 - Invoice Page
def test_invoice_page(driver):

    logger.info("===== Test Case 4: Invoice Page =====")

    search = FlightSearchPage(driver)
    results = FlightResultsPage(driver)
    booking = BookingPage(driver)
    invoice = InvoicePage(driver)

    search.open_flights_page()
    search.enter_departure(data["departure"])
    search.enter_arrival(data["arrival"])
    search.search_flights()

    results.select_first_flight()

    booking.fill_guest_details(
        data["firstname"],
        data["lastname"],
        data["email"],
        data["phone"]
    )

    booking.confirm_booking()

    logger.info("Downloading invoice")
    invoice.download_invoice()

    logger.info("Invoice downloaded successfully")