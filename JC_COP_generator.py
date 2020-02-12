import pandas as pd
import requests
from bs4 import BeautifulSoup
from datetime import date

def buildUrl(year):
	return "https://www.learnerslodge.com.sg/blog/jc-cut-off-points-"+year+"/"

def scrapeJC():
	info = {}
	years = ['2017', '2018', '2019', '2020']
	for year in years:
		r = requests.get(buildUrl(year))
		soup = BeautifulSoup(r.text, 'lxml')
		table = soup.find('div', class_='table-1')
		for tr in table.find_all('tr')[2: ]:
			columns = tr.find_all('td')

			#print(year)
			info.update({'Year' : year, 'School': columns[0].text, 'Arts' : columns[1].text, 'Science' : columns[2].text})
			# print('School: %s\nArts: %s\nScience: %s\n' % (columns[0].text, columns[1].text, columns[2].text))
			#print(info)
			print(info)
		




scrapeJC()
input(' ')
