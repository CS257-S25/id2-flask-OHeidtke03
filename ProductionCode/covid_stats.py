import csv
from datetime import datetime

def stats(countries, beginning_date, ending_date):
    beginning = datetime.strptime(beginning_date, "%Y-%m-%d")
    ending = datetime.strptime(ending_date, "%Y-%m-%d")

    total_cases = 0
    total_deaths = 0

    with open('covidData.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            country_name = row['Country'].strip()
            country_code = row['Country_code'].strip()
            if country_name in countries or country_code in countries:
                date = datetime.strptime(row['Date_reported'].strip(), "%Y-%m-%d")
                if beginning <= date <= ending:
                    total_cases += int(row['New_cases']) if row['New_cases'] else 0
                    total_deaths += int(row['New_deaths']) if row['New_deaths'] else 0

    return total_cases, total_deaths


if __name__ == "__main__":
    print(stats(["Afghanistan", "Brazil"], "2023-08-06"))
