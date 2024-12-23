import allure
from  selenium import  webdriver
@allure.epic("新能源PC端")
class driver_basePC_class():
    @classmethod
    def setup_class(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')  # 浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
        chrome_options.add_argument('--no-sandbox')  # 解决DevToolsActivePort文件不存在的报错
        chrome_options.add_argument('--disable-dev-shm-usage')  # 可以不加这一条
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get("http://192.168.20.212:5500/#/home")
        self.driver.maximize_window()

    @classmethod
    def teardown_class(self):
        self.driver.quit()

if __name__=="__main__":
    op=driver_basePC_class()
    op.setup_class()


