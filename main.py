from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions

# EdgeDriver path
edge_driver_path = "C:\\Users\\jason\\OneDrive\\Documents\\workspace\\msedgedriver.exe"

# Set Edge service
edge_service = EdgeService(executable_path=edge_driver_path)


# Set Edge options
edge_options = EdgeOptions()
edge_options.use_chromium = True

# Specify Edge browser
edge_options.binary_location = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application"


# Login Credentials
username ="jason.developer@outlook.com"
password ="J@sonJ@mes1458"

# Start the Edge browser
driver = webdriver.Edge(service=edge_service)

# Open YouTube
driver.get("https://www.youtube.com/")

# Click on the sign in button
signin_button = WebDriverWait(driver,20).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR,"buttons"))
)
if signin_button:
    signin_button = signin_button[0]

    # Wait for the element to be clickable
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[aria-label="Sign In"]')))

    signin_button[0].click()
else:
    print("No sign-in buttons found.")


# Fill in the login credentials
username_field = WebDriverWait(driver,10).until(
    EC.presence_of_all_elements_located((By.ID,"identifierID"))
)
username_field.send_keys(username)

# Wait for the password field to be visible
password_field = WebDriverWait(driver,10).until(
    EC.presence_of_all_elements_located((By.NAME,"password"))
)
password_field.send_keys(password)
password_field.send_keys(Keys.RETURN)

# Wait for the login to complete
WebDriverWait(driver,10).until(EC.title_contains("YouTube"))

driver.quit()