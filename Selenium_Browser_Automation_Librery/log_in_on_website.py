from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

service = Service("chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://demoqa.com/login")

wait = WebDriverWait(driver, 10)

username = wait.until(
    EC.visibility_of_element_located((By.ID, "userName"))
)

password = wait.until(
    EC.visibility_of_element_located((By.ID, "password"))
)

login_btn = wait.until(
    EC.presence_of_element_located((By.ID, "login"))
)

username.send_keys("pythonstudent")
password.send_keys("PythonStudent123$")

# ✅ scroll to button (important for demoqa)
driver.execute_script(
    "arguments[0].scrollIntoView({block: 'center'});",
    login_btn
)

# ✅ wait until clickable
wait.until(
    EC.element_to_be_clickable((By.ID, "login"))
)

login_btn.click()

# ✅ VERIFY LOGIN SUCCESS

user_label = wait.until(
    EC.visibility_of_element_located((By.ID, "userName-value"))
)

assert user_label.text == "pythonstudent"

print("Login successful")

driver.quit()