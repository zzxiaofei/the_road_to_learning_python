from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver


def keyboard_click():
    driver = webdriver.Chrome()
    driver.get('http://120.24.56.229:8082/?s=user/loginInfo.html')

    username = driver.find_element(By.NAME, 'accounts')
    username.send_keys('daniel')
    username.send_keys(Keys.CONTROL, 'a')
    # username.send_keys(Keys.)

    actions = ActionChains(driver)
    actions.context_click(username).perform()




    input("Selenium running done.")



if __name__ == '__main__':
    keyboard_click()
