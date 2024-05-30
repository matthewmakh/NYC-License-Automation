import json
import time
import chromedriver_autoinstaller
import ssl
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Bypass SSL verification (not recommended for production)
ssl._create_default_https_context = ssl._create_unverified_context

username = 'Eyalbabayev@gmail.com'
password = 'Hateit#132'
business_name = 'Eyal Babayev'
email = 'eyalbabayev@gmail.com'
phone_number = '6465776917'
first_name = 'Eyal'
last_name = 'Babayev'

chromedriver_autoinstaller.install()

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 17)

# Navigate to a URL or perform other actions here
driver.get('https://a866-dcwpbp.nyc.gov/lottery/apply-lottery')

# click sign in
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/app-root/div/main/app-not-authorized/div/button[1]')))
sign_in_button = driver.find_element(By.XPATH, '/html/body/app-root/div/main/app-not-authorized/div/button[1]')
driver.execute_script("arguments[0].scrollIntoView(true);", sign_in_button)
sign_in_button.click()

# login
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'gigya-loginID')))
driver.find_element(By.ID, 'gigya-loginID').send_keys(username)
driver.find_element(By.ID, 'gigya-password').send_keys(password)
login_button = driver.find_element(By.XPATH, '/html/body/main/div/div[1]/div[2]/div/form/div[1]/div[5]/input')
driver.execute_script("arguments[0].scrollIntoView(true);", login_button)
login_button.click()

# select license type
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'lottery-choice-231daee3-9206-ec11-94ee-001dd8309672')))
license_type = driver.find_element(By.ID, 'lottery-choice-231daee3-9206-ec11-94ee-001dd8309672')
driver.execute_script("arguments[0].scrollIntoView(true);", license_type)
license_type.click()
time.sleep(0.5)
license_type.click()

# wait for district selection
time.sleep(7)

# Enter business name and acknowledge
driver.find_element(By.ID, 'name').send_keys(business_name)
time.sleep(0.3)
acknowledgement_checkbox = driver.find_element(By.ID, 'acknowledgement')
driver.execute_script("arguments[0].scrollIntoView(true);", acknowledgement_checkbox)
time.sleep(0.3)
acknowledgement_checkbox.click()


# Fill in business information
driver.find_element(By.XPATH, '/html/body/app-root/div/main/app-lottery-application/div/div/app-form/div/div[2]/div[2]/app-tab-host/app-business-information/div/div[5]/div[1]/div/div[1]/input').send_keys(first_name)
driver.find_element(By.XPATH, '/html/body/app-root/div/main/app-lottery-application/div/div/app-form/div/div[2]/div[2]/app-tab-host/app-business-information/div/div[5]/div[1]/div/div[3]/input').send_keys(last_name)
time.sleep(0.5)

# Click the 'No' option
no_option = driver.find_element(By.XPATH, "/html/body/app-root/div/main/app-lottery-application/div/div/app-form/div/div[2]/div[2]/app-tab-host/app-business-information/div/div[5]/div[2]/div/div[2]/div[2]/label/input")
driver.execute_script("arguments[0].scrollIntoView(true);", no_option)
time.sleep(0.7)
no_option.click()


# Enter business contact information
driver.find_element(By.ID, 'businessEmail').send_keys(email)
driver.find_element(By.ID, 'businessPhone').send_keys(phone_number)

# Click the next button
next_button = driver.find_element(By.XPATH, '/html/body/app-root/div/main/app-lottery-application/div/div/app-form/div/div[2]/div[6]/div[1]/div[4]')
driver.execute_script("arguments[0].scrollIntoView(true);", next_button)
time.sleep(1)
next_button.click()


# Click the 'No' option for is-auth-rep
is_auth_rep_no = driver.find_element(By.ID, 'is-auth-rep-no')
driver.execute_script("arguments[0].scrollIntoView(true);", is_auth_rep_no)
time.sleep(1)
is_auth_rep_no.click()

# Click the next button
next_button2 = driver.find_element(By.XPATH, '/html/body/app-root/div/main/app-lottery-application/div/div/app-form/div/div[2]/div[6]/div[1]/div[4]/button')
driver.execute_script("arguments[0].scrollIntoView(true);", next_button2)
time.sleep(1)
next_button2.click()


is_ack = driver.find_element(By.ID, 'is-ack')
# Scroll to the bottom of the page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# Wait for the checkbox to be clickable
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'is-ack')))
time.sleep(1)
is_ack.click()

#added
for i in range(0):
    break

# Click the next button
next_button3 = driver.find_element(By.XPATH, '/html/body/app-root/div/main/app-lottery-application/div/div/app-form/div/div[2]/div[6]/div[1]/div[4]/button')
driver.execute_script("arguments[0].scrollIntoView(true);", next_button3)
time.sleep(1)
next_button3.click()


# The browser will remain open until you manually close it
input("Press Enter to close the browser...")
driver.quit()
