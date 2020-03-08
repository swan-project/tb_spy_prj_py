from selenium import webdriver
from pyquery import PyQuery as pq
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from config import *
from urllib.parse import quote
from bs4 import BeautifulSoup
import time
import urllib.request
import urllib.parse
import requests
import re
TAOBAO_TIME_OUT = 9

#driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe');
driver = webdriver.Chrome('C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe');
wait = WebDriverWait(driver, 10)


driver.get('https://login.taobao.com/member/login.jhtml')
#driver.get('https://world.taobao.com/')

#element = driver.find_element_by_link_text("密码登录")
#element = driver.find_element_by_id('J_QRCodeImg');
i=1
html = driver.page_source
doc = pq(html)
id = doc.text()



def get_products(item_list):
    """
    提取商品数据
    """
    html = driver.page_source
    doc = pq(html)
    items = doc('#mainsrp-itemlist .items .item').items()
    for item in items:
        print(item.children())
        product = {
            'image': item.find('.pic .img').attr('src'),
            'item_link': item.find('.pic .pic-link').attr('href'),
            'price': item.find('.price').text(),
            'deal': item.find('.deal-cnt').text(),
            'title': item.find('.title').text(),
            'shop': item.find('.shop').text(),
            'location': item.find('.location').text(),
            'id': item.find('.pic .img').attr('id')
            
        }


        item_list.append(product)
        page = driver.find_element_by_xpath('//*[@id="'+product['id']+'"]');
        
        page.click()
        time.sleep(5)
        #print(item_list[0]['item_link'])
        #driver.get(str(link))
        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)
        b= driver.find_element_by_xpath('//*[@id="J_ImgBooth"]')
        #tb_price = driver.find_element_by_xpath('//*[@id="J_StrPriceModBox"]/dd/span')
        #tb_price = driver.find_element_by_xpath('//*[@id="J_PromoPrice"]/dd/div/span')
        tb_price = driver.find_element_by_xpath('//*[@class="tm-price"]')

        #//*[@id="J_StrPriceModBox"]/dd/span
        print(b.get_attribute('src'))
        print(tb_price.get_attribute('text'))
        print(tb_price.text)
        
        tb_size_options = driver.find_elements_by_xpath('//*[@id="J_DetailMeta"]/div[1]/div[1]/div/div[4]/div/div/dl[1]/dd/ul/li')
        tb_product_options = driver.find_elements_by_xpath('//*[@id="J_DetailMeta"]/div[1]/div[1]/div/div[4]/div/div/dl[2]/dd/ul/li')

        for i in range(len(tb_size_options)):
            print(tb_size_options[i].text)   

       #for i in range(len(tb_product_options)):
       #    print(tb_options[i].text)
      #description > div > table:nth-child(5) > tbody > tr:nth-child(2) > td:nth-child(1) > img
        src=driver.current_url
        for j in range(len(tb_product_options)):
            if(tb_product_options[j]):
              print(tb_product_options[j].find_element_by_css_selector('span').text)
        tb_description = driver.find_elements_by_xpath('//*[@id="description"]/div')
        tb_description_img = tb_description[0].find_elements_by_tag_name("img")
        print(len(tb_description_img))
        print(tb_description_img[0].get_attribute('src'))
        for i in range(len(tb_description_img)):
            #print(tb_description[i].find_elements_by_xpath('//tbody/tr[2]/td[1]/img').text)
            #print(tb_description[i].find_element_by_css_selector('img').get_attribute('src'))
            print(tb_description_img[i].get_attribute('src'))
              
              #html = driver.page_source
        #html_inner = pq(html)
        #pat_id = 'id=(.*?)&'

        #tb_img = re.compile(pat_id).findall(html)

        #//*[@id="shop15676986358"]/div/div/span/table/tbody/tr/td[1]/img
        #////*[@id="description"]/div/table[2]/tbody/tr[3]/td/a/img
        


        #print(src)
        #time.sleep(10)
        #r = requests.get(src, timeout=TAOBAO_TIME_OUT)
        #soup = BeautifulSoup(r.text,"html.parser")
        #aa = soup.find_all('img'z,{'id':'J_ImgBooth'})
        ##bb = soup.find_all('ul',{'data-property':'尺码'})

        #items = {
        #    'item_img': soup.find_all('img',{'id':'J_ImgBooth'}),
        #    'item_price': soup.find_all('span',{'class':'tm-price'}),

        #    }
        ##with urllib.request.urlopen(str(driver.current_url)) as response:
        #with urllib.request.urlopen(src) as fp:
        #   # product_page = response.read()
        #    product_soup = BeautifulSoup(fp,'html.parser')
        #    tb_img = product_soup.find_all('img',{'id':'J_ImgBooth'})
        #    print(tb_img)
 
        #htm=html_inner('#J_DetailMeta .tb-booth').items();
        #abc = htm.find('J_ImgBooth').attr('src');
        #print(htm)
        

        #item_img = item_info.find('.img').attr('src')
        #print(item_info)

        driver.close()
        window_origin = driver.window_handles[0]
        driver.switch_to.window(window_origin)
        src=driver.current_url
        print(src)


        #item_liist.add()



while True :

    #print(driver.find_element_by_id('J_QRCodeImg').is_displayed())
    #qrcode = driver.find_element_by_id('J_QRCodeImg')
    url = driver.current_url
    if(url=='https://world.taobao.com/'):
        print('passed')
        print(url)
        break;

    #qrcode_msg = driver.find_element_by_class_name('qrcode-msg').is_enabled()
    #if qrcode_msg:
    #    if(qrcode_msg):
    #        qrcode_ok = driver.find_element_by_class_name('msg-ok').is_enabled()
    #        if(qrcode_ok):
    #            break

    else:
        print(0)
    #if driver.find_element_by_id('J_QRCodeImg').is_displayed():
    #  print(i)

print("passed")

driver.implicitly_wait(3)

categorys=[]
#categorys = driver.find_elements_by_class_name('category-container')
categorys = driver.find_elements_by_xpath('//div[@class=\'category-container\']/div')

big_categories=[]


for i in range(len(categorys)):
    #print (categorys[i].get_attribute('class')) 
    #link1= (categorys[i].get_attribute('class'))
   # text = '//div[@class=\''+(categorys[i].get_attribute('class'))+'\']'
    if i!=0:
         big_categories.append(categorys[i].find_element_by_css_selector('a').get_attribute('href'))
         #link = categorys[i].find_element_by_css_selector('a')
         #categorys[i].find_element_by_css_selector('href').get_attribute('href').click()
         #print(big_categories[i])
         #link.send_keys('\n')

         #안쪽 카테고리 한 번더 검색



for i in range(len(big_categories)):

    driver.get(big_categories[i])
    current_page = driver.current_url

    print(current_page)
    sales = current_page+'&sort=sale-desc'
    #sales = driver.find_element_by_xpath('//*[@id="J_relative"]/div[1]/div/ul/li[2]/a').get_attribute('href')
    #sales.replace("#","&sort=sale-desc")
    print(sales)
    driver.get(sales)

    #item_list = driver.find_elements_by_class_name('items')
    item_list = []
    get_products(item_list)
    #for j in range(len(item_list)):
    #    item  = item_list[j].find_element_by_css_selector('a').get_attribute('href')
    #    print(item)

    #J_relative > div.sort-row > div > ul > li:nth-child(2) > a



