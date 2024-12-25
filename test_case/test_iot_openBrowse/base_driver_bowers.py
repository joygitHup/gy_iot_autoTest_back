import allure
from  selenium import  webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
@allure.epic("新能源PC端")
class driver_basePC_class():
    @classmethod
    def setup_class(self):
        #为Linux准备
        chrome_path = "/home/apploadpath/chromedriverPath/chrome-linux64/chrome"
        options =Options()
        options.add_argument('--headless')  # 浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
        options.add_argument('--no-sandbox')  # 解决DevToolsActivePort文件不存在的报错
        options.add_argument('--disable-dev-shm-usage')  # 可以不加这一条
        # 本地测试 用一下代码需要在 webdriver.Chrome()注释掉options.binary_location = chrome_path
        options.binary_location = chrome_path
        self.driver =webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=options)
        self.driver.get("http://192.168.20.212:5500/#/home")
        self.driver.maximize_window()

    @classmethod
    def teardown_class(self):
        self.driver.quit()
#
# if __name__=="__main__":
#     op=driver_basePC_class()
#     op.setup_class()


