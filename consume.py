import requests
import time

response = requests.get("http://127.0.0.1:8000/drinks/")

data_feeds = response.json()
print(data_feeds)

"""for data in data_feeds:
    while True:
        name_for_product = input('Dear customer, please enter name of the drink desired: ')
        
        if name_for_product == '':
            break
        if name_for_product in data:
            print('Please Hold while searching through!')
            time.sleep(5)
            print(name_for_product + ' is the description for ' + name_for_product)
        else:
            print('Please Hold while searching through!')
            time.sleep(5)
            print(name_for_product + 'not found')

        break"""