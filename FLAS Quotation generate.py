#!/usr/bin/env python
# coding: utf-8

# In[1]:


import bs4 as bs
import os.path
from pathlib import Path
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
import requests
from urllib.request import Request, urlopen
from selenium import webdriver
import mechanicalsoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
import urllib.request
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from lxml import html
from datetime import datetime

#xml = html.fromstring(h)
browser = mechanicalsoup.StatefulBrowser()


# In[31]:


page = 'https://w7.financial-link.com.my/Agency/loginTAK.jsp'

        
def Quotation_generate(name,NRIC1,NRIC2,NRIC3,phone_num,email,address,postcode,no_plate,model_name):  
        global initial_size
        initial_size = 3  # reset the row size to 3 for child select
        firefox_profile = webdriver.FirefoxProfile()
        firefox_profile.set_preference("browser.privatebrowsing.autostart", True)

        driver = webdriver.Firefox(executable_path = 'C:\Windows\geckodriver.exe',firefox_profile=firefox_profile)

        

        driver.get(page)

        driver.find_element_by_name('field1').send_keys("gtxkatsana")
        driver.find_element_by_name('field2').send_keys("cx97J7JrnpvwAjfB")

        submit = driver.find_element_by_name('Submit')
        submit.click()

        element = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "New Business"))
        )
                                   
        element.click()                                  

        WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "New Business"))
        )

        driver.find_element_by_name('email').send_keys(str(email))
        driver.find_element_by_xpath("//select[@name='nametitle']/option[@value='MR']").click()
        driver.find_element_by_name('name').send_keys(str(name))
        driver.find_element_by_name('new_ic1').send_keys(NRIC1)
        driver.find_element_by_name('new_ic2').send_keys(NRIC2)
        driver.find_element_by_name('new_ic3').send_keys(NRIC3)
        #driver.find_element_by_name('DOB').send_keys("6128")
        driver.find_element_by_xpath("//select[@name='race']/option[@value='C']").click()
        driver.find_element_by_xpath("//select[@name='religion']/option[@value='C']").click()
        driver.find_element_by_name('drvexp').send_keys("3")
        driver.find_element_by_xpath("//select[@name='occupation']/option[@value='106@NULL@OTHERS']").click()
        driver.find_element_by_xpath("//select[@name='emp_status']/option[@value='5']").click()
        driver.find_element_by_name('address1').send_keys(address)
        driver.find_element_by_name('postcode').send_keys(postcode)
        driver.find_element_by_xpath("//select[@name='area']/option[@value='V|W.P. KUALA LUMPUR']").click()
        driver.find_element_by_xpath("//select[@name='claimyr']/option[@value='0']").click()
        driver.find_element_by_xpath("//select[@name='claimyr1']/option[@value='0']").click()
        driver.find_element_by_xpath("//select[@name='claimyr2']/option[@value='0']").click()
        driver.find_element_by_xpath("//select[@name='claimyr3']/option[@value='0']").click()
        driver.find_element_by_xpath("//select[@name='violation']/option[@value='0']").click()
        driver.find_element_by_xpath("//select[@id='vehicle']/option[@value='PRCAR']").click()
        driver.find_element_by_xpath("//select[@id='condition']/option[@value='u']").click()
        driver.find_element_by_xpath("//select[@name='vehiclefrom']/option[@value='1']").click()
        driver.find_element_by_xpath("//select[@name='claimyr']/option[2]").click()
        driver.find_element_by_xpath("//select[@name='claimyr1']/option[2]").click()
        driver.find_element_by_xpath("//select[@name='claimyr2']/option[2]").click()
        driver.find_element_by_xpath("//select[@name='claimyr3']/option[2]").click()
        driver.find_element_by_name('vehregno').send_keys(str(no_plate))
        time.sleep(2)
        driver.find_element_by_name('logbookno').send_keys("6128")

    #driver.find_element_by_id('engineno').send_keys("6128")
    #driver.find_element_by_name('chassisno').send_keys("6128")
    #driver.find_element_by_name('makeyear').send_keys("2018")
        driver.find_element_by_xpath("//select[@id='cover_type']/option[@value='COMP']").click()

    #ale = driver.switch_to_alert();
    #ale.accept();

        time.sleep(2)
    #driver.find_element_by_id('engineno').send_keys("WC5264N")
    #driver.find_element_by_name('chassisno').send_keys("6128")

        driver.find_element_by_name('town').send_keys("ampang")
        driver.find_element_by_xpath("//select[@id='cover_type']/option[@value='COMP']").click()
        driver.find_element_by_xpath("//select[@name='bodyID']/option[@value='81|2WD']").click()

        #select = Select(driver.find_element_by_xpath("//select[@name='make_ID']"))

        #options = select.options
        #driver.find_element_by_xpath("//select[@name='make_ID']/option[%d]" % make_id).click()



                
    #for index in range(0, 1):
    #    select.select_by_index(2)
    #driver.find_element_by_xpath("//select[@name='make_ID']/option[@value='33']").click()
        #driver.find_element_by_xpath("//select[@name='model_ID']/option[%d]" % model_id).click()
        #makeyear = driver.find_element_by_name('makeyear')
        #makeyear.clear()
        #makeyear.send_keys(str(year))



        #driver.find_element_by_name('provCapacity').send_keys(provCapacity)
        driver.find_element_by_xpath("//select[@name='garage']/option[@value='1']").click()
        driver.find_element_by_xpath("//select[@name='safety']/option[@value='07']").click()
        driver.find_element_by_xpath("//select[@name='antitd']/option[@value='12']").click()
        driver.find_element_by_xpath("//select[@name='vehModification']/option[@value='0']").click()
        driver.find_element_by_xpath("//select[@name='funcModification']/option[@value='0']").click()
        driver.find_element_by_xpath("//select[@name='piamdrv']/option[@value='03']").click()  
        #driver.find_element_by_name('makeyear').send_keys("2018")
        nvic = driver.find_element_by_name("nvic").get_attribute("value")
        
        select = Select(driver.find_element_by_name('model_ID'))
        driver.find_element_by_xpath("//select//option[contains(., '%s')]" % model_name).click()
        

        window_before = driver.window_handles[0]
        car_listbutton = driver.find_elements_by_xpath("//input[@name='abibutton' and @value='Check for Proposed Sum Covered']")[0]
        car_listbutton.click()

        window_after = driver.window_handles[1]
        driver.switch_to_window(window_after)
        time.sleep(1)
        rows = driver.find_elements_by_xpath("//table/tbody/tr")
        #driver.find_element_by_css_selector("body > form:nth-child(2) > center:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(%d) > td:nth-child(1)" % initial_size).click()
        driver.find_element_by_xpath("//*[text()='%s']" % nvic).click()
        driver.switch_to_window(window_before)
    
    
        #driver.switch_to_window(window_before)
        market_value = driver.find_element_by_name("abimarketval").get_attribute("value")
        market_value_percentage = float(market_value) * (0.10)
        market_max = float(market_value) + market_value_percentage
        market_min = float(market_value) - market_value_percentage
    
        print(market_max)
    #print(market_min)
    
    
        limit = range(int(market_min),int(market_max),1000)
    
        driver.find_elements_by_xpath("//input[@name='nextButton' and @value='Add Extra Benefit']")[0].click()
        element = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.ID, "genQuotation"))
        )
        element.click()
    
        time.sleep(1)
        cont_pricing = driver.find_element_by_name("tariffpremiumDT").get_attribute("value")
        sum_covered = driver.find_element_by_name("sum_insured").get_attribute("value")
        grossdueDT = driver.find_element_by_name("grossdueDT").get_attribute("value")
        print("Cont Pricing : " + cont_pricing)
        print("Sum Covered : " + sum_covered)
        print("Gross Due Total : " + grossdueDT)
        return rows,limit
   


# In[33]:


# data to be send
name = "Syed Ahmad Fuqaha bin Sd. Agil"
ic1 =  '870820'
ic2 = '29'
ic3 = '5457'
tel = '0174039887'
email = 'fuqaha122@gmail.com'
address = '2805, Jalan Damansara, Kampung Sungai Penchala,'
postcode = '60000'
no_plate = 'VAF2555'
model_name = '330E'


Quotation_generate(name, ic1 ,ic2 , ic3 ,tel ,email ,address ,postcode,no_plate,model_name)


# In[ ]:





# %%
