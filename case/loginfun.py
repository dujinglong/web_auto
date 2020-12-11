# conding:utf-8
def login(driver, user="18321252140", psw="123456"):
    driver.get("https://mms.aixiangdao.top/develop/login")
    driver.find_element_by_xpath("/html/body/div/div/form/div[2]/div[1]/div/div/input").send_keys(user)  # 输入账号
    driver.find_element_by_xpath("/html/body/div/div/form/div[2]/div[2]/div/div/input").send_keys(psw)  # 输入密码
    driver.find_element_by_xpath("/html/body/div/div/form/div[4]/div/button/span").click()  # 点击进入商家页面

