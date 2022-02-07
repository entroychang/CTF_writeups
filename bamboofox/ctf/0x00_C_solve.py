# decimal = '''72, 75, 71, 72, 69, 69, 76, 69, 82, 113, 105, 58, 110, 57, 85, 120, 57, 124, 59, 57, 125, 59, 100, 109, 85, 59, 100, 85, 105, 119'''.split(', ')

# for i in decimal:
#     char = int(i) ^ 10
#     print(chr(char), end='')



# Nessus output file csv parser, remove useless information: none risk, Nessus UDP
# Author: Walter Chen, Sean Li, Jack Liu
# Date: 2019/08/09
# Version: 1.4
# Environment: Python 2.7.9 - 16

# version note:
# v1.1 add Synopsis, Description
# v1.2 change to use path to include all csv input file
# v1.3 add file name column by Sean
# v1.4 add filter vulnerability by Jack

import csv
import sys
import os
import glob


def Remove_Information(row):
    # Plugin ID[0], CVE[1], CVSS[2], Risk[3], Host[4], Protocol[5], Port[6], Name[7], Synopsis[8], Description[9], Solution[10], See Also[11], Plugin Output[12]
    return 0


def main():
    try:
        header = 0
        csvFileList = glob.glob(sys.argv[2] + '/*.csv')
        # print(csvFileList)
        wfile = open(sys.argv[1], 'wb+')
        # buid the result file
        for csvInput in csvFileList:
            filename = csvInput.lstrip(
                sys.argv[2] + '\\').rstrip("vsc.")  # v1.3
            _file = open(csvInput, 'rt')
            # open input file
            print "Parsing %s" % csvInput
            reader = csv.reader(_file)
            fieldnames = ['VulID', 'Host', 'Type', 'Name', 'Protocol', 'Port',
                            'Risk', 'CVE', 'Synopsis', 'Description', 'Solution', 'Date']
            writer = csv.DictWriter(wfile, fieldnames=fieldnames)
            if header == 0:  # add header at first time only
                writer.writeheader()
                header = 1
            for row in reader:
                if row[3] != 'None' and row[3] != 'Risk' and row[7] != 'Nessus UDP scanner' and row[7] != 'DNS Server Cache Snooping Remote Information Disclosure' and row[7] != 'Multiple Ethernet Driver Frame Padding Information Disclosure (Etherleak)' and row[7] != 'SSL Version 2 and 3 Protocol Detection':
                    writer.writerow({'VulID': '', 'Host': row[4], 'Type': '', 'Name': row[7], 'Protocol': row[5], 'Port': row[6],
                                        'Risk': row[3], 'CVE': row[1], 'Synopsis': row[8], 'Description': row[9], 'Solution': row[10], 'Date': filename})

        wfile.close()
        _file.close()
        print "Parsing finished. Output File is %s" % sys.argv[1]

    except:
        print "Oops, it was have error: ", sys.exc_info()
        print 'Error on line {}'.format(sys.exc_info()[-1].tb_lineno)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "[*] Usage: python %s <OutputFileName> <InputFilePath>" % sys.argv[0]

    else:
        replace_file = 'yes'
        if (os.path.exists(sys.argv[1])):
            replace_file = 'no'
            replace_file = raw_input(
                "[Warning] OutputFileName exist, replace it? (y/N)").lower()
        if replace_file == 'y' or replace_file == 'yes':
            main()
        else:
            print "OutputFileName exist and give up to replace, exit();"
