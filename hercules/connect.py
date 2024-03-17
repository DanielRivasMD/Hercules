####################################################################################################

from getpass import getpass
from mysql.connector import connect

####################################################################################################

def insert_articles(articles, user='drivas', password='hercules', database='PubMed'):

  sql_insert_articles = """
  INSERT INTO Articles
  (pmid, journal, title, abstract)
  VALUES (%s, %s, %s, %s)
  """

  ####################################################################################################

  records_articles = []
  for article in articles:
    records_articles.append((article.pmid, article.journal, article.title, article.abstract))

  with connect(
    user=user,
    password=password,
    database=database
  ) as connection:
    with connection.cursor() as cursor:
      cursor.executemany(sql_insert_articles, records_articles)
      connection.commit()

####################################################################################################

def insert_authors(articles, user='drivas', password='hercules', database='PubMed'):

  sql_insert_authors = """
  INSERT INTO Authors
  (author_pmid, author, pmid)
  VALUES (%s, %s, %s)
  """

  ####################################################################################################

  for article in articles:
    records_authors = []
    for author, affiliation in article.authors.items():
      records_authors.append((author + '_' + article.pmid, author, article.pmid))

    with connect(
      user=user,
      password=password,
      database=database
    ) as connection:
      with connection.cursor() as cursor:
        cursor.executemany(sql_insert_authors, records_authors)
        connection.commit()

####################################################################################################

def insert_affiliations(articles, user='drivas', password='hercules', database='PubMed'):

  sql_insert_affiliations = """
  INSERT INTO Affiliations
  (author_affiliation, affiliation, author, pmid, author_pmid)
  VALUES (%s, %s, %s, %s, %s)
  """
  
  ####################################################################################################

  for article in articles:
    for author, affixes in article.authors.items():
      records_affiliations = []
      for affix in affixes:
        records_affiliations.append((author + '_' + article.affiliation[affix], article.affiliation[affix], author, article.pmid, author + '_' + article.pmid))

      with connect(
        user=user,
        password=password,
        database=database
      ) as connection:
        with connection.cursor() as cursor:
          cursor.executemany(sql_insert_affiliations, records_affiliations)
          connection.commit()

####################################################################################################
