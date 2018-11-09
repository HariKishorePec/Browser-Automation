from selenium import webdriver 
import time
browser = webdriver.Chrome("C:\webdriver\chromedriver.exe")  #your location of chromedriver
#browser.get("http://www.google.com") #Starts a sample website
browser.get("http://nptel.ac.in/courses/nptel_download.php?subjectid=106106182")#This is the subject ID which course i want to download
#click on a link
#elem = browser.find_element_by_link_text("FLV Download") #Link selection
#elem.click()   #clicking on the link
time.sleep(20)
count=0
for j in range(5):
    elem = browser.find_elements_by_link_text("FLV Download")
    for i in elem:
        count+=1
        i.click()
        time.sleep(10)
        print("File ",count, "Downloaded")
    ele = browser.find_element_by_link_text("Next")
    ele.click()
    time.sleep(5)     #average time given to download a video, can change depending on your net speed.
