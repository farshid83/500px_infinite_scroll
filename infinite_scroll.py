import os
import sys
import selenium
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.common.by import By

browser = webdriver.PhantomJS("phantomjs") # "phantomjs" or executable_path='C:\python27\scripts\phantomjs.exe'
# browser.get("https://twitter.com/StackStatus")
browser.get("https://500px.com/search?q=portrait")  # https://twitter.com/StackOverheards # https://500px.com/search?q=portrait
print browser.title

i = 0
# browser.get_screenshot_as_file("test03_2_" + str(i) + ".jpg")
while True:
    print "i = ", i
    #html = browser.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
    #print html
    elemsCount = browser.execute_script("return document.querySelectorAll('.photo_thumbnail').length") # ('.stream-items > li.stream-item').length")

    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # element = WebDriverWait(browser, 20).until(
    #	EC.presence_of_element_located((By.XPATH,
    #		"//*[contains(@class,'GridTimeline-items')]/li[contains(@class,'stream-item')]["+str(elemsCount+1)+"]")))
    try:
        WebDriverWait(browser, 100).until(
            lambda x: x.find_element_by_xpath(
                './/img[@class="lazy-hidden"][" + str(elemsCount + 1) + "]'))
                #'.//a[@class="photo-link"][" + str(elemsCount + 1) + "]'))
    except:
        break

    i += 1
    #browser.get_screenshot_as_file("test03_2_" + str(i) + ".jpg")
    #htmlcontent = browser.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
    if(i%1000 == 0):
        print "count = ", elemsCount
        htmlcontent = browser.page_source.encode('utf-8')
        linkfile = open("linkfile_" + str(i) + ".html", 'w')
        linkfile.write(htmlcontent)
        linkfile.close()

browser.quit()
