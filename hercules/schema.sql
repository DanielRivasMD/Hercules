----------------------------------------------------------------------------------------------------

-- database
CREATE DATABASE PubMed;

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
  author VARCHAR(255),
  pmid INT,
  PRIMARY KEY (author),
  FOREIGN KEY (pmid) REFERENCES `Articles`(pmid)
);

-- author affiliation table
CREATE TABLE Affiliations (
  author_affiliation VARCHAR(255),
  affilitation TEXT,
  author VARCHAR(255),
  pmid INT,
  PRIMARY KEY (author_affiliation),
  FOREIGN KEY (pmid) REFERENCES `Articles`(pmid),
  FOREIGN KEY (author) REFERENCES `Authors`(author)
);

----------------------------------------------------------------------------------------------------
