####################################################################################################

import os
import re
import sys
import time
from csv import writer
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

####################################################################################################

exec(open("src/page.py").read())
exec(open("src/publication.py").read())

####################################################################################################

# ignore warnings
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

# declarations
projDir = '/Users/drivas/Factorem/PUBMEDrecord'
# outDir = projDir + '/' + 'data/wasabiScrappedSource/raw'
# wasabi = 'https://dnazoo.s3.wasabisys.com/'
# dnaAddress = wasabi + 'index.html'

# change directory
os.chdir(projDir)

# arguments
httpSource = "https://pubmed.ncbi.nlm.nih.gov/?term=mauceli+e%5Bauthor%5D"
authorQueried = "Mauceli"

# httpSource = sys.argv[1]
# authorQueried = sys.argv[2]

# launch browser
browser = webdriver.Firefox()

# directing to ncbi
browser.get(httpSource)
browser.maximize_window()

# wait for page to load
time.sleep(3)

# prepare output file
outputFile = authorQueried.replace(" ", "_")
with open('data/' + outputFile + '.csv', 'w') as csv_file:
  csv_writer = writer(csv_file)
  headers = ['Title', 'Journal', 'Position', 'Authors']
  csv_writer.writerow(headers)

  # get from source
  source = requests.get(httpSource)

  # load into bs4 from source
  soup = BeautifulSoup(source.text, 'html.parser')
  publication_collector()

  # page loop
  try:
    pgs = int(soup.find('h3', class_="page").input['last'])
  except AttributeError as e:
    pgs = 1
  else:
    for ix in range(1, pgs):

      # turn the page
      page_turner()

      # load into bs4 from selenium
      soup = BeautifulSoup(browser.page_source, 'html.parser')
      publication_collector()
  finally:
    print("Number of pages:", pgs)

browser.quit()
