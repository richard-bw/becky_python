#!/usr/bin/env python3

import csv

# task 1 read the data from the spreadsheetimport csv
def get_spreadsheet_data(spreadsheet_file):
    spreadsheet_data = []
    with open(spreadsheet_file, 'r') as csv_file:
        spreadsheet = csv.DictReader(csv_file)
        for row in spreadsheet:
            spreadsheet_data.append(dict(row))
            print(dict(row))
    return spreadsheet_data


#task 2 sales figures each month only
def get_sales_figures(spreadsheet_data):
    sales_figures = []
    for row in spreadsheet_data:
        sales_figures.append(row['sales'])
    print (sales_figures)
    return sales_figures


#task 3 total all sales
def main():
    total = 0
    for sales_figure in get_sales_figures(get_spreadsheet_data('sales.csv')):
        total += int(sales_figure)
    print(f'total sales:{total}')    

if __name__ == "__main__": main()
