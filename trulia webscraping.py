# import libraries
import pandas as pd
from bs4 import BeautifulSoup
import requests


website = 'https://www.trulia.com/CA/San_Diego/'

response = requests.get(website)
