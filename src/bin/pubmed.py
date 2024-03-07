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
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

####################################################################################################

# # change directory
# os.chdir("/Users/Daniel/Factorem/PUBMEDrecord/")

# # arguments
# httpSource = sys.argv[1]
# authorQueried = sys.argv[2]

# arguments
httpSource = 'https://pubmed.ncbi.nlm.nih.gov/?term=rivas-carrillo+sd%5Bauthor%5D&sort=date&format=abstract&size=200'
authorQueried = 'Rivas-Carrillo SD'

# launch browser
browser = webdriver.Firefox()

# directing to ncbi
browser.get(httpSource)

# get article number
no = browser.find_element(By.CLASS_NAME, value='results-amount').find_element(By.CLASS_NAME, value='value').text

# iterate on articles
for artix in range(int(no)):
  # adjust index
  artix += 1
  artix = str(artix)

  # expand affiliations
  browser.find_element(By.ID, value='search-result-1-' + artix + '-toggle-authors').click()
  maxaff = 0

  # select article information
  article = browser.find_element(By.ID, value='search-result-1-' + artix + '-full-view-heading')

  article.find_element(By.CLASS_NAME, value='heading-title').text
  # 'Whole-genome comparison of endogenous retrovirus segregation across wild and domestic host species populations'

  # iterate on authors
  for author in article.find_elements(By.CLASS_NAME, value='authors-list-item'):
    # collect author info
    name = author.find_element(By.CLASS_NAME, value='full-name').text
    print(name)
    try:
      # BUG: not finding elements
      affs = author.find_elements(By.CLASS_NAME, value='affiliation-link')
      for aff in range(affs):
        affix = int(aff.text)
      if (maxaff < affix):
        maxaff = affix
      print(affix)
      print(maxaff)
    except:
      print(name + ' has no affiliation')

  # WIP: split into number & text
  aff = browser.find_element(By.ID, value='search-result-1-' + artix + '-full-view-affiliation-1').text.split('\n')
  print(aff)

####################################################################################################

# prepare output file
outputFile = authorQueried.replace(" ", "_")
with open(dataDir + '/' + outputFile + '.csv', 'w') as csv_file:
  csv_writer = writer(csv_file)
  headers = ['Title', 'Journal', 'Position', 'Authors']
  csv_writer.writerow(headers)

  # get from source
  source = requests.get(httpSource)

  # load into bs4 from source
  soup = BeautifulSoup(source.text, 'html.parser')
  .click()
  publication_collector(soup, csv_writer, authorQueried)

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
