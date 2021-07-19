#!/usr/bin/env python3
#  desc: 
#   Months with the highest and lowest sales
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
from task1to3 import get_spreadsheet_data
import xlsxwriter

OUTPUT_FILE='high_low-sales.xlsx'

def main():
    workbook = xlsxwriter.Workbook(OUTPUT_FILE)
    worksheet = workbook.add_worksheet()

    worksheet.write("B1","year")
    worksheet.write("C1","month")
    worksheet.write("D1","sales")

    ss_data = get_spreadsheet_data('sales.csv')
    high = max(ss_data, key=lambda x:x['sales'])
    low  = min(ss_data, key=lambda x:x['sales'])

    worksheet.write("A2","HIGH")
    worksheet.write("B2",high['year'])
    worksheet.write("C2",high['month'])
    worksheet.write("D2",high['sales'])

    worksheet.write("A3","LOW")
    worksheet.write("B3", low['year'])
    worksheet.write("C3", low['month'])
    worksheet.write("D3", low['sales'])
    
    workbook.close()

    print(f"Wrote results to [{OUTPUT_FILE}]")

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
if __name__ == "__main__": main()
#//EOF
