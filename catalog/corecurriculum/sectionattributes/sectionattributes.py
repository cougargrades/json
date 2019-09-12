#!/usr/bin/env python3

import argparse
import requests
from halo import Halo

parser = argparse.ArgumentParser(description='Scrapes UH CollegeScheduler API to enumerate all courses by section attributes.')
parser.add_argument('apiUrl', metavar='API_URL', type=str,
                    help='The API URL used. No trailing slash. Ex: http://uh.collegescheduler.com')

args = parser.parse_args()
HOST = args.apiUrl

spinner = Halo(text=f'Testing API access', spinner='dots')
spinner.start()

try:
    res = requests.get(f'{HOST}/api/terms')
    if res.status_code == 200 and 'studentCareers' in res.json()[0].keys():
        spinner.succeed(text=f'API access confirmed')
    else:
        spinner.fail(text=f'API access failed')
except Exception:
    spinner.fail(text=f'API access failed with an Exception')
