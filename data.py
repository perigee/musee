import requests
import lxml
from bs4 import BeautifulSoup


TABLE_NB_COLUMN = 4

def getRaw():
    wiki_url = 'https://en.wikipedia.org/wiki/List_of_most_visited_museums'
    with requests.get(wiki_url) as resp:
        if resp.status_code != 200:
            return None

        return resp.content


def extractRow(inData):
    tabs = inData.find_all('td')
    if len(tabs) != TABLE_NB_COLUMN:
        return None

    museum = tabs[0].find('a').text
    city = tabs[1].find_all('a')[1].text
    visitors = tabs[2].text
    year = tabs[3].text[0:4]

    return '::'.join([museum, city, visitors, year])

    
def extractTable(rawdata):
        page = BeautifulSoup(rawdata, 'lxml')
        table = page.find('table', class_='wikitable sortable')
        mhead = table.find('thead')
        mbody = table.find('tbody')
        for row in mbody.find_all('tr'):
            datarow = extractRow(row)
            if not datarow:
                continue

            print(datarow)
                
