# 抓取 Google Map 商家的 Review
# Python Need install...
#  $ pip install selenium
#  $ pip install beautifulsoup4
# TODO: 用 WebDriverWait 取代 Sleep

from asyncore import ExitNow
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as Soup
import time


# 此方法是透過 Chrome WebDriver
#  安裝 Driver到 /usr/local/bin，並在程式中指定 path
chrome_driver_path = "/usr/local/bin/chromedriver"
driver = webdriver.Chrome(chrome_driver_path)

# 設定要抓取的 Google Map Place URL
# 千味海鮮餐廳
url = 'https://www.google.com.tw/maps/place/%E5%8D%83%E5%91%B3%E6%B5%B7%E9%AE%AE%E9%A4%90%E5%BB%B3/@24.1318775,120.6438004,19z/data=!4m7!3m6!1s0x34693db5d5ade541:0x78048a5dbd45df6f!8m2!3d24.1321898!4d120.6443686!9m1!1b1'
driver.get(url)

# 捲動頁面，試圖抓取更多內容
SCROLL_PAUSE_SECOND = 2 # Second
MORE_PAUSE_SECOND = 0.5 # Second
MAX_EXPAND_NUMBER = 500

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")
pane_xpath = '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]'
number = 0
MAX_RETRY_COUNT = 2
retry_count = 0
BEFORE_RETRY_DELAY_SECOND = 30 # 每次 Retry 前，Delay的時間

while number < MAX_EXPAND_NUMBER:
    try:
        print(f'{number}) 目前 pane height = {last_height}，等{SCROLL_PAUSE_SECOND}秒 試著取得更多評論...')
        # Scroll down to bottom
        pane_elem = driver.find_elements(By.XPATH, pane_xpath)
        # driver.execute_script('arguments[0].scrollBy(0, 6000);', pane_elem[0])
        driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", pane_elem[0])
        time.sleep(SCROLL_PAUSE_SECOND)

        # 點擊「全文」Button，顯示完整的 Review 內容
        # (怪…找不到) buttons = driver.find_elements(By.CLASS_NAME, 'w8nwRe kyuRq')
        buttons = driver.find_elements(By.TAG_NAME, 'button')
        for btn in buttons:        
            if btn.text == "全文":
                btn.click()
                print('點擊[全文]Button，顯示更多內容…')
                time.sleep(MORE_PAUSE_SECOND)    

        new_height = driver.execute_script("return arguments[0].scrollHeight", pane_elem[0])
        print(f'{number}) 新的 pane height = {new_height}')

        if new_height == last_height:
            if (retry_count >= MAX_RETRY_COUNT):
                print(f'{number}) Exit')
                break
            retry_count = retry_count + 1
            delay_retry_second = BEFORE_RETRY_DELAY_SECOND * retry_count
            print(f'{number}) 沒反應，等{delay_retry_second}秒後再重試({retry_count})...')
            time.sleep(delay_retry_second)
        else:
            last_height = new_height
            number = number+1
            retry_count = 0
            # if (number % 50) == 0:
            #     print(f'{number}) 每抓 xx 筆就休息一下(試試看能不能突破 8x 障礙')
            #     time.sleep(BEFORE_RETRY_DELAY_SECOND)
    except Exception:
        print('發生錯誤離開迴圈，以目前狀態抓取資料。')
        break # break while loop
# ---< while loop >
    
# ----------------------------
import pandas as pd

# Find Review Items
items = driver.find_elements(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[9]')
if (items.count == 0):
    print(quit())

name_list = []
stars_list = []
review_list = []
duration_list = []


for i in items:
    # PS. 點擊「全文」Button，顯示完整的 Review 內容 (效果不好，移到上面scroll擴展頁面處理)
    # ---
    name_elems = i.find_elements(By.CLASS_NAME, "d4r55")
    duration_elems = i.find_elements(By.CLASS_NAME, "rsqaWe")
    star_elems = i.find_elements(By.CLASS_NAME, "kvMYJc")
    review_elems = []
    # FIXED: 如果review中有 "業主回應" 會導致內容錯位，因為兩者 class 都是 wiI7pd
    review_tmp_list = i.find_elements(By.CLASS_NAME, "wiI7pd")
    # 排除業主回應 (顧客評論是 span, 業主回應是 div)
    for chk_review in review_tmp_list:
        if chk_review.tag_name == 'span':
            review_elems.append(chk_review)

    
    # 抓取 評論者名字、星數、評論
    for na, du, st, re in zip(name_elems, duration_elems, star_elems, review_elems):
        # 排除空白評論
        if (re.text == ''):
            continue
        name_list.append(na.text)
        duration_list.append(du.text)
        stars_list.append(st.get_attribute("aria-label"))
        review_list.append(re.text)

driver.close

review_data = pd.DataFrame(
    {'name': name_list,
     'duration': duration_list,
     'rating': stars_list,
     'review': review_list})

review_data.to_csv('google_review.csv',index=False)
print(review_data)