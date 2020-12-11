# coding = utf-8
from selenium import webdriver
import time
import unittest


class Mms(unittest.TestCase):
    '''登录类的案例'''
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()  # 启动浏览器

    def setUp(self):
        self.driver.get("https://mms.aixiangdao.top/develop/login")
        time.sleep(4)
        self.driver.maximize_window()

    def get_login_username(self):
        # 判断是否登录成功
        try:
            t = self.driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[1]/div/ul/div/a[2]/li/span").text
            print(t)
            return t
        except:
            return ""

    def login(self,user,psw ):
        self.driver.find_element_by_xpath("/html/body/div/div/form/div[2]/div[1]/div/div/input").send_keys(user)  # 输入账号
        self.driver.find_element_by_xpath("/html/body/div/div/form/div[2]/div[2]/div/div/input").send_keys(psw)  # 输入密码
        time.sleep(3)
        self.driver.find_element_by_xpath("/html/body/div/div/form/div[4]/div/button/span").click()  # 点击进入商家页面

    def get_login_is_alert(self):
        # 判断提示是否存在
        try:
            time.sleep(3)
            alert = self.driver.switch_to.alert
            text = alert.text
            # alert.accept() # 用alert 点alert
            return text
        except:
            return ""

    def test_01(self):
        '''用例说明:登录成功的案例'''
        time.sleep(2)
        self.login("18321252140", "123456")
        # 判断是否登录成功
        # t = self.driver.title
        # print(t)
        time.sleep(3)
        t = self.get_login_username()
        print("获取的结果：%s"%t)
        self.assertTrue(t == "店铺管理")
        # self.driver.find_element_by_xpath("//*[@id=\"app\"]/div/div[2]/div[1]/div/ul/div[4]/div[3]/div/input").click()
        # time.sleep(2)
        # self.driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/ul/li[4]/span").click()
        # self.driver.quit()

    def test_02(self):
        '''用例说明：登录失败的案例'''
        time.sleep(2)
        # 错误的密码
        self.login("18321252140", "12345")
        # 判断是否登录成功
        # t = self.driver.title
        # print(t)
        t = self.get_login_username()
        print("登录失败，获取的结果：%s"%t)
        self.assertTrue(1 == "测试")  # 断言截图

    def tearDown(self):
        self.get_login_is_alert()
        self.driver.delete_all_cookies()  # 清空cookies
        self.driver.refresh()  # 刷新页面

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()  # 编辑器问题


if __name__ == '__main__':
    unittest.main()