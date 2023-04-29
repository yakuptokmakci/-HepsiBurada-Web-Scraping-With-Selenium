from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


options = Options()
##options.add_experimental_option("detach",True) pencere kapama
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=options)
adress="https://www.hepsiburada.com/huawei-matebook-d15-intel-core-i7-1195g7-16gb-512gb-ssd-windows-11-home-15-6-fhd-tasinabilir-bilgisayar-pm-HBC00003MY12F"
degree=9.5
def Hepsiburada(adress,degree):
    score = []
    price = []
    store = []

    driver.get(adress)
    ##driver.maximize_window() pencere büyütme

    destinations = driver.find_elements("xpath",
                                        "//div[contains(@class,'list-container')]//span[contains(@class,'price product-price')]")
    names = driver.find_elements("xpath",
                                 "//div[contains(@class,'list-container')]//span[contains(@data-bind,'text: merchantName')]")
    points = driver.find_elements("xpath",
                                  "//td[contains(@class,'merchantName')]//span[contains(@class,'merchant-rating lv-5')]")

    for destination in destinations:
        price.append(destination.get_attribute("innerHTML"))

    for name in names:
        store.append(name.get_attribute("innerHTML"))

    for point in points:
        qq = point.get_attribute("innerHTML").replace(",",".") ## hepsi burada "," ile kaydettiği için . ya çevirdik
        score.append(float(qq))

    for x in range(len(score)):
        if score[x]>=degree:
            print(store[x], price[x], score[x])


Hepsiburada(adress,degree)