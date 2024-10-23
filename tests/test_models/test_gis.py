import unittest
from unittest.mock import patch
from models.gis import (
    Output,
    Activity,
    ResponsiblePerson,
    Task,
    gis_data_to_dict_list
)


class TestGISModels(unittest.TestCase):
    """ Tests for the GIS models and their methods. """

    def test_output_creation(self):
        """Test that an Output object can be created with a name attribute."""
        output = Output(name="GIS Output")
        self.assertEqual(output.name, "GIS Output")

    def test_activity_creation(self):
        """Test that an Activity object can be created with activity, output_id, and responsible_person_id."""
        activity = Activity(activity="Field Survey", output_id=1, responsible_person_id=2)
        self.assertEqual(activity.activity, "Field Survey")
        self.assertEqual(activity.output_id, 1)
        self.assertEqual(activity.responsible_person_id, 2)

    def test_responsible_person_creation(self):
        """Test that a ResponsiblePerson object can be created with a name and designation."""
        person = ResponsiblePerson(name="Artkins Mlilo", designation="Engineer")
        self.assertEqual(person.name, "Artkins Mlilo")
        self.assertEqual(person.designation, "Engineer")

    def test_task_creation(self):
        """Test that a Task object can be created with description and activity_id."""
        task = Task(activity_id=1, description="Prepare maps", percentage_of_activity=75.5)
        self.assertEqual(task.activity_id, 1)
        self.assertEqual(task.description, "Prepare maps")
        self.assertEqual(task.percentage_of_activity, 75.5)


    @patch('models.gis.Activity.gis_activity_data_to_dict_list')
    def test_gis_activity_data_retrieval(self, mock_gis_activity_data_to_dict_list):
        """Test that gis_activity_data_to_dict_list returns the expected activity data as a dictionary."""
        mock_gis_activity_data_to_dict_list.return_value = [
            {"activity_id": 1, "activity_name": "Field Survey", "output_id": 1, "responsible_person_id": 2}
        ]
        result = Activity.gis_activity_data_to_dict_list()
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["activity_name"], "Field Survey")
        mock_gis_activity_data_to_dict_list.assert_called_once()

    @patch('models.gis.ResponsiblePerson.gis_responsible_person_data_to_dict_list')
    def test_gis_responsible_person_data_retrieval(self, mock_gis_responsible_person_data_to_dict_list):
        """Test that gis_responsible_person_data_to_dict_list returns the expected responsible person data as a dictionary."""
        mock_gis_responsible_person_data_to_dict_list.return_value = [
            {"responsible_person_id": 1, "responsible_person_name": "John Doe", "designation": "Engineer"}
        ]
        result = ResponsiblePerson.gis_responsible_person_data_to_dict_list()
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["responsible_person_name"], "John Doe")
        mock_gis_responsible_person_data_to_dict_list.assert_called_once()

    @patch('models.gis.Task.gis_task_data_to_dict_list')
    def test_gis_task_data_retrieval(self, mock_gis_task_data_to_dict_list):
        """Test that gis_task_data_to_dict_list returns the expected task data as a dictionary."""
        mock_gis_task_data_to_dict_list.return_value = [
            {"task_id": 1, "task_description": "Prepare maps", "percentage_of_activity": 75.5, "activity_id": 1}
        ]
        result = Task.gis_task_data_to_dict_list()
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["task_description"], "Prepare maps")
        mock_gis_task_data_to_dict_list.assert_called_once()


if __name__ == '__main__':
    unittest.main()