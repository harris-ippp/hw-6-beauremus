#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup as bs

resp = requests.get(
    'http://historical.elections.virginia.gov/elections/search/year_from:1924/year_to:2016/office_id:1/stage:General')

soup = bs(resp.content, 'html.parser')
rows = soup.find_all('tr', class_='election_item')

with open('ELECTION_ID', 'w') as file:
  for row in rows:
    year = row.find('td', class_='year').text
    election_id = row['id'].split('-')[2]
    print(year, election_id)
    file.write(year + ' ' + election_id + '\n')
