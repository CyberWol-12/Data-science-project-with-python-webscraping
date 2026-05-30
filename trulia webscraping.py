#import libraries
import pandas as pd
from bs4 import BeautifulSoup
import requests

#store website in variable
website = 'https://www.rentcafe.com/apartments-for-rent/san-diego-ca/'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36"
}
#Get requests
response = requests.get(website,headers=headers)
#Status Code
print(response.status_code)
