from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import os
import pytest

# Setup Chrome driver options
def setup_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    return webdriver.Chrome(options=chrome_options)

# Path to your local HTML file
html_file_path = os.path.abspath("qa_web_3_wallet_connection.html")
url = "file://" + html_file_path

@pytest.fixture
def driver():
    driver = setup_driver()
    yield driver
    driver.quit()

def test_wallet_connection_status(driver):
    driver.get(url)

    connect_button = driver.find_element(By.ID, "connectButton")
    assert connect_button.is_displayed(), "Connect button not visible."

    connect_button.click()
    time.sleep(2)  # Wait for the status message

    status_text = driver.find_element(By.ID, "status").text
    assert status_text != "", "Status message is empty."

    assert (
        "Connected:" in status_text or "Connection failed" in status_text
    ), f"Unexpected status message: {status_text}"

    print(f"\u2705 Wallet connection test passed with status: {status_text}")
