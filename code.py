#Hacktoberfest2021
#start here!

#!/usr/bin/env python
# coding: utf-8

# In[1]:

import json

cricket = []

with open('text.txt', 'r') as file:
  print(cricket)
  
  for line in file:
      x = line.strip()
      url = 'http://www.espncricinfo.com/' + x.split(',')[0] + '/content/player/country.html?country=' + x.split(',')[1]
      print(url)
      
      html = requests.get(url)
      soup = BeautifulSoup(html.content, 'html.parser')
      
      rawPlayers = soup.find_all('td', class_="divider")
      playerSet = set([])

with open('text.json', 'w', encoding='utf-8') as file:
    json.dump(team, file, ensure_ascii=False, indent=2)
