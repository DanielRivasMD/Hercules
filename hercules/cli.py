####################################################################################################

import click

####################################################################################################

from .pubmed import pubmed
from .connect import create_db, insert_articles, insert_authors, insert_affiliations

####################################################################################################

@click.command()
@click.option('--author', help='Author to search.')
@click.option('--outdir', default='.', help='Output directory.')
def main_hercules(author, outdir):
  """PUBMED web scrapper."""
  articles = pubmed(author, outdir)
  # WIP: modify `author` to lower case & replace whitespace
  create_db(author)
  insert_articles(articles)
  insert_authors(articles)
  insert_affiliations(articles)

####################################################################################################
