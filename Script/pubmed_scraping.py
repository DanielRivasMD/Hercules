import requests
import re
import sys
from bs4 import BeautifulSoup
from csv import writer

# arguments
httpSource = sys.argv[1]
authorQueried = sys.argv[2]

# get from source
source = requests.get(httpSource)

# load into bs4
soup = BeautifulSoup(source.text, 'html.parser')

# prepare output file
outputFile = authorQueried.replace(" ", "_")
# with open('Data/' + outputFile + '.csv', 'w') as csv_file:
with open(outputFile + '.csv', 'w') as csv_file:
  csv_writer = writer(csv_file)
  headers = ['Title', 'Journal', 'Position', 'Authors']
  csv_writer.writerow(headers)

  for article in soup.find_all('div', class_="rslt"):
    # title
    title = article.find('p', class_="title").text
    # journal
    journal = article.find('span', class_="jrnl").text
    # authors
    authorElement = article.find('p', class_="desc")
    authors = authorElement.text
    indAuthors = authorElement.text.split(", ")
    if re.match(authorQueried, indAuthors[0]):
      authorPosition = "First"
    elif re.match(authorQueried, indAuthors[-1]):
      authorPosition = "Corresponding"
    else:
      authorPosition = "Middle"
    # write
    csv_writer.writerow([title, journal, authorPosition, authors])
