
"""uniit tests for the Flask application for COVID-19 stats comparison"""
import unittest
from app import app

class TestFlaskApp(unittest.TestCase):
    """Unit tests for the Flask application"""
    def setUp(self):
        """"Set up the test client for the Flask application"""
        self.client = app.test_client()
    def test_homepage(self):
        """Test if the homepage loads correctly."""
        response = self.app.get('/')
        self.assertIn(b'Welcome to my ID2 Application!', response.data)
    def test_valid_stats(self):
        """Test if valid country stats load correctly."""
        response = self.app.get('/stats/USA/2022-01-01/2022-01-08')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'COVID-19 stats for USA', response.data)
    def test_404_error_handler(self):
        """Test the custom 404 error handler."""
        # Simulate a request to an invalid URL that will trigger the 404 handler
        response = self.client.get('/invalid-url')

        # Assert that the status code is 404
        self.assertEqual(response.status_code, 404)

        # Assert that the response contains the custom error message
        self.assertIn(b'Error 404: The requested resource was not found.', response.data)
        self.assertIn(b'/stats/', response.data)
        self.assertIn(b'Example:', response.data)
if __name__ == '__main__':
    unittest.main()
