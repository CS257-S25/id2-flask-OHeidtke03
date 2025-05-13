
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
        response = self.app.get('/stats/US/2020-03-01/2021-03-10')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'COVID-19 stats for US', response.data)
if __name__ == '__main__':
    unittest.main()
