####################################################################################################

from getpass import getpass
from mysql.connector import connect

####################################################################################################

with connect(
  user='drivas',
  password='hercules',
  database='PubMed'
) as connection:
  s = 'SHOW DATABASES'
  with connection.cursor() as cursor:
    cursor.execute(s)
    for result in cursor:
      print(result)

####################################################################################################
