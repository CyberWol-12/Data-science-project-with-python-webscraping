#import libraries
import pandas as pd
from bs4 import BeautifulSoup
import requests

result_update = []


#baseurl
baseurl = 'https://www.hostelworld.com/'

#store website in variable
website = 'https://www.hostelworld.com/pwa/s?q=San%20Diego,%20California,%20USA&country=California,%20USA&city=San%20Diego&type=city&id=129&from=2026-06-01&to=2026-06-04&guests=2&page=1'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36"
}
#Get requests
r = requests.get(website,headers=headers)
#Status Code
r.status_code

soup = BeautifulSoup(r.content,'html.parser')

#Results
result_container = soup.find_all('div',class_ = "property-card")
#we just want to target the element which have the attribute
for r in result_container:
    if r.has_attr('data-v-64e39c4e'):
        result_update.append(r)
print(len(result_update))

  


    




