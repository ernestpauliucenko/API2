import requests

def getres(r):
    if r.status_code < 400:
        print(r.text)
    else:
        print(r.status_code)

h = {'API-AUTHENTICATION':'6c39370b27d0414ea095b47005b09309:4a1fb827c4954c8bb2b56d74cb085f8dfe4ea12a6cf24297824c68f3d0d843bc', 'user-agent':'ernest/test'}

print("Fetching product categories...")
r = requests.get('https://api-sandbox.revelup.com/weborders/product_categories/?establishment=2', headers = h)
getres(r)
