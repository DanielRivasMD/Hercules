####################################################################################################

# load config
from src.config.config import dataDir
from src.utils.pageTurner import page_turner
from src.utils.publicationCollector import publication_collector

####################################################################################################

# load dependencies
import os
import re
import sys
from csv import writer
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

####################################################################################################

# # change directory
# os.chdir("/Users/Daniel/Factorem/PUBMEDrecord/")

# # arguments
# httpSource = sys.argv[1]
# authorQueried = sys.argv[2]

# arguments
httpSource = "https://pubmed.ncbi.nlm.nih.gov/"
authorQueried = "Rivas-Carrillo SD"

# launch browser
browser = webdriver.Chrome()

# directing to ncbi
browser.get(httpSource)

####################################################################################################

# prepare output file
outputFile = authorQueried.replace(" ", "_")
with open(dataDir + outputFile + '.csv', 'w') as csv_file:
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

####################################################################################################
