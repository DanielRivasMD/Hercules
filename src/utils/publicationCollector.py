####################################################################################################

# TODO: extract affiliation
def publication_collector(soup, csv_writer, authorQueried):

  # publication loop
  for article in soup.find_all('div', class_="docsum-content"):
    # title
    title = article.find('a', class_="docsum-title").text.replace('\n', '').replace('  ', '')
    # journal
    journal = article.find('span', class_="docsum-journal-citation short-journal-citation").text.replace('\n', '').replace('  ', '')
    # pmid
    pmid = article.find('span', class_='docsum-pmid').text.replace('\n', '').replace('  ', '')
    # authors
    authors = article.find('span', class_='docsum-authors full-authors').text.split(', ')
    if (authorQueried in authors[0]):
      position = "First"
    elif (authorQueried in authors[-1]):
      position = "Corresponding"
    else:
      position = "Middle"
    # write
    csv_writer.writerow([title, journal, position, authors])

####################################################################################################
