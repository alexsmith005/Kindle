import requests
import pandas as pd
from bs4 import BeautifulSoup
from time import sleep
import openFile


initFile = openFile.getFile()

try:
 oldWords = pd.read_csv('VocabWords.csv', index_col=[0]).iloc[:,0]
except:
    oldWords = []

vocabDict = {}
vocabWords = []
lineCount = 1
requestCount = 0

# Clean up the old list of words to avoid superfluous lookups
for x, oldW in enumerate(oldWords):
    oldWords.iloc[x] = oldW.partition(' ')[0]
oldWords = oldWords.to_list()

# Create list of words to lookup, avoiding duplicates and already defined words
for line in initFile:
    lineCount += 1
    if lineCount == 5 and len(line) < 50:
        simpLine = line.rstrip(",. \n\"\”\'\"\;\“")
        if (simpLine not in vocabWords) & (simpLine not in oldWords):
            vocabWords.append(simpLine)
        lineCount = 0
    elif lineCount == 5:
        lineCount = 0

print(vocabWords)
print(oldWords)

for word in vocabWords:
    # Scrape the webpage for the word, pronunciation, parts of speech, and the definition
    page = requests.get("https://www.dictionary.com/browse/" + word)
    soup = BeautifulSoup(page.content, 'html.parser')
    # If Word doesn't exist, check spell suggestions and follow their path for new word
    if soup.find(class_="spell-suggestions") != None:
        newWord = soup.find(class_="css-pwhc02 e19m0k9k3").get_text()
        page = requests.get("https://www.dictionary.com/browse/" + newWord)
        soup = BeautifulSoup(page.content, 'html.parser')
    bigTest = soup.find(class_="css-1sprl0b e1wg9v5m5")
    pronTest = soup.find(class_="pron-spell-content css-7iphl0 evh0tcl1")
    grammarTest = soup.find(class_="luna-pos")
    defTest = soup.find(class_="css-10n3ydx e1hk9ate0")
    # Try the exception case if the first case returned None
    if pronTest == None:
        pronTest = soup.find(class_="pron")
    # Ensure that the classifiers returned information before assigning to the dictionary to avoid NoneType error
    if bigTest and pronTest and grammarTest and defTest != None:
        bigWord = bigTest.get_text()
        pron = pronTest.get_text()
        wordType = grammarTest.get_text()
        wordDef = defTest.get_text()
    # Add new word to dictionary with the word, pronunciation, and part of speech as the Key
    vocabDict[bigWord + ' ' + pron + ' ' + wordType] = wordDef
    bigTest, pronTest, grammarTest, defTest = None, None, None, None
    # Built in pause to avoid overloading requests
    requestCount += 1
    if requestCount == 20:
        sleep(10)
        requestCount = 0


# Create a dataframe & save results locally for future use
df = pd.DataFrame(vocabDict.values(), index=vocabDict.keys())
df.reset_index(inplace=True)
df.columns = ['Word', 'Definition']
df.to_csv('VocabWords.csv')
print(df.head())


"""
BRUTE FORCE METHOD

long_def = soup.find_all('body')[0].get_text()


lword = long_def.partition('complexity.')
rword = lword[2].partition(']')
ldef = lword[2].partition('complexity.')
rdef = ldef[2].partition('.')
print(rword[0] + rword[1], rdef[0])
"""

# Close initial file
initFile.close()
