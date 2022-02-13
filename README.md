This is a data pipeline created to take the highlighted words from your Kindle, and create flashcards for studying vocabulary words/terms.
This is made using the ETL framework:

Extraction - the data is uploaded from the Kindle in a raw text file

Transformation - the data is then cleaned and the definitions for the words are found by scraping the web. Error handling is done here to ensure all words are valid, and if   not, find a suitable replacement when available, or delete them.

Load - The resulting dataset is structured inside a Dataframe and loaded into a Postgresql database in the cloud