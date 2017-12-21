"""Connect to Oasis API and pull data"""

from bs4 import BeautifulSoup
import requests
import lxml
import zipfile
import io

params = {'queryname': PRC_LMP, 'startdatetime': 20130919T07: 00 - 0000,
          'enddatetime': 20130920T07: 00 - 0000, 'market_run_id': DAM, 'version': 1,
          'grp_type': ALL_APNODES}
source = requests.get(
    '''http://oasis.caiso.com/oasisapi/SingleZip?queryname=PRC_LMP&startdatetime=20130919T07:00-0000&enddatetime=20130920T07:00-0000&version=1&market_run_id=DAM&node=LAPLMG1_7_B2''')

html = source.text
content = source.content
z = zipfile.ZipFile(io.BytesIO(source.content))
z.extractall()

with open("20130919_20130920_PRC_LMP_DAM_20171220_21_19_29_v1.xml") as test:
    soup = BeautifulSoup(test, 'lxml')
print(soup.prettify())
