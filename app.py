import undetected_chromedriver as uc
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scraper(driver, url):
    driver.get(url)
    elem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
    elem.clear()
    action = ActionChains(driver)
    action.send_keys("randomuser")
    elem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[class^='LoginUsername---login-button']")))
    elem.click()
    pass

if __name__ == "__main__":
    chrome_options = ChromeOptions()
    chrome_options.headless = False
    driver = uc.Chrome(use_subprocess=True, options=chrome_options)
    scraper(driver, "https://www.maybank2u.com.my/home/m2u/common/login.do")