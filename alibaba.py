import time
import pandas as pd
import scrapping

def Items(items):
    # intiate items dataframe
    Results = list()
    for item in items:
        print(item)
        GetItem = {'item':item['Items'],
                'link':'https://www.alibaba.com/trade/search?fsb=y&IndexArea=product_en&CatId=&SearchText={0}'.format(item['Items'].replace(' ','+')),
                'number':item['Search']}
        # get all search results for the given item
        Results.append(scrapping.ItemResults(GetItem))

def main():
    check = True
    while check:
        file = input('Please, enter file name .csv to scrap its list: ')
        try:
            items = pd.read_csv(file)
            check = False
        except:
            print("File not FOUND!\nTry AGAIN!\n'")
    results = Items(items)
    print(results)


if __name__ == '__main__':
    main()
