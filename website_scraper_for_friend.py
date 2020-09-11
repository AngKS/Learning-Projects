from bs4 import BeautifulSoup
import requests
import pandas as pd
import os

def buildUrl():
	return "http://tropical.atmos.colostate.edu/Realtime/"

def scrape():
	r = requests.get(buildUrl())
	soup = BeautifulSoup(r.text, 'lxml')
	table = soup.find('table')
	# print(table)
	processResult(table)

def editStr(s):
	start_pos = s.find("(")
	s = s[: start_pos]
	return s

def processResult(result):
	# Get all the table headers
	headers = []
	for header in result.find_all('th'):
		headers.append(header.text)
	
	# Get row values
	ROWS = []
	rowInfo = []
	for rows in result.find_all('tr', class_="data"):
		for data in rows.find_all('td'):
			rowInfo.append(editStr(data.text))
		ROWS.append(rowInfo)
		rowInfo = []
	
	toDataframe(headers, ROWS)

def toDataframe(headers, values):
	dataframe = pd.DataFrame(values, columns = headers)
	saveFile(dataframe)
	


def saveFile(df):
	filename = "Northern_Hemisphere_Tropical_Cyclone_activity_2020"
	if os.path.exists(f"{filename}.xlsx") == True:
		print("Appending to SpreadSheet...")
		dataframe = pd.read_excel(f"{filename}.xlsx")
		dataframe.append(df, ignore_index = True)
		dataframe.to_excel(f"{filename}.xlsx", index = False)
	else:
		print("No SpreadSheet found! Creating one now...")
		df.to_excel(f"{filename}.xlsx", index = False)
		print(f"File saved!\nFilename: {filename}.xlsx")



scrape()
