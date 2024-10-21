import unittest
from app import app
from flask import url_for
from unittest.mock import patch


class TestAdminDashboardRoute(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_admin_dashboard_route_status_code(self):
        with self.app as client:
            response = client.get(url_for('admin_dashboard.admin_dashboard'))
            self.assertEqual(response.status_code, 200)

    @patch('flask_login.utils._get_user')
    def test_admin_dashboard_route_authenticated(self, mock_get_user):
        mock_get_user.return_value.is_authenticated = True
        mock_get_user.return_value.has_role = lambda role: True
        with self.app as client:
            response = client.get(url_for('admin_dashboard.admin_dashboard'))
            self.assertEqual(response.status_code, 200)

    @patch('flask_login.utils._get_user')
    def test_admin_dashboard_route_unauthenticated(self, mock_get_user):
        mock_get_user.return_value.is_authenticated = False
        with self.app as client:
            response = client.get(url_for('admin_dashboard.admin_dashboard'))
            self.assertEqual(response.status_code, 302)  # Redirects to login page

if __name__ == '__main__':
    unittest.main()