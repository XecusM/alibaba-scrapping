import sys
import requests
from bs4 import BeautifulSoup as soup
import time
import pandas as pd

# https://www.alibaba.com/trade/search?fsb=y&IndexArea=product_en&CatId=&SearchText=Huawei+P30+Lite

def ItemResults(item):
    '''
    Function for scrapping list of items available for the desired one.
    '''
    #Connect to the web-site and scrapping top items details
    try :
        url = requests.get(item['link'])
    except:
        print('Error in reading page!')
        quit()

def main(ItemName):
    item = {'item':ItemName,'link':'https://www.alibaba.com/trade/search?fsb=y&IndexArea=product_en&CatId=&SearchText={0}'.format(ItemName.replace(' ','+'))}
    print(item)
    # Results = ItemResults(item)
    # print(Results)

if __name__ == '__main__':
    main(sys.argv[1])
