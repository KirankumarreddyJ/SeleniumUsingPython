from selenium import webdriver

executable_path = './drivers/chromedriver.exe'
driver = webdriver.Chrome(executable_path)
driver.get('https://www.thetestingworld.com/testings/')


driver.find_element_by_xpath("//label[text()='Login']").click()
driver.find_element_by_name("_txtUserName").send_keys('test')
driver.find_element_by_name("_txtPassword").send_keys('test')
driver.find_element_by_xpath("//input[@type='submit' and @value='Login']").click()

driver.find_element_by_xpath("//a[text()='logout']").click()
driver.close()
print("Code completly executed!")
