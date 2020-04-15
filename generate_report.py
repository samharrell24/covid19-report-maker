import get_news
import get_site
import datetime


def generate_report():
    d = datetime.datetime.today()
    f = open("reports/COVID-19_REPORT_" + str(d.date()) + ".txt", "w")
    country_data = get_site.main()
    news_data = get_news.main()

    f.write("List of Country's and their COVID-19 Data from " + str(d.date()) + "\n\n")

    for x in country_data:
        f.write(x.name + ":\n")
        f.write("=+=+=+=+=\n")

        f.write("Total Cases: " + str(x.totalCases) + "\nNew Cases: " + str(x.newCases) + "\nTotal Deaths: "
                + str(x.totalDeaths) + "\nNew Deaths: " + str(x.newDeaths) + "\nTotal Recovered: " + str(
                x.totalRecovered) + "\nActive Cases: " + str(x.activeCases) + "\nNum in Critical Condition: " + str(
                x.critical) + "\nTotal Cases Per Mil Pop: " + str(x.totalCasesPerMilPop) + "\nDeaths Per Mil Pop: " +
                str(x.deathsPerMilPop) + "\nTotal Tests: " + str(x.totalTests) + "\nTests Per Mil Pop: " +
                str(x.testsPerMilPop) + "\n\n")

    for y in news_data:
        f.write("")


def main():
    generate_report()


if __name__ == '__main__':
    main()
