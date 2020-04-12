from dataclasses import dataclass
from bs4 import BeautifulSoup
import requests


@dataclass(frozen=False)
class Countries:
    name: str
    totalCases: int
    newCases: int
    totalDeaths: int
    newDeaths: int
    totalRecovered: int
    activeCases: int
    critical: int
    totalCasesPerMilPop: int
    deathsPerMilPop: int
    totalTests: int
    testsPerMilPop: int


# Sends get request to worldometers.info and if the request is successful, then
# a copy of the site is stored in a BeautifulSoup object. After this happens,
# the BeautifulSoup object is then parsed through to find specific data.
# This data is then stored in "data.txt" where later it will be parsed to find
# valuable data.
def init():
    f = open("output/data.txt", "w")
    page = requests.get("https://www.worldometers.info/coronavirus/")

    if page.status_code == 200:
        soup = BeautifulSoup(page.content, 'html.parser')
        table = soup.find(id="main_table_countries_today")
        f.write(str(table.find("tbody")))

    f.close()


# Creates a Countries object for every country in listOfCountries.txt and then
# stores it in a list
def initList():
    aList = []

    f = open("listOfCountries.txt", "r")
    for line in f:
        temp = str(line.strip())
        tempCountry = Countries(temp, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        aList.append(tempCountry)
    f.close()
    return aList


# Parses through data.txt to find data on each country. It then takes that data and
# stores it in tempDict which is then passed to updateCountry where countriesList in
# the main function will be updated.
def createCountries(countryList):
    f = open("output/data.txt", "r")
    for line in f:
        if line.strip() == "<tr style=\"\">":
            valueDict = {
                "name": "", "totalCases": 0, "newCases": 0, "totalDeaths": 0,
                "newDeaths": 0, "totalRecovered": 0, "activeCases": 0,
                "critical": 0, "totalCasesPerMilPop": 0, "deathsPerMilPop": 0,
                "totalTests": 0, "testsPerMilPop": 0
            }

            helperDict = {
                0: "name", 1: "totalCases", 2: "newCases", 3: "totalDeaths",
                4: "newDeaths", 5: "totalRecovered", 6: "activeCases", 7: "critical",
                8: "totalCasesPerMilPop", 9: "deathsPerMilPop", 10: "totalTests",
                11: "testsPerMilPop", 12: "testsPerMilPop"
            }

            for x in range(13):
                newLine = f.readline()
                splitLine = newLine.split(">")
                if len(splitLine) == 5:
                    valueDict["name"] = splitLine[2][:splitLine[2].find("<")]
                if len(splitLine) == 3:
                    value = splitLine[1][:splitLine[1].find("<")]
                    # len of tempDict is 12
                    category = helperDict[x]
                    valueDict[category] = value

            updateCountry(countryList, valueDict)


# Updates all the Countries objects values that are stored in the valueDict
# countryList is a list of all the initialized Countries object
def updateCountry(countryList, valueDict):
    for country in countryList:
        if valueDict["name"] == country.name:
            country.totalCases = valueDict["totalCases"]
            country.newCases = valueDict["newCases"]
            country.totalDeaths = valueDict["totalDeaths"]
            country.newDeaths = valueDict["newDeaths"]
            country.totalRecovered = valueDict["totalRecovered"]
            country.activeCases = valueDict["activeCases"]
            country.critical = valueDict["critical"]
            country.totalCasesPerMilPop = valueDict["totalCasesPerMilPop"]
            country.deathsPerMilPop = valueDict["deathsPerMilPop"]
            country.totalTests = valueDict["totalTests"]
            country.testsPerMilPop = valueDict["testsPerMilPop"]
        else:
            pass


# main function and nothing else
def main():
    init()
    countriesList = initList()
    createCountries(countriesList)


if __name__ == '__main__':
    main()
