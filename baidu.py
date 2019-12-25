from selenium import webdriver


url = "https://www.baidu.com"

# 打开浏览器
browser = webdriver.Chrome()

# 最大化窗口
browser.maximize_window()

# 打开对应url地址
browser.get(url)

# 找到输入框，输入内容
browser.find_element_by_id('kw').send_keys("十月枫叶")

# 点击搜索
browser.find_element_by_id("su").click()

# 关闭浏览器
browser.close()


















