####################################################################################################

from getpass import getpass
from mysql.connector import connect

####################################################################################################

def insert_articles(articles, user='drivas', password='hercules', database='PubMed'):

  insert_articles = """
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
      cursor.executemany(insert_articles, records_articles)
      connection.commit()

####################################################################################################

