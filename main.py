from selenium import webdriver
import os
from selenium.webdriver.common.by import By

os.environ['PATH'] += r'/Users/jacobyoo/Desktop/PythonProjects/chromedriver'
driver = webdriver.Chrome()

driver.get("")
