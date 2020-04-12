from dataclasses import dataclass
from bs4 import BeautifulSoup
import requests


@dataclass(frozen=True)
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
def initList(aList):
    f = open("listOfCountries.txt", "r")
    for line in f:
        tempCountry = Countries(str(line.strip), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        aList.append(tempCountry)
    f.close()

    return aList


def createCountries(countryList):
    # go through file and store every value in temp ints
    # then go through list to find the corresponding country and replace it
    f = open("output/data.txt", "r")
    for line in f:
        if line.strip() == "<tr style=\"\">":
            tempDict = {
                "name": "", "totalCases": 0, "newCases": 0, "totalDeaths": 0,
                "newDeaths": 0, "totalRecovered": 0, "activeCases": 0,
                "critical": 0, "totalCasesPerMilPop": 0, "deathsPerMilPop": 0,
                "totalTests": 0, "testsPerMilPop": 0
            }

            for x in range(13):
                newLine = f.readline()
                splitLine = newLine.split(">")
                if len(splitLine) == 5:
                    tempDict["name"] = splitLine[2][:splitLine[2].find("<")]
                if len(splitLine) == 3:
                    value = splitLine[1][:splitLine[1].find("<")]
                    # len of tempDict is 12
                    if x == 1:
                        tempDict["totalCases"] = value
                    elif x == 2:
                        tempDict["newCases"] = value
                    elif x == 3:
                        tempDict["totalDeaths"] = value
                    elif x == 4:
                        tempDict["totalDeaths"] = value
                    elif x == 5:
                        tempDict["newDeaths"] = value
                    elif x == 6:
                        tempDict["totalRecovered"] = value
                    elif x == 7:
                        tempDict["activeCases"] = value
                    elif x == 8:
                        tempDict["critical"] = value
                    elif x == 9:
                        tempDict["totalCasesPerMilPop"] = value
                    elif x == 10:
                        tempDict["deathsPerMilPop"] = value
                    elif x == 11:
                        tempDict["totalTests"] = value
                    elif x == 12:
                        tempDict["testsPerMilPop"] = value

            #updateCountry(countryList, tempDict)


#def updateCountry(countryList, valuesDict):
 #   for country in countryList:
  #      print(country.name)
   #     #if country.name == valuesDict["name"]:



def main():
    init()
    countriesList = []
    initList(countriesList)
    #print(countriesList)
    createCountries(countriesList)


if __name__ == '__main__':
    main()
