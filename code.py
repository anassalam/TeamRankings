#Hacktoberfest2021
#start here!

#!/usr/bin/env python
# coding: utf-8

# In[1]:

import json
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# In[2]:

cricket = []

with open('CricketTeams.txt', 'r') as file:
  print(cricket)
  
  for line in file:
      x = line.strip()
      url = 'http://www.espncricinfo.com/' + x.split(',')[0] + '/content/player/country.html?country=' + x.split(',')[1]
      print(url)
      
      html = requests.get(url)
      soup = BeautifulSoup(html.content, 'html.parser')
      
      rawPlayers = soup.find_all('td', class_="divider")
      playerSet = set([])
      
      for child in rawPlayers:
            playerSet.add(child.text)
          
      listPlayers = []
      for player in playerSet:
          listPlayers.append(player)
      
      team = []
      team.append(x.split(',')[0])
      team.append(listPlayers)
          
      cricket.append(team)
        
  print(cricket)

with open('CricketTeams.json', 'w', encoding='utf-8') as file:
    json.dump(cricket, file, ensure_ascii=False, indent=2)
    
x_name_of_team = []
for i in range(0, len(cricket)):
    x_name_of_team.append(cricket[i][0])
print(x_name_of_team)

y_number_of_players = []
for i in range(0, len(cricket)):
    y_number_of_players.append(len(cricket[i][1]))
print(y_number_of_players)

#to check if number of teams on index [0] matches with their players in index [1]
print(len(x_name_of_team))
print(len(y_number_of_players))

plt.bar(x_name_of_team, y_number_of_players, width=.5)

plt.xticks(x_name_of_team, x_name_of_team, rotation='vertical')

avg = np.mean(y_number_of_players)
plt.plot(x_name_of_team, [avg] * len(y_number_of_players), color='red', lw=1, ls='--')

