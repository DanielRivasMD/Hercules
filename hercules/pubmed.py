####################################################################################################

# load dependencies
import os
import re
import sys
from csv import writer
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

####################################################################################################

class Article:
  def __init__(self):
    self.title = ''
    self.journal = ''
    self.authors = {}
    self.affiliation = {}
    self.pmid = ''
    self.abstract = ''

  def __str__(self):
    return f'Article:\nTitle: {self.title}\nJournal: {self.journal}\nPMID: {self.pmid}\nAuthors: {self.authors}\nAffiliation: {self.affiliation}\n\nAbstract: {self.abstract}'

def pubmed(author, outdir):

  # arguments
  httpSource = 'https://pubmed.ncbi.nlm.nih.gov/?term=' + author.replace(" ", "+") + '%5Bauthor%5D&sort=date&format=abstract&size=200'

  # launch browser
  browser = webdriver.Chrome()
  browser.maximize_window()

  # directing to ncbi
  browser.get(httpSource)

  # get article number
  no = browser.find_element(By.CLASS_NAME, value='results-amount').find_element(By.CLASS_NAME, value='value').text

  # preallocate array
  articles = []

  # iterate on articles
  for artix in range(int(no)):

    # instantiate article
    article = Article()

    # adjust index
    artix += 1
    artix = str(artix)

    # expand affiliations
    browser.find_element(By.ID, value='search-result-1-' + artix + '-toggle-authors').click()
    maxaff = 0

    # select header information
    artelem = browser.find_element(By.ID, value='search-result-1-' + artix + '-full-view-heading')

    # assign journal
    article.journal = artelem.find_element(By.ID, value='search-result-1-' + artix + '-full-view-journal-trigger').text

    # assign title
    article.title = artelem.find_element(By.CLASS_NAME, value='heading-title').text

    # assign pmid
    article.pmid = artelem.find_element(By.CLASS_NAME, value='current-id').text

    # iterate on authors
    for aut in artelem.find_elements(By.CLASS_NAME, value='authors-list-item'):
      # collect author info
      name = aut.find_element(By.CLASS_NAME, value='full-name').text
      affiliations = []

      # collect affiliation info
      try:
        affs = aut.find_elements(By.CLASS_NAME, value='affiliation-link')
      except:
        affs = []
        print(name + ' has no affiliation')

      if (len(affs) > 0):
        for ax in range(len(affs)):
          affix = int(affs[ax].text)
          affiliations.append(affix)
          if (maxaff < affix):
            maxaff = affix

      # collect author affiliations
      article.authors[name] = affiliations

    # iterate on affiliations
    for ax in range(maxaff):
      ax += 1
      # split into index & text
      aff = browser.find_element(By.ID, value='search-result-1-' + artix + '-full-view-affiliation-' + str(ax)).text.split('\n')
      if (len(aff) > 1):
        article.affiliation[int(aff[0])] = aff[1]

    # select body information
    # assign abstract
    article.abstract = browser.find_element(By.ID, value='search-result-1-' + artix + '-eng-abstract').text

    # push article
    articles.append(article)

  ####################################################################################################

  # prepare output file
  outputFile = author.replace(" ", "_")
  with open(outdir + '/' + outputFile + '.csv', 'w') as csv_file:
    csv_writer = writer(csv_file)

    # header
    headers = ['Title', 'Journal', 'PMID', 'Authors']
    csv_writer.writerow(headers)

    # iterate on results
    for article in articles:
      row = [article.title, article.journal, article.pmid, ""]
      csv_writer.writerow(row)

  ####################################################################################################

  # close scrapper
  browser.quit()

  ####################################################################################################
