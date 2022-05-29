from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
# from django.contrib import messages
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
# from rest_framework import serializers
from selenium.webdriver import ActionChains
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import json
from collections import Counter


driver = webdriver.Chrome(executable_path='D:\\Rahulbhai\\chromedriver_win32\\\\chromedriver.exe')


df = pd.read_csv('mp_full.csv')

profile_url = df['Profile_url']

print(len(profile_url))

termList = []
for each in profile_url:
    x=each.split('=')
    # print(x)
    if x[2] == '11':
    	termList.append(each)
    
# print(termList)

# print(Counter(termList).keys())
# print(Counter(termList).values())
res = []
# firstLi = termList[0:12]
# print(firstLi)
for each in termList:
	driver.get(each)
	soupd = BeautifulSoup(driver.page_source,"html.parser")

	data12 = soupd.find_all('pre')
	# print(len(data12))
	# print(data12[1])
	try:
		data12 = soupd.find_all('pre')

	except AttributeError:
		data12 = ""

	print(each)
	if len(data12) > 1:
		sss = data12[1]
	# elif len(data12) == 1:
	# 	sss = data12[0]
	


		allb = sss.find_all("b")
		data = []
		results = dict()
		for tag in allb:
			try:
				if tag.next_sibling.string == None:
				    data.append(" ")
				else:
				    data.append(tag.next_sibling.string)
			except:
				data.append(" ")
		# print(data[0])
		try:
			fn = data[0].text.strip()
		except:
			fn = 'NA'

		try:
			dob = data[1].text.strip()
		except:
			dob = 'NA'

		try:
			pbb = data[2].text.strip()
		except:
			pbb = 'NA'

		try:
			ed = data[6].text.strip()
		except:
			ed = 'NA'

		try:
			pr = data[7].text.strip()
		except:
			pr = 'NA'

		try:
			pa = data[8].text.strip()
		except:
			pa = 'NA'

		try:
			pe = data[9].text.strip()
		except:
			pe = 'NA'
		results['Father_Name'] =fn
		# results['Mother_Name'] = mother_name
		results['DOB'] = dob
		results['Place_Of_Birth'] = pbb
		results['Education'] = ed
		results['Profession'] = pr
		results['Permanent_Address'] = pa
		results['Present_Address'] = pe
		res.append(results)


df = pd.DataFrame(res)

# Save the output.
df.to_csv('mp11term.csv')