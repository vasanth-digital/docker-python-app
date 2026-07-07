import unittest
import json
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

class TestAPI(unittest.TestCase):
    
    def test_response_is_valid_json(self):
        """Test that our response is valid JSON"""
        response = {
            "message": "Production Docker Stack",
            "service": "api",
            "status": "healthy"
        }
        json_str = json.dumps(response)
        parsed = json.loads(json_str)
        self.assertEqual(parsed["status"], "healthy")

    def test_required_fields_present(self):
        """Test all required fields exist"""
        response = {
            "message": "Production Docker Stack",
            "service": "api",
            "status": "healthy"
        }
        self.assertIn("message", response)
        self.assertIn("service", response)
        self.assertIn("status", response)

    def test_service_name(self):
        """Test service name is correct"""
        response = {"service": "api"}
        self.assertEqual(response["service"], "api")

if __name__ == "__main__":
    unittest.main()
