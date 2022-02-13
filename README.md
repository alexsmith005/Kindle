# Kindle
This is a data pipeline created to take the highlighted words from your Kindle, and create flashcards for studying vocabulary words/terms.
This is made using the ETL framework:

Extraction - the data is uploaded from the Kindle in a raw text file

Transformation - the data is then cleaned and the definitions for the words are found by scraping the web. Error handling is done here to ensure all words are valid, and if   not, find a suitable replacement when available, or delete them.

Load - The resulting dataset is structured inside a Dataframe and loaded into a Postgresql database in the cloud

Example Database:

    0	precipitous [ pri-sip-i-tuhs ] adjective	of the nature of or characterized by precipices: a precipitous wall of rock.extremely or impassably steep: precipitous mountain trails.precipitate.

    1	surreptitiously [ sur-uhp-tish-uhs-lee ] adverb	in a secret or unauthorized way; stealthily: After it surreptitiously installs itself on a user's phone, the spyware program can steal credit card numbers, passwords, and other personal information.

    2	imperiously [ im-peer-ee-uhs-lee ] adverb	in a domineering or haughty manner:She held out her hand imperiously, but the messenger did not immediately hand over the letter.in an imperative way; urgently: The need to be accepted can be felt as imperiously as the needs for food, clothing, and shelter.

    3	querulous [ kwer-uh-luhs, kwer-yuh- ] adjective	full of complaints; complaining.characterized by or uttered in complaint; peevish: a querulous tone; constant querulous reminders of things to be done.
    
    4	emanation [ em-uh-ney-shuhn ] noun	an act or instance of emanating. something that emanates or is emanated. Physical Chemistry. a gaseous product of radioactive disintegration, including radon, thoron, and actinon. Symbol: Em