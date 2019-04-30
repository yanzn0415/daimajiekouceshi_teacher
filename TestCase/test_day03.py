
import os
import time

import pytest
from selenium import webdriver

from Common.baseui import baseUI
from Common.read_excel import read_excel_list


class TestMall():
    @pytest.mark.s
    def test_login(self,driver):
        # #打开浏览器
        # # 确定chromedriver.exe的位置
        # driver_path = os.path.join(os.path.dirname(__file__), "../chromedriver/chromedriver.exe")
        # # 打开浏览器
        # driver = webdriver.Chrome(driver_path)
        # driver.maximize_window()  # 最大化浏览器
        # driver.set_page_load_timeout(10)  # 网页加载超时为10s
        # driver.set_script_timeout(10)  # js脚本运行超时10s
        # driver.implicitly_wait(10)  # 元素查找超时时间10s
        base = baseUI(driver)
        #打开网址
        driver.get("http://192.168.1.137/#/login")
        #定位用户名输入框//input[@name='username']
        #username = driver.find_element_by_xpath("//input[@name='username']")
        #输入用户名
        #username.clear()
        #username.send_keys("admin")
        #定位密码输入框//input[@name='password']
        #password = driver.find_element_by_xpath("//input[@name='password']")
        #输入密码
        #password.clear()
        #password.send_keys("123456")
        #定位登录按钮//span[contains(text(),'登录')])                      #点击登录按钮
        base.click("点击登录按钮","//span[contains(text(),'登录')]")
        # driver.find_element_by_xpath("//span[contains(text(),'登录')]").click()
        #点击登录按钮
        # 定位并处理异常弹框//span[contains(text(),'残忍拒绝')]                      #点击登录按钮
        try:
            base.click("点击残忍拒绝", "//span[contains(text(),'残忍拒绝')]")
        except:
            pass
        time.sleep(2)
        base.click("点击登录按钮", "//span[contains(text(),'登录')]")
        # driver.find_element_by_xpath("(//span[contains(text(),'登录')])[1]").click()
        time.sleep(1)
        #断言页面是否跳转到首页
        print(driver.page_source)
        assert "首页" in driver.page_source
    # def test_order_1(self,driver):
    #     print("查询订单")
    l_name = read_excel_list("d:\\daa.xlsx")
    @pytest.fixture(params=l_name)
    def name(self,request):
        return request.param
    def test_order_2(self,name):
        print(name[0])