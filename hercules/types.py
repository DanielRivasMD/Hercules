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

####################################################################################################
