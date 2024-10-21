import unittest
from unittest.mock import patch, MagicMock
from flask import Flask
from app import app
from models.gis import Activity
from models.engine.database import session


class GisActivityRoutesTestCase(unittest.TestCase):
    def setUp(self):
        """
        Set up the test client and mock objects before each test.
        """
        self.app = app.test_client()  # Create a test client
        self.app.testing = True  # Enable testing mode

    def tearDown(self):
        """
        Tear down the session and any other resources after each test.
        """
        pass

    @patch('flask_login.current_user')
    @patch('models.engine.database.session.commit')
    @patch('models.engine.database.session.add')
    def test_insert_gis_activity_data_success(self, mock_add, mock_commit, mock_current_user):
        """
        Test successful insertion of GIS activity data.
        """
        mock_current_user.is_authenticated = True
        mock_current_user.has_role = MagicMock(return_value=True)

        data = {
            'activity_name': 'New Activity',
            'output_id': 1,
            'responsible_person_id': 2
        }

        with self.app.post('/insert_gis_activity_data', data=data, follow_redirects=True) as response:
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Data inserted successfully', response.data)

            mock_add.assert_called_once()  # Ensure that the new activity was added to the session
            mock_commit.assert_called_once()  # Ensure that the session was committed

    @patch('flask_login.current_user')
    @patch('models.engine.database.session.rollback')
    def test_insert_gis_activity_data_failure(self, mock_rollback, mock_current_user):
        """
        Test failure when inserting GIS activity data (database exception).
        """
        mock_current_user.is_authenticated = True
        mock_current_user.has_role = MagicMock(return_value=True)

        with patch('models.engine.database.session.add', side_effect=Exception("Insert error")):
            data = {
                'activity_name': 'New Activity',
                'output_id': 1,
                'responsible_person_id': 2
            }

            response = self.app.post('/insert_gis_activity_data', data=data)

            self.assertEqual(response.status_code, 400)
            self.assertIn(b'Insert error', response.data)
            mock_rollback.assert_called_once()  # Ensure that the session rollback is called on error

    @patch('flask_login.current_user')
    @patch('models.engine.database.session.commit')
    @patch('models.engine.database.session.query')
    def test_update_gis_activity_data_success(self, mock_query, mock_commit, mock_current_user):
        """
        Test successful update of GIS activity data.
        """
        mock_current_user.is_authenticated = True
        mock_current_user.has_role = MagicMock(return_value=True)

        mock_activity = MagicMock()
        mock_query.return_value.filter_by.return_value.first.return_value = mock_activity

        data = {
            'activity_name': 'Updated Activity',
            'output_id': 1,
            'responsible_person_id': 2
        }

        response = self.app.post('/update_gis_activity_data/1', data=data, follow_redirects=True)

        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Data updated successfully', response.data)
        mock_commit.assert_called_once()  # Ensure session commit was called

    @patch('flask_login.current_user')
    @patch('models.engine.database.session.commit')
    @patch('models.engine.database.session.query')
    def test_delete_gis_activity_data_success(self, mock_query, mock_commit, mock_current_user):
        """
        Test successful deletion of GIS activity data.
        """
        mock_current_user.is_authenticated = True
        mock_current_user.has_role = MagicMock(return_value=True)

        mock_activity = MagicMock()
        mock_query.return_value.filter_by.return_value.first.return_value = mock_activity

        response = self.app.get('/delete_gis_activity_data/1', follow_redirects=True)

        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Data deleted successfully', response.data)
        mock_commit.assert_called_once()  # Ensure session commit was called

    @patch('flask_login.current_user')
    @patch('models.engine.database.session.query')
    def test_delete_gis_activity_data_failure(self, mock_query, mock_current_user):
        """
        Test failure to delete GIS activity data (activity not found).
        """
        mock_current_user.is_authenticated = True
        mock_current_user.has_role = MagicMock(return_value=True)

        mock_query.return_value.filter_by.return_value.first.return_value = None

        response = self.app.get('/delete_gis_activity_data/1', follow_redirects=True)

        self.assertEqual(response.status_code, 400)
        self.assertIn(b'error', response.data)  # Ensure error message in response


if __name__ == '__main__':
    unittest.main()
