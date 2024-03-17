----------------------------------------------------------------------------------------------------

-- database
CREATE DATABASE PubMed;

-- connect database
USE PubMed;

-- article information table
CREATE TABLE Articles (
  pmid INT,
  journal TEXT,
  title TEXT,
  abstract TEXT,
  PRIMARY KEY (pmid)
);

-- authors table
CREATE TABLE Authors (
  author_pmid VARCHAR(255),
  author VARCHAR(255),
  pmid INT,
  PRIMARY KEY (author_pmid),
  FOREIGN KEY (pmid) REFERENCES `Articles`(pmid)
);

-- author affiliation table
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

----------------------------------------------------------------------------------------------------
