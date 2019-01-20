import requests
import lxml
from bs4 import BeautifulSoup
import pandas as pd


TABLE_NB_COLUMN = 4
POPULATION_FILENAME = 'population.csv'


def getRaw():
    wiki_url = 'https://en.wikipedia.org/wiki/List_of_most_visited_museums'
    with requests.get(wiki_url) as resp:
        if resp.status_code != 200:
            return None

        return resp.content


def readPopulation(filename):
    return pd.read_csv(filename, header=0)


def formatterCity(txt):
    txt = txt.replace(',','')
    return txt.lower()

def extractRow(inData):
    tabs = inData.find_all('td')
    if len(tabs) != TABLE_NB_COLUMN:
        return None

    museum = tabs[0].find('a').text
    city = formatterCity(tabs[1].find_all('a')[1].text)
    visitors = tabs[2].text
    year = tabs[3].text[0:4]

    return [museum, city, visitors, year]


def extractTable(rawdata):
    col_title = ['museum', 'city', 'visitors', 'year']
    museums = pd.DataFrame(columns=col_title)
    page = BeautifulSoup(rawdata, 'lxml')
    table = page.find('table', class_='wikitable sortable')
    mhead = table.find('thead')
    mbody = table.find('tbody')
    for row in mbody.find_all('tr'):
        datarow = extractRow(row)
        if not datarow:
            continue

        museums.loc[len(museums)] = datarow
        print(datarow)
    
    return museums

if __name__ == "__main__":
    museums = extractTable(getRaw())
    population = readPopulation(POPULATION_FILENAME)
    datasource = pd.merge(museums, population, on='city')