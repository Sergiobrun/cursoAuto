
from selenium import webdriver
import unittest
import time

tc = unittest.TestCase('__init__')

driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://www.youtube.com/')
driver.find_element_by_id('search').send_keys('gol del pity autotune')
driver.find_element_by_id('search-icon-legacy').click()


time.sleep(5)
tc.assertEqual('Gol del Pity - Mariano Closs | Version Musical con Autotune | (Video: @martinofll) de Pasion Millonaria hace 2 años 1 minuto y 20 segundos 19,913 vistas', driver.find_element_by_xpath('//*[@id="video-title"]/yt-formatted-string').text ) 

driver.close()
driver.quit()