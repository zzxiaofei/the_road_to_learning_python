import time
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""
1. 强制等待
2. 隐式等待 implicitly_wait
    
3. 显式等待
"""


def wait_for():
    driver = webdriver.Chrome()
    # driver.implicitly_wait()
    driver.get('https://www.kuaidi100.com/')
    time.sleep(5)
    size = driver.get_window_size()
    driver.maximize_window()
    action = ActionChains(driver)
    action.scroll_by_amount(0, 1000).perform()

    driver.find_element(By.ID, 'uDeskTarget').click()
    driver.switch_to.frame(2)

    # driver.switch_to.frame('uDesk_iframe')

    WebDriverWait(driver, 10, 0.5).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="footer"]/div[3]/div[2]/textarea')))

    driver.find_element(By.XPATH, '//*[@id="footer"]/div[3]/div[2]/textarea').send_keys('你好')

    input("Selenium running done.")


if __name__ == '__main__':
    wait_for()
