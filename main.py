from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

chrome_driver_path="D:\Chrome Driver\chromedriver.exe"
driver=webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")
time.sleep(3)
signin=driver.find_element(By.XPATH,'/html/body/div[3]/a[1]')
signin.click()
time.sleep(3)
email=driver.find_element(By.NAME,'session_key')
password=driver.find_element(By.NAME,'session_password')
fsign=driver.find_element(By.XPATH,'//*[@id="organic-div"]/form/div[3]/button')
email.send_keys("Your id")
password.send_keys("Your Password")
fsign.click()
# gsign=driver.find_element(By.ID,"sign-in-with-google-button")
# gsign.click()
time.sleep(10)
job_list=driver.find_elements(By.CSS_SELECTOR,'.jobs-search-results__list-item')
for job in job_list:
    job.click()
    time.sleep(10)
    try:
        apply=driver.find_element(By.CSS_SELECTOR,'.jobs-s-apply button')
        apply.click()
        time.sleep(10)
        mobile=driver.find_element(By.XPATH,'//*[@id="single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3422412883-9-phoneNumber-nationalNumber"]')
        if mobile=="":
            mobile.send_keys("Your Mobile No.")
            time.sleep(3)
        
        submit_button=driver.find_element(By.CSS_SELECTOR,'footer button span')
        submit_button.click()
        time.sleep(3)
        try:
            progress=driver.find_element(By.CSS_SELECTOR,'.artdeco-completeness-meter-linear__progress-container ')
            time.sleep(3)
            close_button = driver.find_element(By.CLASS_NAME,'artdeco-button--tertiary')
            close_button.click()
            time.sleep(2)
            discard_button = driver.find_element(By.CLASS_NAME,'artdeco-button--secondary')
            discard_button.click()
            print("Complex application, skipped.")
            continue
        except NoSuchElementException:
            pass

        # if "Submit_button application" in submit_button.text:
        #     submit_button.click()
        #     continue

        # else:
        #     cancel=driver.find_element(By.CLASS_NAME,'artdeco-button--tertiary')
        #     cancel.click()
        #     time.sleep(5)
        #     discard=driver.find_element(By.CLASS_NAME,'artdeco-button--secondary')
        #     discard.click()
        #     print("Complex application, skipped.")
            
            

        time.sleep(2)
        close_button = driver.find_element(By.CLASS_NAME,"artdeco-modal__dismiss")
        close_button.click()
            
        
    except NoSuchElementException:
        print("No application button, skipped.")
        continue
time.sleep(5000)