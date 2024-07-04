from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time


def main():
    global driver
    options = webdriver.ChromeOptions()  # 浏览器可选项配置 FirefoxOption
    options.add_argument('--headless')  # 添加无头模式的参数
    driver = webdriver.Chrome()  # 实例化浏览器对象
    driver.get("https://wwww.baidu.com")
    url = driver.current_url
    print('当前运行的url:', url)
    driver.save_screenshot('./test.png')  # 截图
    driver.refresh()  # 刷新

    # 窗口相关内容

    size = driver.get_window_size()  # 获取窗口大小，设置窗口大小
    print(size)
    driver.set_window_size(500, 806)  # 参数1:宽 参数2: 高
    driver.maximize_window()
    driver.minimize_window()
    driver.fullscreen_window()  # 窗口全屏
    #
    # driver.back()  # 浏览器后退
    # driver.forward()  # 浏览器前进

    window = driver.window_handles  # 1. 获取窗口，返回窗口个数的列表，len或者[]可以指定
    driver.switch_to.window(window[0])  # 2. 切换窗口

    # driver.get("file:///Users/xiaofeizhang/Desktop/pythonweb.html")
    # driver.find_element(By.ID, "kw").send_keys("seleium")
    # driver.find_element(By.NAME, "password").send_keys("123")
    # driver.find_element(By.CLASS_NAME, "kw").send_keys(Keys)
    # driver.find_element(By.PARTIAL_LINK_TEXT, Keys.ENTER).click()
    # driver.find_element(By.TAG_NAME, "body").send_keys("")
    # driver.find_element(By.LINK_TEXT, Keys.ENTER).click()
    # driver.find_element(By.XPATH, "//*[@id='kw']")
    # driver.find_element(By.CSS_SELECTOR,)
    # driver.find_elements(By.TAG_NAME,)

    # time.sleep(1)
    # driver.quit()


if __name__ == '__main__':
    main()
