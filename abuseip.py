#!/usr/bin/env python
# -*- coding: utf-8 -*-
__version__ = '0.1'
__author__ = 'Ajil Raju <ajil.r@poornam.com>'

import ast
import argparse
import json
import re
import requests

# Defining the api-endpoint
url = 'https://api.abuseipdb.com/api/v2/check'

headers = {
    'Accept': 'application/json',
    'Key': '<YOUR_API_KEY>'
}

def spider(ipAddress):

    querystring = {
        'ipAddress': ipAddress,
        'maxAgeInDays': '90'
    }
    response = requests.request(method='GET', url=url, headers=headers, params=querystring)

    # Formatted output
    decodedResponse = json.loads(response.text)
    json_data =  json.dumps(decodedResponse)

    json_data = re.sub('true', 'True',json_data)
    json_data = re.sub('false', 'False', json_data)

    parse_data = ast.literal_eval(json_data)
	
    banner = "Abuse Report of {}".format(ipAddress)
    print banner.center(50,"=")
    for key in sorted(parse_data['data'].keys()):
        print "{disptxt}: {value}".format(disptxt=key.capitalize(), value=parse_data['data'][key])

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--ipAddress", 
                        type=str, required=True, help="Check the IP Abuse")
    args = parser.parse_args()
    
    if args.ipAddress:
        spider(args.ipAddress)

if __name__ == '__main__':
    main()

