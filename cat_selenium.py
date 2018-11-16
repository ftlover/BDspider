from selenium import webdriver
# 创建chrome参数对象
opt = webdriver.ChromeOptions()
# 把chrome设置成无界面模式，不论windows还是linux都可以，自动适配对应参数
# opt.set_headless()
# 创建chrome无界面对象
browser = webdriver.Chrome(options=opt)
url = "https://www.feemoo.com/fmdown.php?2e64ZrHsnlJsLoxm/gVvOB42/eFdxCOjBJUqIuR1gqQTSy7ox21L2h1cAk2ZiLC8l9W25BkaxBZlh2xG7OR76aH9Kla0H7HRmTmZ+P1MocIbWH9fy8c"
browser.get(url)
print(browser.get_cookies())
browser.execute_script("vip_downvip_down('com','2027551')")
