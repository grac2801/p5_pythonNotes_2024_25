'''
Created on Oct 16, 2024

@author: ogracias
'''

import requests


data = requests.get("https://opentdb.com/api.php?amount=10")
data = data.json()
print(data)