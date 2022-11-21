import json
import os

import requests

output = './src/json/ranges.json'


guide = requests.get('https://fonts.googleapis.com/css2?family=Roboto&display=swap',
                     headers={'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:107.0) Gecko/20100101 Firefox/107.0'})

block_height = 9
lines = guide.text.strip().split('\n')
ranges = {}
for i in range(len(lines)//9):
    offset = i * block_height
    variation = lines[offset: offset+block_height]
    name = variation[0][2:-3]
    codes = variation[7].replace('unicode-range:', '').replace(';', '').split(',')
    codes = [code.strip() for code in codes]
    ranges[name] = codes

output = os.path.abspath(output)
os.makedirs(os.path.dirname(output), exist_ok=True)
with open('./src/json/ranges.json', 'w') as f:
    json.dump(ranges, f)
