from flask import Flask, request, jsonify
from datetime import datetime, timedelta
from ProductionCode.production import stats

app = Flask(__name__)

@app.route('/')
def homepage():
    return '''
    <h2>COVID Comparison App</h2>
    <p>To compare up to 5 countries during a week, use the following format:</p>
    <p><code>/compare/2021-05-01?countries=USA,IND,BRA</code></p>
    <p>The date can be any day in the week you want to analyze.</p>
    '''

@app.route('/compare/<date>', methods=['GET'])
def compare_route(date):
    try:
        base_date = datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        return "Invalid date format. Use YYYY-MM-DD.", 400

    country_list = request.args.get('countries')
    if not country_list:
        return "Please provide 2–5 comma-separated countries in the 'countries' query param.", 400

    countries = country_list.split(',')
    if not (2 <= len(countries) <= 5):
        return "Please select between 2 and 5 countries.", 400

    # Calculate start and end of the week (Sunday–Saturday)
    start_of_week = base_date - timedelta(days=base_date.weekday())
    end_of_week = start_of_week + timedelta(days=6)

    results = {}
    for country in countries:
        total_cases, total_deaths = stats(country.strip(), start_of_week.strftime("%Y-%m-%d"), end_of_week.strftime("%Y-%m-%d"))
        results[country.strip()] = {
            "total_cases": total_cases,
            "total_deaths": total_deaths
        }

    return jsonify(results)

@app.route('/about')
def aboutpage():
    return "Hello, this is the about page."

@app.route('/<favorite_number>', strict_slashes=False)
def favorite_number(favorite_number):
    return f"Your favorite number is {favorite_number}."

if __name__ == "__main__":
    app.run(debug=True)
