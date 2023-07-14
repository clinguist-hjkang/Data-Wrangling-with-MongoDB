# Your task is to read the input DATAFILE line by line, and for the first 10 lines (not including the header)
# split each line on "," and then for each line, create a dictionary
# where the key is the header title of the field, and the value is the value of that field in the row.
# The function parse_file should return a list of dictionaries,
# each data line in the file being a single list entry.
# Field names and values should not contain extra whitespace, like spaces or newline characters.
# You can use the Python string method strip() to remove the extra whitespace.
# You have to parse only the first 10 data lines in this exercise,
# so the returned list should have 10 entries!
import os

DATADIR = ""
DATAFILE = "beatles-diskography.csv"
header = "Title,Released,Label,UK Chart Position,US Chart Position,BPI Certification,RIAA Certification"


def parse_file(datafile):
    data = []
    line_dict = {}
    with open(datafile, "r") as f:
        for line in f:
            line = "".join(line.strip())
            if line != header:
                line_dict["Title"] = line.split(",")[0]
                line_dict["UK Chart Position"] = line.split(",")[3]
                line_dict["Label"] = line.split(",")[2]
                line_dict["Released"] = line.split(",")[1]
                line_dict["US Chart Position"] = line.split(",")[-3]
                line_dict["RIAA Certification"] = line.split(",")[-1]
                line_dict["BPI Certification"] = line.split(",")[-2]
                
                data.append(line_dict)
                line_dict = {}

    return data


def test():
    # a simple test of your implemetation
    datafile = os.path.join(DATADIR, DATAFILE)
    d = parse_file(datafile)
    firstline = {'Title': 'Please Please Me', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '22 March 1963', 'US Chart Position': '-', 'RIAA Certification': 'Platinum', 'BPI Certification': 'Gold'}
    tenthline = {'Title': '', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '10 July 1964', 'US Chart Position': '-', 'RIAA Certification': '', 'BPI Certification': 'Gold'}
    #print d[0]
    
    assert d[0] == firstline
    assert d[9] == tenthline
    
    print(d)

    
test()