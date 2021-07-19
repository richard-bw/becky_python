#!/usr/bin/env python3
#  desc: 
#   Months with the highest and lowest sales
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
from task1to3 import get_spreadsheet_data
import csv

OUTPUT_FILE='high_low-sales.csv'

def main():
    data_to_file = open(OUTPUT_FILE, 'w')

    csv_writer = csv.writer(data_to_file)
    csv_writer.writerow(["","year","month", "sales"])

    ss_data = get_spreadsheet_data('sales.csv')
    high = max(ss_data, key=lambda x:x['sales'])
    low  = min(ss_data, key=lambda x:x['sales'])
    csv_writer.writerow( ["HIGH", high['year'], high['month'], high['sales'] ]  )
    csv_writer.writerow( ["LOW", low['year'], low['month'], low['sales'] ]  )
    
    data_to_file.close()

    print(f"Wrote results to [{OUTPUT_FILE}]")

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
if __name__ == "__main__": main()
#//EOF
