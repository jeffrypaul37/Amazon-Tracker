from dataclasses import field
import requests
import numpy as np
import time
import matplotlib.pyplot as plt
from matplotlib import animation
from bs4 import BeautifulSoup
import pandas as pd
import datetime
import smtplib
import csv
import re
from csv import DictWriter
import matplotlib.pyplot as plt
import numpy as np
import csv
import random
import time
import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
import threading
import os

headers={"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',"Regerer":''}


def send_mail(url,title):
        server=smtplib.SMTP('smtp.gmail.com',587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login('yourmail@gmail.com','password')
        subject ='Attention ! Price has dropped !'+'\n'+title.strip()
        body='Check the link!! '+url
        msg=f"subject:{subject}\n\n{body}"
        server.sendmail('yourmail@gmail.com','yourmail@gmail.com',msg)
        print("Email sent!")
        
        



def check_price(url,Price):
        proxies_list = [
                '167.172.248.53:3128',
                '194.226.34.132:5555',
                '203.202.245.62:80',
                '141.0.70.211:8080',
                '118.69.50.155:80',
                '201.55.164.177:3128',
                '51.15.166.107:3128',
                '91.205.218.64:80',
                '128.199.237.57:8080',
                ] 
        proxies = {
                'http': random.choice(proxies_list)
                }
        
        flag=0
        print("Fetching product data...")
        page=requests.get(url,headers=headers,proxies=proxies)         
        soup=BeautifulSoup(page.content,'lxml')

        title=soup.find(id="productTitle").get_text()
        print(title.strip())
        prices=[]

        fieldnames = ["x_value", "total_1", "total_2"]
        threadLocalVariable = threading.local()
        threadLocalVariable.productName = title.strip()[:20]
        projectDir=os.path.dirname(os.path.abspath("__file__"))
                                
                          
        
        while(True):   
                page=requests.get(url,headers=headers)         
                soup=BeautifulSoup(page.content,'lxml')        

                http_proxy  = "http://10.10.1.10:3128"
                https_proxy = "https://10.10.1.11:1080"               
                ftp_proxy   = "ftp://10.10.1.10:3128"                           

                proxyDict = { 
                                "http"  : http_proxy, 
                                "https" : https_proxy, 
                                "ftp"   : ftp_proxy
                        }
                        
                price=soup.find(class_="a-offscreen").get_text()
                converted_price=float(price[1:10].replace(",",""))
                time_stamp=datetime.datetime.now()
                time_stamp=time_stamp.strftime("%d-%m-%Y %H:%M:%S")
                
                print(time_stamp+' '+title)
                print("Price is now "+price)
                print(' ')
                prices.append(converted_price)
                if(converted_price <=Price and flag==0):
                        flag=1
                        send_mail(url,title)
                if(converted_price >Price and flag==1):
                        flag=0
                x_value = time_stamp
                total_1 = converted_price
                file_name = threadLocalVariable.productName+'.csv'
                with open(os.path.join(projectDir,'data',file_name), 'a') as csv_file:
                        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                        info = {
                        "x_value": x_value,
                        "total_1": total_1,
                }
                        csv_writer.writerow(info)
             
                
productCount = 3                      
productLinks = []
pdtPrice=[]
for i in range(productCount):
     
        productLink1 = 'https://www.amazon.in/gp/product/B09V7ZJYBN?th=1'
        productLink2 = 'https://www.amazon.in/Dell-E6330-i5-4-GB-120-GB-Integrated/dp/B07LBDB5RY'
        productLink3 = 'https://www.amazon.in/Dell-Docking-Station-Power-Delivery/dp/B07RF9FZCS'
        productLinks.append(productLink1)
        productLinks.append(productLink2)
        productLinks.append(productLink3)
        
        
      
        pdtprice1=15000
        pdtprice2=15000
        pdtprice3=30000
        pdtPrice.append(pdtprice1)
        pdtPrice.append(pdtprice2)
        pdtPrice.append(pdtprice3)

for productLink,price in zip(productLinks,pdtPrice):
        thread = threading.Thread(target=check_price, args=(productLink,price,))
        thread.start()

 


