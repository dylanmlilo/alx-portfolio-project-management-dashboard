import unittest
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from models.base import Base


class TestBaseModel(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Set up the test database and session."""
        cls.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(cls.engine)
        cls.Session = sessionmaker(bind=cls.engine)
        cls.session = cls.Session()

    @classmethod
    def tearDownClass(cls):
        """Tear down the test database and session."""
        cls.session.close()
        Base.metadata.drop_all(cls.engine)

    def test_create_model(self):
        """Test creating a new model using Base."""
        class TestModel(Base):
            __tablename__ = 'test_model'
            id = Column(Integer, primary_key=True)
            name = Column(String)

        Base.metadata.create_all(self.engine)

        test_instance = TestModel(name='Test Name')
        self.session.add(test_instance)
        self.session.commit()

        result = self.session.query(TestModel).first()
        self.assertEqual(result.name, 'Test Name')

    def test_relationships(self):
        """Test relationships using Base."""
        class Parent(Base):
            __tablename__ = 'parents'
            id = Column(Integer, primary_key=True)
            name = Column(String)
            children = relationship("Child", back_populates="parent")

        class Child(Base):
            __tablename__ = 'children'
            id = Column(Integer, primary_key=True)
            name = Column(String)
            parent_id = Column(Integer, ForeignKey('parents.id'))
            parent = relationship("Parent", back_populates="children")

        Base.metadata.create_all(self.engine)

        parent_instance = Parent(name='Parent 1')
        child_instance = Child(name='Child 1', parent=parent_instance)

        self.session.add(parent_instance)
        self.session.add(child_instance)
        self.session.commit()


        parent = self.session.query(Parent).first()
        self.assertEqual(parent.name, 'Parent 1')
        self.assertEqual(len(parent.children), 1)
        self.assertEqual(parent.children[0].name, 'Child 1')


if __name__ == '__main__':
    unittest.main()
