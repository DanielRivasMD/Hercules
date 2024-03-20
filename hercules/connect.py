####################################################################################################

from getpass import getpass
from mysql.connector import connect

####################################################################################################

def create_db(database, user='drivas', password='hercules'):

  sql_create_db = "CREATE DATABASE " + database + ";"
  sql_use_db = "USE " + database + ";"

  sql_create_articles = """
  CREATE TABLE Articles (
    pmid INT,
    journal TEXT,
    title TEXT,
    abstract TEXT,
    PRIMARY KEY (pmid)
  );
  """

  sql_create_authors = """
  CREATE TABLE Authors (
    author_pmid VARCHAR(255),
    author VARCHAR(255),
    pmid INT,
    PRIMARY KEY (author_pmid),
    FOREIGN KEY (pmid) REFERENCES `Articles`(pmid)
  );
  """

  sql_create_affiliations = """
  CREATE TABLE Affiliations (
    author_affiliation VARCHAR(255),
    affiliation VARCHAR(255),
    author VARCHAR(255),
    pmid INT,
    author_pmid VARCHAR(255),
    PRIMARY KEY (author_affiliation),
    FOREIGN KEY (pmid) REFERENCES `Articles`(pmid),
    FOREIGN KEY (author_pmid) REFERENCES `Authors`(author_pmid)
  );
  """

  ####################################################################################################

  # WIP: look up how to create database
  with connect(
    user=user,
    password=password
  ) as connection:
    with connection.cursor() as cursor:
      cursor.execute(sql_create_db)
      cursor.execute(sql_use_db)
      cursor.execute(sql_create_articles)
      cursor.execute(sql_create_authors)
      cursor.execute(sql_create_affiliations)
      connection.commit()

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
