#import libraries
import pandas as pd
from bs4 import BeautifulSoup
import requests

result_update = []
result_link = []


#baseurl
baseurl = 'https://www.homestay.com/'

#store website in variable
website = 'https://www.homestay.com/homestays/search?utf8=%E2%9C%93&search_type=search_box&latitude=&longitude=&country_code=&ne_lat=&ne_lng=&sw_lat=&sw_lng=&radius=&type=&order=&location_id=117&google_place_id=&price_filter_nights=&location=San+Diego%2C+California%2C+United+States&check_in=&check_out=&guests=1'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36"
}
#Get requests
r = requests.get(website,headers=headers)
#Status Code
print(r.status_code)

soup = BeautifulSoup(r.content,'html.parser')




        




    




