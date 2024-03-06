####################################################################################################

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

####################################################################################################
