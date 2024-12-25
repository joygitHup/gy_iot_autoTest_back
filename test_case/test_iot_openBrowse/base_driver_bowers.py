import allure
from  selenium import  webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
@allure.epic("新能源PC端")
class driver_basePC_class():
    @classmethod
    def setup_class(self):
        #为Linux准备
        # service = Service(executable_path='/home/apploadpath/chromedriverPath/chrome-linux64')
        service = ChromeService(ChromeDriverManager().install())
        #本地测试 用一下代码需要在 webdriver.Chrome()注释掉servervice
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')  # 浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
        chrome_options.add_argument('--no-sandbox')  # 解决DevToolsActivePort文件不存在的报错
        chrome_options.add_argument('--disable-dev-shm-usage')  # 可以不加这一条
        self.driver = webdriver.Chrome(options=chrome_options,service=service)
        self.driver.get("http://192.168.20.212:5500/#/home")
        self.driver.maximize_window()

    @classmethod
    def teardown_class(self):
        self.driver.quit()

if __name__=="__main__":
    op=driver_basePC_class()
    op.setup_class()


