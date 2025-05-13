import csv
from datetime import datetime

def stats(countries, beginning_date, ending_date):
    """Calculate total COVID-19 cases and deaths for given countries within a date range.
    args:
        countries (list): List of country names or codes.
        beginning_date (str): Start date in YYYY-MM-DD format.
        ending_date (str): End date in YYYY-MM-DD format.
    returns:
        tuple: Total cases and total deaths for the specified countries."""
    beginning = datetime.strptime(beginning_date, "%Y-%m-%d")
    ending = datetime.strptime(ending_date, "%Y-%m-%d")

    total_cases = 0
    total_deaths = 0
    found_country = False  # Track if any input country exists in data

    with open('covidData.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            country_name = row['Country'].strip()
            country_code = row['Country_code'].strip()
            if any(code in countries for code in [country_name, country_code]):
                found_country = True
                date = datetime.strptime(row['Date_reported'].strip(), "%Y-%m-%d")
                if beginning <= date <= ending:
                    total_cases += int(row['New_cases']) if row['New_cases'] else 0
                    total_deaths += int(row['New_deaths']) if row['New_deaths'] else 0

    # If no matching country was found in the dataset, raise KeyError
    if not found_country:
        raise KeyError(f"Country code(s) {countries} not found in dataset.")

    return total_cases, total_deaths

if __name__ == "__main__":
    print(stats(["Afghanistan", "Brazil"], "2023-08-06"))
