from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

service = Service("chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://the-internet.herokuapp.com/login")

wait = WebDriverWait(driver, 10)

username = wait.until(
    EC.visibility_of_element_located((By.ID, "username"))
)

password = wait.until(
    EC.visibility_of_element_located((By.ID, "password"))
)

login_btn = wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]'))
)

username.send_keys("tomsmith")
password.send_keys("SuperSecretPassword!")

# ✅ scroll to button (important for demoqa)
driver.execute_script(
    "arguments[0].scrollIntoView({block: 'center'});",
    login_btn
)

# ✅ wait until clickable
wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]'))
)

login_btn.click()

# ✅ VERIFY LOGIN SUCCESS

flash_message = wait.until(
    EC.visibility_of_element_located((By.ID, "flash"))
)

assert "You logged into a secure area!" in flash_message.text

print("Login successful")

driver.quit()