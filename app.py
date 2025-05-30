"""Flask app to show COVID-19 statistics."""

from flask import Flask, render_template_string
from ProductionCode import covid_stats

app = Flask(__name__)

@app.route('/')
def homepage():
    """Show homepage instructions.
    Returns:
        str: Instructions for using the app in html format.
    """
    return (
        "<h1>Welcome to my ID2 Application!</h1>"
        "- To get COVID-19 statistics, use this URL format:"
        "/stats/<country>/<beginning_date>/<ending_date>"
        "Example:\n"
        "/stats/USA/2020-03-01/2020-03-10<br>"
    )
@app.route("/stats/<country>/<beginning_date>/<ending_date>", strict_slashes=False)
def stats(country, beginning_date, ending_date):
    """Show COVID-19 stats for a country between two dates.
    Args:
        country (str): The name of the country.
        beginning_date (str): The start date in YYYY-MM-DD format.
        ending_date (str): The end date in YYYY-MM-DD format.
    """
    try:
        # Wrap country string in a list
        total_cases, total_deaths = covid_stats.stats([country], beginning_date, ending_date)
        return (
            f"COVID-19 stats for {country} from {beginning_date} to {ending_date}:<br>"
            f"Total Cases: {total_cases}<br>"
            f"Total Deaths: {total_deaths}"
        )
    except (ValueError, KeyError) as e:
        return f"Error: Invalid input or missing data. {str(e)}"

@app.errorhandler(404)
def page_not_found(_error):
    """Handle 404 errors with a custom message.
    uses argument _error to avoid unused variable warning"""
    return render_template_string("""
        <h1>Error 404: The requested resource was not found.</h1>
        <p>- To get COVID-19 statistics, use this URL format:</p>
        <p>/stats/&lt;country&gt;/&lt;beginning_date&gt;/&lt;ending_date&gt;</p>
        <p>Example:</p>
        <p>/stats/USA/2020-03-01/2020-03-10</p>
    """), 404

if __name__ == '__main__':
    app.run()
