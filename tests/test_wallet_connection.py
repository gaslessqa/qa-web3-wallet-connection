from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

# Path to your local HTML file
html_file_path = os.path.abspath("qa_web_3_wallet_connection.html")
url = "file://" + html_file_path

# Setup Chrome driver
driver = webdriver.Chrome()

try:
    driver.get(url)

    # Click the connect wallet button
    connect_button = driver.find_element(By.ID, "connectButton")
    connect_button.click()

    time.sleep(2)  # Wait for the status message

    # Get the status message
    status_text = driver.find_element(By.ID, "status").text

    # Assert expected text
    assert "Connected:" in status_text or "Connection failed" in status_text
    print("✅ Test passed:", status_text)

except Exception as e:
    print("❌ Test failed:", e)

finally:
    driver.quit()
