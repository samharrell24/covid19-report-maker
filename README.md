# CRM (COVID-19 Report Maker) - What is it?
CRM, generates a report using data gathered from various news sites and `https://www.worldometers.info/coronavirus/`. Specifically, it uses BeautifulSoup, a Python based web scraper to gather data from `https://www.worldometers.info/coronavirus/` which hosts data on every country in the world related to coronavirus and how they are being affected. To gather the most recent news articles related to the coronavirus, CRM uses newsAPI, which allows you to search through over 50,000 news sites using one API.  

## Preface
In order to run `generate_report.py`, you must first install the latest version of Python. You can download the latest verison of Python at `python.org/downloads`. Once you have done this, you now need to install, the following packages so the project can run properly. 

BeautifulSoup: `pip install BeautifulSoup`

newsAPI: `pip install newsapi-python`

datatime: `pip install datetime`

requests: `pip install requests`

Once all of the packages are installed, download the repository and run `generate_report.py`. Once you run it, it should generate a report in the reports folder named `COVID-19_REPORT_YEAR-MONTH-DATE.txt`. You can then open this to view the report. 

## Future Plans
In the future, we plan on converting this to a web app where anyone can view this information and generate reports using specific parameters. These personal reports will be a lot more user friendly and you will be able to download them and share them on social media.
