import requests
import json

def getres(r):
    if r.status_code < 400:
        return r.text
    else:
        return r.status_code

h = {'API-AUTHENTICATION':'6c39370b27d0414ea095b47005b09309:4a1fb827c4954c8bb2b56d74cb085f8dfe4ea12a6cf24297824c68f3d0d843bc', 'user-agent':'ernest/test'}

b = {
    'establishment':2,
    'items':[
        {
        'modifieritems':[],
        'special_request':'',
        'price':16,
        'product':274,
        'product_name_override':'Red Sparkling',
        'quantity':1
        }
    ],
    'orderInfo':{
        'dining_option':0
    }
}

print("Calculating cart...")
r = requests.post('https://api-playground.revelup.com/specialresources/cart/calculate/', data = json.dumps(b), headers = h)
res = getres(r)
if r.status_code < 400:
    print(res[26:(len(res.split("items")[0])-3)])    #"final_total" always starts at char 27, but the end is calculated by the amount of characters until the first mention of "items" minus 3. This guarantees a perfect slice every time without using regex.
else:
    print(r.status_code)