"""Connect to Oasis API and pull data"""

from bs4 import BeautifulSoup
import requests
import lxml
import zipfile
import io
import glob
import os

url = "http://oasis.caiso.com/oasisapi/SingleZip"
params = {'queryname': ' PRC_LMP', 'startdatetime': ' 20130919T07: 00 - 0000',
          'enddatetime': '20130920T07: 00 - 0000', 'market_run_id': ' DAM', 'version': 1,
          'grp_type': 'ALL_APNODES'}
source = requests.get(url, params)
content = source.content
z = zipfile.ZipFile(io.BytesIO(source.content))
z.extractall()
f = glob.glob('*.xml')
print(f[0])
print(str(f[0]))

with open(str(f[0])) as test:
    soup = BeautifulSoup(test, 'lxml')
print(soup.prettify())
20130919_20130920_PRC_LMP_DAM_20171220_21_19_29_v1.xml
