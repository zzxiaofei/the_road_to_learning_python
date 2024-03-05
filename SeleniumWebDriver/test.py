from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# driver = webdriver.Chrome()
# driver.get("https://wwww.baidu.com")

def main():
    global driver
    driver = webdriver.Chrome()
    driver.get("file:///Users/xiaofeizhang/Desktop/pythonweb.html")
    time.sleep(1)
    driver.find_element(By.ID, 'email').send_keys("tynan@test.com")
    driver.find_element(By.NAME, "password").send_keys("123")
    driver.find_element(By.ID, "btn-login").click()
    time.sleep(30)
    driver.quit()


if __name__ == '__main__':
    main()


