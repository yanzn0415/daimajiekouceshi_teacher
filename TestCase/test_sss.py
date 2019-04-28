import time
import  os

from selenium import webdriver


class TestFirstUIDeno:
    def test_testdemo1(self):


#确定chromedriver.exe的位置
        driver_path = os.path.join(os.path.dirname(__file__),"../vinson/chromedriver.exe")
        # 打开浏览器
        driver = webdriver.Chrome(driver_path)
        driver.maximize_window()  # 最大化浏览器
        driver.set_page_load_timeout(10)#网页加载超时为10s
        driver.set_script_timeout(10)#js脚本运行超时10s
        driver.implicitly_wait(10)#元素查找超时时间10s
        time.sleep(2)
        driver.get['htpps://www.baidu.com']
        driver.quit()