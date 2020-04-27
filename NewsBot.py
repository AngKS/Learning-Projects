from bs4 import BeautifulSoup
import requests
import json
import pyttsx3
import webbrowser

def buildUrl():
	return "http://newsapi.org/v2/top-headlines?country=sg&apiKey=3233fb544384439ea8c1eef1274ba0a0"


engine = pyttsx3.init()


def scrape():
	r = requests.get(buildUrl())
	articles = r.json()['articles']

	
	for article in articles:
		engine.say(f"Here is the news article from {article['source']['name']}.")

		headline = article['title']
		pos = headline.find(" -")
		url = article['url']
		engine.say(headline[:pos])
		print(headline[:pos])
		print(url)
		engine.say(f"by: {article['source']['name']}")
		print(f"by: {article['source']['name']}")
		
		engine.say("Would you like to find out more about the article?")
		engine.runAndWait()
		choice = input("Yes or No?\n> ")
		if choice == "yes":
			webbrowser.open(url, new=2)
		else:
			continue
        
scrape()
