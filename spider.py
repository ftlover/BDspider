from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import re
import bdspider
import json

# browser.set_window_size(480, 760)
def sign_in(browser):
	# 登录百度云
	browser.get("https://pan.baidu.com")
	sleep(2)
	element = browser.find_element_by_xpath(".//*[@class='tang-pass-footerBarULogin pass-link']")
	sleep(0.2)
	ActionChains(browser).click(element).perform()  # 单击某元素
	browser.find_element_by_xpath(".//*[@class='pass-text-input pass-text-input-userName']").send_keys(
		"mail_xupengfei@163.com")
	sleep(0.5)
	browser.find_element_by_xpath(".//*[@class='pass-text-input pass-text-input-password']").send_keys("xupengfei")
	sleep(0.5)
	browser.find_element_by_xpath(".//*[@class='pass-button pass-button-submit']").send_keys(Keys.ENTER)
	return browser


def enter_file(browser, url, key):
	browser.get(url)
	sleep(1)
	elem = browser.find_element_by_xpath("//*[@class='QKKaIE LxgeIt']")
	sleep(0.2)
	elem.send_keys(key)
	sleep(0.2)
	elem.send_keys(Keys.ENTER)
	return browser


def transfer(browser):
	page = browser.page_source
	uk = re.search(r"\"uk\":\d*", page).group()
	uk = re.search(r"\d+", uk).group()
	shareid = re.search(r"\"shareid\":\d*", page).group()
	shareid = re.search(r"\d+", shareid).group()
	bdstokendict = eval("{" + re.search(r"\"bdstoken\":\"\w+\"", page).group() + "}")
	bdstoken = bdstokendict["bdstoken"]
	file_list = eval("{" + re.search(r"\"path\":\".+?\"", page).group().replace(r"\/", "/") + "}")
	# print(re.search(r"\"path\":\".+?\"",page).group())
	file_list = file_list["path"]
	selenium_cookies = browser.get_cookies()
	cookies = {}
	for cookie in selenium_cookies:
		cookies[cookie["name"]] = cookie['value']
	# if cookie["name"] == 'STOKEN':
	# 	stoken = cookie["value"]
	# if cookie["name"] == "BDUSS":
	# 	bduss = cookie["value"]
	# print(cookies)
	bds = bdspider.Spider(cookies, url, bdstoken)
	bds.create_folder("/hello")
	bds.transfer(shareid, uk, file_list, "/hello")

if __name__ == '__main__':
	# 创建chrome参数对象
	opt = webdriver.ChromeOptions()
	# 把chrome设置成无界面模式，不论windows还是linux都可以，自动适配对应参数
	# opt.set_headless()
	# 创建chrome无界面对象
	browser = webdriver.Chrome(options=opt)
	browser = sign_in(browser=browser)
	url = "https://pan.baidu.com/s/1rhhKLdoJLdWh9-Dc-SUbsg"
	url_key = "hwdx"
	browser = enter_file(browser, url, url_key)
	sleep(1)
	browser.get(url)
	transfer(browser)


