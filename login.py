from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
import pickle

class Connect:
    def get_cookie(self):
        try:
            cookies = pickle.load(open("cookies.pkl", "rb"))
            for cookie in cookies:
                cookie_dict = {
                    'domain':'.damai.cn',
                    'name':cookie.get('name'),
                    'value':cookie.get('value')
                }
                driver.add_cookie(cookie_dict)
            print('载入Cookie')
        except Exception as e:
                print(e)

    def login(self):
        if self.
    def login_fr(url, username, password):
        option = webdriver.ChromeOptions()
        # 设置代理服务器ip
        option.add_argument('--proxy-server=http://218.7.171.91:3128')
        # 规避google部分bug
        option.add_argument('--disable-gpu')
        # 禁止加载图片
        option.add_argument('--blink-settings=imagesEnabled=false')
        # 无痕模式
        option.add_argument('--incognito')
        # 无界面浏览
        option.add_argument('--headless')
        driver = webdriver.Chrome(options=option)
        # 打开链接
        driver.get(url)

        # 登录页面是iframe
        driver.switch_to.frame('alibaba-login-box')

        # 找到输入框，这里需要自行在F12的Elements中找输入框的位置，然后在这里写入
        user_input = driver.find_element(by=By.NAME, value='fm-login-id')
        pw_input = driver.find_element(by=By.NAME, value='fm-login-password')
        login_btn = driver.find_element(by=By.XPATH, value='/html/body/div/div/div[2]/div/form/div[4]/button')

        # 打印定位到的元素
        print(user_input.id)
        print(pw_input.text)
        print(login_btn.location)

        # 输入用户名和密码，点击登录
        user_input.send_keys(username)
        pw_input.send_keys(password)
        login_btn.click()

        # 回到主页面
        driver.switch_to.default_content()

        #获取cookies
        cookies = driver.get_cookies()
        pickle.dump(cookies, open("cookies.pkl", "wb"))
        # print(cookies)
        print('登录成功')

        return driver
 
if __name__ == '__main__':
    # 定义目标URL信息
    aim_url = {
        'url': 'https://passport.damai.cn/login?ru=https%3A%2F%2Fwww.damai.cn%2F',
        'username': '',
        'password': ''
    }

    # 登录
    driver = login_fr(aim_url['url'], aim_url['username'], aim_url['password'])
