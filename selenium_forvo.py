from selenium import webdriver
from selenium.webdriver.common.by import By
# python -m pip install selenium

#Crhome closes automatically. Using Firefox
browser = webdriver.Firefox()
browser.get('https://forvo.com/')
searchBar = browser.find_element(By.ID,'word_search_header')
searchBar.send_keys('Gesundheit')
searchBar.submit
