#!/usr/bin/env python
"""
Your task is as follows:
- read the provided Excel file
- find and return the min, max and average values for the COAST region
- find and return the time value for the min and max entries
- the time values should be returned as Python tuples

Please see the test function for the expected return format

"""

import xlrd
from zipfile import ZipFile
datafile = "2013_ERCOT_Hourly_Load_Data.xls"


def open_zip(datafile):
    with ZipFile('{0}.zip'.format(datafile), 'r') as myzip:
        myzip.extractall()


def parse_file(datafile):
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)

    ### example on how you can get the data
    sheet_data = [[sheet.cell_value(r, col) for col in range(sheet.ncols)] for r in range(sheet.nrows)]
    print("Get a list of values in column 1('COAST'), from all rows (exclude header)")
    COAST_list = sheet.col_values(1, start_rowx=1, end_rowx=None)   
    # print(COAST_list)
    max_value = max(COAST_list)
    max_index = COAST_list.index(max_value)+1
    print(f"max value: {max_value}, max index: {max_index}")

    min_value = min(COAST_list)
    min_index = COAST_list.index(min_value)+1
    print(f"min value: {min_value}, min index: {min_index}")

    average = sum(COAST_list) / len(COAST_list), 2
    print(f"COAST average: {average}")

    print("\nDATES:")
    max_time = sheet.cell_value(max_index, 0)
    print("Max time in Excel format:")
    print("Convert max time to a Python datetime tuple, from the Excel float:")
    final_maxtime = xlrd.xldate_as_tuple(max_time,0)
    print(final_maxtime)

    min_time = sheet.cell_value(min_index, 0)
    print("Min time in Excel format:")
    print("Convert min time to a Python datetime tuple, from the Excel float:")
    final_mintime = xlrd.xldate_as_tuple(min_time,0)
    print(final_mintime)

    
    data = {
            'maxtime': final_maxtime,
            'maxvalue': max_value,
            'mintime': final_mintime,
            'minvalue': min_value,
            'avgcoast': average
    }
    return data


def test():
    open_zip(datafile)
    data = parse_file(datafile)
    # print(data)

    assert data['maxtime'] == (2013, 8, 13, 17, 0, 0)
    assert round(data['maxvalue'], 10) == round(18779.02551, 10)


test()