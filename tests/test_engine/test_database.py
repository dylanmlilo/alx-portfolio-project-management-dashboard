import unittest
import os
from sqlalchemy import create_engine
from sqlalchemy.exc import NoSuchModuleError, ArgumentError
from models.engine.database import engine, Session


class TestDatabaseConnection(unittest.TestCase):
    def test_engine_creation(self):
        """Test if the SQLAlchemy engine is created successfully."""
        self.assertIsNotNone(engine)
        self.assertTrue(engine.name in ['sqlite', 'mysql', 'postgresql'])

    def test_session_creation(self):
        """Test if a session can be created from the engine."""
        session = Session()
        self.assertIsNotNone(session)

    def test_db_connection_string_loaded(self):
        """Test if the database connection string is loaded from environment variables."""
        connection_string = os.getenv('db_connection_string')
        self.assertIsNotNone(connection_string)
        self.assertTrue('sqlite' in connection_string or 'mysql' in connection_string or 'postgresql' in connection_string)

    def test_invalid_db_connection_string(self):
        """Test if an error is raised when using an invalid connection string."""
        original_connection_string = os.getenv('db_connection_string')
        os.environ['db_connection_string'] = 'invalid_connection_string'
        
        with self.assertRaises((NoSuchModuleError, ArgumentError)):
            engine = create_engine(os.getenv('db_connection_string'))

        os.environ['db_connection_string'] = original_connection_string


if __name__ == '__main__':
    unittest.main()
