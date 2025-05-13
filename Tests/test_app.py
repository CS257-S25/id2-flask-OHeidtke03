
"""uniit tests for the Flask application for COVID-19 stats comparison"""
import unittest
from app import app

class TestFlaskApp(unittest.TestCase):
    """Unit tests for the Flask application"""
    def setUp(self):
        """"Set up the test client for the Flask application"""
        self.app = app.test_client()
    def test_homepage(self):
        """Test if the homepage loads correctly."""
        response = self.app.get('/')
        self.assertIn(b'Welcome to my ID2 Application!', response.data)
    def test_valid_stats(self):
        """Test if valid country stats load correctly."""
        response = self.app.get('/stats/USA/2022-01-01/2022-01-08')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'COVID-19 stats for USA', response.data)
    def test_invalid_date_format(self):
        """Test invalid date format that triggers a ValueError in the stats route."""
        # Simulate a request with an invalid date format (e.g., "2020-03-01" instead of "2020/03/01")
        response = self.app.get('/stats/USA/2020-03-01/2020-03-10')  # Invalid date format

        # Assert that the status code is 200 (no internal error)
        self.assertEqual(response.status_code, 200)

        # Assert that the error message is returned
        self.assertIn(b'Error: Invalid input or missing data.', response.data)
    """def test_invalid_country(self):
        """Test an invalid country that triggers a KeyError in the stats route."""
        # Simulate a request for a non-existent country
        response = self.app.get('/stats/NonExistentCountry/2020-01-01/2020-01-08')

        # Assert that the status code is 200 (no internal error)
        self.assertEqual(response.status_code, 200)

        # Assert that the error message is returned
        self.assertIn(b'Error: Invalid input or missing data.', response.data)
    def test_404_error_handler(self):
        """Test the custom 404 error handler."""
        # Simulate a request to an invalid URL that will trigger the 404 handler
        response = self.app.get('/invalid-url')  # Corrected to use self.app here

        # Assert that the status code is 404
        self.assertEqual(response.status_code, 404)

        # Assert that the response contains the custom error message
        self.assertIn(b'Error 404: The requested resource was not found.', response.data)
        self.assertIn(b'/stats/', response.data)
        self.assertIn(b'Example:', response.data)"""
if __name__ == '__main__':
    unittest.main()
