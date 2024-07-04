import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def mail_login():
    global webdriver
    options = webdriver.ChromeOptions()  # 浏览器可选项配置 FirefoxOption
    options.add_argument('--headless')  # 添加无头模式的参数
    driver = webdriver.Chrome()
    driver.get('https://mail.qq.com/')
    #
    # time.sleep(10)
    # driver.switch_to.frame(driver.find_elements(By.CLASS_NAME, "QQMailSdkTool_login_loginBox_qq_iframe")[0])
    #
    # driver.quit()

    """
    切换frame
            :Usage:
            ::

                element = driver.switch_to.active_element
                alert = driver.switch_to.alert
                driver.switch_to.default_content()
                driver.switch_to.frame('frame_name') #name
                driver.switch_to.frame(1) # 索引，页面包含了多个frame标签，
                driver.switch_to.frame(driver.find_elements(By.TAG_NAME, "iframe")[0])
                driver.switch_to.parent_frame()
                driver.switch_to.window('main')
    
    """
    try:
        # 等待iframe出现
        wait = WebDriverWait(driver, 10)
        iframe = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "QQMailSdkTool_login_loginBox_qq_iframe")))

        # 切换到iframe
        driver.switch_to.frame(iframe)

        # 检查是否成功切换到iframe
        try:
            # 尝试查找iframe中的元素
            # driver.find_element(By.ID, "switcher_plogin").click()

            element_in_iframe = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="u"]')))
            # driver.find_element(By.XPATH, '//*[@id="u"]').send_keys('305332527'))
            print(f"Successfully switched to iframe and found element: {element_in_iframe.text}")
        except Exception as e:
            print(f"Failed to find element in iframe: {e}")

        # 切回主内容
        driver.switch_to.default_content()

    except Exception as e:
        print(f"Error: {e}")

    driver.switch_to.frame('ptlogin_iframe')
    driver.switch_to.frame(1)
    driver.switch_to.frame(driver.find_elements(By.XPATH, '//*[@id="QQMailSdkTool_login_loginBox_qq"]'))
    driver.find_element(By.ID, 'u').send_keys('305332527')

    driver.find_element(By.XPATH, "//*[@id='u']").send_keys('305332527')


if __name__ == '__main__':
    mail_login()
