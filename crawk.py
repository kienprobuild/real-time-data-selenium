from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


options = Options()

options.add_experimental_option('excludeSwitches', ['enable-logging'])

# 1. Khai báo browser
browser = webdriver.Chrome(executable_path="./chromedriver",chrome_options=options)
# url = "https://shopee.sg/-Pre-Order-MSI-Optix-MAG274QRF-QD-Gaming-Monitor-(27inch-WQHD-Rapid-IPS-Panel-165hz-1ms-G-Sync-3Y)-i.235042613.6761847522?sp_atk=4a4f3668-b0be-45ff-b89a-e861279f7c14"
url = "https://shopee.sg/Lead-Fishing-Sinker-Fishing-Bullet-Shaped-Weights-Casting-Sinkers-Weight-i.169185575.3114732181?sp_atk=c5899ef1-e6a6-4f1b-a558-374a54a880a7"
# 2. Mở URL của post
browser.get(url)

browser.execute_script("window.scrollTo(0," + "300" + " )") 

sleep(3)

element = browser.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[1]/div/div[2]/div/div[3]/div[2]/div[1]/div[1]"); 
#get x, y coordinates//*[@id='main']/div/div[2]/div[1]/div/div[2]/div[2]/div[3]/div[3]/div[1]/div[1]/div[2]/div[2]/div

loc = element.location
#get height, width
s = element.size
print(loc)
print(s)
h = str(loc["y"] + s["height"])
browser.execute_script("window.scrollTo(0," + h + " )") 
sleep(5)


# sleep(5)

# # 3. Lấy link hiện comment
# #browser.find_elements_by_class_name("shopee-product-rating__main")
a=browser.find_elements_by_class_name("shopee-product-rating__main")
# print(a)
# # # 3. Lấy link hiện comm
# # comment_list = browser.find_element_by_class_name("_3NrdYc")
l=[]
for i in a:
    b=i.find_element_by_class_name("_3NrdYc")
    print(b.text)
    

sleep(5)


# browser.close()
