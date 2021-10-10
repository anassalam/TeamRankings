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

plt.legend(['avg no. of players'])

plt.show()
plt.savefig('myfig.jpg', dpi=300)

# In[3]:

array = []
for i in range(0, 10):
    for j in range(0, 10):
        for k in range(0, 10):
            array.append(i * j * k)

my_array = [i*j*k for i in range(0,10) for j in range(0,10) for k in range(0,10)]
print (my_array)

assert array == my_array

print (my_array)

def numerical_analysis(randList):
    mn = min(randList)
    mx = max(randList)
    av = sum(randList) / len(randList)
    return mn, mx, av

import random
num = [random.randint(0,10) for x in range(100)]
mn, mx, av = numerical_analysis(num)
assert mn <= av <= mx

print (num)

lines = list()
with open('colours.tsv', 'r') as file:
    for line in file:
        lines.append(line.strip().split('\t'))
print(lines)

colour_dic = dict()
for i in lines[:10]:
    col = i[1].split(',')
    colour_dic[i[0]] = {
        "red" : col[0], 
        "green": col[1],
        "blue" : col[2]
    }
print(colour_dic)

with open('colour_dic.json', 'w') as file:
    json.dump(colour_dic, file)

dictPoets = {}
engPoets = open("rekhta_poets_english.tsv","r")
hindiPoets = open("rekhta_poets_hindi.tsv","r",encoding="utf8")
urduPoets = open("rekhta_poets_urdu.tsv","r",encoding="utf8")

for poet in engPoets:
    poetInfo = poet.split("\t")
    name = poetInfo[0].strip()
    link = poetInfo[1].strip()
    dictPoets[link] = { "english" : name }

engPoets.close()

for poet in hindiPoets:
    poetInfo = poet.split("\t")
    name = poetInfo[0].strip()
    link = poetInfo[1].strip().split("?")[0]
    poetObj = dictPoets.get(link)
    if poetObj == None:
        dictPoets[link]={"hindi":name}
    else:
        poetObj["hindi"]=name

hindiPoets.close()

for poet in urduPoets:
    poetInfo = poet.split("\t")
    name = poetInfo[0].strip()
    link = poetInfo[1].strip().split("?")[0]
    poetObj = dictPoets.get(link)
    if poetObj == None:
        dictPoets[link]={"urdu":name}
    else:
        poetObj["urdu"]=name

urduPoets.close()
