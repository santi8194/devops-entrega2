import json
import os

# Since the tests are in a different directory, I need to adjust the path
# to import the application and its components correctly.
import sys
import unittest
from unittest.mock import MagicMock, patch

from flask import Flask, jsonify

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from application import application


class TestBlacklists(unittest.TestCase):
    def setUp(self):
        """Set up a test client for the Flask application."""
        self.app = application.test_client()
        self.app.testing = True

    @patch("blacklists.src.blueprints.blacklists.Authenticate")
    @patch("blacklists.src.blueprints.blacklists.CreateBlacklist")
    def test_create_blacklist_entry(self, mock_create_blacklist, mock_authenticate):
        """Test the endpoint for creating a new blacklist entry."""
        # Configure mocks
        mock_authenticate.return_value.execute.return_value = "test_user_id"
        mock_create_blacklist.return_value.execute.return_value = {
            "id": 1,
            "email": "test@example.com",
            "reason": "Test reason",
        }

        # Define test data
        payload = {"email": "test@example.com", "reason": "Test reason"}
        headers = {"Authorization": "Bearer valid_token"}

        # Make the request
        response = self.app.post(
            "/blacklists",
            headers=headers,
            data=json.dumps(payload),
            content_type="application/json",
        )

        # Assertions
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.get_json()["email"], "test@example.com")

    @patch("blacklists.src.blueprints.blacklists.Authenticate")
    @patch("blacklists.src.blueprints.blacklists.GetBlacklist")
    def test_get_blacklist_info(self, mock_get_blacklist, mock_authenticate):
        """Test the endpoint for retrieving blacklist information."""
        # Configure mocks
        mock_authenticate.return_value.execute.return_value = "test_user_id"
        mock_get_blacklist.return_value.execute.return_value = {
            "is_blacklisted": True,
            "reason": "Test reason",
        }

        # Define test data
        email = "test@example.com"
        headers = {"Authorization": "Bearer valid_token"}

        # Make the request
        response = self.app.get(f"/blacklists/{email}", headers=headers)

        # Assertions
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.get_json()["is_blacklisted"])

    def test_health_check(self):
        """Test the health check endpoint."""
        # Make the request
        response = self.app.get("/")

        # Assertions
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"status": "ok"})


if __name__ == "__main__":
    unittest.main()
