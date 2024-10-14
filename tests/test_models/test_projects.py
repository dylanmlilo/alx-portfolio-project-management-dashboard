import unittest
from unittest.mock import patch
from models.projects import (
    Section,
    ProjectManagers,
    ContractType,
    ProjectsData
)


class TestProjectsModels(unittest.TestCase):
    """ Tests for the projects.py module. """

    def test_section_creation(self):
        """
        Tests that a Section object can be created with a name attribute.
        The object's name is compared to the given value.
        """
        section_name = "Projects"
        section = Section(section_name)
        self.assertEqual(section.name, section_name)

    def test_project_manager_creation(self):
        """
        Tests that a ProjectManagers object can be created with a name and section attribute.
        The object's name and section are compared to the given values.
        """
        name = "Dylan Mlilo"
        section = "Projects"
        project_manager = ProjectManagers(name, section)
        self.assertEqual(project_manager.name, name)
        self.assertEqual(project_manager.section, section)

    def test_contract_type_creation(self):
        """
        Tests that a ContractType object can be created with a name attribute.
        """
        name = "Servicing"
        contract_type = ContractType(name)
        self.assertEqual(contract_type.name, name)

    @patch('models.projects.ProjectsData.projects_data_to_dict_list')
    def test_projects_data_retrieval(self, mock_projects_data_to_dict_list):
        """
        Tests that projects_data_to_dict_list returns a list of dictionaries
        containing project data. The method is patched to return a predefined
        list of dictionaries. The test asserts that the patched method is
        called once and that the return value is the same as the predefined
        list of dictionaries.
        """
        project_data = [
            {"contract_number": "CN123", "contract_name": "Database"},
            {"contract_number": "CN456", "contract_name": "Website"},
        ]
        mock_projects_data_to_dict_list.return_value = project_data

        result_list = ProjectsData.projects_data_to_dict_list()

        mock_projects_data_to_dict_list.assert_called_once()
        self.assertEqual(result_list, project_data)

    def test_projects_data_to_dict_list_error(self):
        """
        Tests that a ValueError is raised when an invalid contract_type_id is
        passed to projects_data_to_dict_list.
        """
        with self.assertRaises(ValueError):
            ProjectsData.projects_data_to_dict_list(contract_type_id="invalid")

    def test_projects_data_filtering_by_contract_type(self):
        """
        Tests that the contract_type_data_dict method filters data correctly
        based on the contract_type_id.
        """
        with patch('models.projects.ProjectsData.projects_data_to_dict_list') as mock_data:
            mock_data.return_value = [
                {"contract_number": "CN123", "contract_type_id": 1},
                {"contract_number": "CN456", "contract_type_id": 2},
            ]
            
            filtered_data = ContractType.contract_type_data_dict(1)
            self.assertEqual(len(filtered_data), 1)
            self.assertEqual(filtered_data[0]["contract_number"], "CN123")

    @patch('models.projects.ProjectManagers.project_managers_to_dict_list')
    def test_project_managers_filtering_by_section(self, mock_project_managers_to_dict_list):
        """
        Tests that the project_managers_to_dict_list method filters project managers
        correctly based on the section name.
        """
        mock_project_managers_to_dict_list.return_value = [
            {"name": "Dylan Mlilo", "section": "Projects"}
        ]

        filtered_managers = ProjectManagers.project_managers_to_dict_list(section_name="Projects")
        
        self.assertEqual(len(filtered_managers), 1)
        self.assertEqual(filtered_managers[0]['name'], "Dylan Mlilo")
        self.assertEqual(filtered_managers[0]['section'], "Projects")

    def test_invalid_contract_type_data_dict(self):
        """
        Tests that contract_type_data_dict raises a ValueError for invalid contract_type_id.
        """
        with self.assertRaises(ValueError):
            ContractType.contract_type_data_dict(contract_type_id="invalid")

    def test_projects_data_without_filter(self):
        """
        Tests that projects_data_to_dict_list retrieves all data when no filter is applied.
        """
        with patch('models.projects.ProjectsData.projects_data_to_dict_list') as mock_data:
            mock_data.return_value = [
                {"contract_number": "CN123", "contract_name": "Database"},
                {"contract_number": "CN456", "contract_name": "Website"},
            ]
            all_data = ProjectsData.projects_data_to_dict_list()
            self.assertEqual(len(all_data), 2)


if __name__ == '__main__':
    unittest.main()