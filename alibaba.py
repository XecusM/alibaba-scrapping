import time
import pandas as pd
import scrapping

def Items(items):
    # intiate items dataframe
    # Results = pd.DataFrame(columns=['name','item','link','price','min-order'])
    Results = pd.DataFrame()
    for counter in range(len(items['Items'])):
        # print(items[counter])
        GetItem = {'item':items['Items'][counter],
                'link':'https://www.alibaba.com/trade/search?fsb=y&IndexArea=product_en&CatId=&SearchText={0}'.format(items['Items'][counter].replace(' ','+')),
                'number':items['Search'][counter]}
        # pause for 1 second to avoid web blocking
        time.sleep(1)
        # scrapping results on a temp DataFrame
        temp = scrapping.ItemResults(GetItem)
        # append the results to Results DataFrame
        Results = pd.concat([Results,temp],ignore_index=True)

        print('Item {0} has been successfully scrapped.'.format(items['Items'][counter]))
    return Results

def main():
    check = True
    while check:
        file = input('Please, enter file name .csv to scrap its list: ')
        try:
            items = pd.read_csv(file)
            check = False
        except:
            print("File not FOUND!\nTry AGAIN!\n'")
    # print items need to be scrapped
    print(items)
    # get the scapping data as DataFrame
    results = Items(items)
    # export data to excel file
    writer = pd.ExcelWriter('results.xlsx', engine='xlsxwriter')
    results.to_excel(writer, index=False, header=True)
    writer.save()

if __name__ == '__main__':
    main()
