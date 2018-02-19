from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
from twilio.rest import Client
import time

driver = webdriver.Firefox()
#driver = webdriver.Chrome()
driver.get("https://www.weather.gov/")

#Enter the zip code
city_search = driver.find_element_by_name ("inputstring")
city_search.click()
city_search.send_keys("80908")

#Wait for all elements to load
time.sleep(3) 

#Click the Go button
city_search_go = driver.find_element_by_id ("btnSearch")
city_search_go.click()

#Get the current URL and request the html w/Requests
currentURL = driver.current_url
page = requests.get(currentURL)

#Create BeautifulSoup object of the page
soup = BeautifulSoup(page.text, 'html.parser')

#Locate area of the page with the weekly forecast
weekly_forecast = soup.find(id="seven-day-forecast")
weekly_forecast_items = weekly_forecast.findAll(class_="tombstone-container")

#Locate the first four forecast items and determine if a keyword is present
#Four forecast items should cover two days (ex. today, tonight, tomorrow, tomorrow night)

x=0
while x < 1:
    daily_forecast = weekly_forecast_items[x]
    img = daily_forecast.find("img")
    desc = img['title']          
    if 'Snow' in desc:
        print(desc)

        account_sid = "YOUR ID"
        auth_token = "YOUR AUTH TOKEN"
        client = Client(account_sid, auth_token)
        message = client.messages.create(
        "+15559998877",
        body=desc,
        from_="+15552223333")
        x = x+1
        
    elif 'snow' in desc:
        print(desc)

        account_sid = "YOUR ID"
        auth_token = "YOUR AUTH TOKEN"
        client = Client(account_sid, auth_token)
        message = client.messages.create(
        "+15559998877",
        body=desc,
        from_="+115552223333")
        x = x+1
    else:
        print('Snow not in forecast')
        x = x+1

driver.quit()
