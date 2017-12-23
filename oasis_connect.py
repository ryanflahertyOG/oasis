"""Connect to Oasis API and pull data"""

import requests
import zipfile
import io
import glob
import os
import pandas as pd

url = "http://oasis.caiso.com/oasisapi/SingleZip"
params = {'queryname': 'PRC_INTVL_LMP', 'version': 3, 'resultformat': 6,
          'startdatetime': '20171221T08:00-0000',
          'enddatetime': '20171222T08:00-0000', 'market_run_id': 'RTM',
          'node': 'ELAP_PGE-APND'}
source = requests.get(url, params)
content = source.content
z = zipfile.ZipFile(io.BytesIO(source.content))
z.extractall()
f = glob.glob('*.csv')

print(f[0])

raw = pd.read_csv(f[0])
