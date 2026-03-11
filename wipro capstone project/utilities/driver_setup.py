from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def get_driver():

    options = webdriver.ChromeOptions()

    download_path = r"C:\Users\Admin\PycharmProjects\wiprocapstone\downloads"

    prefs = {
        "download.default_directory": download_path,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "plugins.always_open_pdf_externally": True
    }

    options.add_experimental_option("prefs", prefs)

    service = Service()

    driver = webdriver.Chrome(service=service, options=options)

    driver.maximize_window()

    return driver