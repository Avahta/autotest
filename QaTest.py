from selenium import webdriver

#driver = webdriver.Chrome()
#driver.get("https://www.google.com/")
#driver.implicitly_wait(3)
#driver.find_element_by_name("q").send_keys("webdriver")
#driver.find_element_by_css_selector("body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf > div.FPdoLc.lJ9FBc > center > input.gNO89b").click()

#driver = webdriver.Chrome()
#driver.get("http://testerlaru.temp.swtest.ru/index.php?route=account/login")
#driver.find_element_by_name("email").send_keys("janchik-91@mail.ru")
#driver.find_element_by_name("password").send_keys("janatroha1991")
#driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[2]/div/form/input").click()

driver = webdriver.Chrome()
driver.get("http://testerlaru.temp.swtest.ru/index.php?route=account/login")
driver.find_element_by_name("email").send_keys("janchik-91@mail.ru")
driver.find_element_by_name("password").send_keys("janatroha1991")
driver.find_element_by_css_selector("#content > div > div:nth-child(2) > div > form > input").click()
driver.quit()