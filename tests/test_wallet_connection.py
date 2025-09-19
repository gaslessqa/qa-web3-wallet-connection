from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import os


# Path to your local HTML file
html_file_path = os.path.abspath("qa_web_3_wallet_connection.html")
url = "file://" + html_file_path


# Setup Chrome driver in headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=1920,1080")




def run_wallet_connection_test():
driver = webdriver.Chrome(options=chrome_options)


try:
print(f"Opening local dApp at: {url}")
driver.get(url)


connect_button = driver.find_element(By.ID, "connectButton")
assert connect_button.is_displayed(), "Connect button not visible."


print("Clicking 'Connect Wallet' button...")
connect_button.click()


time.sleep(2) # Wait for wallet connection simulation


status_text = driver.find_element(By.ID, "status").text
assert status_text != "", "Status message is empty."


if "Connected:" in status_text:
print("\u2705 Test passed: Wallet connected successfully.")
elif "Connection failed" in status_text:
print("\u26a0\ufe0f Test warning: Wallet connection failed.")
else:
raise AssertionError(f"Unexpected status message: {status_text}")


except AssertionError as ae:
print("\u274C Assertion failed:", ae)


except Exception as e:
print("\u274C Test execution error:", e)


finally:
driver.quit()




if __name__ == "__main__":
run_wallet_connection_test()
