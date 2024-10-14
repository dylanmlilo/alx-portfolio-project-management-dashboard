import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base import Base
from models.projects import ProjectManagers
from models.strategic import StrategicTask


class TestStrategicTask(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Set up the test database and session."""
        cls.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(cls.engine)
        cls.Session = sessionmaker(bind=cls.engine)
        cls.session = cls.Session()

        cls.pm = ProjectManagers(name="John Doe", section="Engineering")
        cls.session.add(cls.pm)
        cls.session.commit()

    @classmethod
    def tearDownClass(cls):
        """Tear down the test database and session."""
        cls.session.close()
        Base.metadata.drop_all(cls.engine)

    def test_initialization(self):
        """Test the initialization of StrategicTask."""
        task = StrategicTask(
            status="Pending",
            priority="High",
            deadline="2024-12-31",
            task="Implement feature X",
            description="Description of the task",
            assigned_to=self.pm.id,
            deliverables="Deliverable details",
            percentage_done=0.0,
            fixed_cost=1000.00,
            estimated_hours=10.00,
            actual_hours=0.00
        )
        self.assertEqual(task.status, "Pending")
        self.assertEqual(task.priority, "High")
        self.assertEqual(task.task, "Implement feature X")
        self.assertEqual(task.assigned_to, self.pm.id)

    def test_str_repr(self):
        """Test the string representation of StrategicTask."""
        task = StrategicTask(
            status="Pending",
            priority="High",
            deadline="2024-12-31",
            task="Implement feature X",
            description="Description of the task",
            assigned_to=self.pm.id,
            deliverables="Deliverable details",
            percentage_done=0.0,
            fixed_cost=1000.00,
            estimated_hours=10.00,
            actual_hours=0.00
        )
        self.assertEqual(str(task), "<StrategicTask(task='Implement feature X', description='Description of the task', assigned_to='1')>")

    def test_strategic_tasks_to_dict_list(self):
        """Test the strategic_tasks_to_dict_list method."""
        task = StrategicTask(
            status="Pending",
            priority="High",
            deadline="2024-12-31",
            task="Implement feature X",
            description="Description of the task",
            assigned_to=self.pm.id,
            deliverables="Deliverable details",
            percentage_done=0.0,
            fixed_cost=1000.00,
            estimated_hours=10.00,
            actual_hours=0.00
        )
        self.session.add(task)
        self.session.commit()

        tasks_list = StrategicTask.strategic_tasks_to_dict_list()
        self.assertEqual(len(tasks_list), 1)
        self.assertEqual(tasks_list[0]['task'], "Implement feature X")
        self.assertEqual(tasks_list[0]['project_manager'], "John Doe")

    def test_strategic_tasks_to_dict_list_error_handling(self):
        """Test error handling in strategic_tasks_to_dict_list method."""
        StrategicTask.strategic_tasks_to_dict_list()


if __name__ == '__main__':
    unittest.main()
