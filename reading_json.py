import json

cxxx = '''{
    "name": "Mike",
    "height": 178,
    "weight": 150,
    "title": "husband"
}
'''

cxxx = json.loads(cxxx)  # load string into dictionary
cxxx['name'] = "kevin"   # make some changes to the dictionary

cxxx_str = json.dumps(cxxx) # convert back to being string
print(cxxx_str)
