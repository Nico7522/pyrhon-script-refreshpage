import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# browser.get('https://www.youtube.com/')
# browser.refresh()

# seconds = time.time()
# print("Time in seconds since the epoch:", seconds)
# local_time = time.ctime(seconds)
# print("Local time:", local_time)
# # print("Local time:", local_time + 3600)

# print("This is the start of the program.")
# time.sleep(5)
# print("This prints five seconds later.")


options = webdriver.ChromeOptions() 
options.add_experimental_option("excludeSwitches", ["enable-logging"])
PATH = r"E:\DEV\chromedriver.exe"
s = Service(PATH)
inputUserWebSite = input('Entrez le lien du site Web que vous voulez rafraîchir : ')
browser = webdriver.Chrome(options=options , service=s)
browser.get(inputUserWebSite)
inputUserRefresh = input('Combien de fois voulez-vous rafraichir ? ')
x = int(inputUserRefresh)
i = 0
while(i < x):
    browser.refresh()
    time.sleep(3)
    i = i + 1



