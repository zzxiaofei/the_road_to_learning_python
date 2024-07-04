import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


def login():
    global webdriver
    driver = webdriver.Chrome()
    driver.get('http://120.24.56.229:8082/')
    time.sleep(5)
    driver.maximize_window()
    driver.find_element(By.XPATH, "//*[text()='登录' and contains(@class,'am-fl')]").click()

    # driver.quit()


"""
1. element not interactable by selenium
2. Unable to locate element
3. unexpected alert open: {Alert text}

思路：
1. 检查元素的定位是否正确
2. 页面元素进行获取的时候查看是否已经加载出来，等待时间
3. 元素在页面上不可见，需要拖动下拉框或者放大窗口
4. 页面元素在iframe标签里面
5. 元素需要切换到信窗口
6.元素隐藏

"""

if __name__ == '__main__':
    login()
