#!/usr/bin/env python3
#  desc: 
#   Calculate the following:
#      Monthly changes as a percentage
#      The average
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
from task1to3 import get_spreadsheet_data

def main():
    ss_data = get_spreadsheet_data('sales.csv')
    prev_row = None
    for row in ss_data:
        if prev_row is not None:
            print(f"Change {prev_row['year']}/{prev_row['month']} to {row['year']}/{row['month']}") 
            print(f"Sales       : {round((int(row['sales']) / int(prev_row['sales']))*100, 2)}%" )
            print(f"Expenditure : {round((int(row['expenditure']) / int(prev_row['expenditure']))*100, 2)}%" )
            print()

        prev_row = row

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
if __name__ == "__main__": main()
#//EOF
