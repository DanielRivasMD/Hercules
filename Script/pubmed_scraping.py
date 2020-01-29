import os
import re
import sys
import csv
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# change directory
os.chdir("/Users/Daniel/Factorem/PUBMEDrecord/")

# arguments
httpSource = sys.argv[1]
authorQueried = sys.argv[2]

# launch browser
browser = webdriver.Chrome()

# directing to ncbi
browser.get(httpSource)


def publication_collector():

  # publication loop
  for article in soup.find_all('div', class_="rslt"):
    # title
    title = article.find('p', class_="title").text
    # journal
    journal = article.find('span', class_="jrnl").text
    # authors
    author_element = article.find('p', class_="desc")
    authors = author_element.text
    ind_authors = author_element.text.split(", ")
    if re.match(authorQueried, ind_authors[0]):
      author_position = "First"
    elif re.match(authorQueried, ind_authors[-1]):
      author_position = "Corresponding"
    else:
      author_position = "Middle"
    # write
    csv_writer.writerow([title, journal, author_position, authors])


def page_turner():
  # iterator control
  pagination = browser.find_element_by_class_name('pagination')
  input_value = "input[value='" + str(ix) + "']"
  turn_page = pagination.find_element_by_css_selector(input_value)
  turn_page.clear()
  turn_page.send_keys((ix + 1))
  turn_page.send_keys(Keys.RETURN)


# prepare output file
outputFile = authorQueried.replace(" ", "_")
# with open('Data/' + outputFile + '.csv', 'w') as csv_file:
with open(outputFile + '.csv', 'w') as csv_file:
  csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_NONE)
  headers = ['Title', 'Journal', 'Position', 'Authors']
  csv_writer.writerow(headers)

  # get from source
  source = requests.get(httpSource)

  # load into bs4 from source
  soup = BeautifulSoup(source.text, 'html.parser')
  publication_collector()

  # page loop
  pgs = int(soup.find('h3', class_="page").input['last'])
  for ix in range(1, pgs):

    # turn the page
    page_turner()

    # load into bs4 from selenium
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    publication_collector()

browser.quit()
