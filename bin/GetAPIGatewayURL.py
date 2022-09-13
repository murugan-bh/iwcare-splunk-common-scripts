import sys
import os
import csv
from splunk.clilib.bundle_paths import make_splunkhome_path

def getURLs():
    with open(make_splunkhome_path(['etc', 'apps', 'iwcare-splunk-common-scripts',"lookups","api_gateway_urls_list.csv"]), newline='') as csvfile:
        csvData = csv.DictReader(csvfile)
        csvDataFormatted = {}
        for row in csvData:
            csvDataFormatted.update({row["Key"]:row["Value"]})
    return csvDataFormatted
getURLs()