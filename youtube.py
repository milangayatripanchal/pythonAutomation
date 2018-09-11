from selenium import webdriver

usr = input('enter the search ')

driver = webdriver.Chrome()
driver.get('https://www.youtube.com')

search_box = driver.find_element_by_id('search')
search_box.send_keys(usr)

search = driver.find_element_by_id('search-icon-legacy')
search.click()