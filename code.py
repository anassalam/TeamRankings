#Hacktoberfest2021
#start here!

#!/usr/bin/env python
# coding: utf-8

# In[1]:
cricket = []

with open('text.txt', 'r') as file:
  print(cricket)

with open('text.json', 'w', encoding='utf-8') as file:
    json.dump(team, file, ensure_ascii=False, indent=2)
