import sys
import re
import requests
from bs4 import BeautifulSoup as soup
import pandas as pd

def ItemResults(item):
    '''
    Function for scrapping list of items available for the desired one.
    The function scrapping:
        - Item name
        - Item link
        - Item price per piece
        - Minimum order quantity
    '''
    #Connect to the web-site and scrapping top items details
    try :
        url = requests.get(item['link'])
    except:
        print('Error in reading page!')
        quit()
    #get all contents
    page = soup(url.content, 'html.parser')
    # Find result items div
    containers = page.findAll('div',{'class':'item-info'})
    # intiate items dataframe
    items = pd.DataFrame(columns=['name','item','link','price','min-order'])
    # help counter for getting links
    counter = 0
    # get all details for every item result
    for con in containers:
        # get all items names and links
        link = con.find('a')
        # get items prices
        price = page.find('div',{'class':'price'})
        # get items minimum order quantity
        min_order = page.find('div',{'class':'min-order'})
        # Add item details to dataframe
        temp1 = re.sub('\s+',' ',link.text.strip())
        temp2 = temp1.replace('  ',' ')
        # remove extra spaces
        while not temp1 == temp2:
            temp1 = temp1.replace('  ',' ').strip()
            temp2 = temp1.replace('  ',' ').strip()
        # add data to items DataFrame
        items.loc[counter] = [item['item'],
                            temp1.strip(),
                            'https:{0}'.format(link['href']),
                            re.sub('\s+',' ',price.text.strip()),
                            re.sub('\s+',' ',min_order.text.strip())]
        # counter for the next link
        counter += 1
        # check if scraped items reach the limit
        if counter >= item['number']:
            break
    return items

def main(ItemName):
    '''
    This main function to test the script alone
    '''
    # create link for the given item name
    item = {'item':ItemName,
            'link':'https://www.alibaba.com/trade/search?fsb=y&IndexArea=product_en&CatId=&SearchText={0}'.format(ItemName.replace(' ','+')),
            'number':10}
    print(item)
    # get all search results for the given item
    Results = ItemResults(item)
    print(Results)

if __name__ == '__main__':
    # get the item name as string in the command line
    # after calling the script
    main(sys.argv[1])
