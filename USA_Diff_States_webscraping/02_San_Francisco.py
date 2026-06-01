#import libraries
import pandas as pd
from bs4 import BeautifulSoup
import requests

result_update = []
result_link = []


#baseurl
baseurl = 'https://www.homestay.com/'
for x in range(1,100):
    #store website in variable
    website = (f"https://www.homestay.com/homestays/search?utf8=%E2%9C%93&search_type=search_box&latitude=&longitude=&country_code=&ne_lat=&ne_lng=&sw_lat=&sw_lng=&radius=&type=&order=&location_id=172&google_place_id=&price_filter_nights=&location=San+Francisco%2C+California%2C+United+States&check_in=&check_out=&guests=1&page={x}")

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36"
    }
    #Get requests
    r = requests.get(website,headers=headers)
    #Status Code
    r.status_code

    soup = BeautifulSoup(r.content,'html.parser')

    result_container = soup.find_all('li',class_ = 'fallback-bg homestay-card')

    #Concatenate 2 url parts to get absolute Url
    for item in result_container:
        for link in item.find_all('a',href = True):
            result_link.append(baseurl + link['href'])
result_link = list(dict.fromkeys(result_link))
print(len(result_link))
#Get Data from the first link

# testlink = 'https://www.homestay.com/united-states/san-diego/161798-homestay-in-bay-ho-southwest-clairemont-mission-bay-san-diego'
for link in result_link:
    r = requests.get(link,headers=headers)
    soup = BeautifulSoup(r.content,'html.parser')
    #visitor name
    visitor_name = soup.find('h2').text
    #visiting criteria
    criteria = soup.find('div',class_ = "col-xs-6").text
    #About homestay
    about_homestay = soup.find('div',class_ = 'connect-tags pull-right-md spacer-half-sm')
    about_homestay = about_homestay.text.strip() if about_homestay else "NaN"
    #Availability
    available_for = soup.find('ul','list-unstyled tick-list list-inline').get_text(separator=" ")
    #House facilities
    house_facilities = soup.find('ul',class_ = 'list-unstyled tick-list').get_text(separator=" ")
    housing_data = {
        "visitor":visitor_name,
        "Criteria":criteria,
        "Homestay":about_homestay,
        "Available_for":available_for,
        "House_facilities":house_facilities,
        "absolute_link": link
    }
    result_update.append(housing_data)

df = pd.DataFrame(result_update)
df.to_csv("San_Francisco.csv")

