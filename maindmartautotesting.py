from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
# Set up the WebDriver using ChromeDriverManager
#service = Service(ChromeDriverManager().install())
#driver = webdriver.Chrome(service=service)
# Set up the WebDriver (e.g., Chrome)
#driver = webdriver.Chrome(executable_path='C:\Program Files\Google\Chrome\Application\chromedriver-win64\chromedriver.exe')
#driver.maximize_window()
#driver.get('https://www.dmart.in')
driver = webdriver.Chrome()
driver.get("https://www.dmart.in")


# Wait for the page to load
time.sleep(4)

# Accept cookies if prompted
try:
    accept_cookies = driver.find_element(By.XPATH, '//button[contains(text(), "Accept All Cookies")]')
    accept_cookies.click()
    time.sleep(2)
except Exception as e:
    print("No cookie prompt found.")
driver.find_element(By.XPATH,"/html/body/div[2]/div[3]/div/div/div/div[1]/div[2]/input").click()
time.sleep(2)
driver.find_element(By.XPATH,"/html/body/div[2]/div[3]/div/div/div/div[1]/div[2]/input").send_keys("560058")
time.sleep(5)
driver.find_element(By.XPATH,"/html/body/div[2]/div[3]/div/div/div").click()
time.sleep(5)
driver.find_element(By.XPATH,"/html/body/div[2]/div[3]/div/div/div/div[2]/div[2]/div[2]/div/div[2]/button").click()
time.sleep(5)
driver.find_element(By.XPATH,"/html/body/div/div[1]/header/div/div[1]/div[3]/div/div[1]/div/div/button").click()
time.sleep(2)
driver.find_element(By.XPATH,"/html/body/div[2]/div[3]/div/div[2]/div/form/div/div[2]/input").send_keys("8431338659")
time.sleep(10)
driver.find_element(By.XPATH,"/html/body/div[2]/div[3]/div/div[2]/div/form/button").click()
time.sleep(10)

#driver.find_element(By.XPATH,"/html/body/div[2]/div[3]/div/div[2]/div/div/div/form/div[1]/div[1]/div[2]/input").click()
#time.sleep(2)
#driver.find_element(By.XPATH,"/html/body/div[2]/div[3]/div/div[2]/div/div/div/form/div[1]/div[1]/div[2]/input").send_keys("Sharath")
#time.sleep(10)
#driver.find_element(By.XPATH,"/html/body/div[2]/div[3]/div/div[2]/div/div/div/form/div[1]/div[2]/div[2]/input").click()
#time.sleep(2)
#driver.find_element(By.XPATH,"/html/body/div[2]/div[3]/div/div[2]/div/div/div/form/div[1]/div[2]/div[2]/input").send_keys("Gowda")
#time.sleep(10)
#driver.find_element(By.XPATH,"/html/body/div[2]/div[3]/div/div[2]/div/div/div/form/button").click()
#time.sleep(2)
#driver.find_element(By.XPATH,"/html/body/div[2]/div[3]/div/div[2]/div/div/div/form/div[1]/div[2]/input").click()
#time.sleep(30)
#driver.find_element(By.XPATH,"/html/body/div[2]/div[3]/div/div[2]/div/div/div/form/button").click()
#time.sleep(10)


driver.find_element(By.XPATH,"/html/body/div[2]/div[3]/div/div[2]/div/div[1]/form/div[1]/div[2]/input").click()
time.sleep(20)
driver.find_element(By.XPATH,"/html/body/div[2]/div[3]/div/div[2]/div/div[1]/form/button").click()
time.sleep(5)

driver.find_element(By.XPATH,"/html/body/div/div[1]/header/div/div[1]/div[2]/div/div[1]/div/div/input").click()
time.sleep(10)
driver.find_element(By.XPATH,"//html/body/div/div[1]/header/div/div[1]/div[2]/div/div[1]/div/div/input").send_keys("Briyani Rice")
time.sleep(10)
driver.find_element(By.XPATH,"/html/body/div/div[1]/header/div/div[1]/div[2]/div/div[1]/div/div/button").click()
time.sleep(10)

driver.find_element(By.XPATH,"/html/body/div/div[1]/main/div/div/div[2]/div").click()
time.sleep(8)
driver.find_element(By.XPATH,"/html/body/div/div[1]/main/div/div/div[2]/div[3]/div[3]/div[2]/button").click()
time.sleep(8)


driver.find_element(By.XPATH,"/html/body/div/div[1]/header/div/div[1]/div[3]/div/div[3]/button").click()
time.sleep(8)
driver.find_element(By.XPATH,"/html/body/div/div[5]/div[2]/div[3]/div/button").click()
time.sleep(8)

driver.find_element(By.XPATH,"/html/body/div/div[1]/main/div/div/div/div[3]/div/div[2]/div/div/button").click()
time.sleep(8)




driver.find_element(By.XPATH,"/html/body/div/div[1]/main/div/div/div[1]/div/div[1]/div[2]/div[2]/div[1]/div[1]/div/div/div[2]/div[3]/span/span").click()
time.sleep(8)
driver.find_element(By.XPATH,"/html/body/div/div[1]/main/div/div/div[1]/div/div[1]/div[2]/div[2]/div[1]/div[2]/div/div/div/div[1]/div[2]/div/button").click()
time.sleep(8)

driver.find_element(By.XPATH,"/html/body/div[2]/div[3]/div[2]/form/div[1]/div/input").click()
time.sleep(2)
driver.find_element(By.XPATH,"/html/body/div[2]/div[3]/div[2]/form/div[1]/div/input").send_keys("manoj s")
time.sleep(8)

driver.find_element(By.XPATH,"/html/body/div[2]/div[3]/div[2]/form/div[2]/div/input").click()
time.sleep(2)
driver.find_element(By.XPATH,"/html/body/div[2]/div[3]/div[2]/form/div[2]/div/input").send_keys("560075")
time.sleep(8)

driver.find_element(By.XPATH,"/html/body/div[2]/div[3]/div[2]/form/div[4]/div[2]/div/div/textarea[1]").click()
time.sleep(2)
driver.find_element(By.XPATH,"/html/body/div[2]/div[3]/div[2]/form/div[4]/div[2]/div/div/textarea[1]").send_keys("New Thippasandra Main Rd, Bhoomi Reddy Colony")
time.sleep(8)

driver.find_element(By.XPATH,"/html/body/div[2]/div[3]/div[2]/form/div[5]/div/textarea").click()
time.sleep(2)
driver.find_element(By.XPATH,"/html/body/div[2]/div[3]/div[2]/form/div[5]/div/textarea").send_keys("735")
time.sleep(10)

driver.find_element(By.XPATH,"/html/body/div[2]/div[3]/div[2]/form/div[6]/div/input").click()
time.sleep(2)
driver.find_element(By.XPATH,"/html/body/div[2]/div[3]/div[2]/form/div[6]/div/input").send_keys("bhoomi reddy colony")
time.sleep(10)
driver.find_element(By.XPATH," /html/body/div[2]/div[3]/div[3]/button ").click()#cart
time.sleep(10)

driver.find_element(By.XPATH,"/html/body/div[3]/div[3]/div[2]/div[2]/button").click()#cart
time.sleep(10)



driver.find_element(By.XPATH," /html/body/div/div[1]/main/div/div/div[1]/div/div[1]/div[2]/div[2]/div[1]/div[2]/div/div/div/div[2]/button ").click()  #cart x
time.sleep(4)
driver.find_element(By.XPATH,"/html/body/div/div[1]/main/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[4]/button").click()
time.sleep(10)


driver.find_element(By.XPATH,"/html/body/div/div[1]/main/div/div/div[1]/div/div[2]/div/div[2]/div/div[1]/button").click()
time.sleep(10)
driver.find_element(By.XPATH,"/html/body/div[2]/div[3]/div[2]/div[2]/button").click()
time.sleep(10)


print("order place successfully")