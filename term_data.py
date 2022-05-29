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


# driver = webdriver.Chrome(executable_path='D:\\Rahulbhai\\chromedriver_win32\\\\chromedriver.exe')


df = pd.read_csv('mp_full.csv')

profile_url = df['Profile_url']

print(len(profile_url))

termList = []
for each in profile_url:
    x=each.split('=')
    df2=df.loc[df['Profile_url'] == each, 'Name']
	print(df2)
    # print(x)
    if x[2] == '12':
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
	if len(data12) != 0:
		name = data12[0]
		nameb = name.find_all('b')
		print(nameb[2])
		sss = data12[1]


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

		results['Name'] = df2
		results['Father_Name'] = data[0].text.strip()
		# results['Mother_Name'] = mother_name
		results['DOB'] = data[1]
		results['Place_Of_Birth'] = data[2].text.strip()
		results['Education'] = ed
		results['Profession'] = pr
		results['Permanent_Address'] = pa
		results['Present_Address'] = pe
		res.append(results)


df = pd.DataFrame(res)

# Save the output.
df.to_csv('mp12term27.csv')